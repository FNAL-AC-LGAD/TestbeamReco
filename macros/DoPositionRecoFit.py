from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,TF1,gStyle,gROOT
import ROOT
import os
import optparse
import myStyle
import stripBox

organized_mode=True
gROOT.SetBatch( True )

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
parser.add_option('--xmax', dest='xmax', type='float', default = 0.75, help="Set the xmax for the final histogram")
# parser.add_option('--pitch', dest='pitch', type='float', default = 100, help="Set the pitch for the fit")
parser.add_option('--fitOrder', dest='fitOrder', type='int', default = 4, help="Set the poly order for the fit")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()

dataset = options.Dataset
outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_RecoAnalyzer.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")   

sensor_Geometry = myStyle.GetGeometry(dataset)

xmin=0.50
xmax=options.xmax
pitch = 0.001*sensor_Geometry['pitch'] #0.001*options.pitch
fitOrder = options.fitOrder
fitFunction = getFitFunction(fitOrder)
newFitFunction = getNewFitFunction(fitOrder)
print(fitFunction)
print(newFitFunction)

#Get dX vs a1/(a1+a2) hist
Amp1OverAmp1and2_vs_deltaXmax = inputfile.Get("Amp1OverAmp1and2_vs_deltaXmax")
  
#Define profile hist
Amp1OverAmp1and2_vs_deltaXmax_profile = Amp1OverAmp1and2_vs_deltaXmax.ProjectionY().Clone("Amp1OverAmp1and2_vs_deltaXmax_profile")

canvas = TCanvas("cv","cv",800,800)

#loop over  Amp1OverAmp1and2 bins
for i in range(0, Amp1OverAmp1and2_vs_deltaXmax.GetYaxis().GetNbins() + 1):
    #print ("Bin " + str(i))

    ##For Debugging
    #if not (i==46 and j==5):
    #    continue

    tmpHist = Amp1OverAmp1and2_vs_deltaXmax.ProjectionX("px",i,i)
    myMean = tmpHist.GetMean()
    myRMS = tmpHist.GetRMS()
    nEntries = tmpHist.GetEntries()
    
    if(nEntries > 20.0):
        myGausFunction = TF1("mygaus","gaus(0)",0, pitch);
        tmpHist.Fit(myGausFunction,"Q","",0, pitch);
        mean = myGausFunction.GetParameter(1)
        meanErr = myGausFunction.GetParError(1)
        sigma = myGausFunction.GetParameter(2)
        
        # #For Debugging
        # tmpHist.Draw("hist")
        # myGausFunction.Draw("same")
        # canvas.SaveAs("%sq_%i.gif"%(outdir,i))
        # print ("Bin : " + str(i) + " -> " + str(mean))
    else:
        mean=0.0
        meanErr=0.0

    Amp1OverAmp1and2_vs_deltaXmax_profile.SetBinContent(i,mean)
    Amp1OverAmp1and2_vs_deltaXmax_profile.SetBinError(i,meanErr)           
        
# Save amplitude histograms
outputfile = TFile(outdir+"positionRecoFitPlots.root","RECREATE")   
#Amp1OverAmp1and2_vs_deltaXmax_profile.Write()
#outputfile.Close()

gStyle.SetOptFit(1011)
fit = TF1("mainFit",fitFunction,xmin,xmax)
fit.FixParameter(0, 0.5*pitch)
Amp1OverAmp1and2_vs_deltaXmax_profile.SetMaximum(0.6*pitch)
Amp1OverAmp1and2_vs_deltaXmax_profile.SetMinimum(0.00)
#Amp1OverAmp1and2_vs_deltaXmax_profile.GetXaxis().SetRangeUser(xmin,xmax)
Amp1OverAmp1and2_vs_deltaXmax_profile.GetXaxis().SetRangeUser(xmin,1.0)
results = Amp1OverAmp1and2_vs_deltaXmax_profile.Fit(fit,"SQ","",xmin,xmax)
results.Print("V")

fit2 = TF1("mainFit",getNewFitFunction(1),xmin,1.0)
fit2.FixParameter(0, pitch)
fit2.SetLineColor(ROOT.kBlack)
results2 = Amp1OverAmp1and2_vs_deltaXmax_profile.Fit(fit2,"SQ","",xmin,1.0)
#results2.Print("V")

fit3 = TF1("mainFit",newFitFunction,xmin,xmax)
fit3.FixParameter(0, pitch)
fit3.SetLineColor(ROOT.kBlue+2)
results3 = Amp1OverAmp1and2_vs_deltaXmax_profile.Fit(fit3,"SQ","",xmin,xmax)

string_for_geo = "\nstd::vector<double> positionRecoPar = {"
for deg in range(fitOrder+1):
    string_for_geo+= "%0.6f, "%fit.GetParameter(deg)

string_for_geo+="};\n\n"
string_for_geo = string_for_geo.replace(", }","}")

print(string_for_geo)

width = (inputfile.Get("stripBoxInfo03")).GetMean(2)
#boxes = stripBox.getStripBoxForRecoFit(width, pitch, 0.6*pitch, xmax, xmin)
boxes = stripBox.getStripBoxForRecoFit(width, pitch, 0.6*pitch, 1.0, xmin)
for box in boxes:
         box.Draw()

Amp1OverAmp1and2_vs_deltaXmax_profile.Draw("same axis")
Amp1OverAmp1and2_vs_deltaXmax_profile.Draw("same")
fit.Draw("same")
fit2.Draw("same")
fit3.Draw("same")

line = TF1("line","0.0",xmin,1.0)
line.SetLineColor(ROOT.kBlack)
line.Draw("same")

canvas.SaveAs(outdir+"PositionFit.gif")
canvas.SaveAs(outdir+"PositionFit.pdf")
Amp1OverAmp1and2_vs_deltaXmax_profile.Write()
fit.Write()
outputfile.Close()

