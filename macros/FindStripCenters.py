from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite, TF1
import os
import EfficiencyUtils
import langaus
import optparse
import time
#from stripBox import getStripBox
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
organized_mode=True

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-s','--sensor', dest='sensor', default = "", help="Type of sensor (BNL, HPK, ...)")
parser.add_option('-p','--pitch', dest='pitch', default = 500, help="pitch in um")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 220, help="Bias Voltage value in [V]")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()

sensor = options.sensor
bias = options.biasvolt
pitch = options.pitch

num_strips=7

dataset = options.Dataset
outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_InitialAnalyzer.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")   

colors = myStyle.GetColors(True)


def findCenter(hist):

    maxLoc = hist.GetBinCenter(hist.FindFirstBinAbove(0.999*hist.GetMaximum()))
    range_min = maxLoc-0.4*pitch/1000.
    range_max = maxLoc+0.4*pitch/1000.

    f1 = TF1("f1%s"%hist.GetName(),"gaus",range_min,range_max)
    f1.SetParameter("Mean",maxLoc)
    hist.Fit(f1,"Q","",range_min,range_max)

    print("%s, gauss center: %0.4f mm, sigma: %0.3f mm" % (hist.GetName(),f1.GetParameter("Mean"),f1.GetParameter("Sigma")))
    return f1



# #Define histo names
# h00 = "amplitude_vs_xy_channel00"
# h01 = "amplitude_vs_xy_channel01"
# h02 = "amplitude_vs_xy_channel02"
# h03 = "amplitude_vs_xy_channel03"
# h04 = "amplitude_vs_xy_channel04"
# h05 = "amplitude_vs_xy_channel05"
# h06 = "amplitude_vs_xy_channel06"
# htot = "totamplitude_vs_xy"

# #Get 3D histograms 
# th3_amplitude_vs_xy_channel00 = inputfile.Get(h00)
# th3_amplitude_vs_xy_channel01 = inputfile.Get(h01)
# th3_amplitude_vs_xy_channel02 = inputfile.Get(h02)
# th3_amplitude_vs_xy_channel03 = inputfile.Get(h03)
# th3_amplitude_vs_xy_channel04 = inputfile.Get(h04)
# th3_amplitude_vs_xy_channel05 = inputfile.Get(h05)
# th3_amplitude_vs_xy_channel06 = inputfile.Get(h06)



# th3_amplitude_vs_xy_channelall = inputfile.Get(htot)

#th3_amplitude_vs_xy_channel00.RebinX(3)
#th3_amplitude_vs_xy_channel01.RebinX(3)
#th3_amplitude_vs_xy_channel02.RebinX(3)
#th3_amplitude_vs_xy_channel03.RebinX(3)
#th3_amplitude_vs_xy_channel04.RebinX(3)
#th3_amplitude_vs_xy_channel05.RebinX(3)
#th3_amplitude_vs_xy_channel06.RebinX(3)
#th3_amplitude_vs_xy_channelall.RebinX(3)

#shift = (inputfile.Get("stripBoxInfo02").GetMean(1)+inputfile.Get("stripBoxInfo03").GetMean(1))/2.
# shift = inputfile.Get("stripBoxInfo03").GetMean(1)

#Build 2D amp vs x histograms
# amplitude_vs_x_channel00 = th3_amplitude_vs_xy_channel00.Project3D("zx")
# amplitude_vs_x_channel01 = th3_amplitude_vs_xy_channel01.Project3D("zx")
# amplitude_vs_x_channel02 = th3_amplitude_vs_xy_channel02.Project3D("zx")
# amplitude_vs_x_channel03 = th3_amplitude_vs_xy_channel03.Project3D("zx")
# amplitude_vs_x_channel04 = th3_amplitude_vs_xy_channel04.Project3D("zx")
# amplitude_vs_x_channel05 = th3_amplitude_vs_xy_channel05.Project3D("zx")
# amplitude_vs_x_channel06 = th3_amplitude_vs_xy_channel06.Project3D("zx")
# amplitude_vs_x_channelall= th3_amplitude_vs_xy_channelall.Project3D("zx")

