from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle
import os
import EfficiencyUtils
import langaus
import optparse
import time
from stripBox import getStripBox

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('--run', dest='run', action='store_true', default = False, help="run fits or not")
parser.add_option('-t', dest='UseRawHistos', action='store_true', default = False, help="Use nominal amp or raw histograms")
options, args = parser.parse_args()

RunFits = options.run
UseRawHistos = options.UseRawHistos
suffex = "_raw" if UseRawHistos else ""

inputfile = TFile("../test/myoutputfile.root")     
if (RunFits):
    #Define histo names
    h00 = "baselineRMS_vs_xy_channel00" 
    h01 = "baselineRMS_vs_xy_channel01" 
    h02 = "baselineRMS_vs_xy_channel02" 
    h03 = "baselineRMS_vs_xy_channel03" 
    h04 = "baselineRMS_vs_xy_channel04" 
    h05 = "baselineRMS_vs_xy_channel05" 


    #Get 3D histograms 
    th3_baselineRMS_vs_xy_channel00 = inputfile.Get(h00)
    th3_baselineRMS_vs_xy_channel01 = inputfile.Get(h01)
    th3_baselineRMS_vs_xy_channel02 = inputfile.Get(h02)
    th3_baselineRMS_vs_xy_channel03 = inputfile.Get(h03)
    th3_baselineRMS_vs_xy_channel04 = inputfile.Get(h04)
    th3_baselineRMS_vs_xy_channel05 = inputfile.Get(h05)
    
    #Build 2D amp vs x histograms
    baselineRMS_vs_x_channel00 = th3_baselineRMS_vs_xy_channel00.Project3D("zx")
    baselineRMS_vs_x_channel01 = th3_baselineRMS_vs_xy_channel01.Project3D("zx")
    baselineRMS_vs_x_channel02 = th3_baselineRMS_vs_xy_channel02.Project3D("zx")
    baselineRMS_vs_x_channel03 = th3_baselineRMS_vs_xy_channel03.Project3D("zx")
    baselineRMS_vs_x_channel04 = th3_baselineRMS_vs_xy_channel04.Project3D("zx")
    baselineRMS_vs_x_channel05 = th3_baselineRMS_vs_xy_channel05.Project3D("zx")
        
    list_th2_baselineRMS_vs_x = []
    list_th2_baselineRMS_vs_x.append(baselineRMS_vs_x_channel00)
    list_th2_baselineRMS_vs_x.append(baselineRMS_vs_x_channel01)
    list_th2_baselineRMS_vs_x.append(baselineRMS_vs_x_channel02)
    list_th2_baselineRMS_vs_x.append(baselineRMS_vs_x_channel03)
    list_th2_baselineRMS_vs_x.append(baselineRMS_vs_x_channel04)
    list_th2_baselineRMS_vs_x.append(baselineRMS_vs_x_channel05)
       
    #Build baselineRMS histograms
    baselineRMS_vs_x = th3_baselineRMS_vs_xy_channel00.ProjectionX().Clone("baselineRMS_vs_x")
    baselineRMS_vs_x_channel00 = baselineRMS_vs_x.Clone("baselineRMS_vs_x_channel00")
    baselineRMS_vs_x_channel01 = baselineRMS_vs_x.Clone("baselineRMS_vs_x_channel01")
    baselineRMS_vs_x_channel02 = baselineRMS_vs_x.Clone("baselineRMS_vs_x_channel02")
    baselineRMS_vs_x_channel03 = baselineRMS_vs_x.Clone("baselineRMS_vs_x_channel03")
    baselineRMS_vs_x_channel04 = baselineRMS_vs_x.Clone("baselineRMS_vs_x_channel04")
    baselineRMS_vs_x_channel05 = baselineRMS_vs_x.Clone("baselineRMS_vs_x_channel05")
    
    print ("Noise vs X: " + str(baselineRMS_vs_x.GetXaxis().GetBinLowEdge(1)) + " -> " + str(baselineRMS_vs_x.GetXaxis().GetBinUpEdge(baselineRMS_vs_x.GetXaxis().GetNbins())))
    
    list_baselineRMS_vs_x = []
    list_baselineRMS_vs_x.append(baselineRMS_vs_x_channel00)
    list_baselineRMS_vs_x.append(baselineRMS_vs_x_channel01)
    list_baselineRMS_vs_x.append(baselineRMS_vs_x_channel02)
    list_baselineRMS_vs_x.append(baselineRMS_vs_x_channel03)
    list_baselineRMS_vs_x.append(baselineRMS_vs_x_channel04)
    list_baselineRMS_vs_x.append(baselineRMS_vs_x_channel05)
    
    print("Setting up Langaus")
    fit = langaus.LanGausFit()
    print("Setup Langaus")
    canvas = TCanvas("cv","cv",800,800)

    #loop over X,Y bins
    for channel in range(0, len(list_baselineRMS_vs_x)):
        print("Channel : " + str(channel))
        for i in range(1, list_baselineRMS_vs_x[channel].GetXaxis().GetNbins()):
            #print ("Bin " + str(i))

            ##For Debugging
            #if not (i==46 and j==5):
            #    continue

            tmpHist = list_th2_baselineRMS_vs_x[channel].ProjectionY("py",i,i)
            myTotalEvents=tmpHist.Integral()
            myMean = tmpHist.GetMean()
            myRMS = tmpHist.GetRMS()
            value = myMean            
            nEvents = tmpHist.GetEntries()

            #if(nEvents > 50):
                #use coarser bins when the signal is bigger
            #    if (myMean > 50) :
            #        tmpHist.Rebin(5)
            #    else :
            #        tmpHist.Rebin(10)
            #    
            #    myLanGausFunction = fit.fit(tmpHist, fitrange=(myMean-1*myRMS,myMean+3*myRMS))
            #    myMPV = myLanGausFunction.GetParameter(1)
            #    value = myMPV

                ##For Debugging
                #tmpHist.Draw("hist")
                #myLanGausFunction.Draw("same")
                #canvas.SaveAs("q_"+str(i)+"_"+str(channel)+".gif")
            #else:
            #   value = 0.0

            value = value if(value>0.0) else 0.0

            #print(myTotalEvents)
            #print ("Bin : " + str(i) + " -> " + str(value))

            list_baselineRMS_vs_x[channel].SetBinContent(i,value)
                     
    # Save baselineRMS histograms
    outputfile = TFile("plotsNoise.root","RECREATE")
    for channel in range(0, len(list_baselineRMS_vs_x)):
        list_baselineRMS_vs_x[channel].Write()
    outputfile.Close()


