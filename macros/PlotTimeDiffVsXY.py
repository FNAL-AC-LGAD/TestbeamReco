from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack
import os
import optparse
import myStyle


organized_mode=True

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


parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-z','--zmin', dest='zmin', default =   -50.0, help="Set min TimeRes value in final plot")
parser.add_option('-Z','--zmax', dest='zmax', default = 150.0, help="Set max TimeRes value in final plot")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")

options, args = parser.parse_args()
dataset = options.Dataset
zmin = float(options.zmin)
zmax = float(options.zmax)
debugMode = options.debugMode

outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")

outdir = myStyle.GetPlotsDir(outdir, "TimeRes/")

all_histoInfos = [
    #HistoInfo("timeDiff_vs_xy_channel00",inputfile, "channel_1"),
    #HistoInfo("timeDiff_vs_xy_channel01",inputfile, "channel_2"),
    #HistoInfo("timeDiff_vs_xy_channel02",inputfile, "channel_3"),
    #HistoInfo("timeDiff_vs_xy_channel03",inputfile, "channel_4"),
    #HistoInfo("timeDiff_vs_xy_channel04",inputfile, "channel_5"),
    #HistoInfo("timeDiff_vs_xy_channel05",inputfile, "channel_6"),
    #HistoInfo("timeDiff_vs_xy_channel06",inputfile, "channel_7"),
    HistoInfo("timeDiff_vs_xy", inputfile, "time_diff"),
    HistoInfo("timeDiffTracker_vs_xy", inputfile, "timeDiffTracker"),
    #HistoInfo("timeDiff_vs_xy_amp2", inputfile, "time_diff_amp2"),
    #HistoInfo("timeDiff_vs_xy_amp3", inputfile, "time_diff_amp3"),
    HistoInfo("weighted2_timeDiff_tracker_vs_xy", inputfile, "weighted2_timeDiff_tracker"),
]

canvas = TCanvas("cv","cv",800,800)
gPad.SetLeftMargin(0.12)
gPad.SetRightMargin(0.15)
gPad.SetTopMargin(0.08)
gPad.SetBottomMargin(0.12)
gPad.SetTicks(1,1)


if debugMode:
    outdir_q = myStyle.CreateFolder(outdir, "q_resTimeXY0/")

nXBins = all_histoInfos[0].th2.GetXaxis().GetNbins()
nYBins = all_histoInfos[0].th2.GetYaxis().GetNbins()


#loop over X bins
for i in range(0, nXBins+1):
    for j in range(0, nYBins+1):
        ##For Debugging
        #if not (i==46 and j==5):
        #    continue
        
        for info in all_histoInfos:
            totalEvents = info.th2.GetEntries()
            tmpHist = info.th3.ProjectionZ("pz",i,i,j,j)
            myMean = tmpHist.GetMean()
            myRMS = tmpHist.GetRMS()
            nEvents = tmpHist.GetEntries()
            fitlow = myMean - 1.5*myRMS
            fithigh = myMean + 1.5*myRMS
            value = myRMS
            error = 0.0
            

            minEvtsCut = totalEvents/(nXBins*(4*nYBins))
            #minEvtsCut = totalEvents/(nXBins*nYBins)
            #print(minEvtsCut, totalEvents)
            if i==0 and j==0:
                print("%s: nEvents > %.2f (Total events: %i)"%(info.inHistoName, minEvtsCut, totalEvents))



            #Do fit 
            if(nEvents > minEvtsCut):
                #tmpHist.Rebin(4) #Only for EIC_W2_1cm_500um_200um_gap_240V
                
                fit = TF1('fit','gaus',fitlow,fithigh)
                tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
                myMean = fit.GetParameter(1)
                mySigma = fit.GetParameter(2)
                mySigmaError = fit.GetParError(2)
                value = 1000.0*mySigma
                #error = 1000.0*mySigmaError
                #value = 1000.0*myMean
                error = 0
                
                
                if (debugMode):
                    tmpHist.Draw("hist")
                    fit.Draw("same")
                    canvas.SaveAs(outdir_q+"q_"+info.outHistoName+str(i)+".gif")
                    print ("Bin: %i (x center = %.3f) -> Resolution: %.3f +/- %.3f"%(i, info.th1.GetXaxis().GetBinCenter(i), value, error))


                ##For Debugging
                #tmpHist.Draw("hist")
                ##myLanGausFunction.Draw("same")
                #fit.Draw("same")
                #canvas.SaveAs("q_"+str(i)+"_"+str(j)+".gif")
                #
                #print ("Bin : " + str(i) + " , " + str(j) + " -> " + str(value))
            else:
                value = -100.0            
                
            info.th2.SetBinContent(i,j,value)
            info.th2.SetBinError(i,j,error)
            #print("Bin " + str(i) + " " + str(j) + " " + str(value))
                

# Plot 2D histograms
outputfile = TFile("%splotsTimeDiffVsXY.root"%outdir,"RECREATE")
for info in all_histoInfos:
    info.th2.Draw("colz")
    info.th2.SetStats(0)
    info.th2.SetTitle(info.outHistoName)
    info.th2.SetMinimum(zmin)
    info.th2.SetMaximum(zmax)
    info.th2.SetLineColor(kBlack)

    canvas.SaveAs(outdir+"TimeRes_vs_xy_"+info.outHistoName+".gif")
    canvas.SaveAs(outdir+"TimeRes_vs_xy_"+info.outHistoName+".pdf")
    info.th2.Write()

outputfile.Close()

