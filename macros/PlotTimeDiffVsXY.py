from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,gROOT,gPad
import os
import EfficiencyUtils
import langaus

gROOT.SetBatch( True )

#inputfile = TFile("/afs/cern.ch/work/s/sixie/public/releases/run2/analysis/testbeam/CMSSW_11_2_0_pre5/src/TestbeamReco/test/BNL2020_220V.root")
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
list_th3_timeDiff_vs_xy = []
list_th3_timeDiff_vs_xy.append(th3_timeDiff_vs_xy_channel00)
list_th3_timeDiff_vs_xy.append(th3_timeDiff_vs_xy_channel01)
list_th3_timeDiff_vs_xy.append(th3_timeDiff_vs_xy_channel02)
list_th3_timeDiff_vs_xy.append(th3_timeDiff_vs_xy_channel03)
list_th3_timeDiff_vs_xy.append(th3_timeDiff_vs_xy_channel04)
list_th3_timeDiff_vs_xy.append(th3_timeDiff_vs_xy_channel05)
list_th3_timeDiff_vs_xy.append(th3_timeDiff)
list_th3_timeDiff_vs_xy.append(th3_weighted_timeDiff)

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
efficiency_vs_xy_numerator = inputfile.Get("efficiency_vs_xy_highThreshold_numerator")
timeDiff_vs_xy = efficiency_vs_xy_numerator.Clone("timeDiff_vs_xy_channel")
timeDiff_vs_xy_channel00 = timeDiff_vs_xy.Clone("timeDiff_vs_xy_channel00")
timeDiff_vs_xy_channel01 = timeDiff_vs_xy.Clone("timeDiff_vs_xy_channel01")
timeDiff_vs_xy_channel02 = timeDiff_vs_xy.Clone("timeDiff_vs_xy_channel02")
timeDiff_vs_xy_channel03 = timeDiff_vs_xy.Clone("timeDiff_vs_xy_channel03")
timeDiff_vs_xy_channel04 = timeDiff_vs_xy.Clone("timeDiff_vs_xy_channel04")
timeDiff_vs_xy_channel05 = timeDiff_vs_xy.Clone("timeDiff_vs_xy_channel05")
timeDiff_vs_xy_timeDiff = timeDiff_vs_xy.Clone("timeDiff")
timeDiff_vs_xy_weighted_timeDiff = timeDiff_vs_xy.Clone("weighted_timeDiff")

list_timeDiff_vs_xy = []
list_timeDiff_vs_xy.append(timeDiff_vs_xy_channel00)
list_timeDiff_vs_xy.append(timeDiff_vs_xy_channel01)
list_timeDiff_vs_xy.append(timeDiff_vs_xy_channel02)
list_timeDiff_vs_xy.append(timeDiff_vs_xy_channel03)
list_timeDiff_vs_xy.append(timeDiff_vs_xy_channel04)
list_timeDiff_vs_xy.append(timeDiff_vs_xy_channel05)
list_timeDiff_vs_xy.append(timeDiff_vs_xy_timeDiff)
list_timeDiff_vs_xy.append(timeDiff_vs_xy_weighted_timeDiff)
print("Finished cloning histograms")

canvas = TCanvas("cv","cv",800,800)
gPad.SetLeftMargin(0.12)
gPad.SetRightMargin(0.15)
gPad.SetTopMargin(0.08)
gPad.SetBottomMargin(0.12)
gPad.SetTicks(1,1)
fit = langaus.LanGausFit()
print("Finished setting up langaus fit class")

#loop over X,Y bins
for i in range(1, timeDiff_vs_xy.GetXaxis().GetNbins()):
    for j in range(1, timeDiff_vs_xy.GetYaxis().GetNbins()):

        ##For Debugging
        #if not (i==46 and j==5):
        #    continue

        for channel in range(0, len(list_timeDiff_vs_xy)):
            tmpHist = list_th3_timeDiff_vs_xy[channel].ProjectionZ("pz",i,i,j,j)
            myMean = tmpHist.GetMean()
            myRMS = tmpHist.GetRMS()
            nEvents = tmpHist.GetEntries()
            value = myRMS

            #Do Langaus fit if histogram mean is larger than 10
            #and mean is larger than RMS (a clear peak away from noise)
            if (value > 0.0 and nEvents > 50):
                tmpHist.Rebin(2)

                myLanGausFunction = fit.fit(tmpHist, fitrange=(myMean-2*myRMS,myMean+3*myRMS))
                myMPV = myLanGausFunction.GetParameter(1)
                mySigma = myLanGausFunction.GetParameter(3)
                value = 1000.0*mySigma
            
                ##For Debugging
                #tmpHist.Draw("hist")
                #myLanGausFunction.Draw("same")
                #canvas.SaveAs("q_"+str(i)+"_"+str(j)+".gif")
                #
                #print ("Bin : " + str(i) + " , " + str(j) + " -> " + str(value))
            else:
                value = 0.0

            list_timeDiff_vs_xy[channel].SetBinContent(i,j,value)
                        
# Plot 2D histograms
outputfile = TFile("plots.root","RECREATE")
for channel in range(0, len(list_timeDiff_vs_xy)):
    list_timeDiff_vs_xy[channel].Draw("colz")
    list_timeDiff_vs_xy[channel].SetStats(0)
    list_timeDiff_vs_xy[channel].SetTitle(names[channel])
    list_timeDiff_vs_xy[channel].SetMinimum(0.0)
    list_timeDiff_vs_xy[channel].SetMaximum(50.0)

    canvas.SaveAs("TimeRes_vs_xy_"+names[channel]+".gif")
    canvas.SaveAs("TimeRes_vs_xy_"+names[channel]+".pdf")

    list_timeDiff_vs_xy[channel].Write()

outputfile.Close()

