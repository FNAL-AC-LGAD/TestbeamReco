from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle
import os
#import EfficiencyUtils
#import langaus

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

inputfile = TFile("../test/myoutputfile.root")

#Get 3D histograms 
th3_timeDiff_vs_xy_channel00 = inputfile.Get("timeDiff_vs_xy_channel00")
th3_timeDiff_vs_xy_channel01 = inputfile.Get("timeDiff_vs_xy_channel01")
th3_timeDiff_vs_xy_channel02 = inputfile.Get("timeDiff_vs_xy_channel02")
th3_timeDiff_vs_xy_channel03 = inputfile.Get("timeDiff_vs_xy_channel03")
th3_timeDiff_vs_xy_channel04 = inputfile.Get("timeDiff_vs_xy_channel04")
th3_timeDiff_vs_xy_channel05 = inputfile.Get("timeDiff_vs_xy_channel05")
th3_timeDiff = inputfile.Get("timeDiff_vs_xy")
th3_weighted_timeDiff = inputfile.Get("weighted_timeDiff_vs_xy")

#Build 2D timeDiff vs x histograms
th2_timeDiff_vs_x_channel00 = th3_timeDiff_vs_xy_channel00.Project3D("zx")
th2_timeDiff_vs_x_channel01 = th3_timeDiff_vs_xy_channel01.Project3D("zx")
th2_timeDiff_vs_x_channel02 = th3_timeDiff_vs_xy_channel02.Project3D("zx")
th2_timeDiff_vs_x_channel03 = th3_timeDiff_vs_xy_channel03.Project3D("zx")
th2_timeDiff_vs_x_channel04 = th3_timeDiff_vs_xy_channel04.Project3D("zx")
th2_timeDiff_vs_x_channel05 = th3_timeDiff_vs_xy_channel05.Project3D("zx")
th2_timeDiff = th3_timeDiff.Project3D("zx")
th2_weighted_timeDiff = th3_weighted_timeDiff.Project3D("zx")

list_th2_timeDiff_vs_x = []
list_th2_timeDiff_vs_x.append(th2_timeDiff_vs_x_channel00)
list_th2_timeDiff_vs_x.append(th2_timeDiff_vs_x_channel01)
list_th2_timeDiff_vs_x.append(th2_timeDiff_vs_x_channel02)
list_th2_timeDiff_vs_x.append(th2_timeDiff_vs_x_channel03)
list_th2_timeDiff_vs_x.append(th2_timeDiff_vs_x_channel04)
list_th2_timeDiff_vs_x.append(th2_timeDiff_vs_x_channel05)
list_th2_timeDiff_vs_x.append(th2_timeDiff)
list_th2_timeDiff_vs_x.append(th2_weighted_timeDiff)

names = [
    "channel_1",
    "channel_2",
    "channel_3",
    "channel_4",
    "channel_5",
    "channel_6",
    "time_diff",
    "weighted_time_diff",
]

#Build timeDiff histograms
timeDiff_vs_x = th3_timeDiff.ProjectionX().Clone("timeDiff_vs_x_channel")
timeDiff_vs_x_channel00 = timeDiff_vs_x.Clone("timeDiff_vs_x_channel00")
timeDiff_vs_x_channel01 = timeDiff_vs_x.Clone("timeDiff_vs_x_channel01")
timeDiff_vs_x_channel02 = timeDiff_vs_x.Clone("timeDiff_vs_x_channel02")
timeDiff_vs_x_channel03 = timeDiff_vs_x.Clone("timeDiff_vs_x_channel03")
timeDiff_vs_x_channel04 = timeDiff_vs_x.Clone("timeDiff_vs_x_channel04")
timeDiff_vs_x_channel05 = timeDiff_vs_x.Clone("timeDiff_vs_x_channel05")
timeDiff_vs_x_timeDiff = timeDiff_vs_x.Clone("timeDiff")
timeDiff_vs_x_weighted_timeDiff = timeDiff_vs_x.Clone("weighted_timeDiff")

list_timeDiff_vs_x = []
list_timeDiff_vs_x.append(timeDiff_vs_x_channel00)
list_timeDiff_vs_x.append(timeDiff_vs_x_channel01)
list_timeDiff_vs_x.append(timeDiff_vs_x_channel02)
list_timeDiff_vs_x.append(timeDiff_vs_x_channel03)
list_timeDiff_vs_x.append(timeDiff_vs_x_channel04)
list_timeDiff_vs_x.append(timeDiff_vs_x_channel05)
list_timeDiff_vs_x.append(timeDiff_vs_x_timeDiff)
list_timeDiff_vs_x.append(timeDiff_vs_x_weighted_timeDiff)
print("Finished cloning histograms")

canvas = TCanvas("cv","cv",800,800)
gPad.SetLeftMargin(0.12)
gPad.SetRightMargin(0.15)
gPad.SetTopMargin(0.08)
gPad.SetBottomMargin(0.12)
gPad.SetTicks(1,1)
#fit = langaus.LanGausFit()
print("Finished setting up langaus fit class")

#loop over X bins
for i in range(0, timeDiff_vs_x.GetXaxis().GetNbins()+1):
    ##For Debugging
    #if not (i==46 and j==5):
    #    continue

    for channel in range(0, len(list_timeDiff_vs_x)):
        tmpHist = list_th2_timeDiff_vs_x[channel].ProjectionY("py",i,i)
        myMean = tmpHist.GetMean()
        myRMS = tmpHist.GetRMS()
        nEvents = tmpHist.GetEntries()
        fitlow = myMean - 1.5*myRMS
        fithigh = myMean + 1.5*myRMS
        value = myRMS
        error = 0.0

        #Do Langaus fit if histogram mean is larger than 10
        #and mean is larger than RMS (a clear peak away from noise)
        if(nEvents > 50):
            tmpHist.Rebin(4)

            #myLanGausFunction = fit.fit(tmpHist, fitrange=(myMean-2*myRMS,myMean+3*myRMS))
            fit = TF1('fit','gaus',fitlow,fithigh)
            tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
            #myMPV = myLanGausFunction.GetParameter(1)
            #mySigma = myLanGausFunction.GetParameter(3)
            myMPV = fit.GetParameter(1)
            mySigma = fit.GetParameter(2)
            mySigmaError = fit.GetParError(2)
            value = 1000.0*mySigma
            error = 1000.0*mySigmaError
            
            ##For Debugging
            #tmpHist.Draw("hist")
            ##myLanGausFunction.Draw("same")
            #fit.Draw("same")
            #canvas.SaveAs("q_"+str(i)+".gif")
            #
            #print ("Bin : " + str(i) + " -> " + str(value) + " +/- " + str(error))
        else:
            value = 0.0            

        list_timeDiff_vs_x[channel].SetBinContent(i,value)
        list_timeDiff_vs_x[channel].SetBinError(i,error)
                        
# Plot 2D histograms
outputfile = TFile("plots.root","RECREATE")
for channel in range(0, len(list_timeDiff_vs_x)):
    list_timeDiff_vs_x[channel].Draw("hist e")
    list_timeDiff_vs_x[channel].SetStats(0)
    list_timeDiff_vs_x[channel].SetTitle(names[channel])
    list_timeDiff_vs_x[channel].SetMinimum(0.0)
    list_timeDiff_vs_x[channel].SetMaximum(100.0)

    canvas.SaveAs("TimeRes_vs_x_"+names[channel]+".gif")
    canvas.SaveAs("TimeRes_vs_x_"+names[channel]+".pdf")

    list_timeDiff_vs_x[channel].Write()

outputfile.Close()

