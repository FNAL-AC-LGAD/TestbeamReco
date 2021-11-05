from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle
import os
import EfficiencyUtils
import langaus
import optparse
import time
from stripBox import getStripBox,getStripBoxY

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('--plotsonly', dest='plotsonly', action='store_false', default = True, help="run fits or not")
parser.add_option('-t', dest='UseRawHistos', action='store_true', default = False, help="Use nominal amp or raw histograms")
options, args = parser.parse_args()

RunFits = options.plotsonly
UseRawHistos = options.UseRawHistos
suffex = "_raw" if UseRawHistos else ""

projection = ["zx","zy"]

for l in range(len(projection)) : 
        
    inputfile = TFile("../test/myoutputfile.root")     
    if (RunFits):
        #Define histo names
        GoodHistos = not UseRawHistos
        
        if (l==0) :
            h00 = "amplitudeTop_vs_xy_channel00" if GoodHistos else "raw_amp_vs_xy_channel00"
            h01 = "amplitudeTop_vs_xy_channel01" if GoodHistos else "raw_amp_vs_xy_channel01"
            h10 = "amplitudeBot_vs_xy_channel10" if GoodHistos else "raw_amp_vs_xy_channel10"
            h11 = "amplitudeBot_vs_xy_channel11" if GoodHistos else "raw_amp_vs_xy_channel11"
            htot = "totamplitudePad_vs_xy" if GoodHistos else "totrawamplitude_vs_xy"
        else :
            h00 = "amplitudeLeft_vs_xy_channel00" if GoodHistos else "raw_amp_vs_xy_channel00"
            h01 = "amplitudeRight_vs_xy_channel01" if GoodHistos else "raw_amp_vs_xy_channel01"
            h10 = "amplitudeLeft_vs_xy_channel10" if GoodHistos else "raw_amp_vs_xy_channel10"
            h11 = "amplitudeRight_vs_xy_channel11" if GoodHistos else "raw_amp_vs_xy_channel11"
            htot = "totamplitudePad_vs_xy" if GoodHistos else "totrawamplitude_vs_xy"

    
        #Get 3D histograms 
        th3_amplitude_vs_xy_channel00 = inputfile.Get(h00)
        th3_amplitude_vs_xy_channel01 = inputfile.Get(h01)
        th3_amplitude_vs_xy_channel10 = inputfile.Get(h10)
        th3_amplitude_vs_xy_channel11 = inputfile.Get(h11)
        th3_amplitude_vs_xy_channelall = inputfile.Get(htot)    
        
        #Build 2D amp vs x histograms
        amplitude_vs_x_channel00 = th3_amplitude_vs_xy_channel00.Project3D(projection[l])
        amplitude_vs_x_channel01 = th3_amplitude_vs_xy_channel01.Project3D(projection[l])
        amplitude_vs_x_channel10 = th3_amplitude_vs_xy_channel10.Project3D(projection[l])
        amplitude_vs_x_channel11 = th3_amplitude_vs_xy_channel11.Project3D(projection[l])
        amplitude_vs_x_channelall= th3_amplitude_vs_xy_channelall.Project3D(projection[l])

        list_th2_amplitude_vs_x = []
        list_th2_amplitude_vs_x.append(amplitude_vs_x_channel00)
        list_th2_amplitude_vs_x.append(amplitude_vs_x_channel01)
        list_th2_amplitude_vs_x.append(amplitude_vs_x_channel10)
        list_th2_amplitude_vs_x.append(amplitude_vs_x_channel11)
        list_th2_amplitude_vs_x.append(amplitude_vs_x_channelall)
        
        #Build amplitude histograms

        if l==0 :
            amplitude_vs_x = th3_amplitude_vs_xy_channel00.ProjectionX().Clone("amplitude_vs_x")
        else :
            amplitude_vs_x = th3_amplitude_vs_xy_channel00.ProjectionY().Clone("amplitude_vs_x")
       
        amplitude_vs_x_channel00 = amplitude_vs_x.Clone("amplitude_vs_x_channel00")
        amplitude_vs_x_channel01 = amplitude_vs_x.Clone("amplitude_vs_x_channel01")
        amplitude_vs_x_channel10 = amplitude_vs_x.Clone("amplitude_vs_x_channel10")
        amplitude_vs_x_channel11 = amplitude_vs_x.Clone("amplitude_vs_x_channel11")
        amplitude_vs_x_channelall = amplitude_vs_x.Clone("amplitude_vs_x_channelall")
        
        print ("Amplitude vs X: " + str(amplitude_vs_x.GetXaxis().GetBinLowEdge(1)) + " -> " + str(amplitude_vs_x.GetXaxis().GetBinUpEdge(amplitude_vs_x.GetXaxis().GetNbins())))
        
        list_amplitude_vs_x = []
        list_amplitude_vs_x.append(amplitude_vs_x_channel00)
        list_amplitude_vs_x.append(amplitude_vs_x_channel01)
        list_amplitude_vs_x.append(amplitude_vs_x_channel10)
        list_amplitude_vs_x.append(amplitude_vs_x_channel11)
        list_amplitude_vs_x.append(amplitude_vs_x_channelall)
    
        print("Setting up Langaus")
        fit = langaus.LanGausFit()
        print("Setup Langaus")
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
                nEvents = tmpHist.GetEntries()
    
                if(nEvents > 50):
                    #use coarser bins when the signal is bigger
                    if (myMean > 50) :
                        tmpHist.Rebin(5)
                    else :
                        tmpHist.Rebin(10)
                    
                    myLanGausFunction = fit.fit(tmpHist, fitrange=(myMean-1*myRMS,myMean+3*myRMS))
                    myMPV = myLanGausFunction.GetParameter(1)
                    value = myMPV
    
                    ##For Debugging
                    tmpHist.Draw("hist")
                    myLanGausFunction.Draw("same")
                    #canvas.SaveAs("q_"+str(i)+"_"+str(channel)+".gif")
                else:
                   value = 0.0
    
                value = value if(value>0.0) else 0.0
    
                #print(myTotalEvents)
                #print ("Bin : " + str(i) + " -> " + str(value))
    
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
    plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel10"))
    plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel11"))
    plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channelall"))
    
    print(plotList_amplitude_vs_x[3])
      
    #Do zero suppression
    #for channel in range(0, len(plotList_amplitude_vs_x)):
    #    for i in range(1, plotList_amplitude_vs_x[channel].GetXaxis().GetNbins()+1):
    #        if plotList_amplitude_vs_x[channel].GetBinContent(i) < 18:
    #                plotList_amplitude_vs_x[channel].SetBinContent(i,0)
    
    
    canvas = TCanvas("cvv","cvv",800,800)
    canvas.SetLeftMargin(0.12)
    plotList_amplitude_vs_x[0].GetYaxis().SetRangeUser(0,150)
    plotList_amplitude_vs_x[0].Draw("hist")
    plotList_amplitude_vs_x[0].SetStats(0)
    plotList_amplitude_vs_x[0].SetTitle("")
    
    ymin = plotList_amplitude_vs_x[3].GetMinimum()
    ymax = plotList_amplitude_vs_x[3].GetMaximum()
    plotList_amplitude_vs_x[3].SetMaximum(ymax*1.05)
  
    if (l==0) :
        boxes = getStripBox(inputfile,ymin,ymax*1.04,False,18,False)
    else : 
        boxes = getStripBoxY(inputfile,ymin,ymax*1.04,False,18)
    for box in boxes:
       box.Draw()
    plotList_amplitude_vs_x[3].Draw("AXIS same")
    plotList_amplitude_vs_x[3].Draw("hist same")
     
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
    plotList_amplitude_vs_x[0].SetLineColor(416+2) #kGreen+2
    plotList_amplitude_vs_x[1].SetLineColor(432+2) #kCyan+2
    plotList_amplitude_vs_x[2].SetLineColor(600) #kBlue
    plotList_amplitude_vs_x[3].SetLineColor(880) #kViolet
    plotList_amplitude_vs_x[0].Draw("histsame")
    plotList_amplitude_vs_x[1].Draw("histsame")
    plotList_amplitude_vs_x[2].Draw("histsame")
    plotList_amplitude_vs_x[3].Draw("histsame")
    
    legend = TLegend(0.15,0.65,0.25,0.85);
    legend.SetBorderSize(0)
    legend.SetTextSize(0.04)
    legend.AddEntry(plotList_amplitude_vs_x[0], "Pad 00")
    legend.AddEntry(plotList_amplitude_vs_x[1], "Pad 01")
    legend.AddEntry(plotList_amplitude_vs_x[2], "Pad 10")
    legend.AddEntry(plotList_amplitude_vs_x[3], "Pad 11")
    legend.Draw();
   
    if l==0 :
        canvas.SaveAs("Amplitude_vs_x"+suffex+".pdf")
    else :
        canvas.SaveAs("Amplitude_vs_y"+suffex+".pdf")
         
    #totalAmplitude_vs_x = plotList_amplitude_vs_x[0].Clone("totalAmplitude_vs_x")
    #for i in range(1, totalAmplitude_vs_x.GetXaxis().GetNbins()+1):
    #    totalAmp = plotList_amplitude_vs_x[0].GetBinContent(i) + plotList_amplitude_vs_x[1].GetBinContent(i) + plotList_amplitude_vs_x[2].GetBinContent(i) + plotList_amplitude_vs_x[3].GetBinContent(i) + plotList_amplitude_vs_x[4].GetBinContent(i) + plotList_amplitude_vs_x[5].GetBinContent(i)
    #    totalAmplitude_vs_x.SetBinContent(i,totalAmp)
    
    canvas = TCanvas("cv2","cv2",800,800)
    canvas.SetLeftMargin(0.12)
    totalAmplitude_vs_x=plotList_amplitude_vs_x[4]
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
    
    ymin = totalAmplitude_vs_x.GetMinimum()
    ymax = totalAmplitude_vs_x.GetMaximum()
    totalAmplitude_vs_x.SetMaximum(ymax*1.05)
   
    if (l==0) :
        boxes = getStripBox(inputfile,ymin,ymax*1.04,False,18,False)
    else : 
        boxes = getStripBoxY(inputfile,ymin,ymax*1.04,False,18)
    for box in boxes:
       box.Draw() 
    totalAmplitude_vs_x.Draw("AXIS same")
    totalAmplitude_vs_x.Draw("hist same")
    
    plotList_amplitude_vs_x[0].Draw("histsame")
    plotList_amplitude_vs_x[1].Draw("histsame")
    plotList_amplitude_vs_x[2].Draw("histsame")
    plotList_amplitude_vs_x[3].Draw("histsame")
    plotList_amplitude_vs_x[4].Draw("histsame")

    
    legend = TLegend(0.15,0.65,0.25,0.85);
    legend.SetBorderSize(0)
    legend.SetTextSize(0.04)
    legend.AddEntry(totalAmplitude_vs_x, "Total")
    legend.AddEntry(plotList_amplitude_vs_x[0], "Pad 00")
    legend.AddEntry(plotList_amplitude_vs_x[1], "Pad 01")
    legend.AddEntry(plotList_amplitude_vs_x[2], "Pad 10")
    legend.AddEntry(plotList_amplitude_vs_x[3], "Pad 11")
    legend.Draw();
 
    if l==0 : 
        canvas.SaveAs("TotalAmplitude_vs_x"+suffex+".pdf")
    else :
        canvas.SaveAs("TotalAmplitude_vs_y"+suffex+".pdf")
 
        
    
    plotList_amplitudeFraction_vs_x  = []
    plotList_amplitudeFraction_vs_x.append(plotList_amplitude_vs_x[0].Clone("amplitudeFraction_vs_x_channel00"))
    plotList_amplitudeFraction_vs_x.append(plotList_amplitude_vs_x[0].Clone("amplitudeFraction_vs_x_channel01"))
    plotList_amplitudeFraction_vs_x.append(plotList_amplitude_vs_x[0].Clone("amplitudeFraction_vs_x_channel10"))
    plotList_amplitudeFraction_vs_x.append(plotList_amplitude_vs_x[0].Clone("amplitudeFraction_vs_x_channel11"))
    
    for channel in range(0, (len(plotList_amplitude_vs_x)-1)):
        for i in range(0, plotList_amplitude_vs_x[channel].GetXaxis().GetNbins()+1):
             totalAmp = plotList_amplitude_vs_x[0].GetBinContent(i) + plotList_amplitude_vs_x[1].GetBinContent(i) + plotList_amplitude_vs_x[2].GetBinContent(i) + plotList_amplitude_vs_x[3].GetBinContent(i)
             if (totalAmp > 0):
                 plotList_amplitudeFraction_vs_x[channel].SetBinContent(i,plotList_amplitude_vs_x[channel].GetBinContent(i)/totalAmp)
             else:
                 plotList_amplitudeFraction_vs_x[channel].SetBinContent(i,0)
    
    
    canvas = TCanvas("c","c",800,800)
    canvas.SetLeftMargin(0.12)
    plotList_amplitudeFraction_vs_x[0].Draw("hist")
    plotList_amplitudeFraction_vs_x[0].SetStats(0)
    plotList_amplitudeFraction_vs_x[0].SetTitle("")
    plotList_amplitudeFraction_vs_x[0].SetMaximum(1.05)
    
    ymin = plotList_amplitudeFraction_vs_x[0].GetMinimum()
    #ymax = plotList_amplitudeFraction_vs_x[0].GetMaximum()
    ymax = 1.0

    if (l==0) :
        boxes = getStripBox(inputfile,ymin,ymax*1.04,False,18,False)
    else : 
        boxes = getStripBoxY(inputfile,ymin,ymax*1.04,False,18)
    
    for box in boxes:
       box.Draw()
    plotList_amplitudeFraction_vs_x[0].Draw("AXIS same")
    plotList_amplitudeFraction_vs_x[0].Draw("hist same")
    
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
    plotList_amplitudeFraction_vs_x[0].SetLineColor(416+2) #kGreen+2
    plotList_amplitudeFraction_vs_x[1].SetLineColor(432+2) #kCyan+2
    plotList_amplitudeFraction_vs_x[2].SetLineColor(600) #kBlue
    plotList_amplitudeFraction_vs_x[3].SetLineColor(880) #kViolet
    plotList_amplitudeFraction_vs_x[1].Draw("histsame")
    plotList_amplitudeFraction_vs_x[2].Draw("histsame")
    plotList_amplitudeFraction_vs_x[3].Draw("histsame")
    
    legend = TLegend(0.4,0.65,0.7,0.88);
    legend.SetBorderSize(0)
    legend.SetTextSize(0.04)
    legend.AddEntry(plotList_amplitudeFraction_vs_x[0], "Pad 00")
    legend.AddEntry(plotList_amplitudeFraction_vs_x[1], "Pad 01")
    legend.AddEntry(plotList_amplitudeFraction_vs_x[2], "Pad 10")
    legend.AddEntry(plotList_amplitudeFraction_vs_x[3], "Pad 11")
    legend.Draw();
    
    plotList_amplitudeFraction_vs_x[0].Draw("AXIS same")
    plotList_amplitudeFraction_vs_x[0].Draw("hist same")
  
    if l==0 : 
        canvas.SaveAs("AmplitudeFraction_vs_x"+suffex+".pdf")
    else :
        canvas.SaveAs("AmplitudeFraction_vs_y"+suffex+".pdf")

