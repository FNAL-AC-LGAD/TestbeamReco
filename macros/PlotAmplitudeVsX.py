from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT
import os
import EfficiencyUtils
import langaus
import argparse
import time

gROOT.SetBatch( True )

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-r", "--run", required=False,
   help="run fits or not")
args = vars(ap.parse_args())

RunFits = False
if args['run'] == 'true':
   RunFits = True
     

if (RunFits):
    inputfile = TFile("/uscms/home/amolnar/work/TestbeamReco/test/myoutputfile.root")    
    #inputfile = TFile("/afs/cern.ch/work/s/sixie/public/releases/testbeam/CMSSW_11_2_0_pre5/src/TestbeamReco/test/BNL2020_220V.20210405.root")            
    
    #Get 3D histograms 
    th3_amplitude_vs_xy_channel00 = inputfile.Get("amplitude_vs_xy_channel00")
    th3_amplitude_vs_xy_channel01 = inputfile.Get("amplitude_vs_xy_channel01")
    th3_amplitude_vs_xy_channel02 = inputfile.Get("amplitude_vs_xy_channel02")
    th3_amplitude_vs_xy_channel03 = inputfile.Get("amplitude_vs_xy_channel03")
    th3_amplitude_vs_xy_channel04 = inputfile.Get("amplitude_vs_xy_channel04")
    th3_amplitude_vs_xy_channel05 = inputfile.Get("amplitude_vs_xy_channel05")
    
    th3_amplitude_vs_xy_channelall = inputfile.Get("totamplitude_vs_xy_channel")    

    #list_th3_amplitude_vs_xy = []
    #list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel00)
    #list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel01)
    #list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel02)
    #list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel03)
    #list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel04)
    #list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel05)

    #list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channelall)
    
    
    #Build 2D amp vs x histograms
    amplitude_vs_x_channel00 = th3_amplitude_vs_xy_channel00.Project3D("zx")
    amplitude_vs_x_channel01 = th3_amplitude_vs_xy_channel01.Project3D("zx")
    amplitude_vs_x_channel02 = th3_amplitude_vs_xy_channel02.Project3D("zx")
    amplitude_vs_x_channel03 = th3_amplitude_vs_xy_channel03.Project3D("zx")
    amplitude_vs_x_channel04 = th3_amplitude_vs_xy_channel04.Project3D("zx")
    amplitude_vs_x_channel05 = th3_amplitude_vs_xy_channel05.Project3D("zx")

    amplitude_vs_x_channelall= th3_amplitude_vs_xy_channelall.Project3D("zx")
    
    list_th2_amplitude_vs_x = []
    list_th2_amplitude_vs_x.append(amplitude_vs_x_channel00)
    list_th2_amplitude_vs_x.append(amplitude_vs_x_channel01)
    list_th2_amplitude_vs_x.append(amplitude_vs_x_channel02)
    list_th2_amplitude_vs_x.append(amplitude_vs_x_channel03)
    list_th2_amplitude_vs_x.append(amplitude_vs_x_channel04)
    list_th2_amplitude_vs_x.append(amplitude_vs_x_channel05)

    list_th2_amplitude_vs_x.append(amplitude_vs_x_channelall)
    

    #Build amplitude histograms
    amplitude_vs_x = th3_amplitude_vs_xy_channel00.ProjectionX().Clone("amplitude_vs_x")
    amplitude_vs_x_channel00 = amplitude_vs_x.Clone("amplitude_vs_x_channel00")
    amplitude_vs_x_channel01 = amplitude_vs_x.Clone("amplitude_vs_x_channel01")
    amplitude_vs_x_channel02 = amplitude_vs_x.Clone("amplitude_vs_x_channel02")
    amplitude_vs_x_channel03 = amplitude_vs_x.Clone("amplitude_vs_x_channel03")
    amplitude_vs_x_channel04 = amplitude_vs_x.Clone("amplitude_vs_x_channel04")
    amplitude_vs_x_channel05 = amplitude_vs_x.Clone("amplitude_vs_x_channel05")
 
    amplitude_vs_x_channelall = amplitude_vs_x.Clone("amplitude_vs_x_channelall")
    
    print ("Amplitude vs X: " + str(amplitude_vs_x.GetXaxis().GetBinLowEdge(1)) + " -> " + str(amplitude_vs_x.GetXaxis().GetBinUpEdge(amplitude_vs_x.GetXaxis().GetNbins())))
    

    list_amplitude_vs_x = []
    list_amplitude_vs_x.append(amplitude_vs_x_channel00)
    list_amplitude_vs_x.append(amplitude_vs_x_channel01)
    list_amplitude_vs_x.append(amplitude_vs_x_channel02)
    list_amplitude_vs_x.append(amplitude_vs_x_channel03)
    list_amplitude_vs_x.append(amplitude_vs_x_channel04)
    list_amplitude_vs_x.append(amplitude_vs_x_channel05)

    list_amplitude_vs_x.append(amplitude_vs_x_channelall)
    
    fit = langaus.LanGausFit()
    canvas = TCanvas("cv","cv",800,800)

    #loop over X,Y bins
    for channel in range(0, len(list_amplitude_vs_x)):

        print("Channel : " + str(channel))

        for i in range(1, list_amplitude_vs_x[channel].GetXaxis().GetNbins()):

            #print ("Bin " + str(i))

            ##For Debugging
            #if not (i==46 and j==5):
            #    continue

            tmpHist = list_th2_amplitude_vs_x[channel].ProjectionY("py",i,i)
            myTotalEvents=tmpHist.Integral()
            myMean = tmpHist.GetMean()
            myRMS = tmpHist.GetRMS()
            value = myMean            

            #use coarser bins when the signal is bigger
            if (myMean > 50) :
                tmpHist.Rebin(10)
            else :
                tmpHist.Rebin(5)

            myLanGausFunction = fit.fit(tmpHist, fitrange=(myMean-1*myRMS,myMean+3*myRMS))
            myMPV = myLanGausFunction.GetParameter(1)
            value = myMPV
            print(value)
            ##For Debugging
            tmpHist.Draw("hist")
            myLanGausFunction.Draw("same")
            #canvas.SaveAs("q_"+str(i)+"_"+channel+".gif")

            if (tmpHist.GetEntries() == 0 or not (value == value) or value<0 or value>1000): #or myTotalEvents<200):
               value = 0
            #print(myTotalEvents)
            print ("Bin : " + str(i) + " -> " + str(value))

            list_amplitude_vs_x[channel].SetBinContent(i,value)
            
            
       
            
    # Save amplitude histograms
    outputfile = TFile("plots.root","RECREATE")
    for channel in range(0, len(list_amplitude_vs_x)):
        list_amplitude_vs_x[channel].Write()
    outputfile.Close()



