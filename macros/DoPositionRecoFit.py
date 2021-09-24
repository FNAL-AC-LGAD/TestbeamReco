from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,TF1,gStyle,gROOT
import ROOT
import os
import optparse

gROOT.SetBatch( True )

def getFitFunction(fitOrder):
    assert(fitOrder >= 1)
    fitFunction = "[0]"
    for i in range(fitOrder):
        fitFunction += " + [{0}]*pow(x - 0.5, {0})".format(i+1)
    return fitFunction

parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('--xmax', dest='xmax', type='float', default = 0.75, help="Set the xmax for the final histogram")
parser.add_option('--pitch', dest='pitch', type='float', default = 100, help="Set the pitch for the fit")
parser.add_option('--fitOrder', dest='fitOrder', type='int', default = 4, help="Set the poly order for the fit")
options, args = parser.parse_args()

inputfile = TFile("../test/myoutputfile.root")

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
       
    Amp1OverAmp1and2_vs_deltaXmax_profile.SetBinContent(i,mean)
    Amp1OverAmp1and2_vs_deltaXmax_profile.SetBinError(i,meanErr)           
        
# Save amplitude histograms
outputfile = TFile("positionRecoFitPlots.root","RECREATE")   
#Amp1OverAmp1and2_vs_deltaXmax_profile.Write()
#outputfile.Close()

xmin=0.50
xmax=options.xmax
pitch = 0.001*options.pitch
fitOrder = options.fitOrder
fitFunction = getFitFunction(fitOrder)
print(fitFunction)

gStyle.SetOptFit(1011)
#fit = TF1("mainFit","pol3",xmin,xmax)
fit = TF1("mainFit",fitFunction,xmin,xmax)
fit.FixParameter(0, 0.5*pitch)
Amp1OverAmp1and2_vs_deltaXmax_profile.SetMaximum(0.17)
Amp1OverAmp1and2_vs_deltaXmax_profile.SetMinimum(0.00)
Amp1OverAmp1and2_vs_deltaXmax_profile.GetXaxis().SetRangeUser(xmin,xmax)
results = Amp1OverAmp1and2_vs_deltaXmax_profile.Fit(fit,"SQ","",xmin,xmax)
results.Print("V")


Amp1OverAmp1and2_vs_deltaXmax_profile.Draw()
fit.Draw("same")
Amp1OverAmp1and2_vs_deltaXmax_profile.Draw("same")

line = TF1("line","0.0",xmin,1.0)
line.SetLineColor(ROOT.kBlack)
line.Draw("same")

canvas.SaveAs("PositionFit.gif")
canvas.SaveAs("PositionFit.pdf")
Amp1OverAmp1and2_vs_deltaXmax_profile.Write()
fit.Write()
outputfile.Close()