list_th2_amplitude_vs_x = []
# list_th2_amplitude_vs_x.append(amplitude_vs_x_channel00)
# list_th2_amplitude_vs_x.append(amplitude_vs_x_channel01)
# list_th2_amplitude_vs_x.append(amplitude_vs_x_channel02)
# list_th2_amplitude_vs_x.append(amplitude_vs_x_channel03)
# list_th2_amplitude_vs_x.append(amplitude_vs_x_channel04)
# list_th2_amplitude_vs_x.append(amplitude_vs_x_channel05)
# list_th2_amplitude_vs_x.append(amplitude_vs_x_channel06)
# list_th2_amplitude_vs_x.append(amplitude_vs_x_channelall)

th3_amplitude_vs_xy_channels =[]
for i in range(num_strips):
    th3_amp_vs_xy_channel = inputfile.Get("amplitude_vs_xy_channel0%i"%i)
    th3_amplitude_vs_xy_channels.append(th3_amp_vs_xy_channel)
    amp_vs_x_channel = th3_amp_vs_xy_channel.Project3D("zx")
    list_th2_amplitude_vs_x.append(amp_vs_x_channel)

#Build amplitude histograms
th1 = th3_amplitude_vs_xy_channels[0].ProjectionX().Clone("th1")
xmin = th1.GetXaxis().GetXmin()
xmax = th1.GetXaxis().GetXmax()

amplitude_vs_x_channel00 = TH1F("amplitude_vs_x_channel00","",th1.GetXaxis().GetNbins(),xmin,xmax)
amplitude_vs_x_channel01 = TH1F("amplitude_vs_x_channel01","",th1.GetXaxis().GetNbins(),xmin,xmax)
amplitude_vs_x_channel02 = TH1F("amplitude_vs_x_channel02","",th1.GetXaxis().GetNbins(),xmin,xmax)
amplitude_vs_x_channel03 = TH1F("amplitude_vs_x_channel03","",th1.GetXaxis().GetNbins(),xmin,xmax)
amplitude_vs_x_channel04 = TH1F("amplitude_vs_x_channel04","",th1.GetXaxis().GetNbins(),xmin,xmax)
amplitude_vs_x_channel05 = TH1F("amplitude_vs_x_channel05","",th1.GetXaxis().GetNbins(),xmin,xmax)
amplitude_vs_x_channel06 = TH1F("amplitude_vs_x_channel06","",th1.GetXaxis().GetNbins(),xmin,xmax)
# amplitude_vs_x_channelall = TH1F("amplitude_vs_x_channelall","",th1.GetXaxis().GetNbins(),th1.GetXaxis().GetXmin(),th1.GetXaxis().GetXmax())

print ("Amplitude vs X: " + str(th1.GetXaxis().GetBinLowEdge(1)) + " -> " + str(th1.GetXaxis().GetBinUpEdge(th1.GetXaxis().GetNbins())))

list_amplitude_vs_x = []
list_amplitude_vs_x.append(amplitude_vs_x_channel00)
list_amplitude_vs_x.append(amplitude_vs_x_channel01)
list_amplitude_vs_x.append(amplitude_vs_x_channel02)
list_amplitude_vs_x.append(amplitude_vs_x_channel03)
list_amplitude_vs_x.append(amplitude_vs_x_channel04)
list_amplitude_vs_x.append(amplitude_vs_x_channel05)
list_amplitude_vs_x.append(amplitude_vs_x_channel06)
# list_amplitude_vs_x.append(amplitude_vs_x_channelall)

print("Setting up Langaus")
fit = langaus.LanGausFit()
print("Setup Langaus")
canvas = TCanvas("cv","cv",1000,800)

maxAmpChannels = []
maxAmpALL = 0
n_channels = 0
#loop over X,Y bins
for channel in range(0, len(list_amplitude_vs_x)):
    # print("Channel : " + str(channel))
    maxAmp = 0
    maxLoc=-999
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
            #canvas.SaveAs(outdir+"q_"+str(i)+"_"+str(channel)+".gif")
        else:
            value = 0.0

        value = value if(value>0.0) else 0.0

        if value > maxAmp:
            maxAmp = value
            maxLoc = list_amplitude_vs_x[channel].GetXaxis().GetBinCenter(i)

        #print(myTotalEvents)
        #print ("Bin : " + str(i) + " -> " + str(value))

        list_amplitude_vs_x[channel].SetBinContent(i,value)
    print("Channel : %i; Max Amplitude = %0.2f mV; x-val of max: %0.4f mm" %(channel,maxAmp,maxLoc))
    maxAmpChannels.append(maxAmp)
    if channel!=(len(list_amplitude_vs_x)-1):
        maxAmpALL+=maxAmp
        if maxAmp!=0: n_channels+=1

