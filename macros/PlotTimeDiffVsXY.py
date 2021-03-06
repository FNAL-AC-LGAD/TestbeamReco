from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack
import os

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.th3 = self.getTH3(f, inHistoName)
        self.th2 = self.getTH2(self.th3, outHistoName)

    def getTH3(self, f, name):
        return f.Get(name)        

    def getTH2(self, th3, name):
        return th3.Project3D("yx").Clone(name)

inputfile = TFile("../test/myoutputfile.root")

all_histoInfos = [
    HistoInfo("timeDiff_vs_xy_channel00",inputfile, "channel_1"),
    HistoInfo("timeDiff_vs_xy_channel01",inputfile, "channel_2"),
    HistoInfo("timeDiff_vs_xy_channel02",inputfile, "channel_3"),
    HistoInfo("timeDiff_vs_xy_channel03",inputfile, "channel_4"),
    HistoInfo("timeDiff_vs_xy_channel04",inputfile, "channel_5"),
    HistoInfo("timeDiff_vs_xy_channel05",inputfile, "channel_6"),
    HistoInfo("timeDiff_vs_xy", inputfile, "time_diff"),
    HistoInfo("timeDiff_vs_xy_amp2", inputfile, "time_diff_amp2"),
    HistoInfo("timeDiff_vs_xy_amp3", inputfile, "time_diff_amp3"),
    HistoInfo("weighted_timeDiff_vs_xy", inputfile, "weighted_time_diff"),
]

canvas = TCanvas("cv","cv",800,800)
gPad.SetLeftMargin(0.12)
gPad.SetRightMargin(0.15)
gPad.SetTopMargin(0.08)
gPad.SetBottomMargin(0.12)
gPad.SetTicks(1,1)
print("Finished setting up langaus fit class")

#loop over X bins
for i in range(0, all_histoInfos[0].th2.GetXaxis().GetNbins()+1):
    for j in range(0, all_histoInfos[0].th2.GetYaxis().GetNbins()+1):
        ##For Debugging
        #if not (i==46 and j==5):
        #    continue

        for info in all_histoInfos:
            tmpHist = info.th3.ProjectionZ("pz",i,i,j,j)
            myMean = tmpHist.GetMean()
            myRMS = tmpHist.GetRMS()
            nEvents = tmpHist.GetEntries()
            fitlow = myMean - 1.5*myRMS
            fithigh = myMean + 1.5*myRMS
            value = myRMS
            error = 0.0

            #Do fit 
            if(nEvents > 50):
                tmpHist.Rebin(4)

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
                #canvas.SaveAs("q_"+str(i)+"_"+str(j)+".gif")
                #
                #print ("Bin : " + str(i) + " , " + str(j) + " -> " + str(value))
            else:
                value = 0.0            

            info.th2.SetBinContent(i,j,value)
            info.th2.SetBinError(i,j,error)
                        
# Plot 2D histograms
outputfile = TFile("plots.root","RECREATE")
for info in all_histoInfos:
    info.th2.Draw("colz")
    info.th2.SetStats(0)
    info.th2.SetTitle(info.outHistoName)
    info.th2.SetMinimum(0.0)
    info.th2.SetMaximum(100.0)
    info.th2.SetLineColor(kBlack)

    canvas.SaveAs("TimeRes_vs_xy_"+info.outHistoName+".gif")
    canvas.SaveAs("TimeRes_vs_xy_"+info.outHistoName+".pdf")
    info.th2.Write()

outputfile.Close()

