from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite
import os
import EfficiencyUtils
import langaus
import optparse
import time
from stripBox import getStripBox
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-f', dest='file', default = "myoutputfile.root", help="File name (or path from ../test/)")
parser.add_option('-s','--sensor', dest='sensor', default = "BNL2020", help="Type of sensor (BNL, HPK, ...)")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 220, help="Bias Voltage value in [V]")
options, args = parser.parse_args()

file = options.file
sensor = options.sensor
bias = options.biasvolt

inputfile = TFile("../test/"+file,"READ")

colors = myStyle.GetColors(True)

#Define histo names
h00 = "amplitude_vs_xy_channel00"
h01 = "amplitude_vs_xy_channel01"
h02 = "amplitude_vs_xy_channel02"
h03 = "amplitude_vs_xy_channel03"
h04 = "amplitude_vs_xy_channel04"
h05 = "amplitude_vs_xy_channel05"
h06 = "amplitude_vs_xy_channel06"
htot = "totamplitude_vs_xy"

#Get 3D histograms 
th3_amplitude_vs_xy_channel00 = inputfile.Get(h00)
th3_amplitude_vs_xy_channel01 = inputfile.Get(h01)
th3_amplitude_vs_xy_channel02 = inputfile.Get(h02)
th3_amplitude_vs_xy_channel03 = inputfile.Get(h03)
th3_amplitude_vs_xy_channel04 = inputfile.Get(h04)
th3_amplitude_vs_xy_channel05 = inputfile.Get(h05)
th3_amplitude_vs_xy_channel06 = inputfile.Get(h06)
th3_amplitude_vs_xy_channelall = inputfile.Get(htot)

#th3_amplitude_vs_xy_channel00.RebinX(3)
#th3_amplitude_vs_xy_channel01.RebinX(3)
#th3_amplitude_vs_xy_channel02.RebinX(3)
#th3_amplitude_vs_xy_channel03.RebinX(3)
#th3_amplitude_vs_xy_channel04.RebinX(3)
#th3_amplitude_vs_xy_channel05.RebinX(3)
#th3_amplitude_vs_xy_channel06.RebinX(3)
#th3_amplitude_vs_xy_channelall.RebinX(3)

#shift = (inputfile.Get("stripBoxInfo02").GetMean(1)+inputfile.Get("stripBoxInfo03").GetMean(1))/2.
shift = inputfile.Get("stripBoxInfo03").GetMean(1)

#Build 2D amp vs x histograms
amplitude_vs_x_channel00 = th3_amplitude_vs_xy_channel00.Project3D("zx")
amplitude_vs_x_channel01 = th3_amplitude_vs_xy_channel01.Project3D("zx")
amplitude_vs_x_channel02 = th3_amplitude_vs_xy_channel02.Project3D("zx")
amplitude_vs_x_channel03 = th3_amplitude_vs_xy_channel03.Project3D("zx")
amplitude_vs_x_channel04 = th3_amplitude_vs_xy_channel04.Project3D("zx")
amplitude_vs_x_channel05 = th3_amplitude_vs_xy_channel05.Project3D("zx")
amplitude_vs_x_channel06 = th3_amplitude_vs_xy_channel06.Project3D("zx")
amplitude_vs_x_channelall= th3_amplitude_vs_xy_channelall.Project3D("zx")

list_th2_amplitude_vs_x = []
list_th2_amplitude_vs_x.append(amplitude_vs_x_channel00)
list_th2_amplitude_vs_x.append(amplitude_vs_x_channel01)
list_th2_amplitude_vs_x.append(amplitude_vs_x_channel02)
list_th2_amplitude_vs_x.append(amplitude_vs_x_channel03)
list_th2_amplitude_vs_x.append(amplitude_vs_x_channel04)
list_th2_amplitude_vs_x.append(amplitude_vs_x_channel05)
list_th2_amplitude_vs_x.append(amplitude_vs_x_channel06)
list_th2_amplitude_vs_x.append(amplitude_vs_x_channelall)

