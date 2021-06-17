from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack
import os
from stripBox import getStripBox

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

inputfile = TFile("../test/myoutputfile.root")

#Build 2D deltaX vs x histograms
th2_deltaX_vs_x_channel00 = inputfile.Get("deltaX_vs_Xtrack")

list_th2_deltaX_vs_x = []
list_th2_deltaX_vs_x.append(th2_deltaX_vs_x_channel00)

names = [
    "deltaX_vs_x",
]

#Build deltaX histograms
deltaX_vs_x = th2_deltaX_vs_x_channel00.ProjectionX().Clone("deltaX_vs_x_channel")
deltaX_vs_x_channel00 = deltaX_vs_x.Clone("deltaX_vs_x_channel00")

list_deltaX_vs_x = []
list_deltaX_vs_x.append(deltaX_vs_x_channel00)
print("Finished cloning histograms")

canvas = TCanvas("cv","cv",800,800)
gPad.SetLeftMargin(0.12)
gPad.SetRightMargin(0.15)
gPad.SetTopMargin(0.08)
gPad.SetBottomMargin(0.12)
gPad.SetTicks(1,1)
print("Finished setting up langaus fit class")

#loop over X bins
for i in range(0, deltaX_vs_x.GetXaxis().GetNbins()+1):
    ##For Debugging
    #if not (i==46 and j==5):
    #    continue

    for channel in range(0, len(list_deltaX_vs_x)):
        tmpHist = list_th2_deltaX_vs_x[channel].ProjectionY("py",i,i)
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
            tmpHist.Rebin(2)

            fit = TF1('fit','gaus',fitlow,fithigh)
            tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
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

        list_deltaX_vs_x[channel].SetBinContent(i,value)
        list_deltaX_vs_x[channel].SetBinError(i,error)
                        
# Plot 2D histograms
outputfile = TFile("plots.root","RECREATE")
for channel in range(0, len(list_deltaX_vs_x)):
    list_deltaX_vs_x[channel].Draw("hist e")
    list_deltaX_vs_x[channel].SetStats(0)
    list_deltaX_vs_x[channel].SetTitle(names[channel])
    list_deltaX_vs_x[channel].SetMinimum(0.0)
    list_deltaX_vs_x[channel].SetMaximum(30.0)
    list_deltaX_vs_x[channel].SetLineColor(kBlack)

    ymin = list_deltaX_vs_x[channel].GetMinimum()
    ymax = list_deltaX_vs_x[channel].GetMaximum()
    boxes = getStripBox(inputfile,ymin,ymax)
    for box in boxes:
        box.Draw()
    list_deltaX_vs_x[channel].Draw("AXIS same")
    list_deltaX_vs_x[channel].Draw("hist e same")

    canvas.SaveAs("PositionRes_vs_x_"+names[channel]+".gif")
    canvas.SaveAs("PositionRes_vs_x_"+names[channel]+".pdf")

    list_deltaX_vs_x[channel].Write()

outputfile.Close()

