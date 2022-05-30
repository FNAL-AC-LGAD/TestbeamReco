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

def getFitFunction(parameters):
    for i,par in enumerate(parameters):
        if i==0:
            fitFunction = "%.6f"%(par)
        else:
            fitFunction += " + %.6f*pow(x - 0.5, %i)"%(par,i)
    return fitFunction

# parser = optparse.OptionParser("usage: %prog [options]\n")
# # parser.add_option('--xmax', dest='xmax', type='float', default = 0.75, help="Set the xmax for the final histogram")
# # parser.add_option('--pitch', dest='pitch', type='float', default = 100, help="Set the pitch for the fit")
# # parser.add_option('--fitOrder', dest='fitOrder', type='int', default = 4, help="Set the poly order for the fit")
# # parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
# options, args = parser.parse_args()

dataset = "EIC_W1_1cm_255V"
outdir = myStyle.getOutputDir(dataset)

colors = myStyle.GetColors()

# outdir=""
# if organized_mode: 
#     outdir = myStyle.getOutputDir(dataset)
#     inputfile = TFile("%s%s_RecoAnalyzer.root"%(outdir,dataset))
# else: 
#     inputfile = TFile("../test/myoutputfile.root")

# pitch = 0.001*sensor_Geometry['pitch'] #0.001*options.pitch
# fitOrder = options.fitOrder

sensor_list = ["EIC_W2_1cm_500um_200um_gap_240V", "EIC_W1_1cm_255V", "EIC_W2_1cm_500um_400um_gap_220V"]

sensor_reco = { "EIC_W2_1cm_500um_200um_gap_240V": {'recomax': 0.72, 'xmax': 0.74, 'recoPars':[0.250000, -0.654507, 8.251580, -118.137841, 684.216545, -1407.697202]},
                "EIC_W1_1cm_255V": {'recomax': 0.77, 'xmax': 0.81, 'recoPars':[0.250000, -0.414954, -3.861040, 37.128136, -141.558350, 162.643997]},
                "EIC_W2_1cm_500um_400um_gap_220V": {'recomax': 0.81, 'xmax': 0.82, 'recoPars':[0.250000, -0.615442, -0.768993, 5.082484, -12.892653]},}

xmin=0.50
xmax=0.82
ymin=0.00
ymax=0.30

# gStyle.SetOptFit(0)
# gROOT.ForceStyle()
canvas = TCanvas("cv","cv",800,800)

# Save amplitude histograms
outputfile = TFile(outdir+"ComparePosRecoFit.root","RECREATE")   
#Amp1OverAmp1and2_vs_deltaXmax_profile.Write()
#outputfile.Close()

temp_hist = TH1F("htemp","", 1, xmin-0.05, xmax+0.05)
temp_hist.GetXaxis().SetTitle("Relative signal amplitude")
temp_hist.GetYaxis().SetRangeUser(ymin, ymax)
temp_hist.Draw("axis")

pitch = 0.5
for i,item in enumerate(sensor_list):
    sensor_Geometry = myStyle.GetGeometry(item)
    width = 0.001*sensor_Geometry['stripWidth']
    boxes = stripBox.getStripBoxForRecoFit(width, pitch, 0.6*pitch, xmax, xmin)
    for box in boxes:
        box.SetFillColorAlpha(colors[i],0.2)
        box.DrawClone("same")

temp_hist.Draw("same axis")

legend = TLegend(1-myStyle.GetMargin()-0.55,1-myStyle.GetMargin()-0.2,1-myStyle.GetMargin()-0.05,1-myStyle.GetMargin()-0.02)
legend.SetBorderSize(0)
legend.SetFillColor(ROOT.kWhite)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-14)
legend.SetFillStyle(0)

for i,item in enumerate(sensor_list):
    fitFunction = getFitFunction(sensor_reco[item]['recoPars'])
    xmax_s = sensor_reco[item]['xmax']
    recomax_s = sensor_reco[item]['recomax']

    print(fitFunction)

    sensor_Geometry = myStyle.GetGeometry(item)

    func = TF1("f%s"%(item),fitFunction,xmin,xmax_s)
    func.SetLineColor(colors[i])
    name = sensor_Geometry['sensor']
    legend.AddEntry(func, name,"L")
    func.DrawCopy("same")
    ### FINISH DRAWING ALL FIT FUNCTIONS AND ADD A DIFFERENT COLOR OR STYLE WHEN REACHING THE MAX RECO VALUE

legend.Draw();

# line = TF1("line","0.0",xmin,1.0)
# line.SetLineColor(ROOT.kBlack)
# line.Draw("same")

canvas.SaveAs(outdir+"ComparePosRecoFit.gif")
canvas.SaveAs(outdir+"ComparePosRecoFit.pdf")
# Amp1OverAmp1and2_vs_deltaXmax_profile.Write()
# fit.Write()
outputfile.Close()