#Build amplitude histograms
th1 = th3_amplitude_vs_xy_channel00.ProjectionX().Clone("th1")
amplitude_vs_x_channel00 = TH1F("amplitude_vs_x_channel00","",th1.GetXaxis().GetNbins(),th1.GetXaxis().GetXmin()-shift,th1.GetXaxis().GetXmax()-shift)
amplitude_vs_x_channel01 = TH1F("amplitude_vs_x_channel01","",th1.GetXaxis().GetNbins(),th1.GetXaxis().GetXmin()-shift,th1.GetXaxis().GetXmax()-shift)
amplitude_vs_x_channel02 = TH1F("amplitude_vs_x_channel02","",th1.GetXaxis().GetNbins(),th1.GetXaxis().GetXmin()-shift,th1.GetXaxis().GetXmax()-shift)
amplitude_vs_x_channel03 = TH1F("amplitude_vs_x_channel03","",th1.GetXaxis().GetNbins(),th1.GetXaxis().GetXmin()-shift,th1.GetXaxis().GetXmax()-shift)
amplitude_vs_x_channel04 = TH1F("amplitude_vs_x_channel04","",th1.GetXaxis().GetNbins(),th1.GetXaxis().GetXmin()-shift,th1.GetXaxis().GetXmax()-shift)
amplitude_vs_x_channel05 = TH1F("amplitude_vs_x_channel05","",th1.GetXaxis().GetNbins(),th1.GetXaxis().GetXmin()-shift,th1.GetXaxis().GetXmax()-shift)
amplitude_vs_x_channel06 = TH1F("amplitude_vs_x_channel06","",th1.GetXaxis().GetNbins(),th1.GetXaxis().GetXmin()-shift,th1.GetXaxis().GetXmax()-shift)
amplitude_vs_x_channelall = TH1F("amplitude_vs_x_channelall","",th1.GetXaxis().GetNbins(),th1.GetXaxis().GetXmin()-shift,th1.GetXaxis().GetXmax()-shift)

print ("Amplitude vs X: " + str(th1.GetXaxis().GetBinLowEdge(1)-shift) + " -> " + str(th1.GetXaxis().GetBinUpEdge(th1.GetXaxis().GetNbins())-shift))

list_amplitude_vs_x = []
list_amplitude_vs_x.append(amplitude_vs_x_channel00)
list_amplitude_vs_x.append(amplitude_vs_x_channel01)
list_amplitude_vs_x.append(amplitude_vs_x_channel02)
list_amplitude_vs_x.append(amplitude_vs_x_channel03)
list_amplitude_vs_x.append(amplitude_vs_x_channel04)
list_amplitude_vs_x.append(amplitude_vs_x_channel05)
list_amplitude_vs_x.append(amplitude_vs_x_channel06)
list_amplitude_vs_x.append(amplitude_vs_x_channelall)

print("Setting up Langaus")
fit = langaus.LanGausFit()
print("Setup Langaus")
canvas = TCanvas("cv","cv",1000,800)

maxAmpChannels = []
maxAmpALL = 0
n_channels = 0
#loop over X,Y bins
for channel in range(0, len(list_amplitude_vs_x)-1):
    # print("Channel : " + str(channel))
    maxAmp = 0
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
            #tmpHist.Draw("hist")
            #myLanGausFunction.Draw("same")
            #canvas.SaveAs("q_"+str(i)+"_"+str(channel)+".gif")
        else:
            value = 0.0

        value = value if(value>0.0) else 0.0

        if value > maxAmp and channel!=(len(list_amplitude_vs_x)-1):
            maxAmp = value

        #print(myTotalEvents)
        #print ("Bin : " + str(i) + " -> " + str(value))

        list_amplitude_vs_x[channel].SetBinContent(i,value)
    print("Channel : " + str(channel) + "; Max Amplitude = " + str(maxAmp) + " [mV]")
    maxAmpChannels.append(maxAmp)
    if channel!=(len(list_amplitude_vs_x)-1):
        maxAmpALL+=maxAmp
        if maxAmp!=0: n_channels+=1

maxAmpAvg = maxAmpALL/n_channels
print("Average Max Amplitude = " + str(maxAmpAvg) + "; N of non-empty channels: " + str(n_channels))

