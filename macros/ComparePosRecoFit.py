from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,TF1,gStyle,gROOT
import ROOT
import os
import optparse
import myStyle
import stripBox

myStyle.ForceStyle()
gStyle.SetOptStat(0)
organized_mode=True
gROOT.SetBatch( True )
tsize = myStyle.GetSize()

ROOT.gStyle.SetLabelSize(tsize-10,"x")
ROOT.gStyle.SetTitleSize(tsize,"x")
ROOT.gStyle.SetLabelSize(tsize-10,"y")
ROOT.gStyle.SetTitleSize(tsize,"y")
ROOT.gStyle.SetLabelSize(tsize-10,"z")
ROOT.gStyle.SetTitleSize(tsize,"z")
ROOT.gROOT.ForceStyle()

def getFitFunction(parameters):
    for i,par in enumerate(parameters):
        if i==0:
            fitFunction = "%.6f"%(par)
        else:
            fitFunction += " + %.6f*pow(x - 0.5, %i)"%(par,i)
    return fitFunction

dataset = "EIC_W1_1cm_255V"
outdir = myStyle.getOutputDir(dataset)

colors = myStyle.GetColors()
# colors = [ROOT.kRed, ROOT.kGreen, ROOT.kBlue]

sensor_list = ["EIC_W2_1cm_500um_200um_gap_240V", "EIC_W1_1cm_255V", "EIC_W2_1cm_500um_400um_gap_220V"]

sensor_reco = { "EIC_W2_1cm_500um_200um_gap_240V": {'recomax': 0.72, 'xmax': 0.74, 'recoPars':[0.250000, -0.654507, 8.251580, -118.137841, 684.216545, -1407.697202]},
                "EIC_W1_1cm_255V": {'recomax': 0.77, 'xmax': 0.81, 'recoPars':[0.250000, -0.414954, -3.861040, 37.128136, -141.558350, 162.643997]},
                "EIC_W2_1cm_500um_400um_gap_220V": {'recomax': 0.81, 'xmax': 0.82, 'recoPars':[0.250000, -0.615442, -0.768993, 5.082484, -12.892653]},}

xmin=0.50
xmax=0.82
ymin=0.001
ymax=0.30

# gStyle.SetOptFit(0)
# gROOT.ForceStyle()
canvas = TCanvas("cv","cv",800,800)

# Save amplitude histograms
outputfile = TFile(outdir+"ComparePosRecoFit.root","RECREATE")   
#Amp1OverAmp1and2_vs_deltaXmax_profile.Write()
#outputfile.Close()

temp_hist = TH1F("htemp","", 1, xmin, xmax)
temp_hist.GetXaxis().SetTitle("Amplitude fraction")
temp_hist.GetYaxis().SetRangeUser(ymin, ymax)
temp_hist.GetYaxis().SetTitle("Position [#mum]")
temp_hist.Draw("axis")

pitch = 0.5
for i,item in enumerate(sensor_list):
    sensor_Geometry = myStyle.GetGeometry(item)
    width = 0.001*sensor_Geometry['stripWidth']
    boxes = stripBox.getStripBoxForRecoFit(width, pitch, 0.6*pitch, xmax, xmin)
    for box in boxes:
        box.SetFillColorAlpha(colors[i],0.1)
        box.DrawClone("same")

temp_hist.Draw("same axis")

legend = TLegend(1-myStyle.GetMargin()-0.55,1-myStyle.GetMargin()-0.2,1-myStyle.GetMargin()-0.05,1-myStyle.GetMargin()-0.02)
legend.SetBorderSize(0)
legend.SetFillColor(ROOT.kWhite)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-14)
legend.SetFillStyle(0)

fitFunction_list = []
for i,item in enumerate(sensor_list):
    fitFunction = getFitFunction(sensor_reco[item]['recoPars'])
    xmax_s = sensor_reco[item]['xmax']
    recomax_s = sensor_reco[item]['recomax']

    print(fitFunction)

    sensor_Geometry = myStyle.GetGeometry(item)

    func1 = TF1("f1%i"%(i),fitFunction,xmin,recomax_s)
    func1.SetLineColor(colors[i])
    name = sensor_Geometry['sensor']
    fitFunction_list.append(func1)
    func1.DrawCopy("same")
    legend.AddEntry(fitFunction_list[-1], name,"L")

    func2 = TF1("f2%i"%(i),fitFunction,recomax_s,xmax_s)
    func2.SetLineStyle(2)
    func2.SetLineColorAlpha(colors[i],0.8)
    func2.DrawCopy("same")

legend.Draw();

canvas.SaveAs(outdir+"ComparePosRecoFit.gif")
canvas.SaveAs(outdir+"ComparePosRecoFit.pdf")
# Amp1OverAmp1and2_vs_deltaXmax_profile.Write()
# fit.Write()
outputfile.Close()