#Make final plots


plotfile = TFile("plots.root","READ")
plotList_amplitude_vs_x  = []
plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel00"))
plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel01"))
plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel02"))
plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel03"))
plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel04"))
plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel05"))

plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channelall"))

  
#Do zero suppression
#for channel in range(0, len(plotList_amplitude_vs_x)):
#    for i in range(1, plotList_amplitude_vs_x[channel].GetXaxis().GetNbins()+1):
#        if plotList_amplitude_vs_x[channel].GetBinContent(i) < 18:
#                plotList_amplitude_vs_x[channel].SetBinContent(i,0)


canvas = TCanvas("cv","cv",800,800)
canvas.SetLeftMargin(0.12)
plotList_amplitude_vs_x[5].Draw("hist")
plotList_amplitude_vs_x[5].SetStats(0)
plotList_amplitude_vs_x[5].SetTitle("")

plotList_amplitude_vs_x[0].GetYaxis().SetTitle("Signal MPV Amplitude [mV]")
plotList_amplitude_vs_x[0].GetYaxis().SetTitleSize(0.05)
plotList_amplitude_vs_x[0].GetYaxis().SetLabelSize(0.035)
plotList_amplitude_vs_x[0].GetYaxis().SetTitleOffset(1.0)
plotList_amplitude_vs_x[0].GetXaxis().SetTitleSize(0.05)
plotList_amplitude_vs_x[0].GetXaxis().SetLabelSize(0.035)
plotList_amplitude_vs_x[0].GetXaxis().SetTitleOffset(0.95)

plotList_amplitude_vs_x[0].SetLineWidth(2)
plotList_amplitude_vs_x[1].SetLineWidth(2)
plotList_amplitude_vs_x[2].SetLineWidth(2)
plotList_amplitude_vs_x[3].SetLineWidth(2)
plotList_amplitude_vs_x[4].SetLineWidth(2)
plotList_amplitude_vs_x[5].SetLineWidth(2)
plotList_amplitude_vs_x[0].SetLineColor(416+2) #kGreen+2
plotList_amplitude_vs_x[1].SetLineColor(432+2) #kCyan+2
plotList_amplitude_vs_x[2].SetLineColor(600) #kBlue
plotList_amplitude_vs_x[3].SetLineColor(880) #kViolet
plotList_amplitude_vs_x[4].SetLineColor(632) #kRed
plotList_amplitude_vs_x[5].SetLineColor(400+2) #kYellow
plotList_amplitude_vs_x[0].Draw("histsame")
plotList_amplitude_vs_x[1].Draw("histsame")
plotList_amplitude_vs_x[2].Draw("histsame")
plotList_amplitude_vs_x[3].Draw("histsame")
plotList_amplitude_vs_x[4].Draw("histsame")
plotList_amplitude_vs_x[5].Draw("histsame")

