from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,TF1,gStyle,gROOT
import ROOT
import os
import optparse
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(0)
gStyle.SetOptStat(0)

## Defining Style
myStyle.ForceStyle()

def getFitFunction(fitOrder):
    assert(fitOrder >= 1)
    fitFunction = "[0]"
    for i in range(fitOrder):
        fitFunction += " + [{0}]*pow(x - 0.5, {0})".format(i+1)
    return fitFunction

parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-f','--file', dest='file', default = "myoutputfile.root", help="File name (or path from ../test/)")
parser.add_option('--xmax', dest='xmax', type='float', default = 0.75, help="Set the xmax for the final histogram")
parser.add_option('--pitch', dest='pitch', type='float', default = 100, help="Set the pitch for the fit")
parser.add_option('--fitOrder', dest='fitOrder', type='int', default = 4, help="Set the poly order for the fit")
options, args = parser.parse_args()

file = options.file
inputfile = TFile("../test/"+file)

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
    
    if(nEntries > 0.0):
        myGausFunction = TF1("mygaus","gaus(0)",0,0.1);
        tmpHist.Fit(myGausFunction,"Q","",0,0.1);
        mean = myGausFunction.GetParameter(1)
        meanErr = myGausFunction.GetParError(1)
        sigma = myGausFunction.GetParameter(2)
        
        ###For Debugging
        #tmpHist.Draw("hist")
        #myGausFunction.Draw("same")
        #canvas.SaveAs("q_"+str(i)+".gif")
        #print ("Bin : " + str(i) + " -> " + str(mean))
    else:
        mean=0.0
        meanErr=0.0
       
    Amp1OverAmp1and2_vs_deltaXmax_profile.SetBinContent(i,1000*mean)
    Amp1OverAmp1and2_vs_deltaXmax_profile.SetBinError(i,1000*meanErr)           
        
# Save amplitude histograms
outputfile = TFile("positionRecoFitPlots.root","RECREATE")   
#Amp1OverAmp1and2_vs_deltaXmax_profile.Write()
#outputfile.Close()

xmin=0.50
xmax=options.xmax
pitch = options.pitch
fitOrder = options.fitOrder
fitFunction = getFitFunction(fitOrder)
print(fitFunction)

#fit = TF1("mainFit","pol3",xmin,xmax)
fit = TF1("mainFit",fitFunction,xmin,xmax)
fit.FixParameter(0, 0.5*pitch)
ymax=70
Amp1OverAmp1and2_vs_deltaXmax_profile.SetMaximum(ymax)
Amp1OverAmp1and2_vs_deltaXmax_profile.SetMinimum(0.0001)
Amp1OverAmp1and2_vs_deltaXmax_profile.GetXaxis().SetRangeUser(xmin,xmax)
Amp1OverAmp1and2_vs_deltaXmax_profile.GetXaxis().SetTitle("Amplitude fraction")
Amp1OverAmp1and2_vs_deltaXmax_profile.GetYaxis().SetTitle("Position [#mum]")
results = Amp1OverAmp1and2_vs_deltaXmax_profile.Fit(fit,"SQ","",xmin,xmax)
results.Print("V")


stripWidth = 80
boxes = []
i=0
while i<=ymax+stripWidth/2:
    yt = i+stripWidth/2
    yl = i-stripWidth/2
    if yt>ymax: yt=ymax
    if yl<0: yl=0
    box = ROOT.TBox(xmin,yl, xmax,yt)
    box.SetFillColor(18)
    boxes.append(box)
    i+=pitch

for box in boxes:
    box.Draw()

Amp1OverAmp1and2_vs_deltaXmax_profile.Draw("AXIS same")
Amp1OverAmp1and2_vs_deltaXmax_profile.Draw("same")
fit.Draw("same")
Amp1OverAmp1and2_vs_deltaXmax_profile.Draw("same")

# line = TF1("line","0.0",xmin,1.0)
# line.SetLineColor(ROOT.kBlack)
# line.Draw("same")

myStyle.BeamInfo()
myStyle.SensorInfo("BNL2020", "220")

canvas.SaveAs("PositionFit.gif")
canvas.SaveAs("PositionFit.pdf")
Amp1OverAmp1and2_vs_deltaXmax_profile.Write()
fit.Write()
outputfile.Close()

