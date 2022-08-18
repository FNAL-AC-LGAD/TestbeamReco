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

ROOT.gStyle.SetPadRightMargin(2*myStyle.GetMargin())
ROOT.gROOT.ForceStyle()

def getFitFunction(parameters, scale):
    for i,par in enumerate(parameters):
        if i==0:
            fitFunction = "%.6f"%(scale*par)
        else:
            fitFunction += " + %.6f*pow(x - 0.5, %i)"%(scale*par,i)
    return fitFunction

outdir = myStyle.getOutputDir("Paper2022")

colors = myStyle.GetColors(True)
# colors = [ROOT.kRed, ROOT.kRed, ROOT.kGreen, ROOT.kGreen, ROOT.kBlue, ROOT.kBlue, ROOT.kMagenta, ROOT.kMagenta,]

# sensor_list = ["EIC_W2_1cm_500up_300uw_240V", "EIC_W1_1cm_500up_200uw_255V", "EIC_W2_1cm_500up_100uw_220V"]
sensor_list = ["EIC_W1_2p5cm_500up_200uw_215V", "EIC_W1_1cm_500up_200uw_255V", "EIC_W1_0p5cm_500up_200uw_1_4_245V"]

# sensor_reco = { "EIC_W2_1cm_500um_200um_gap_240V": {'recomax': 0.72, 'xmax': 0.74, 'recoPars':[0.250000, -0.654507, 8.251580, -118.137841, 684.216545, -1407.697202]},
#                 # "EIC_W1_1cm_255V": {'recomax': 0.77, 'xmax': 0.81, 'recoPars':[0.250000, -0.414954, -3.861040, 37.128136, -141.558350, 162.643997]},
#                 "EIC_W1_1cm_255V": {'recomax': 0.77, 'xmax': 0.81, 'recoPars':[0.250000, -0.483075, -1.464649, 9.779935, -18.860555, -22.898713]},
#                 "EIC_W2_1cm_500um_400um_gap_220V": {'recomax': 0.81, 'xmax': 0.82, 'recoPars':[0.250000, -0.615442, -0.768993, 5.082484, -12.892653]},}

sensor_reco = { "EIC_W1_2p5cm_500up_200uw_215V"    : {'recomax': 0.73, 'xmax': 0.74, 'recoPars':[0.250000, -0.786175, 1.527987, -7.541677, 8.530849]},
                "EIC_W1_1cm_500up_200uw_255V"      : {'recomax': 0.77, 'xmax': 0.81, 'recoPars':[0.250000, -0.483075, -1.464649, 9.779935, -18.860555, -22.898713]},
                "EIC_W1_0p5cm_500up_200uw_1_4_245V": {'recomax': 0.84, 'xmax': 0.88, 'recoPars':[0.250000, -0.504018, 1.821950, -18.300502, 73.162455, -104.089614]},}


pitch = 500 #um
y_scale = 1000 # mm to micron

xmin=0.50
xmax=0.90
ymin=0.001
ymax=0.30*y_scale

# gStyle.SetOptFit(0)
# gROOT.ForceStyle()
canvas = TCanvas("cv","cv",1000,800)

# Save amplitude histograms
outputfile = TFile(outdir+"ComparePosRecoFit_DiffLength.root","RECREATE")   
#Amp1OverAmp1and2_vs_deltaXmax_profile.Write()
#outputfile.Close()

temp_hist = TH1F("htemp","", 1, xmin, xmax)
temp_hist.GetXaxis().SetTitle("Amplitude fraction")
temp_hist.GetYaxis().SetRangeUser(ymin, ymax)
temp_hist.GetYaxis().SetTitle("Position [#mum]")
temp_hist.Draw("axis")

## Add second axis at the right
right_axis = ROOT.TGaxis(xmax,0.0001,xmax, ymax,0.0001, ymax/pitch,510,"+L")
right_axis.UseCurrentStyle()
right_axis.SetTitle("Pitch fraction")
right_axis.SetLabelSize(myStyle.GetSize()-10)
right_axis.SetTitleSize(myStyle.GetSize())
right_axis.SetLabelFont(myStyle.GetFont())
right_axis.SetTitleFont(myStyle.GetFont())
# right_axis.SetLineColor(ROOT.kRed)
right_axis.Draw()

# for i,item in enumerate(sensor_list):
#     sensor_Geometry = myStyle.GetGeometry(item)
#     width = sensor_Geometry['stripWidth']
#     boxes = stripBox.getStripBoxForRecoFit(width, pitch, ymax, xmax, xmin)
#     for box in boxes:
#         box.SetFillColorAlpha(colors[2*i],0.3)
#         box.DrawClone("same")

boxes = stripBox.getStripBoxForRecoFit(200, pitch, ymax, xmax, xmin)
for box in boxes:
        box.DrawClone("same")

for i,item in enumerate(sensor_list):
    sensor_Geometry = myStyle.GetGeometry(item)
    width = sensor_Geometry['stripWidth']
    horizontal_line = ROOT.TLine(xmin, width/2., xmax, width/2.)
    horizontal_line.SetLineWidth(3)
    horizontal_line.SetLineStyle(9)
    horizontal_line.SetLineColorAlpha(colors[2*i],0.4)
    horizontal_line.DrawClone("same")

temp_hist.Draw("same axis")

# legend = TLegend(1-myStyle.GetMargin()-0.55,1-myStyle.GetMargin()-0.2,1-myStyle.GetMargin()-0.05,1-myStyle.GetMargin()-0.02)
legend = TLegend(1-myStyle.GetMargin()-0.35,1-myStyle.GetMargin()-0.25,1-myStyle.GetMargin()-0.03,1-myStyle.GetMargin()-0.05)
legend.SetBorderSize(0)
legend.SetFillColor(ROOT.kWhite)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-14)
legend.SetFillStyle(0)

fitFunction_list = []
for i,item in enumerate(sensor_list):
    fitFunction = getFitFunction(sensor_reco[item]['recoPars'], y_scale)
    xmax_s = sensor_reco[item]['xmax']
    recomax_s = sensor_reco[item]['recomax']

    print(fitFunction)

    sensor_Geometry = myStyle.GetGeometry(item)

    func1 = TF1("f1%i"%(i),fitFunction,xmin,recomax_s)
    func1.SetLineColor(colors[2*i])
    name = sensor_Geometry['sensor']
    fitFunction_list.append(func1)
    func1.DrawCopy("same")
    legend.AddEntry(fitFunction_list[-1], name,"L")

    func2 = TF1("f2%i"%(i),fitFunction,recomax_s,xmax_s)
    func2.SetLineStyle(2)
    func2.SetLineColorAlpha(colors[2*i],0.8)
    func2.DrawCopy("same")

legend.Draw();

myStyle.BeamInfo()

TopRightText = ROOT.TLatex()
TopRightText.SetTextSize(myStyle.GetSize()-4)
TopRightText.SetTextAlign(31)
TopRightText.DrawLatexNDC(1-2*myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{Diff Length}")

canvas.SaveAs(outdir+"ComparePosRecoFit_DiffLength.gif")
canvas.SaveAs(outdir+"ComparePosRecoFit_DiffLength.pdf")
# Amp1OverAmp1and2_vs_deltaXmax_profile.Write()
# fit.Write()
outputfile.Close()

