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
parser.add_option('-s','--sensor', dest='sensor', default = "EIC W1-1cm", help="Type of sensor (BNL, HPK, ...)")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 180, help="Bias Voltage value in [V]")
options, args = parser.parse_args()

file = options.file
sensor = options.sensor
bias = options.biasvolt

inputfile = TFile("../test/"+file)

#Get 3D histograms 
th3_amplitude_vs_xy_channel00 = inputfile.Get("amplitude_vs_xy_channel00")
th3_amplitude_vs_xy_channel01 = inputfile.Get("amplitude_vs_xy_channel01")
th3_amplitude_vs_xy_channel02 = inputfile.Get("amplitude_vs_xy_channel02")
th3_amplitude_vs_xy_channel03 = inputfile.Get("amplitude_vs_xy_channel03")
th3_amplitude_vs_xy_channel04 = inputfile.Get("amplitude_vs_xy_channel04")
th3_amplitude_vs_xy_channel05 = inputfile.Get("amplitude_vs_xy_channel05")
th3_amplitude_vs_xy_channel06 = inputfile.Get("amplitude_vs_xy_channel06")
list_th3_amplitude_vs_xy = []
list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel00)
list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel01)
list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel02)
list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel03)
list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel04)
list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel05)
list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel06)


#Build amplitude histograms
efficiency_vs_xy_denominator = inputfile.Get("efficiency_vs_xy_denominator")
amplitude_vs_xy = efficiency_vs_xy_denominator.Clone("amplitude_vs_xy")
amplitude_vs_xy_channel00 = amplitude_vs_xy.Clone("amplitude_vs_xy_channel00")
amplitude_vs_xy_channel01 = amplitude_vs_xy.Clone("amplitude_vs_xy_channel01")
amplitude_vs_xy_channel02 = amplitude_vs_xy.Clone("amplitude_vs_xy_channel02")
amplitude_vs_xy_channel03 = amplitude_vs_xy.Clone("amplitude_vs_xy_channel03")
amplitude_vs_xy_channel04 = amplitude_vs_xy.Clone("amplitude_vs_xy_channel04")
amplitude_vs_xy_channel05 = amplitude_vs_xy.Clone("amplitude_vs_xy_channel05")
amplitude_vs_xy_channel06 = amplitude_vs_xy.Clone("amplitude_vs_xy_channel06")



list_amplitude_vs_xy = []
list_amplitude_vs_xy.append(amplitude_vs_xy_channel00)
list_amplitude_vs_xy.append(amplitude_vs_xy_channel01)
list_amplitude_vs_xy.append(amplitude_vs_xy_channel02)
list_amplitude_vs_xy.append(amplitude_vs_xy_channel03)
list_amplitude_vs_xy.append(amplitude_vs_xy_channel04)
list_amplitude_vs_xy.append(amplitude_vs_xy_channel05)
list_amplitude_vs_xy.append(amplitude_vs_xy_channel06)


canvas = TCanvas("cv","cv",800,800)
fit = langaus.LanGausFit()

#loop over X,Y bins
for i in range(1, amplitude_vs_xy.GetXaxis().GetNbins()):
    for j in range(1, amplitude_vs_xy.GetYaxis().GetNbins()):
#for i in range(amplitude_vs_xy.GetXaxis().FindFixBin(-2.6), amplitude_vs_xy.GetXaxis().FindFixBin(-2.0)):
#    for j in range(amplitude_vs_xy.GetYaxis().FindFixBin(-3.0), amplitude_vs_xy.GetYaxis().FindFixBin(9.0)):

        ##For Debugging
        #if not (i==46 and j==5):
        #    continue

        for channel in range(0, len(list_amplitude_vs_xy)):
            tmpHist = list_th3_amplitude_vs_xy[channel].ProjectionZ("pz",i,i,j,j)
            myMean = tmpHist.GetMean()
            myRMS = tmpHist.GetRMS()
            value = myMean

            #Do Langaus fit if histogram mean is larger than 10
            #and mean is larger than RMS (a clear peak away from noise)
            if (myMean > 10 and myMean > 0.5*myRMS):                

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

            print ("Bin : " + str(i) + " , " + str(j) + " -> " + str(value))
            list_amplitude_vs_xy[channel].SetBinContent(i,j,value)
            
            
            
outputfile = TFile("plots.root","RECREATE")


# Plot 2D histograms
for channel in range(0, len(list_amplitude_vs_xy)):

    list_amplitude_vs_xy[channel].Draw("colz")
    list_amplitude_vs_xy[channel].SetStats(0)
    list_amplitude_vs_xy[channel].SetTitle("Channel "+str(channel))
    list_amplitude_vs_xy[channel].SetMinimum(0)
    list_amplitude_vs_xy[channel].SetMaximum(150)

    canvas.SetRightMargin(0.18)
    canvas.SetLeftMargin(0.12)

    canvas.SaveAs("Amplitude_vs_xy_channel"+str(channel)+".gif")
    canvas.SaveAs("Amplitude_vs_xy_channel"+str(channel)+".pdf")

    list_amplitude_vs_xy[channel].Write()


outputfile.Close()





