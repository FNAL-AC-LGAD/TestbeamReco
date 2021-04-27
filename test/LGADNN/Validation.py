from DataGetter import get_data, getSamplesToRun
import numpy as np
import os
from scipy.stats import norm
import ROOT
ROOT.gROOT.SetBatch(True)

# Little incantation to display trying to X display
import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
plt.style.use({'legend.frameon':False,'legend.fontsize':16,'legend.edgecolor':'black'})
from matplotlib.colors import LogNorm
import matplotlib.lines as ml
from sklearn.metrics import roc_curve, auc, precision_recall_curve, average_precision_score, roc_auc_score
import json

class Validation:

    def __init__(self, model, config, trainData, result_log=None):
        self.model = model
        self.config = config
        self.trainData = trainData
        self.result_log = result_log
        self.metric = {}
        self.doLog = False

    def __del__(self):
        del self.model
        del self.config
        del self.trainData
        del self.result_log
        del self.metric
        
    def plot2DVar(self, name, binxl, binxh, numbin, xIn, yIn, nbiny):
        fig = plt.figure()
        h, xedges, yedges, image = plt.hist2d(xIn, yIn, bins=[numbin, nbiny], range=[[binxl, binxh], [binxl, binxh]], cmap=plt.cm.jet)
        plt.colorbar()
    
        bin_centersx = 0.5 * (xedges[:-1] + xedges[1:])
        bin_centersy = 0.5 * (yedges[:-1] + yedges[1:])
        y = []
        ye = []
        for i in range(h.shape[0]):
            ynum = 0
            ynum2 = 0
            ydom = 0
            for j in range(len(h[i])):
                ynum += h[i][j] * bin_centersy[j]
                ynum2 += h[i][j] * (bin_centersy[j]**2)
                ydom += h[i][j]        
            yavg = ynum / ydom if ydom != 0 else -1
            yavg2 = ynum2 / ydom if ydom != 0 else -1
            sigma = np.sqrt(yavg2 - (yavg**2)) if ydom != 0 else 0
            y.append(yavg)
            ye.append(sigma)
            
        xerr = 0.5*(xedges[1]-xedges[0])
        #plt.errorbar(bin_centersx, y, xerr=xerr, yerr=ye, fmt='o', color='xkcd:red')
        fig.savefig(self.config["outputDir"]+"/"+name+".png", dpi=fig.dpi)       
        #fig.savefig(self.config["outputDir"]+"/"+name+"_discriminator.pdf", dpi=fig.dpi) 

        plt.close(fig)

    def getResults(self, output, outputNum=0, columnNum=0):
        return output[outputNum][:,columnNum].ravel()
        #return output[:,columnNum].ravel()

    # Plot a set of 1D hists together, where the hists, colors, labels, weights
    # are provided as a list argument.
    def plotDisc(self, hists, colors, labels, name, xlab, ylab, bins=100, arange=(0,1), doLog=False):
        # Plot predicted mass
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_ylabel(xlab); ax.set_xlabel(ylab)

        for i in range(0, len(hists)): 
            mu, sigma = norm.fit(hists[i])
            mean = round(np.average(hists[i]), 6)
            std = round(np.std(hists[i]), 6)
            #print("sigma: {} std: {}".format(sigma, std))
            #label = labels[i]+" mean="+str(mean)+" std="+str(std)
            label = labels[i]+" std="+str(std)
            plt.hist(hists[i], bins=bins, range=arange, color="xkcd:"+colors[i], alpha=0.9, histtype='step', lw=2, label=label, density=True, log=doLog)

        ax.legend(loc=1, frameon=False)
        fig.savefig(self.config["outputDir"]+"/%s.png"%(name), dpi=fig.dpi)        
        plt.close(fig)

    def plot1D(self, hists, colors, labels, name, xlab, ylab, bins=100, arange=(0,1), doLog=False):
        ROOT.gStyle.SetOptFit(1)
        c = ROOT.TCanvas("c","c",1000,1000)
        ROOT.gPad.SetLeftMargin(0.12)
        ROOT.gPad.SetRightMargin(0.15)
        ROOT.gPad.SetTopMargin(0.08)
        ROOT.gPad.SetBottomMargin(0.12)
        ROOT.gPad.SetTicks(1,1)
        ROOT.TH1.SetDefaultSumw2()
        if doLog: ROOT.gPad.SetLogy()

        hdummy = ROOT.TH1D(name,name,bins,arange[0],arange[1])
        hdummy.GetXaxis().SetTitle(ylab)
        hdummy.GetYaxis().SetTitle(xlab)
        hdummy.Draw()

        plotMax = 1.0
        for i in range(0, len(hists)):
            h = ROOT.TH1D(name,name,bins,arange[0],arange[1])
            for x in hists[i]:
                h.Fill(x)
            h.Draw("sames")
            plotMax = h.GetMaximum()

            fit = ROOT.TF1("fit", "gaus")    
            fit.SetLineColor(ROOT.kRed)
            fit.Draw("same")    
            h.Fit(fit)
            fit.Draw("same")    

        hdummy.SetMaximum(plotMax*1.1)
        c.Print(self.config["outputDir"]+"/%s.png"%(name))

    # Plot loss of training vs test
    def plotAccVsEpoch(self, h1, h2, title, name):
        fig = plt.figure()
        plt.plot(self.result_log.history[h1])
        plt.plot(self.result_log.history[h2])
        plt.title(title, pad=45.0)
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='best')
        fig.savefig(self.config["outputDir"]+"/%s.png"%(name), dpi=fig.dpi)
        plt.close(fig)

    def plotAccVsEpochAll(self, h2, h3, h4, h5, n2, n3, n4, n5, val, title, name):
        fig = plt.figure()
        plt.plot(self.result_log.history["%s%s_loss"%(val,h2)])
        plt.plot(self.result_log.history["%s%s_output_loss"%(val,h3)])
        plt.plot(self.result_log.history["%s%s_output_loss"%(val,h4)])
        plt.plot(self.result_log.history["%s%s_loss"%(val,h5)])
        plt.title(title, pad=45.0)
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend([n2, n3, n4, n5], loc='best')
        fig.savefig(self.config["outputDir"]+"/%s.png"%(name), dpi=fig.dpi)
        plt.close(fig)

    def makePlots(self, doQuickVal=True):
        valData = get_data(["BNL2020_220V_272_Val.root"], self.config)
        output_Train = self.model.predict(self.trainData["data"])
        output_Val = self.model.predict(valData["data"])
        y_Train = self.getResults(output_Train, outputNum=0, columnNum=0)
        y_Train_true = self.trainData["targetX"][:,0]
        y_Val = self.getResults(output_Val, outputNum=0, columnNum=0)
        y_Val_true = valData["targetX"][:,0]

        t_Train = self.getResults(output_Train, outputNum=1, columnNum=0)
        t_Train_true = self.trainData["targetT"][:,0]
        t_Val = self.getResults(output_Val, outputNum=1, columnNum=0)
        t_Val_true = valData["targetT"][:,0]


        #############################
        # X position measurement
        #############################
        nBinsReg = 90
        sensorRange = (-0.1, 0.8)
        maskRange = (0.23, 0.53)
        arange = (-0.5, 0.5)
        colors = ["red", "green", "blue", "magenta", "orange", "black"]; labels = ["Train", "Val"]
        maskTrain = (maskRange[0] < y_Train_true) & (y_Train_true < maskRange[1])        
        maskVal = (maskRange[0] < y_Val_true) & (y_Val_true < maskRange[1])        

        positionDiffTrain = y_Train - y_Train_true
        positionDiffVal = y_Val - y_Val_true
        self.plotDisc([positionDiffTrain, positionDiffVal], colors, labels, "xRes", 'Events', 'NN - tracker', arange=arange, bins=nBinsReg)
        #self.plotDisc([positionDiffTrain, positionDiffVal], colors, labels, "xResLog", 'Events', 'NN - tracker', arange=arange, bins=nBinsReg, doLog=True)
        self.plot2DVar(name="xNN_Tracker", binxl=sensorRange[0], binxh=sensorRange[1], numbin=nBinsReg, xIn=y_Train, yIn=y_Train_true, nbiny=nBinsReg)
        self.plot1D([positionDiffTrain], colors, labels, "xResROOT", 'Events', 'NN - tracker', arange=arange, bins=nBinsReg, doLog=True)

        positionDiffTrain = y_Train[maskTrain] - y_Train_true[maskTrain]
        positionDiffVal = y_Val[maskVal] - y_Val_true[maskVal]
        self.plotDisc([positionDiffTrain, positionDiffVal], colors, labels, "xRes_Mask", 'Events', 'NN - tracker', arange=arange, bins=nBinsReg)
        #self.plotDisc([positionDiffTrain, positionDiffVal], colors, labels, "xResLog", 'Events', 'NN - tracker', arange=arange, bins=nBinsReg, doLog=True)
        self.plot2DVar(name="xNN_Tracker_Mask", binxl=sensorRange[0], binxh=sensorRange[1], numbin=nBinsReg, xIn=y_Train[maskTrain], yIn=y_Train_true[maskTrain], nbiny=nBinsReg)

        #############################
        # T position measurement
        #############################
        nBinsReg = 100
        timeRange = (-4, 4)
        arange = (-4, 4)
        timeDiffTrain = t_Train - t_Train_true
        timeDiffVal = t_Val - t_Val_true
        self.plotDisc([timeDiffTrain, timeDiffVal], colors, labels, "tRes", 'Events', 'NN - photek', arange=arange, bins=nBinsReg)
        #self.plotDisc([timeDiffTrain, timeDiffVal], colors, labels, "tResLog", 'Events', 'NN - photek', arange=arange, bins=nBinsReg, doLog=True)
        self.plotDisc([self.trainData["time3"][:,0] - t_Train_true], colors, labels, "tResTime3", 'Events', 'time3 - photek', arange=(-14,-6), bins=nBinsReg)
        self.plot2DVar(name="tNN_Photek", binxl=timeRange[0], binxh=timeRange[1], numbin=nBinsReg, xIn=t_Train, yIn=t_Train_true, nbiny=nBinsReg)
        self.plotDisc([t_Train, t_Val], colors, labels, "timeTrain", 'Events', 'NN', arange=timeRange, bins=nBinsReg)
        self.plotDisc([t_Train_true, t_Val_true], colors, labels, "timeTrainTrue", 'Events', 'NN', arange=timeRange, bins=nBinsReg)
        self.plot1D([timeDiffTrain], colors, labels, "tResROOT", 'Events', 'NN - photek', arange=arange, bins=nBinsReg, doLog=True)

        timeDiffTrain = t_Train[maskTrain] - t_Train_true[maskTrain]
        timeDiffVal = t_Val[maskVal] - t_Val_true[maskVal]
        self.plotDisc([timeDiffTrain, timeDiffVal], colors, labels, "tRes_Mask", 'Events', 'NN - photek', arange=arange, bins=nBinsReg)
        #self.plotDisc([timeDiffTrain, timeDiffVal], colors, labels, "tResLog_Mask", 'Events', 'NN - photek', arange=arange, bins=nBinsReg, doLog=True)
        self.plot2DVar(name="tNN_Photek_Mask", binxl=timeRange[0], binxh=timeRange[1], numbin=nBinsReg, xIn=t_Train[maskTrain], yIn=t_Train_true[maskTrain], nbiny=nBinsReg)


        self.plot1D([self.trainData["time3"][:,0] - t_Train_true], colors, labels, "tResTime3ROOT", 'Events', 'time3 - photek', arange=(-14,-6), bins=nBinsReg, doLog=True)
        

        # Plot Acc vs Epoch
        self.plotAccVsEpoch('loss', 'val_loss', 'model loss', 'loss_train_val')
               
        for key in self.metric:
            print(key, self.metric[key])
        
        self.config["metric"] = self.metric
        with open(self.config["outputDir"]+"/config.json",'w') as configFile:
            json.dump(self.config, configFile, indent=4, sort_keys=True)

        return self.metric

