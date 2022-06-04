from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack
import os
import optparse
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)
organized_mode=True

class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, zmin, zmax):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.th3 = self.getTH3(f, inHistoName)
        self.th2 = self.getTH2(self.th3, outHistoName)
        self.zmin = zmin
        self.zmax = zmax

    def getTH3(self, f, name):
        return f.Get(name)        

    def getTH2(self, th3, name):
        return th3.Project3D("yx").Clone(name)

parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-z','--zmin', dest='zmin', default =   0.0, help="Set zmin")
parser.add_option('-Z','--zmax', dest='zmax', default = 50.0, help="Set zmax")
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

all_histoInfos = [
    HistoInfo("deltaX_vs_Xtrack_vs_Ytrack", inputfile, "PositionX_Resolution",zmin,zmax),
    HistoInfo("deltaY_vs_Xtrack_vs_Ytrack", inputfile, "PositionY_Resolution",0.0,3000),
    HistoInfo("deltaY_vs_Xtrack_vs_Ytrack", inputfile, "PositionY_ResolutionCloserLook",0.0,500),
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
                #tmpHist.Rebin(4)
                
                fit = TF1('fit','gaus',fitlow,fithigh)
                tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
                myMean = fit.GetParameter(1)
                mySigma = fit.GetParameter(2)
                mySigmaError = fit.GetParError(2)
                value = 1000.0*mySigma
                #error = 1000.0*mySigmaError
                #value = 1000.0*myMean
                error = 0
                
                
                
                ##For Debugging
                #tmpHist.Draw("hist")
                ##myLanGausFunction.Draw("same")
                #fit.Draw("same")
                #canvas.SaveAs(outdir+"q_"+str(i)+"_"+str(j)+".gif")
                #
                #print ("Bin : " + str(i) + " , " + str(j) + " -> " + str(value))
            else:
                value = -100.0            
                
            info.th2.SetBinContent(i,j,value)
            info.th2.SetBinError(i,j,error)
            #print("Bin " + str(i) + " " + str(j) + " " + str(value))
                
# Plot 2D histograms
outputfile = TFile(outdir+"plots_RecoDiff.root","RECREATE")
for info in all_histoInfos:
    info.th2.Draw("colz")
    info.th2.SetStats(0)
    info.th2.SetTitle(info.outHistoName)
    info.th2.SetMinimum(info.zmin)
    info.th2.SetMaximum(info.zmax)
    info.th2.SetLineColor(kBlack)

    canvas.SaveAs(outdir+"PosRes_vs_xy_"+info.outHistoName+".gif")
    canvas.SaveAs(outdir+"PosRes_vs_xy_"+info.outHistoName+".pdf")
    info.th2.Write()

outputfile.Close()

