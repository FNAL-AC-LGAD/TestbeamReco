import ROOT
import optparse
ROOT.gROOT.SetBatch(True)
from array import array
from AlignBinning import z_values, alpha_values, beta_values

def cosmetic_tgraph(graph):
        # graph.SetLineColor(colors[colorindex])
        # graph.SetMarkerColor(colors[colorindex])
        graph.SetMarkerSize(0.75)
        graph.SetMarkerStyle(20)

def plot1D(hists, colors, labels, name, xlab, ylab, bins=100, arange=(0,1)):
        ROOT.gStyle.SetOptFit(1)
        c = ROOT.TCanvas("c","c",1000,1000)
        ROOT.gPad.SetLeftMargin(0.12)
        ROOT.gPad.SetRightMargin(0.15)
        ROOT.gPad.SetTopMargin(0.08)
        ROOT.gPad.SetBottomMargin(0.12)
        ROOT.gPad.SetTicks(1,1)
        ROOT.TH1.SetDefaultSumw2()
        #ROOT.gPad.SetLogy()

        h = hists[0]
        h.GetXaxis().SetTitle(ylab)
        h.GetYaxis().SetTitle(xlab)
        h.Draw('hists e')
        myMean = h.GetMean()
        myRMS = h.GetRMS()
        fitlow = myMean - 1.2*myRMS
        fithigh = myMean + myRMS

        fit = ROOT.TF1("fit", "gaus", fitlow, fithigh)    
        fit.SetLineColor(ROOT.kRed)
        #fit.Draw("same")
        h.Fit(fit,"Q", "", fitlow, fithigh)
        fit.Draw("same")    

        #c.Print("%s.png"%(name))
     #   c.Print("%s.gif"%(name))
        return 1000.*fit.GetParameter(2),1000.*fit.GetParError(2)



# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('--runPad', dest='runPad', action='store_true', default = False, help="run fits or not")
options, args = parser.parse_args()

f = ROOT.TFile('../test/myout2.root')

hists=[]
for i in range(len(z_values)):
        i_z = 4 + 4*9 + i*81
        #if i%81 == 40:
        hists.append(('deltaX_var%i'%i_z,'deltaX_variant_%i'%i_z,"tracker"))

resolutions=[]
res_errs=[]
for ivar,t in enumerate(hists):
        h = f.Get(t[0])
        resolution,error = plot1D([h], [ROOT.kBlack], [t[1]], t[0], 'Events', t[1]+' - '+t[2])
        resolutions.append(resolution)
        res_errs.append(error)
        print("res:%0.2f, z: %0.f "%(resolutions[-1],z_values[ivar]))


resolution_vs_z = ROOT.TGraphErrors(len(z_values),array("d",z_values),array("d",resolutions),array("d",[0.01 for i in z_values]),array("d",res_errs))
resolution_vs_z.SetTitle(";Assigned Z position [mm];Resolution [microns]")
cosmetic_tgraph(resolution_vs_z)


c = ROOT.TCanvas("c","c",1000,600)

fitFunc = ROOT.TF1("","pol2",z_values[0], z_values[-1]);
results = resolution_vs_z.Fit(fitFunc,"Q","",z_values[0], z_values[-1]);
#results.Print("V")
a = fitFunc.GetParameter(2)
b = fitFunc.GetParameter(1)
print(a, b)
print("Minimum at: {}".format(-(b)/(2*a)))


resolution_vs_z.Draw("aep")


#mean = myGausFunction.GetParameter(1)
#meanErr = myGausFunction.GetParError(1)
#sigma = myGausFunction.GetParameter(2)
fitFunc.Draw("same")

c.Print("%s.pdf"%("scan_summary_overlay"))

