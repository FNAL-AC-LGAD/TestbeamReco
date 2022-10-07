from ROOT import TH1, TH1F, TH1D, TFile, TCanvas, gStyle, gROOT
import ROOT
import optparse
import myStyle

ROOT.gROOT.SetBatch(True)
colors = myStyle.GetColors(True)
myStyle.ForceStyle()
# ROOT.gStyle.SetLegendBorderSize(2)
# ROOT.gROOT.ForceStyle()

# ROOT.gStyle.SetOptFit(1)
# ROOT.gStyle.SetPadRightMargin(2*myStyle.GetMargin())
# ROOT.gStyle.SetTextSize(myStyle.GetSize()-5)
# ROOT.gStyle.SetLabelSize(myStyle.GetSize()-10,"x")
# ROOT.gStyle.SetLabelSize(myStyle.GetSize()-10,"y")
# ROOT.gStyle.SetLabelSize(myStyle.GetSize()-10,"z")
# ROOT.gStyle.SetHistLineWidth(2)
# ROOT.gROOT.ForceStyle()

def draw1D(h, n, legend, fmin=-1, fmax=1):
    # ROOT.gStyle.SetOptFit(1)
    # c = ROOT.TCanvas("c","c",1000,1000)
    # ROOT.gPad.SetTicks(1,1)
    # ROOT.TH1.SetDefaultSumw2()
    #ROOT.gPad.SetLogy()
    # ROOT.gROOT.ForceStyle()

    # h = hist
    h.Rebin(2)
    # h.GetXaxis().SetTitle(xTitle)
    # h.GetYaxis().SetTitle(yTitle)
    h.SetLineColor(colors[2*n])
    h.SetLineWidth(2)
    # h = normHist(hist)
    # h.Scale(1.0/h.Integral())
    h.Scale(1.0/h.GetMaximum())
    h.Draw('hist e same')
    myMean = h.GetMean()
    myRMS = h.GetRMS()
    # Range used to reproduce Paper plots [myMean + (fmin)*myRMS, myMean + (fmax)*myRMS] -> [fmin, fmax]

    fitlow = myMean + fmin*myRMS
    fithigh = myMean + fmax*myRMS

    fit = ROOT.TF1("fit%i"%n, "gaus", fitlow, fithigh)    
    fit.SetLineColor(colors[2*n])
    fit.SetLineStyle(2)
    fit.SetLineWidth(3)
    #fit.Draw("same")
    h.Fit(fit,"Q", "", fitlow, fithigh)
    fit.Draw("same")

    subscript = "25-200" if "25-200" in myStyle.GetGeometry(sensor_list[n])["sensor"] else "10-200"

    # print("%.2f, %.2f, %.2f"%(fit.GetParameter(0),fit.GetParameter(1),fit.GetParameter(2)))
    legend.AddEntry(h, "#splitline{%s}{#sigma_{%s} = %.2f [mm]}"%(myStyle.GetGeometry(sensor_list[n])["sensor"], subscript, fit.GetParameter(2)))
    # legend.AddEntry(h, myStyle.GetGeometry(sensor_list[n])["sensor"])
    # legend.AddEntry(fit, "#sigma_{%s} = %.2f [mm]"%(myStyle.GetGeometry(sensor_list[n])["sensor"], fit.GetParameter(2)))

    # c.Print("%s.png"%(name))
    # c.Print("%s.gif"%(name))
    # c.Print("%s.pdf"%(name))

def normHist(hist):
    # h = f.Get(name)
    # h.Rebin(rebin)
    h = hist.Scale(1.0/hist.Integral())
    # h.SetLineColor(color)
    # h.SetLineWidth(2)
    return h

# fit_range = {   "EIC_W2_1cm_500up_300uw_240V": {'one': [-2.7,2.7], 'two': [-0.8,0.8]}, "EIC_W1_1cm_500up_200uw_255V": {'one': [-3.0,3.0], 'two': [-1.1,1.1]},
#                 "EIC_W2_1cm_500up_100uw_220V": {'one': [-2.7,2.7], 'two': [-1.4,1.4]}, "EIC_W1_2p5cm_500up_200uw_215V": {'one': [-3.0,3.0], 'two': [-0.8,0.6]},
#                 "EIC_W1_0p5cm_500up_200uw_1_4_245V": {'one': [-4.0,4.0], 'two': [-1.1,1.1]} }


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
# parser.add_option('--runPad', dest='runPad', action='store_true', default = False, help="Is pad (True) or strip (False). Needed when -a=True.")
# parser.add_option('-a', dest='plotAll', action='store_true', default = False, help="Draw all channels")
parser.add_option('-m', '--min', dest='min', default=-1.0, type="float", help="Low limit of the fit (fmin): myMean + (fmin)*myRMS.")
parser.add_option('-M', '--max', dest='max', default=1.0, type="float", help="High limit of the fit (fmax): myMean + (fmax)*myRMS.")
# parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()

# dataset = options.Dataset
# runPad = options.runPad
fitmin = options.min
fitmax = options.max

# outdir=""
# outdir = myStyle.getOutputDir(dataset)
# inputfile = ROOT.TFile("%s%s_Analyze.root"%(outdir,dataset))
outdir = myStyle.getOutputDir("Paper2022")

canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)

# hist_info = ('deltaY_twoStrips','deltaY_twoStrips','tracker',fitmin,fitmax)

# hdummy = TH1D("","", 1,-24.0,24.0)
hdummy = TH1D("","", 1,-20.0,20.0)
hdummy.GetXaxis().SetTitle("Position y reconstructed - tracker [mm]")
hdummy.GetYaxis().SetTitle("Counts / Maximum count")
# hdummy.SetMaximum(90.0)
# hdummy.SetMaximum(25000.0)
hdummy.SetMaximum(1.1)
hdummy.SetMinimum(0.0001)
hdummy.Draw("AXIS")

# legend = ROOT.TLegend(2*myStyle.GetMargin()+0.01, 1-myStyle.GetMargin()-0.01-0.24, 2*myStyle.GetMargin()+0.01+0.35, 1-myStyle.GetMargin()-0.01)
legend = ROOT.TLegend(1-myStyle.GetMargin()-0.03-0.35, 1-myStyle.GetMargin()-0.02-0.24, 1-myStyle.GetMargin()-0.03, 1-myStyle.GetMargin()-0.02)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-4)

fit_limits = [[-1.5, 1.5], [-2.0, 2.0]]

sensor_list = ["EIC_W1_2p5cm_500up_200uw_215V", "EIC_W1_1cm_500up_200uw_255V"] # , "EIC_W1_0p5cm_500up_200uw_1_4_245V"
list_input = []
for i,name in enumerate(sensor_list):
    file = TFile("../output/%s/%s_Analyze.root"%(name,name),"READ")
    list_input.append(file)
    this_hist = list_input[-1].Get('deltaY_twoStrips')
    # draw1D(this_hist, i, legend, fitmin,fitmax)
    draw1D(this_hist, i, legend, fit_limits[i][0],fit_limits[i][1])

legend.Draw()

myStyle.BeamInfo()
text = ROOT.TLatex()
text.SetTextSize(myStyle.GetSize()-4)
text.SetTextAlign(31)
text.DrawLatexNDC(1-myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{Varying length}")

canvas.Print("%s1DRes_1cmVs2p5cm.gif"%(outdir))
canvas.Print("%s1DRes_1cmVs2p5cm.pdf"%(outdir))

for f in list_input:
    f.Close()