# Define amplitude correction
for i in range(0,len(maxAmpChannels)):
    print("Channel number; {:0.2f}, Max Amp: {:0.2f}, Average Max Amplitude: {:0.2f}, Amp. Correction: {:0.4f}".format(i, maxAmpChannels[i], maxAmpAvg, maxAmpAvg/maxAmpChannels[i]))

                    
# Save amplitude histograms
outputfile = TFile("PlotAmplitudeVsX.root","RECREATE")
for channel in range(0, len(list_amplitude_vs_x)):
    list_amplitude_vs_x[channel].Write()
outputfile.Close()


#Make final plots
plotfile = TFile("PlotAmplitudeVsX.root","READ")
plotList_amplitude_vs_x  = []
plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel00"))
plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel01"))
plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel02"))
plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel03"))
plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel04"))
plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel05"))
plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel06"))
# plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channelall"))

plotList_amplitude_vs_x[0].SetLineWidth(2)
plotList_amplitude_vs_x[1].SetLineWidth(2)
plotList_amplitude_vs_x[2].SetLineWidth(2)
plotList_amplitude_vs_x[3].SetLineWidth(2)
plotList_amplitude_vs_x[4].SetLineWidth(2)
plotList_amplitude_vs_x[5].SetLineWidth(2)
plotList_amplitude_vs_x[6].SetLineWidth(2)

plotList_amplitude_vs_x[0].SetLineColor(colors[0])
plotList_amplitude_vs_x[1].SetLineColor(colors[1])
plotList_amplitude_vs_x[2].SetLineColor(colors[2])
plotList_amplitude_vs_x[3].SetLineColor(colors[3])
plotList_amplitude_vs_x[4].SetLineColor(colors[4])
plotList_amplitude_vs_x[5].SetLineColor(colors[5])
plotList_amplitude_vs_x[6].SetLineColor(colors[6])

totalAmplitude_vs_x = TH1F("htemp","",1,-2.5,2.5)
totalAmplitude_vs_x.Draw("hist")
totalAmplitude_vs_x.SetStats(0)
totalAmplitude_vs_x.SetTitle("")
totalAmplitude_vs_x.GetXaxis().SetTitle("Track x position [mm]")
totalAmplitude_vs_x.GetYaxis().SetTitle("MPV signal amplitude [mV]")
totalAmplitude_vs_x.SetLineWidth(2)

totalAmplitude_vs_x.SetMaximum(150.0)

boxes = getStripBox(inputfile,0,140,False, 18, True, shift)
for box in boxes:
   box.Draw()
totalAmplitude_vs_x.Draw("AXIS same")
totalAmplitude_vs_x.Draw("hist same")

plotList_amplitude_vs_x[0].Draw("histsame")
plotList_amplitude_vs_x[1].Draw("histsame")
plotList_amplitude_vs_x[2].Draw("histsame")
plotList_amplitude_vs_x[3].Draw("histsame")
plotList_amplitude_vs_x[4].Draw("histsame")
plotList_amplitude_vs_x[5].Draw("histsame")
plotList_amplitude_vs_x[6].Draw("histsame")

legend = TLegend(2*myStyle.GetMargin()+0.02,1-myStyle.GetMargin()-0.02-0.2,1-myStyle.GetMargin()-0.02,1-myStyle.GetMargin()-0.02)
legend.SetNColumns(3)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize())
legend.SetBorderSize(0)
legend.SetFillColor(kWhite)
legend.AddEntry(plotList_amplitude_vs_x[0], "Strip 1")
legend.AddEntry(plotList_amplitude_vs_x[1], "Strip 2")
legend.AddEntry(plotList_amplitude_vs_x[2], "Strip 3")
legend.AddEntry(plotList_amplitude_vs_x[3], "Strip 4")
legend.AddEntry(plotList_amplitude_vs_x[4], "Strip 5")
legend.AddEntry(plotList_amplitude_vs_x[5], "Strip 6")
legend.AddEntry(plotList_amplitude_vs_x[6], "Strip 7")
legend.Draw();

myStyle.BeamInfo()
myStyle.SensorInfo(sensor, bias)

canvas.SaveAs("TotalAmplitude_vs_x_"+sensor+".gif")
canvas.SaveAs("TotalAmplitude_vs_x_"+sensor+".pdf")

