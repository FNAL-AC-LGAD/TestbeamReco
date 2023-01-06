from ROOT import TFile,TTree,TCanvas,TH1F,TArrow,TH2F,TH1D,TH2D,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle,TBox,TGraph,TMarker
import os
import EfficiencyUtils
import langaus
import optparse
import time
from stripBox import getStripBox,getStripBoxY
import myStyle
from array import array
import ROOT
import EfficiencyUtils

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)
organized_mode=True

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.25)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 0, help="Bias Voltage value in [V]")
parser.add_option('-z','--zmin', dest='zmin', default =   0.0, help="Set min Amp value in final plot")
parser.add_option('-Z','--zmax', dest='zmax', default = 120.0, help="Set max Amp value in final plot")
options, args = parser.parse_args()

dataset = options.Dataset
zmin = float(options.zmin)
zmax = float(options.zmax)

outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")

sensor_Geometry = myStyle.GetGeometry(dataset)
sensor = sensor_Geometry['sensor']
bias   = sensor_Geometry['BV'] if options.biasvolt == 0 else options.biasvolt

#outdir = myStyle.GetPlotsDir(outdir, "AmpPlots/")
outdir = myStyle.getOutputDir("Paper2022")
#Get 3D histograms
channel_good_index = []
th3_amplitude_vs_xy_ch = []
for i in range(7):
    hname = "amplitude_vs_xy_channel0"+str(i)
    if inputfile.Get(hname):
        channel_good_index.append(i)
        th3_amplitude_vs_xy_ch.append(inputfile.Get(hname))

th3_amplitude_vs_xy_ch.append(inputfile.Get("amplitude_vs_xy"))


#Build amplitude histograms
#efficiency_vs_xy_denominator = inputfile.Get("efficiency_vs_xy_denominator")
#amplitude_vs_xy_temp = efficiency_vs_xy_denominator.Clone("amplitude_vs_xy")
amplitude_th2_4binning = inputfile.Get("amplitude_vs_xy")
amplitude_vs_xy_temp = amplitude_th2_4binning.Project3D("yx")

list_amplitude_vs_xy = []
for i,ch in enumerate(channel_good_index):
    list_amplitude_vs_xy.append(amplitude_vs_xy_temp.Clone("amplitude_vs_xy_channel0%i"%(ch)))

list_amplitude_vs_xy.append(amplitude_vs_xy_temp.Clone("amplitude_vs_xy"))


canvas = TCanvas("cv","cv",1000,800)
fit = langaus.LanGausFit()

#loop over X,Y bins
for i in range(1, amplitude_vs_xy_temp.GetXaxis().GetNbins()):
    for j in range(1, amplitude_vs_xy_temp.GetYaxis().GetNbins()):
#for i in range(amplitude_vs_xy.GetXaxis().FindFixBin(-2.6), amplitude_vs_xy.GetXaxis().FindFixBin(-2.0)):
#    for j in range(amplitude_vs_xy.GetYaxis().FindFixBin(-3.0), amplitude_vs_xy.GetYaxis().FindFixBin(9.0)):

        ##For Debugging
        #if not (i==46 and j==5):
        #    continue

        for channel in range(0, len(list_amplitude_vs_xy)):
            tmpHist = th3_amplitude_vs_xy_ch[channel].ProjectionZ("pz",i,i,j,j)
            myMean = tmpHist.GetMean()
            myRMS = tmpHist.GetRMS()
            value = myMean

            #Do Langaus fit if histogram mean is larger than 10
            #and mean is larger than RMS (a clear peak away from noise)
            if (myMean > 10 and myMean > 0.5*myRMS):                
                # if channel==0: 
                #     print(tmpHist.GetEntries(), myMean)
                #use coarser bins when the signal is bigger
                if (myMean > 50) :
                    tmpHist.Rebin(10)
                else :
                    tmpHist.Rebin(5)

                #myLanGausFunction = fit.fit(tmpHist, fitrange=(myMean-2*myRMS,myMean+3*myRMS))
                #myMPV = myLanGausFunction.GetParameter(1)
                #value = myMPV

                ##For Debugging
                #tmpHist.Draw("hist")
                #myLanGausFunction.Draw("same")
                #canvas.SaveAs("q_"+str(i)+"_"+str(j)+".gif")

            #print ("Bin : " + str(i) + " , " + str(j) + " -> " + str(value))
            # if tmpHist.GetEntries()>20: 
            list_amplitude_vs_xy[channel].SetBinContent(i,j,value)
            
            

outputfile=TFile("%splotsAmplitudevsXY.root"%outdir,"RECREATE")


