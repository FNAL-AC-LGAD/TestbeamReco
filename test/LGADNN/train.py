#!/bin/env python
import sys, ast, os
os.environ['KMP_WARNINGS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
import tensorflow.keras as K
from tensorflow.python.framework.convert_to_constants import convert_variables_to_constants_v2
import numpy as np
from DataGetter import get_data,getSamplesToRun
import shutil
from Validation import Validation
import json
import argparse
import os
import time

class Train:
    def __init__(self, USER, seed, saveAndPrint, hyperconfig, doQuickVal=False, doReweight=False, model="*", tree = "myMiniTree"):
        self.user = USER
        #self.logdir = "/storage/local/data1/gpuscratch/%s"%(self.user)
        #self.logdir = "./"
        self.config = {}
        self.config["seed"] = seed
        self.saveAndPrint = saveAndPrint
        self.model = model
        self.config["tree"] = tree
        self.config["verbose"] = 1
        self.config["dataSet"] = "./"
        self.config["metrics"]=['accuracy']
        print("Using "+self.config["dataSet"]+" data set")

        # Define ouputDir based on input config
        self.makeOutputDir(hyperconfig)
        self.config.update(hyperconfig)
        self.logdir = self.config["outputDir"]

        if not os.path.exists(self.logdir): os.makedirs(self.logdir)
        
    # Define loss functions
    def loss_crossentropy(self, c):
        def loss_model(y_true, y_pred):
            return c * K.losses.binary_crossentropy(y_true, y_pred)
        return loss_model
    
    def make_loss_adversary(self, c):
        def loss_adversary(y_true, y_pred):
            return c * K.losses.categorical_crossentropy(y_true, y_pred)
            #return c * K.backend.binary_crossentropy(y_true, y_pred)
        return loss_adversary

    def make_loss_MSE(self, c):
        def loss_MSE(y_true, y_pred):
            return c * K.losses.mean_squared_error(y_true, y_pred)
            #return c * K.losses.mean_squared_logarithmic_error(y_true, y_pred)
        return loss_MSE

    def make_loss_MAPE(self, c):
        def loss_MAPE(y_true, y_pred):
            return c * K.losses.mean_absolute_percentage_error(y_true, y_pred)
        return loss_MAPE

    def model_reg(self, config, trainData):
        optimizer = K.optimizers.Adam(lr=config["lr"], beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
        n_hidden_layers_X = list(config["nNodesX"] for x in range(config["nHLayersX"]))
        n_hidden_layers_T = list(config["nNodesT"] for x in range(config["nHLayersT"]))

        main_input = K.layers.Input(shape=(trainData["data"].shape[1],), name='main_input')
        # Set the rescale inputs to have unit variance centered at 0 between -1 and 1
        layerLambda = K.layers.Lambda(lambda x: (x - K.backend.constant(trainData["mean"])) * K.backend.constant(trainData["scale"]), name='normalizeData')(main_input)
        #layerSplit = K.layers.Dense(config["nNodesX"], activation='relu')(layerLambda)
        layerSplit = layerLambda

        layer = layerSplit
        for n in n_hidden_layers_X:
            layer = K.layers.Dense(n, activation='relu')(layer)
        layer = K.layers.Dropout(config["drop_out"],seed=config["seed"])(layer)
        first_output = K.layers.Dense(trainData["targetX"].shape[1], activation=None, name='first_output')(layer)

        #layer = K.layers.Dense(config["nNodesT"], activation='relu')(layerSplit)
        #layer = K.layers.concatenate([layer, layerLambda], name='concat_layer')
        layer = layerSplit
        for n in n_hidden_layers_T:
            layer = K.layers.Dense(n, activation='linear')(layer)
        #layer = K.layers.Dropout(config["drop_out"],seed=config["seed"])(layer)
        second_output = K.layers.Dense(trainData["targetT"].shape[1], activation=None, name='second_output')(layer)

        model = K.models.Model(inputs=main_input, outputs=[first_output, second_output], name='model')
        model.summary()
        return model, optimizer

    def make_model_reg(self, trainData):
        model, optimizer = self.model_reg(self.config, trainData)
        model.compile(loss=[K.losses.MeanSquaredError(), K.losses.MeanSquaredError()], optimizer=optimizer)
        #model.compile(loss=[self.make_loss_MSE(c=1.0)], optimizer=optimizer)
        #model.compile(loss=[self.make_loss_MAPE(c=1.0)], optimizer=optimizer)
        
        return model

    def get_callbacks(self):
        tbCallBack = K.callbacks.TensorBoard(log_dir=self.logdir+"/log_graph", histogram_freq=0, write_graph=True, write_images=True)
        log_model = K.callbacks.ModelCheckpoint(self.config["outputDir"]+"/BestNN.hdf5", monitor='val_loss', verbose=self.config["verbose"], save_best_only=True)
        earlyStop = K.callbacks.EarlyStopping(monitor="val_loss", min_delta=0, patience=5, verbose=0, mode="auto", baseline=None)
        callbacks = []
        if self.config["verbose"] == 1: 
            #callbacks = [log_model, tbCallBack, earlyStop]
            #callbacks = [log_model, tbCallBack]
            callbacks = [tbCallBack]
        return callbacks

    def gpu_allow_mem_grow(self):
        gpus = tf.config.experimental.list_physical_devices('GPU')
        if gpus:
            try:
                for gpu in gpus:
                    tf.config.experimental.set_memory_growth(gpu, True)
            except RuntimeError as e:
                print("Error: gpu_mem_grow failed: ",e)

    def save_model_pb(self, model):
        #https://github.com/leimao/Frozen_Graph_TensorFlow/tree/master/TensorFlow_v2

        # Save model as hdf5 format
        model.save(self.config["outputDir"]+"/keras_model")

        # Convert Keras model to ConcreteFunction
        full_model = tf.function(lambda x: model(x))
        full_model = full_model.get_concrete_function(x=tf.TensorSpec(model.inputs[0].shape, model.inputs[0].dtype))

        # Get frozen ConcreteFunction
        frozen_func = convert_variables_to_constants_v2(full_model)
        frozen_func.graph.as_graph_def()
        self.config["input_output"] = list(x.name.split(':')[0] for x in frozen_func.inputs + frozen_func.outputs)
        
        # Save frozen graph from frozen ConcreteFunction to hard drive
        tf.io.write_graph(graph_or_graph_def=frozen_func.graph, logdir=self.config["outputDir"], name="keras_frozen.pb", as_text=False)

    def plot_model(self, model):
        try:
            K.utils.plot_model(model, to_file=self.config["outputDir"]+"/model.png", show_shapes=True)
        except AttributeError as e:
            print("Error: plot_model failed: ",e)

    def makeOutputDir(self,d):
        outputDir = "Output/"
        for key in sorted(d.keys()):
            outputDir += key+"_"+str(d[key])+"_"
        d["outputDir"] = outputDir
        if os.path.exists(d["outputDir"]):
            print("Removing old training files: ", d["outputDir"])
            shutil.rmtree(d["outputDir"])

        os.makedirs(d["outputDir"]+"/log_graph")    

    def defineVars(self):
        self.config["allVars"] = [
            "amp1","amp2","amp3","amp4","amp5","amp6",
            "time1","time2","time3","time4","time5","time6",
            #"amp2","amp3","amp4",
            #"time2","time3","time4",
        ]

    def importData(self):
        # Import data
        print("----------------Preparing data------------------")
        #Get Data set used in training and validation
        trainData = get_data(["BNL2020_220V_272_Train.root"], self.config)
        testData = get_data(["BNL2020_220V_272_Test.root"], self.config)        
        return trainData, testData
       
    def train(self):   
        # Define vars for training
        self.defineVars()
        print("Training variables:")
        print(len(self.config["allVars"]), self.config["allVars"])

        #Get stuff from input ROOT files
        trainData, testData = self.importData()

        # Make model
        print("----------------Preparing training model------------------")
        self.gpu_allow_mem_grow()
        model = self.make_model_reg(trainData)
        callbacks = self.get_callbacks()
        
        # Training model
        print("----------------Training model------------------")
        result_log = model.fit(trainData["data"], [trainData["targetX"], trainData["targetT"]], 
                               batch_size=self.config["batch_size"], epochs=self.config["epochs"], callbacks=callbacks,
                               validation_data=(testData["data"], [testData["targetX"], testData["targetT"]]), 
                               )

        # Model Visualization
        print("----------------Printed model layout------------------")
        self.plot_model(model)

        if self.saveAndPrint:            
            # Save trainig model as a protocol buffers file
            print("----------------Saving model------------------")
            self.save_model_pb(model)
       
        #Plot results
        print("----------------Validation of training------------------")
        val = Validation(model, self.config, trainData, result_log)
        val.makePlots()
        del val
        
        #Clean up training
        del model

if __name__ == '__main__':
    usage = "usage: %prog [options]"
    parser = argparse.ArgumentParser(usage)
    parser.add_argument("--quickVal",     dest="quickVal",     help="Do quick validation", action="store_true", default=False) 
    parser.add_argument("--reweight",     dest="reweight",     help="Do event reweighting", action="store_true", default=False) 
    parser.add_argument("--json",         dest="json",         help="JSON config file", default="NULL") 
    parser.add_argument("--model",        dest="model",        help="Signal model to train on", type=str, default="*") 
    parser.add_argument("--tree",         dest="tree",         help="myMiniTree to train on", default="myMiniTree")
    parser.add_argument("--saveAndPrint", dest="saveAndPrint", help="Save pb and print model", action="store_true", default=False)
    parser.add_argument("--seed",         dest="seed",         help="Use specific seed", type=int, default=-1)
    args = parser.parse_args()

    # Get seed from time, but allow user to reseed with their own number
    masterSeed = int(time.time())
    if args.seed != -1:
        masterSeed = args.seed

    # Seed the tensorflow here, seed numpy in datagetter
    tf.random.set_seed(masterSeed)

    # _After_ setting seed, for reproduceability, try these resetting/clearing commands
    # Enforce 64 bit precision
    K.backend.clear_session()
    tf.compat.v1.reset_default_graph()
    K.backend.set_floatx('float64')
    USER = os.getenv("USER")

    hyperconfig = {}
    if args.json != "NULL": 
        with open(str(args.json), "r") as f:
            hyperconfig = json.load(f)
    else: 
        hyperconfig = {"atag" : "GoldenTEST", "nNodesX":100, "nHLayersX":3, "nNodesT":100, "nHLayersT":2, "drop_out":0.3, "batch_size":5000, "epochs":200, "lr":0.001}

    t = Train(USER, masterSeed, args.saveAndPrint, hyperconfig, args.quickVal, args.reweight, model=args.model, tree=args.tree)
    t.train()