maxAmpAvg = maxAmpALL/n_channels
print("Average Max Amplitude = " + str(maxAmpAvg) + "; N of non-empty channels: " + str(n_channels))

# Define amplitude correction
# for i in range(0,len(maxAmpChannels)):
#     print("Channel number; {:0.2f}, Max Amp: {:0.2f}, Average Max Amplitude: {:0.2f}, Amp. Correction: {:0.4f}".format(i, maxAmpChannels[i], maxAmpAvg, maxAmpAvg/maxAmpChannels[i]))

                    


#Make final plots
# plotfile = TFile("PlotAmplitudeVsX.root","READ")
# plotList_amplitude_vs_x  = []
# plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel00"))
# plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel01"))
# plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel02"))
# plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel03"))
# plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel04"))
# plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel05"))
# plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channel06"))
# plotList_amplitude_vs_x.append(plotfile.Get("amplitude_vs_x_channelall"))

list_of_fit_functions=[]

ymax = list_amplitude_vs_x[0].GetMaximum()
for i in range(num_strips):
    if list_amplitude_vs_x[i].GetMaximum()>ymax: ymax = list_amplitude_vs_x[i].GetMaximum()
    
    list_of_fit_functions.append(findCenter(list_amplitude_vs_x[i]))

    list_amplitude_vs_x[i].SetLineWidth(2)
    list_amplitude_vs_x[i].SetLineColor(colors[i])
    list_of_fit_functions[i].SetLineColor(colors[i])


totalAmplitude_vs_x = TH1F("htemp","",1,xmin,xmax)
totalAmplitude_vs_x.Draw("hist")
totalAmplitude_vs_x.SetStats(0)
totalAmplitude_vs_x.SetTitle("")
totalAmplitude_vs_x.GetXaxis().SetTitle("Track x position [mm]")
totalAmplitude_vs_x.GetYaxis().SetTitle("MPV signal amplitude [mV]")
totalAmplitude_vs_x.SetLineWidth(2)

totalAmplitude_vs_x.SetMaximum(ymax*1.5)

# boxes = getStripBox(inputfile,0,ylength-10.0,False, 18, True, shift)
# for box in boxes:
#    box.Draw()
totalAmplitude_vs_x.Draw("AXIS same")
totalAmplitude_vs_x.Draw("hist same")
for i in range(num_strips):
    list_amplitude_vs_x[i].Draw("histsame")
    list_of_fit_functions[i].Draw("same")


legend = TLegend(2*myStyle.GetMargin()+0.02,1-myStyle.GetMargin()-0.02-0.2,1-myStyle.GetMargin()-0.02,1-myStyle.GetMargin()-0.02)
legend.SetNColumns(3)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize())
legend.SetBorderSize(0)
legend.SetFillColor(kWhite)
for i in range(num_strips):
    legend.AddEntry(list_amplitude_vs_x[i], "Strip %i"%(i+1))

legend.Draw();

myStyle.BeamInfo()
myStyle.SensorInfo(sensor, bias)

canvas.SaveAs(outdir+"TotalAmplitude_vs_x_"+sensor+".gif")
canvas.SaveAs(outdir+"TotalAmplitude_vs_x_"+sensor+".pdf")

center_list = []
delta_center_list=[]
for channel in range(num_strips):
    center_list.append(list_of_fit_functions[channel].GetParameter("Mean"))
    if channel>0:
        delta_center_list.append(center_list[channel]-center_list[channel-1])

print("Centers, ", center_list)
print("Deltas, ",delta_center_list)

string_for_geo = "std::vector<double> stripCenterXPosition = {"
for channel in range(8):
    if channel < len(list_of_fit_functions):
        string_for_geo+= "%0.3f, "%list_of_fit_functions[channel].GetParameter("Mean")
    else:
         string_for_geo+= "0.0, "
         
string_for_geo+="};"
string_for_geo = string_for_geo.replace(", }","}")

print(string_for_geo)
# Save amplitude histograms
outputfile = TFile(outdir+"PlotAmplitudeVsX.root","RECREATE")

for channel in range(num_strips):
    list_amplitude_vs_x[channel].Write()
    list_of_fit_functions[channel].Write()
outputfile.Close()