legend = TLegend(0.65,0.55,0.9,0.8);
legend.SetBorderSize(0)
legend.SetTextSize(0.04)
legend.AddEntry(plotList_amplitude_vs_x[0], "Strip 1")
legend.AddEntry(plotList_amplitude_vs_x[1], "Strip 2")
legend.AddEntry(plotList_amplitude_vs_x[2], "Strip 3")
legend.AddEntry(plotList_amplitude_vs_x[3], "Strip 4")
legend.AddEntry(plotList_amplitude_vs_x[4], "Strip 5")
legend.AddEntry(plotList_amplitude_vs_x[5], "Strip 6")
legend.Draw();

canvas.SaveAs("Amplitude_vs_x.gif")






#totalAmplitude_vs_x = plotList_amplitude_vs_x[0].Clone("totalAmplitude_vs_x")
#for i in range(1, totalAmplitude_vs_x.GetXaxis().GetNbins()+1):
#    totalAmp = plotList_amplitude_vs_x[0].GetBinContent(i) + plotList_amplitude_vs_x[1].GetBinContent(i) + plotList_amplitude_vs_x[2].GetBinContent(i) + plotList_amplitude_vs_x[3].GetBinContent(i) + plotList_amplitude_vs_x[4].GetBinContent(i) + plotList_amplitude_vs_x[5].GetBinContent(i)
#    totalAmplitude_vs_x.SetBinContent(i,totalAmp)

canvas = TCanvas("cv","cv",800,800)
canvas.SetLeftMargin(0.12)
totalAmplitude_vs_x=plotList_amplitude_vs_x[6]
totalAmplitude_vs_x.Draw("hist")
totalAmplitude_vs_x.SetStats(0)
totalAmplitude_vs_x.SetTitle("")
totalAmplitude_vs_x.GetYaxis().SetTitle("Signal MPV Amplitude [mV]")
totalAmplitude_vs_x.GetYaxis().SetTitleSize(0.05)
totalAmplitude_vs_x.GetYaxis().SetLabelSize(0.035)
totalAmplitude_vs_x.GetYaxis().SetTitleOffset(1.0)
totalAmplitude_vs_x.GetXaxis().SetTitleSize(0.05)
totalAmplitude_vs_x.GetXaxis().SetLabelSize(0.035)
totalAmplitude_vs_x.GetXaxis().SetTitleOffset(0.95)
totalAmplitude_vs_x.SetLineWidth(2)
totalAmplitude_vs_x.SetLineColor(1) #kBlack

plotList_amplitude_vs_x[0].Draw("histsame")
plotList_amplitude_vs_x[1].Draw("histsame")
plotList_amplitude_vs_x[2].Draw("histsame")
plotList_amplitude_vs_x[3].Draw("histsame")
plotList_amplitude_vs_x[4].Draw("histsame")
plotList_amplitude_vs_x[5].Draw("histsame")

legend = TLegend(0.65,0.55,0.9,0.8);
legend.SetBorderSize(0)
legend.SetTextSize(0.04)
legend.AddEntry(totalAmplitude_vs_x, "Total")
legend.AddEntry(plotList_amplitude_vs_x[0], "Strip 1")
legend.AddEntry(plotList_amplitude_vs_x[1], "Strip 2")
legend.AddEntry(plotList_amplitude_vs_x[2], "Strip 3")
legend.AddEntry(plotList_amplitude_vs_x[3], "Strip 4")
legend.AddEntry(plotList_amplitude_vs_x[4], "Strip 5")
legend.AddEntry(plotList_amplitude_vs_x[5], "Strip 6")
legend.Draw();


canvas.SaveAs("TotalAmplitude_vs_x.gif")




plotList_amplitudeFraction_vs_x  = []
plotList_amplitudeFraction_vs_x.append(plotList_amplitude_vs_x[0].Clone("amplitudeFraction_vs_x_channel00"))
plotList_amplitudeFraction_vs_x.append(plotList_amplitude_vs_x[0].Clone("amplitudeFraction_vs_x_channel01"))
plotList_amplitudeFraction_vs_x.append(plotList_amplitude_vs_x[0].Clone("amplitudeFraction_vs_x_channel02"))
plotList_amplitudeFraction_vs_x.append(plotList_amplitude_vs_x[0].Clone("amplitudeFraction_vs_x_channel03"))
plotList_amplitudeFraction_vs_x.append(plotList_amplitude_vs_x[0].Clone("amplitudeFraction_vs_x_channel04"))
plotList_amplitudeFraction_vs_x.append(plotList_amplitude_vs_x[0].Clone("amplitudeFraction_vs_x_channel05"))

