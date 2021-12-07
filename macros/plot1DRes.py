import ROOT
import optparse
ROOT.gROOT.SetBatch(True)

def plot1D(hists, colors, labels, name, xlab, ylab, pads=False, bins=100, arange=(0,1)):
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
        # fitlow = myMean - 0.8*myRMS
        fitlow = myMean - 0.65*myRMS
        fithigh = myMean + 0.6*myRMS

    
            
        fit = ROOT.TF1("fit", "gaus", fitlow, fithigh)    
        fit.SetLineColor(ROOT.kRed)
        #fit.Draw("same")
        h.Fit(fit,"Q", "", fitlow, fithigh)
        fit.Draw("same")    

        c.Print("%s.png"%(name))
        c.Print("%s.gif"%(name))
        c.Print("%s.pdf"%(name))

def getHisto(f, name, rebin, color):
        h = f.Get(name)
        h.Rebin(rebin)
        h.Scale(1.0/h.Integral())
        h.SetLineColor(color)
        h.SetLineWidth(2)
        return h

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('--runPad', dest='runPad', action='store_true', default = False, help="run fits or not")
options, args = parser.parse_args()

f = ROOT.TFile('../test/myoutputfile.root')

channelMap = [(0,0),(0,1),(1,0),(1,1)] if options.runPad else [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5)]

hists = list(('weighted_timeDiff_channel{0}{1}'.format(t[0],t[1]),'weightedTime','photek') for t in channelMap)
hists += list(('timeDiff_channel{0}{1}'.format(t[0],t[1]),'time','photek') for t in channelMap)
hists += [("weighted_timeDiff","weightedTime","photek"), ("timeDiff","time","photek"), ("timeDiff_amp2","time","photek"), ("timeDiff_amp3","time","photek"),('deltaX','deltaX',"tracker"),('deltaY','deltaY',"tracker")]
hists += [('deltaX_TopRow','deltaX_TopRow',"tracker"),('deltaX_BotRow','deltaX_BotRow',"tracker"),('deltaY_RightCol','deltaY_RightCol',"tracker"),('deltaY_LeftCol','deltaY_LeftCol',"tracker")] 
hists += [("weighted2_timeDiff","weighted2Time","photek"), ("weighted_timeDiff_goodSig","weighted_goodSig","photek"), ("weighted2_timeDiff_goodSig","weighted2_goodSig","photek")]

for t in hists:
    h = f.Get(t[0])
    plot1D([h], [ROOT.kBlack], [t[1]], t[0], 'Events', t[1]+' - '+t[2], True) if options.runPad else plot1D([h], [ROOT.kBlack], [t[1]], t[0], 'Events', t[1]+' - '+t[2])

        


# Plot 1D of normalized amp
#ROOT.gStyle.SetOptFit(1)
c = ROOT.TCanvas("c","c",1000,1000)
ROOT.gPad.SetLeftMargin(0.12)
ROOT.gPad.SetRightMargin(0.05)
ROOT.gPad.SetTopMargin(0.05)
ROOT.gPad.SetBottomMargin(0.12)
ROOT.gPad.SetTicks(1,1)
ROOT.TH1.SetDefaultSumw2()
ROOT.gStyle.SetOptStat(0)
#ROOT.gPad.SetLogx()
ROOT.gPad.SetLogy()

h1 = getHisto(f, "ampRank1", 5, ROOT.kBlack)
h2 = getHisto(f, "ampRank2", 5, ROOT.kOrange+2)
h3 = getHisto(f, "ampRank3", 5, ROOT.kGreen+2)
h4 = getHisto(f, "ampRank4", 5, ROOT.kRed)
h5 = getHisto(f, "ampRank5", 5, ROOT.kBlue)
h6 = getHisto(f, "ampRank6", 5, ROOT.kGray+1)

#h6.Draw('hists')
h5.Draw('hists')
h4.Draw('hists same')
h3.Draw('hists same')
h2.Draw('hists same')
h1.Draw('hists same')

legend = ROOT.TLegend(0.6,0.65,0.9,0.88);
legend.SetBorderSize(0)
legend.SetTextSize(0.04)
legend.AddEntry(h1, "Strip Rank 1")
legend.AddEntry(h2, "Strip Rank 2")
legend.AddEntry(h3, "Strip Rank 3")
legend.AddEntry(h4, "Strip Rank 4")
legend.AddEntry(h5, "Strip Rank 5")
#legend.AddEntry(h6, "Strip Rank 6")
legend.Draw();

h5.SetTitle("")
h5.GetXaxis().SetTitle("Amplitude [mV]")
h5.GetYaxis().SetTitle("A.U.")
h5.SetMinimum(0.0005)
h5.GetXaxis().SetRangeUser(0.0,200.0)


name = "ampRankPlot"
c.Print("%s.png"%(name))
c.Print("%s.gif"%(name))
c.Print("%s.pdf"%(name))

