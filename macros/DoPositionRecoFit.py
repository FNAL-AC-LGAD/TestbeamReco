from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,TF1,gStyle,gROOT
import ROOT
import os
import optparse
import myStyle
import stripBox

gROOT.SetBatch( True )
colors = myStyle.GetColors(True)

## Defining Style
myStyle.ForceStyle()


def getFitFunction(fitOrder):
    assert(fitOrder >= 1)
    fitFunction = "[0]"
    for i in range(fitOrder):
        fitFunction += " + [{0}]*pow(x - 0.5, {0})".format(i+1)
    return fitFunction

def getNewFitFunction(fitOrder):
    fitFunction = "(1-x)*[0]"
    if(fitOrder>=2):
        for i in range(2,fitOrder+2):
            if(i<=2): continue
            fitFunction += " + [{0}]*pow(x, {1})".format(i-2,i-1)
    return fitFunction


parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xmax', dest='xmax', type='float', default = 0.75, help="Set the xmax for the final histogram")
# parser.add_option('--pitch', dest='pitch', type='float', default = 100, help="Set the pitch for the fit")
parser.add_option('-O','--fitOrder', dest='fitOrder', type='int', default = 4, help="Set the poly order for the fit")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-A', dest='Use_Analyze', action='store_true', default = False, help="Use Analyze file as input")
parser.add_option('-R', dest='Use_Reco', action='store_true', default = False, help="Use RecoAnalyze file as input")
options, args = parser.parse_args()

useAnalyze = options.Use_Analyze
useReco = options.Use_Reco
dataset = options.Dataset

if (useAnalyze == useReco):
    print(" >> Using Analyze file by default.")
    useAnalyze = True

outdir = myStyle.getOutputDir(dataset)
analyze = "Analyze" if useAnalyze else "RecoAnalyzer"
inputfile = TFile("%s%s_%s.root"%(outdir, dataset, analyze))

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch = sensor_Geometry['pitch']
width = sensor_Geometry['stripWidth']
strip_length = sensor_Geometry['length']

xmin = 0.50
xmax = float(options.xmax)
pitch = 0.001*pitch
width = 0.001*width
fitOrder = options.fitOrder

# Setting fit functions
fitFunction = getFitFunction(fitOrder)
newFitFunction = getNewFitFunction(fitOrder)
print(" - Fit function: %s"%fitFunction)
print(" - Extra fit: %s"%newFitFunction)

#Get dX vs a1/(a1+a2) hist
Amp1OverAmp1and2_vs_deltaXmax = inputfile.Get("Amp1OverAmp1and2_vs_deltaXmax")

#Define profile hist
Amp1OverAmp1and2_vs_deltaXmax_profile = Amp1OverAmp1and2_vs_deltaXmax.ProjectionY().Clone("Amp1OverAmp1and2_vs_deltaXmax_profile")

canvas = TCanvas("cv","cv",1000,800)
gStyle.SetOptStat(1)

nbins = Amp1OverAmp1and2_vs_deltaXmax.GetYaxis().GetNbins()

# Loop over Amp1OverAmp1and2 bins
for i in range(1, nbins+1):
    tmpHist = Amp1OverAmp1and2_vs_deltaXmax.ProjectionX("px",i,i)
    myMean = tmpHist.GetMean()
    myRMS = tmpHist.GetRMS()
    nEntries = tmpHist.GetEntries()

    if (nEntries > 20.0):
        myGausFunction = TF1("mygaus","gaus(0)",0, pitch);
        tmpHist.Fit(myGausFunction,"Q","",0, pitch);
        mean = myGausFunction.GetParameter(1)
        meanErr = myGausFunction.GetParError(1)
        sigma = myGausFunction.GetParameter(2)

    else:
        mean = 0.0
        meanErr = 0.0

    Amp1OverAmp1and2_vs_deltaXmax_profile.SetBinContent(i, mean)
    Amp1OverAmp1and2_vs_deltaXmax_profile.SetBinError(i, meanErr)

# Define output file
output_path = "%spositionRecoFit.root"%(outdir)
outputfile = TFile(output_path,"RECREATE")

gStyle.SetOptFit(1011)
ymin, ymax = 0.0, 0.6*pitch
Amp1OverAmp1and2_vs_deltaXmax_profile.SetMinimum(ymin)
Amp1OverAmp1and2_vs_deltaXmax_profile.SetMaximum(ymax)
Amp1OverAmp1and2_vs_deltaXmax_profile.GetXaxis().SetRangeUser(xmin, 1.0)
Amp1OverAmp1and2_vs_deltaXmax_profile.SetLineWidth(1)
frac_title = ";Amplitude fraction;Position [mm]"
Amp1OverAmp1and2_vs_deltaXmax_profile.SetTitle(frac_title)


# Reference line - fit
fitLine = TF1("refLine", getNewFitFunction(1), xmin, 1.0)
fitLine.FixParameter(0, pitch)
fitLine.SetLineColor(ROOT.kBlack)
results2 = Amp1OverAmp1and2_vs_deltaXmax_profile.Fit(fitLine, "SQ", "", xmin, 1.0)
#results2.Print("V")

# Use "new" fit (just a second reference)
fit2nd = TF1("secondFit", newFitFunction, xmin, xmax)
fit2nd.FixParameter(0, pitch)
fit2nd.SetLineColor(ROOT.kBlue+2)
results3 = Amp1OverAmp1and2_vs_deltaXmax_profile.Fit(fit2nd, "SQ", "" ,xmin, xmax)

# Main fit
fit = TF1("mainFit", fitFunction, xmin, xmax)
fit.FixParameter(0, 0.5*pitch)
results = Amp1OverAmp1and2_vs_deltaXmax_profile.Fit(fit, "SQ", "", xmin, xmax)
results.Print("V")


# Print fit info to be directly copied into Geometry
str_geometry = "\ndouble positionRecoMaxPoint = %.2f;"%xmax
str_geometry+= "\nstd::vector<double> positionRecoPar = {"
for deg in range(fitOrder+1):
    str_geometry+= "%0.6f, "%fit.GetParameter(deg)
str_geometry+="};\n\n"
str_geometry = str_geometry.replace(", }","}")
print(str_geometry)

# Draw and save fits
Amp1OverAmp1and2_vs_deltaXmax_profile.Draw("AXIS")

boxes = stripBox.getStripBoxForRecoFit(width, pitch, ymax, 1.0, xmin)
for box in boxes:
    box.Draw()

Amp1OverAmp1and2_vs_deltaXmax_profile.Draw("same")
fitLine.Draw("same")
fit2nd.Draw("same")
fit.Draw("same")

Amp1OverAmp1and2_vs_deltaXmax_profile.Draw("AXIS same")

save_path = "%sPositionRecoFit"%(outdir)

canvas.SaveAs("%s.gif"%save_path)
canvas.SaveAs("%s.pdf"%save_path)

Amp1OverAmp1and2_vs_deltaXmax_profile.Write()
fit.Write()
outputfile.Close()
