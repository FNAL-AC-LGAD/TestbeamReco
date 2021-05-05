import uproot
import numpy as np
import pandas as pd
from glob import glob
import time
import matplotlib.pyplot as plt

def getSamplesToRun(names):
    s = glob(names)
    if len(s) == 0:
        raise Exception("No files find that correspond to: "+names)
    return s

# Takes training vars, signal and background files and returns training data
def get_data(dataSet, config):
    dg = DataGetter.DefinedVariables(config["allVars"])
    trainData = dg.importData(samplesToRun = tuple(dataSet), treename = config["tree"])

    # Randomly shuffle the signal and background before mixing them together
    np.random.seed(config["seed"]) 
    perms = np.random.permutation(trainData["data"].shape[0])
    for key in trainData:
        trainData[key] = trainData[key][perms]

    # Get the rescale inputs to have unit variance centered at 0 between -1 and 1
    def scale(data):
        data["mean"] = np.mean(data["data"], 0)
        data["std"] = np.std(data["data"], 0)
        data["scale"] = 1.0 / data["std"]
    scale(trainData)
    return trainData

class DataGetter:
    #The constructor simply takes in a list and saves it to self.l
    def __init__(self, variables):
        self.l = variables
        self.columnHeaders = None
        self.data = None

    #Simply accept a list and pass it to the constructor
    @classmethod
    def DefinedVariables(cls, variables):
        return cls(variables)

    def getList(self):
        return self.l

    def getData(self):
        return self.data

    def getColumnHeaders(self, samplesToRun, treename):
        if self.columnHeaders is None:
            try:
                sample = samplesToRun[0]                
                f = uproot.open(sample)
                self.columnHeaders = f[treename].pandas.df().columns.tolist()
                f.close()
            except IndexError as e:
                print(e)
                raise IndexError("No sample in samplesToRun")
            except Exception as e:
                print("Warning: \"%s\" has issues" % sample, e)
        return self.columnHeaders

    def checkVariables(self, variables):
        for v in variables:            
            if not v in self.columnHeaders:
                raise ValueError("Variable not found in input root file: %s"%v)
        
    def getDataSets(self, samplesToRun, treename):
        dsets = []
        if len(samplesToRun) == 0:
            raise IndexError("No sample in samplesToRun")
        for filename in samplesToRun:
            try:
                f = uproot.open(filename)
                pdf = f[treename].pandas.df()
                dsets.append( pdf )
                f.close()
            except Exception as e:
                print("Warning: \"%s\" has issues" % filename, e)
                continue
        return dsets

    def importData(self, samplesToRun, treename = "myMiniTree"):
        #variables to train
        variables = self.getList()
        self.getColumnHeaders(samplesToRun, treename)
        self.checkVariables(variables)
        
        # Get data into the right format
        dsets = self.getDataSets(samplesToRun, treename)
        data = pd.concat(dsets)
        data = data.dropna()

        #setup and get training data
        npyInputData = data[variables].astype(float).values

        #setup and get labels
        npyInputAnswers = np.zeros((npyInputData.shape[0], 2))
        npyInputAnswers[:,1] = 1

        #setup and get target values
        npyInputTargetX = data[["x"]].values
        npyInputTargetT = data[["timePhotek"]].values
        npyTime3 = data[["time3"]].values
        npyAmp2 = data[["amp2"]].values
        npyAmp3 = data[["amp3"]].values
        npyAmp4 = data[["amp4"]].values

        return {"data":npyInputData, "labels":npyInputAnswers, "targetX":npyInputTargetX, "targetT":npyInputTargetT, "time3":npyTime3, "amp2":npyAmp2, "amp3":npyAmp3, "amp4":npyAmp4}

if __name__ == '__main__':
    config = {}
    config["allVars"] = ["amp1","amp2","amp3","amp4","amp5","amp6","time1","time2","time3","time4","time5","time6","timePhotek","x"]
    config["tree"] = "myMiniTree"
    config["seed"] = int(time.time())

    trainData = get_data(["BNL2020_220V_272_Train.root"], config)
    print(trainData)

    # Make input variable plots
    index=0
    for var in config["allVars"]:
        fig = plt.figure()
        plt.hist(trainData["data"][:,index], bins=30, histtype='step', density=False, log=False, label=var)
        plt.legend(loc='upper right')
        plt.ylabel('norm')
        plt.xlabel(var)
        fig.savefig(var+".png", dpi=fig.dpi)
        index += 1

