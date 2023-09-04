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
organized_mode=True

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 2.5, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 150, help="Max Amp value in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()

dataset = options.Dataset
outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")   

colors = myStyle.GetColors(True)

sensor_Geometry = myStyle.GetGeometry(dataset)
sensor = sensor_Geometry['sensor']
xlength = float(options.xlength)
ylength = float(options.ylength)

outdir = myStyle.GetPlotsDir(outdir, "AmpPlots/")

#Get 3D histograms
channel_good_index = []
th3_amplitude_vs_xy_ch = []
for i in range(7):
    hname = "amplitude_vs_xy_channel0"+str(i)
    if inputfile.Get(hname):
        channel_good_index.append(i)
        th3_amplitude_vs_xy_ch.append(inputfile.Get(hname))

th3_amplitude_vs_xy_channelall = inputfile.Get("totamplitude_vs_xy")

shift = inputfile.Get("stripBoxInfo03").GetMean(1)

#Build 2D amp vs x histograms
list_th2_amplitude_vs_x = []
for i,ch in enumerate(channel_good_index):
    list_th2_amplitude_vs_x.append(th3_amplitude_vs_xy_ch[i].Project3D("zx"))

list_th2_amplitude_vs_x.append(th3_amplitude_vs_xy_channelall.Project3D("zx"))

#Build amplitude histograms
th1 = th3_amplitude_vs_xy_ch[0].ProjectionX().Clone("th1")
th1_Nbins = th1.GetXaxis().GetNbins()
th1_Xmin = th1.GetXaxis().GetXmin()-shift
th1_Xmax = th1.GetXaxis().GetXmax()-shift
list_amplitude_vs_x = []

for i,ch in enumerate(channel_good_index):
    list_amplitude_vs_x.append(TH1F("amplitude_vs_x_channel0%i"%(ch),"", th1_Nbins, th1_Xmin, th1_Xmax))

print ("Amplitude vs X: " + str(th1.GetXaxis().GetBinLowEdge(1)-shift) + " -> " + str(th1.GetXaxis().GetBinUpEdge(th1.GetXaxis().GetNbins())-shift))

print("Setting up Langaus")
fit = langaus.LanGausFit()
print("Setup Langaus")
canvas = TCanvas("cv","cv",1000,800)

maxAmpChannels = []
maxAmpALL = 0
n_channels = 0
for channel in range(0, len(list_amplitude_vs_x)):
    # print("Channel : " + str(channel))
    maxAmp = 0
    totalEvents = list_th2_amplitude_vs_x[channel].GetEntries()
    # Run across X-bins. ROOT convention: bin 0 - underflow, nbins+1 - overflow bin
    for i in range(1, list_amplitude_vs_x[channel].GetXaxis().GetNbins()+1):
        tmpHist = list_th2_amplitude_vs_x[channel].ProjectionY("py",i,i)
        myTotalEvents=tmpHist.Integral()
        myMean = tmpHist.GetMean()
        myRMS = tmpHist.GetRMS()
        value = myMean            
        nEvents = tmpHist.GetEntries()

        nXBins = th1_Nbins
        minEvtsCut = totalEvents/nXBins
        if i==1: print("Channel %i: nEvents > %.2f (Total events: %i; N bins: %i)"%(channel,minEvtsCut,totalEvents,nXBins))

        if(nEvents > minEvtsCut):
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
            #canvas.SaveAs(outdir+"q_"+str(i)+"_"+str(channel)+".gif")
        else:
            value = 0.0

        value = value if(value>0.0) else 0.0

        if value > maxAmp:
            maxAmp = value

        #print(myTotalEvents)
        #print ("Bin : " + str(i) + " -> " + str(value))

        list_amplitude_vs_x[channel].SetBinContent(i,value)
    ### print("Channel : " + str(channel) + "; Max Amplitude = " + str(maxAmp) + " [mV]")
    #print("Channel: %i; Max Amplitude = %.3f [mV]"%(channel, maxAmp))
    maxAmpChannels.append(maxAmp)
    maxAmpALL+=maxAmp
    if maxAmp!=0: n_channels+=1

maxAmpAvg = maxAmpALL/n_channels
# print("Average Max Amplitude = " + str(maxAmpAvg) + "; N of non-empty channels: " + str(n_channels))
print("Average Max Amplitude = %.2f [mV]; N of non-empty channels: %i"%(maxAmpAvg, n_channels))

# Define amplitude correction
for i in range(0,len(maxAmpChannels)):
    # print("Channel number; {:0.2f}, Max Amp: {:0.2f}, Average Max Amplitude: {:0.2f}, Amp. Correction: {:0.4f}".format(i, maxAmpChannels[i], maxAmpAvg, maxAmpAvg/maxAmpChannels[i]))
    print("Channel %i:   Max Amp: %0.3f, Amp. Correction: %0.4f"%(i, maxAmpChannels[i], maxAmpAvg/maxAmpChannels[i]))

                    
# Save amplitude histograms
outputfile = TFile("%sPlotAmplitudeVsX.root"%(outdir),"RECREATE")
# for channel in range(0, len(list_amplitude_vs_x)):
#     list_amplitude_vs_x[channel].Write()

for hist in list_amplitude_vs_x:
    hist.Write()

outputfile.Close()


#Make final plots
plotfile = TFile("%sPlotAmplitudeVsX.root"%(outdir),"READ")
plotList_amplitude_vs_x  = []
for i,ch in enumerate(channel_good_index):
    plot_amplitude = plotfile.Get("amplitude_vs_x_channel0%i"%ch)
    plot_amplitude.SetLineWidth(2)
    plot_amplitude.SetLineColor(colors[i])
    plotList_amplitude_vs_x.append(plot_amplitude)


totalAmplitude_vs_x = TH1F("htemp","",1,-xlength,xlength)
totalAmplitude_vs_x.Draw("hist")
totalAmplitude_vs_x.SetStats(0)
totalAmplitude_vs_x.SetTitle("")
totalAmplitude_vs_x.GetXaxis().SetTitle("Track x position [mm]")
totalAmplitude_vs_x.GetYaxis().SetTitle("MPV signal amplitude [mV]")
totalAmplitude_vs_x.SetLineWidth(2)

totalAmplitude_vs_x.SetMaximum(ylength)

boxes = getStripBox(inputfile,0,ylength-10.0,False, 18, True, shift)
for box in boxes:
   box.Draw()
totalAmplitude_vs_x.Draw("AXIS same")
totalAmplitude_vs_x.Draw("hist same")


legend = TLegend(2*myStyle.GetMargin()+0.02,1-myStyle.GetMargin()-0.02-0.2,1-myStyle.GetMargin()-0.02,1-myStyle.GetMargin()-0.02)
legend.SetNColumns(3)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize())
legend.SetBorderSize(0)
legend.SetFillColor(kWhite)

for i,ch in enumerate(channel_good_index):
    plotList_amplitude_vs_x[i].Draw("histsame")
    legend.AddEntry(plotList_amplitude_vs_x[i], "Strip %i"%(ch+1))
legend.Draw();

# myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

canvas.SaveAs(outdir+"TotalAmplitude_vs_x_"+sensor+".gif")
canvas.SaveAs(outdir+"TotalAmplitude_vs_x_"+sensor+".pdf")