# Plot 2D histograms
for channel in range(0, len(list_amplitude_vs_xy)):
  

    list_amplitude_vs_xy[channel].GetZaxis().SetTitle("Mean amplitude [mV]")
    #list_amplitude_vs_xy[channel].GetZaxis().SetTitleSize(0.05)
    #list_amplitude_vs_xy[channel].GetZaxis().SetTitleOffset(1.0)
    list_amplitude_vs_xy[channel].GetXaxis().SetTitle("Track x position [mm]")
    #list_amplitude_vs_xy[channel].GetXaxis().SetTitleSize(0.05)
    #list_amplitude_vs_xy[channel].GetXaxis().SetTitleOffset(0.90)
    #list_amplitude_vs_xy[channel].GetXaxis().SetLabelSize(0.03)
    list_amplitude_vs_xy[channel].GetXaxis().SetRangeUser(-2.1,2.1)
    list_amplitude_vs_xy[channel].GetYaxis().SetTitle("Track y position [mm]")
    list_amplitude_vs_xy[channel].GetYaxis().SetRangeUser(-5.25,5.25)
    #list_amplitude_vs_xy[channel].GetYaxis().SetTitleSize(0.05)
    #list_amplitude_vs_xy[channel].GetYaxis().SetTitleOffset(1.05)
    #list_amplitude_vs_xy[channel].GetYaxis().SetLabelSize(0.03)
    #list_amplitude_vs_xy[channel].GetYaxis().SetRangeUser(-4.5,4.5)
    list_amplitude_vs_xy[channel].SetMinimum(zmin)
    list_amplitude_vs_xy[channel].SetMaximum(zmax)
    list_amplitude_vs_xy[channel].SetStats(0)
 
    list_amplitude_vs_xy[channel].Draw("colz")
    #list_amplitude_vs_xy[channel].SetTitle("Channel "+str(channel))
   
    BoxHot = TBox(0.90,-1.5,1.10,-0.5)
    BoxHot.SetLineColor(632)
    BoxHot.SetFillStyle(0)
    BoxHot.SetLineWidth(3)
    BoxHot.Draw("same")

    BoxCold = TBox(0.90,-3.5,1.10,-2.5)
    BoxCold.SetLineColor(600)
    BoxCold.SetFillStyle(0)
    BoxCold.SetLineWidth(3)
    BoxCold.Draw("same")

    BoxGap = TBox(0.70,0.5,0.80,2.5)
    BoxGap.SetLineColor(1)
    BoxGap.SetFillStyle(0)
    BoxGap.SetLineWidth(3)
    BoxGap.SetLineStyle(2)
    BoxGap.Draw("same")
   
    #xvalue = array( 'f', [1.525,1.025,0.525,0.025,-0.475,-0.975,-1.475] )
    #p3value = array( 'f', [-0.802083,-0.806145,-1.1938,-1.26825,-1.68453,-1.71641,-2.00437] )
   
    #xvalue = array( 'f', [1.525,1.025,0.525,0.025,-0.475,-0.975,-1.475] )
    xvalue = array( 'f', [1.516, 1.013, 0.514, 0.015, -0.484, -0.985, -1.485] )
    p3value = array( 'f', [-0.802083,-0.806145,-1.1938,-1.26825,-1.68453,-1.71641,-2.004375] )

    gr = TMarker(xvalue[0], p3value[0], 20)
    gr1 = TMarker(xvalue[1], p3value[2], 20)
    gr2 = TMarker(xvalue[2], p3value[2], 20)
    gr3 = TMarker(xvalue[3], p3value[3], 20)
    gr4 = TMarker(xvalue[4], p3value[4], 20)
    gr5 = TMarker(xvalue[5], p3value[5], 20)
    gr6 = TMarker(xvalue[6], p3value[6], 20)

    gr.SetMarkerColor( 1 )
    gr1.SetMarkerColor(1 )
    gr2.SetMarkerColor( 1 )
    gr3.SetMarkerColor( 1 )
    gr4.SetMarkerColor( 1)
    gr5.SetMarkerColor( 1 )
    gr6.SetMarkerColor( 1)

    gr.SetMarkerSize( 2 )
    gr1.SetMarkerSize( 2 )
    gr2.SetMarkerSize( 2 )
    gr3.SetMarkerSize( 2 )
    gr4.SetMarkerSize( 2 )
    gr5.SetMarkerSize( 2 )
    gr6.SetMarkerSize( 2 )

    gr.SetMarkerStyle( 20 )
    gr1.SetMarkerStyle( 20 )
    gr2.SetMarkerStyle( 20 )
    gr3.SetMarkerStyle( 20 )
    gr4.SetMarkerStyle( 20 )
    gr5.SetMarkerStyle( 20 )
    gr6.SetMarkerStyle( 20 )

    #gr.Draw()
    #gr1.Draw()
    #gr2.Draw()
    #gr3.Draw()
    #gr4.Draw()
    #gr5.Draw()
    #gr6.Draw()
    
    myStyle.BeamInfo()
    myStyle.SensorInfoSmart(dataset,2.0*myStyle.GetMargin())
    canvas.SetRightMargin(3.0*myStyle.GetMargin())
    #canvas.SetLeftMargin(0.12)

    name = "Amplitude_vs_xy_channel"+str(channel) if channel != (len(list_amplitude_vs_xy)-1) else "Amplitude_vs_xy"
    canvas.SaveAs(outdir+name+"Amplitude_EIC1cm_200um_v2.gif")
    canvas.SaveAs(outdir+name+"Amplitude_EIC1cm_200um_v2.pdf")

    list_amplitude_vs_xy[channel].Write()

outputfile.Close()