#Make final plots
plotfile = TFile("plotsNoise.root","READ")
plotList_baselineRMS_vs_x  = []
plotList_baselineRMS_vs_x.append(plotfile.Get("baselineRMS_vs_x_channel00"))
plotList_baselineRMS_vs_x.append(plotfile.Get("baselineRMS_vs_x_channel01"))
plotList_baselineRMS_vs_x.append(plotfile.Get("baselineRMS_vs_x_channel02"))
plotList_baselineRMS_vs_x.append(plotfile.Get("baselineRMS_vs_x_channel03"))
plotList_baselineRMS_vs_x.append(plotfile.Get("baselineRMS_vs_x_channel04"))
plotList_baselineRMS_vs_x.append(plotfile.Get("baselineRMS_vs_x_channel05"))

canvas = TCanvas("cvv","cvv",800,800)
canvas.SetLeftMargin(0.12)
plotList_baselineRMS_vs_x[5].GetYaxis().SetRangeUser(0,10)
plotList_baselineRMS_vs_x[5].Draw("hist")
plotList_baselineRMS_vs_x[5].SetStats(0)
plotList_baselineRMS_vs_x[5].SetTitle("")

ymin = plotList_baselineRMS_vs_x[5].GetMinimum()
ymax = plotList_baselineRMS_vs_x[5].GetMaximum()
plotList_baselineRMS_vs_x[5].SetMaximum(ymax*1.05)

boxes = getStripBox(inputfile,ymin,ymax*1.04)
for box in boxes:
   box.Draw()
plotList_baselineRMS_vs_x[5].Draw("AXIS same")
plotList_baselineRMS_vs_x[5].Draw("hist same")

plotList_baselineRMS_vs_x[0].GetYaxis().SetTitle("Noise [mV]")
plotList_baselineRMS_vs_x[0].GetYaxis().SetTitleSize(0.05)
plotList_baselineRMS_vs_x[0].GetYaxis().SetLabelSize(0.035)
plotList_baselineRMS_vs_x[0].GetYaxis().SetTitleOffset(1.0)
plotList_baselineRMS_vs_x[0].GetXaxis().SetTitleSize(0.05)
plotList_baselineRMS_vs_x[0].GetXaxis().SetLabelSize(0.035)
plotList_baselineRMS_vs_x[0].GetXaxis().SetTitleOffset(0.95)

plotList_baselineRMS_vs_x[0].SetLineWidth(2)
plotList_baselineRMS_vs_x[1].SetLineWidth(2)
plotList_baselineRMS_vs_x[2].SetLineWidth(2)
plotList_baselineRMS_vs_x[3].SetLineWidth(2)
plotList_baselineRMS_vs_x[4].SetLineWidth(2)
plotList_baselineRMS_vs_x[5].SetLineWidth(2)
plotList_baselineRMS_vs_x[0].SetLineColor(416+2) #kGreen+2
plotList_baselineRMS_vs_x[1].SetLineColor(432+2) #kCyan+2
plotList_baselineRMS_vs_x[2].SetLineColor(600) #kBlue
plotList_baselineRMS_vs_x[3].SetLineColor(880) #kViolet
plotList_baselineRMS_vs_x[4].SetLineColor(632) #kRed
plotList_baselineRMS_vs_x[5].SetLineColor(400+2) #kYellow
plotList_baselineRMS_vs_x[0].Draw("histsame")
plotList_baselineRMS_vs_x[1].Draw("histsame")
plotList_baselineRMS_vs_x[2].Draw("histsame")
plotList_baselineRMS_vs_x[3].Draw("histsame")
plotList_baselineRMS_vs_x[4].Draw("histsame")
plotList_baselineRMS_vs_x[5].Draw("histsame")

legend = TLegend(0.15,0.65,0.25,0.85);
legend.SetBorderSize(0)
legend.SetTextSize(0.04)
legend.AddEntry(plotList_baselineRMS_vs_x[0], "Strip 1")
legend.AddEntry(plotList_baselineRMS_vs_x[1], "Strip 2")
legend.AddEntry(plotList_baselineRMS_vs_x[2], "Strip 3")
legend.AddEntry(plotList_baselineRMS_vs_x[3], "Strip 4")
legend.AddEntry(plotList_baselineRMS_vs_x[4], "Strip 5")
legend.AddEntry(plotList_baselineRMS_vs_x[5], "Strip 6")
legend.Draw();

canvas.SaveAs("BaselineRMS_vs_x"+suffex+".gif")


