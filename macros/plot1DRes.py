import ROOT
ROOT.gROOT.SetBatch(True)

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

        c.Print("%s.png"%(name))
        c.Print("%s.gif"%(name))


f = ROOT.TFile('../test/myoutputfile.root')

hists = list(('weighted_timeDiff_channel0{}'.format(i),'weightedTime','photek') for i in range(0,5+1))
hists += list(('timeDiff_channel0{}'.format(i),'time','photek') for i in range(0,5+1))
hists += [("weighted_timeDiff","weightedTime","photek"), ("timeDiff","time","photek"), ("timeDiff_amp2","time","photek"), ("timeDiff_amp3","time","photek"),('deltaX','deltaX',"tracker")]

for t in hists:
	h = f.Get(t[0])
	plot1D([h], [ROOT.kBlack], [t[1]], t[0], 'Events', t[1]+' - '+t[2])

