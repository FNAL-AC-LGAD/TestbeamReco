from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TH1D,TH2D,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle
import os
import EfficiencyUtils
import langaus
import optparse
import time
from stripBox import getStripBox,getStripBoxY
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.25)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-f', dest='file', default = "myoutputfile.root", help="File name (or path from ../test/)")
parser.add_option('-s','--sensor', dest='sensor', default = "HPK C2", help="Type of sensor (BNL, HPK, ...)")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 180, help="Bias Voltage value in [V]")
options, args = parser.parse_args()

file = options.file
sensor = options.sensor
bias = options.biasvolt

projection = ["zx","zy"]

for l in range(len(projection)) : 
        
    inputfile = TFile("../test/"+file)
    #Define histo names
    
    if (l==0) :
        h00 = "amplitudeTop_vs_xy_channel00"
        h01 = "amplitudeTop_vs_xy_channel01"
        h10 = "amplitudeBot_vs_xy_channel10"
        h11 = "amplitudeBot_vs_xy_channel11"
        htot = "totamplitudePad_vs_xy"
    else :
        h00 = "amplitudeLeft_vs_xy_channel00"
        h01 = "amplitudeRight_vs_xy_channel01"
        h10 = "amplitudeLeft_vs_xy_channel10"
        h11 = "amplitudeRight_vs_xy_channel11"
        htot = "totamplitudePad_vs_xy"


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
        centerShift = (inputfile.Get("stripBoxInfo00").GetMean(1)+inputfile.Get("stripBoxInfo01").GetMean(1))/2.
    else :
        amplitude_vs_x = th3_amplitude_vs_xy_channel00.ProjectionY().Clone("amplitude_vs_x")
        centerShift = (inputfile.Get("stripBoxInfoY00").GetMean(1)+inputfile.Get("stripBoxInfoY11").GetMean(1))/2.

    xbin = amplitude_vs_x.GetXaxis().GetNbins() #, amplitude_vs_x.GetYaxis().GetNbins()
    xmin, xmax = amplitude_vs_x.GetXaxis().GetXmin()-centerShift, amplitude_vs_x.GetXaxis().GetXmax()-centerShift
    # ymin, ymax = amplitude_vs_x.GetYaxis().GetXmin(), amplitude_vs_x.GetYaxis().GetXmax()
    amplitude_vs_x_channel00 = TH1D("amplitude_vs_x_channel00","",xbin,xmin,xmax) #amplitude_vs_x.Clone("amplitude_vs_x_channel00")
    amplitude_vs_x_channel01 = TH1D("amplitude_vs_x_channel01","",xbin,xmin,xmax) #amplitude_vs_x.Clone("amplitude_vs_x_channel01")
    amplitude_vs_x_channel10 = TH1D("amplitude_vs_x_channel10","",xbin,xmin,xmax) #amplitude_vs_x.Clone("amplitude_vs_x_channel10")
    amplitude_vs_x_channel11 = TH1D("amplitude_vs_x_channel11","",xbin,xmin,xmax) #amplitude_vs_x.Clone("amplitude_vs_x_channel11")
    amplitude_vs_x_channelall = TH1D("amplitude_vs_x_channelall","",xbin,xmin,xmax) #amplitude_vs_x.Clone("amplitude_vs_x_channelall")
    
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
    canvas = TCanvas("cv","cv",1000,800)

    maxAmpALL = 0
    #loop over X,Y bins
    for channel in range(0, len(list_amplitude_vs_x)):
        print("Channel : " + str(channel))
        maxAmp = [0,0,0]
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
                # if (channel==0): canvas.SaveAs("q_"+str(i)+"_"+str(channel)+".gif")
            else:
                value = 0.0

            value = value if(value>0.0) else 0.0

            if channel!=(len(list_amplitude_vs_x)-1):
                for j in range(3):
                    if value>maxAmp[j]:
                        for j2 in range(2,j-1,-1):
                            if j2!=j: maxAmp[j2] = maxAmp[j2-1]
                            else: maxAmp[j2] = value
                        break

            #print(myTotalEvents)
            #print ("Bin : " + str(i) + " -> " + str(value))

            list_amplitude_vs_x[channel].SetBinContent(i,value)
        
        if channel!=(len(list_amplitude_vs_x)-1):
            print("Amp1 = "+str(maxAmp[0])+"; Amp2 = "+str(maxAmp[1])+"; Amp3 = "+str(maxAmp[2]))
            print("Average Amp = " + str((maxAmp[0]+maxAmp[1]+maxAmp[2])/3))
            maxAmpALL+=(maxAmp[0]+maxAmp[1]+maxAmp[2])/3
    print("Total Average amp = "+str(maxAmpALL/4))
    
    for b in range(1, list_amplitude_vs_x[0].GetXaxis().GetNbins()):
        for ch in range(0, len(list_amplitude_vs_x)):
            if list_amplitude_vs_x[ch].GetBinContent(b)==0:
                list_amplitude_vs_x[len(list_amplitude_vs_x)-1].SetBinContent(b,0)
                break

    # Save amplitude histograms
    outputfile = TFile("PlotAmplitudeVsXandY.root","RECREATE")
    for channel in range(0, len(list_amplitude_vs_x)):
        list_amplitude_vs_x[channel].Write()
    outputfile.Close()

    #Make final plots
    plotfile = TFile("PlotAmplitudeVsXandY.root","READ")
    plotList_amplitude_vs_x  = []
    plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel00"))
    plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel01"))
    plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel10"))
    plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel11"))
    # plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channelall"))
    
    print(plotList_amplitude_vs_x[3])
      
    #Do zero suppression
    #for channel in range(0, len(plotList_amplitude_vs_x)):
    #    for i in range(1, plotList_amplitude_vs_x[channel].GetXaxis().GetNbins()+1):
    #        if plotList_amplitude_vs_x[channel].GetBinContent(i) < 18:
    #                plotList_amplitude_vs_x[channel].SetBinContent(i,0)

    
    # plotList_amplitude_vs_x[0].SetLineWidth(2)
    # plotList_amplitude_vs_x[1].SetLineWidth(2)
    # plotList_amplitude_vs_x[2].SetLineWidth(2)
    # plotList_amplitude_vs_x[3].SetLineWidth(2)
    plotList_amplitude_vs_x[0].SetLineColor(416+2) #kGreen+2
    plotList_amplitude_vs_x[1].SetLineColor(432+2) #kCyan+2
    plotList_amplitude_vs_x[2].SetLineColor(600) #kBlue
    plotList_amplitude_vs_x[3].SetLineColor(880) #kViolet
    # plotList_amplitude_vs_x[0].Draw("histsame")
    # plotList_amplitude_vs_x[1].Draw("histsame")
    # plotList_amplitude_vs_x[2].Draw("histsame")
    # plotList_amplitude_vs_x[3].Draw("histsame")
    
    canvas = TCanvas("cv2","cv2",1000,800)
    #totalAmplitude_vs_x=plotList_amplitude_vs_x[0]
    totalAmplitude_vs_x=TH1F("htemp","",1,-0.52, 0.52)
    totalAmplitude_vs_x.Draw("hist")
    totalAmplitude_vs_x.SetStats(0)
    totalAmplitude_vs_x.SetTitle("")
    totalAmplitude_vs_x.GetYaxis().SetTitle("Signal MPV Amplitude [mV]")
    # totalAmplitude_vs_x.GetYaxis().SetTitleSize(0.035) #0.05
    # totalAmplitude_vs_x.GetYaxis().SetLabelSize(0.035)
    #totalAmplitude_vs_x.GetYaxis().SetTitleOffset(1.6) #0.95
    axis_label = "x" if l==0 else "y"
    totalAmplitude_vs_x.GetXaxis().SetTitle("Track "+ axis_label +" position [mm]")
    #totalAmplitude_vs_x.GetXaxis().SetRangeUser(-0.52, 0.52)
    # totalAmplitude_vs_x.GetXaxis().SetTitleSize(0.035) #0.05
    # totalAmplitude_vs_x.GetXaxis().SetLabelSize(0.035)
    #totalAmplitude_vs_x.GetXaxis().SetTitleOffset(1.3) #0.95
    # totalAmplitude_vs_x.SetLineWidth(2)
    # totalAmplitude_vs_x.SetLineColor(1) #kBlack
    
    # ymin = totalAmplitude_vs_x.GetMinimum()
    # ymax = totalAmplitude_vs_x.GetMaximum()
    ymin = 0
    ymax = 180
    totalAmplitude_vs_x.SetMinimum(ymin)
    totalAmplitude_vs_x.SetMaximum(ymax)
   
    if (l==0) :
        boxes = getStripBox(inputfile,ymin,150,False,18,False,centerShift)
    else : 
        boxes = getStripBoxY(inputfile,ymin,150,False,18,centerShift)
    for box in boxes:
       box.Draw() 
    totalAmplitude_vs_x.Draw("AXIS same")
    totalAmplitude_vs_x.Draw("hist same")
    
    plotList_amplitude_vs_x[0].Draw("histsame")
    plotList_amplitude_vs_x[1].Draw("histsame")
    plotList_amplitude_vs_x[2].Draw("histsame")
    plotList_amplitude_vs_x[3].Draw("histsame")
    # plotList_amplitude_vs_x[4].Draw("histsame")

    
    #legend = TLegend(0.12,0.65,0.30,0.85);
    legend = TLegend(2*myStyle.GetMargin()+0.02,1-myStyle.GetMargin()-0.02-0.1,1-myStyle.GetMargin()-0.02,1-myStyle.GetMargin()-0.02)
    legend.SetNColumns(2)
    legend.SetBorderSize(0)
    # legend.SetFillStyle(0)
    legend.SetFillColor(0)
    legend.SetTextFont(myStyle.GetFont())
    legend.SetTextSize(myStyle.GetSize())
    # legend.AddEntry(totalAmplitude_vs_x, "Total")
    legend.AddEntry(plotList_amplitude_vs_x[1], "Top left pad")
    legend.AddEntry(plotList_amplitude_vs_x[0], "Top right pad")
    legend.AddEntry(plotList_amplitude_vs_x[3], "Bottom left pad")
    legend.AddEntry(plotList_amplitude_vs_x[2], "Bottom right pad")
    legend.Draw();

    myStyle.BeamInfo()
    myStyle.SensorInfo(sensor, bias)
 
    if l==0 : 
        canvas.SaveAs("TotalAmplitude_vs_x.pdf")
    else :
        canvas.SaveAs("TotalAmplitude_vs_y.pdf")