for channel in range(0, (len(plotList_amplitude_vs_x)-1)):
    for i in range(1, plotList_amplitude_vs_x[channel].GetXaxis().GetNbins()+1):
         totalAmp = plotList_amplitude_vs_x[0].GetBinContent(i) + plotList_amplitude_vs_x[1].GetBinContent(i) + plotList_amplitude_vs_x[2].GetBinContent(i) + plotList_amplitude_vs_x[3].GetBinContent(i) + plotList_amplitude_vs_x[4].GetBinContent(i) + plotList_amplitude_vs_x[5].GetBinContent(i)
         if (totalAmp > 0):
             plotList_amplitudeFraction_vs_x[channel].SetBinContent(i,plotList_amplitude_vs_x[channel].GetBinContent(i)/totalAmp)
         else:
             plotList_amplitudeFraction_vs_x[channel].SetBinContent(i,0)


canvas = TCanvas("cv","cv",800,800)
canvas.SetLeftMargin(0.12)
plotList_amplitudeFraction_vs_x[0].Draw("hist")
plotList_amplitudeFraction_vs_x[0].SetStats(0)
plotList_amplitudeFraction_vs_x[0].SetTitle("")
plotList_amplitudeFraction_vs_x[0].GetXaxis().SetRangeUser(0.16,0.62)
plotList_amplitudeFraction_vs_x[0].SetMaximum(1.0)

plotList_amplitudeFraction_vs_x[0].GetYaxis().SetTitle("Signal Amplitude Fraction")
plotList_amplitudeFraction_vs_x[0].GetYaxis().SetTitleSize(0.05)
plotList_amplitudeFraction_vs_x[0].GetYaxis().SetLabelSize(0.035)
plotList_amplitudeFraction_vs_x[0].GetYaxis().SetTitleOffset(1.0)
plotList_amplitudeFraction_vs_x[0].GetXaxis().SetTitleSize(0.05)
plotList_amplitudeFraction_vs_x[0].GetXaxis().SetLabelSize(0.035)
plotList_amplitudeFraction_vs_x[0].GetXaxis().SetTitleOffset(0.95)

plotList_amplitudeFraction_vs_x[0].SetLineWidth(2)
plotList_amplitudeFraction_vs_x[1].SetLineWidth(2)
plotList_amplitudeFraction_vs_x[2].SetLineWidth(2)
plotList_amplitudeFraction_vs_x[3].SetLineWidth(2)
plotList_amplitudeFraction_vs_x[4].SetLineWidth(2)
plotList_amplitudeFraction_vs_x[5].SetLineWidth(2)
plotList_amplitudeFraction_vs_x[0].SetLineColor(416+2) #kGreen+2
plotList_amplitudeFraction_vs_x[1].SetLineColor(432+2) #kCyan+2
plotList_amplitudeFraction_vs_x[2].SetLineColor(600) #kBlue
plotList_amplitudeFraction_vs_x[3].SetLineColor(880) #kViolet
plotList_amplitudeFraction_vs_x[4].SetLineColor(632) #kRed
plotList_amplitudeFraction_vs_x[5].SetLineColor(400+2) #kYellow
plotList_amplitudeFraction_vs_x[1].Draw("histsame")
plotList_amplitudeFraction_vs_x[2].Draw("histsame")
plotList_amplitudeFraction_vs_x[3].Draw("histsame")
plotList_amplitudeFraction_vs_x[4].Draw("histsame")
plotList_amplitudeFraction_vs_x[5].Draw("histsame")

legend = TLegend(0.4,0.65,0.7,0.88);
legend.SetBorderSize(0)
legend.SetTextSize(0.04)
legend.AddEntry(plotList_amplitudeFraction_vs_x[0], "Strip 1")
legend.AddEntry(plotList_amplitudeFraction_vs_x[1], "Strip 2")
legend.AddEntry(plotList_amplitudeFraction_vs_x[2], "Strip 3")
legend.AddEntry(plotList_amplitudeFraction_vs_x[3], "Strip 4")
legend.AddEntry(plotList_amplitudeFraction_vs_x[4], "Strip 5")
legend.AddEntry(plotList_amplitudeFraction_vs_x[5], "Strip 6")
legend.Draw();

canvas.SaveAs("AmplitudeFraction_vs_x.gif")


