import ROOT
import optparse
ROOT.gROOT.SetBatch(True)

def plot1D(hists, colors, labels, name, xlab, ylab, pads=False, bins=100, arange=(0,1), fmin=1, fmax=1):
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
        h.Rebin(2)
        h.GetXaxis().SetTitle(ylab)
        h.GetYaxis().SetTitle(xlab)
        h.Draw('hists e')
        myMean = h.GetMean()
        myRMS = h.GetRMS()
        # Range used to reproduce Paper plots [myMean - (fmin)*myRMS, myMean + (fmax)*myRMS] -> [-fmin, fmax]:
        # BNL2020               : [-1.0, 1.0]
        # fitlow = myMean - 1.*myRMS
        # fithigh = myMean + 1.*myRMS

        # BNL2021               : [-1.4, 1.4]
        # fitlow = myMean - 1.4*myRMS
        # fithigh = myMean + 1.4*myRMS

        # HPK C2 (except 230V)  : [-0.7, 0.7]
        # *HPK C2 (230V)        : [-0.4, 0.9] position; [-1.0, 1.0] time

        # HPK B2 (210V, 220V)   : [-2.0, 2.0]
        # HPK B2 (230V)         : [-1.4, 1.4]
        # HPK B2 (250V)         : [-0.9, 0.9]
        # HPK B2 (310V)         : [-0.8, 0.7] position; [-1.0, 0.9] time
        # HPK B2 (360V)         : [-0.7, 0.7] position; [-1.0, 0.4] time

        fitlow = myMean - fmin*myRMS
        fithigh = myMean + fmax*myRMS

    
            
        fit = ROOT.TF1("fit", "gaus", fitlow, fithigh)    
        fit.SetLineColor(ROOT.kRed)
        #fit.Draw("same")
        h.Fit(fit,"Q", "", fitlow, fithigh)
        fit.Draw("same")    

        # c.Print("%s.png"%(name))
        c.Print("%s.gif"%(name))
        # c.Print("%s.pdf"%(name))

def getHisto(f, name, rebin, color):
        h = f.Get(name)
        h.Rebin(rebin)
        h.Scale(1.0/h.Integral())
        h.SetLineColor(color)
        h.SetLineWidth(2)
        return h

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('--runPad', dest='runPad', action='store_true', default = False, help="Is pad (True) or strip (False). Needed when -a=True.")
parser.add_option('-a', dest='plotAll', action='store_true', default = False, help="Draw all channels")
parser.add_option('-f', dest='file', default = "myoutputfile.root", help="File name (or path from ../test/)")
parser.add_option('-m', '--min', dest='min', default=0.5, type="float", help="Low limit of the fit (fmin): myMean - (fmin)*myRMS.")
parser.add_option('-M', '--max', dest='max', default=0.5, type="float", help="High limit of the fit (fmax): myMean + (fmax)*myRMS.")
options, args = parser.parse_args()

f = ROOT.TFile('../test/'+options.file)

channelMap = [(0,0),(0,1),(1,0),(1,1)] if options.runPad else [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5)]

hists = [('deltaX','deltaX',"tracker"), ("timeDiff","time","photek"), ("weighted2_timeDiff","weighted2Time","photek")]
if options.plotAll:
        hists += list(('weighted_timeDiff_channel{0}{1}'.format(t[0],t[1]),'weightedTime','photek') for t in channelMap)
        hists += list(('timeDiff_channel{0}{1}'.format(t[0],t[1]),'time','photek') for t in channelMap)
        hists += [("weighted_timeDiff","weightedTime","photek"), ("timeDiff_amp2","time","photek"), ("timeDiff_amp3","time","photek"), ('deltaY','deltaY',"tracker")]
        hists += [('deltaX_TopRow','deltaX_TopRow',"tracker"), ('deltaX_BotRow','deltaX_BotRow',"tracker"), ('deltaY_RightCol','deltaY_RightCol',"tracker"), ('deltaY_LeftCol','deltaY_LeftCol',"tracker")] 
        hists += [("weighted_timeDiff_goodSig","weighted_goodSig","photek"), ("weighted2_timeDiff_goodSig","weighted2_goodSig","photek")]

for t in hists:
    h = f.Get(t[0])
    if options.runPad:
        plot1D([h], [ROOT.kBlack], [t[1]], t[0], 'Events', t[1]+' - '+t[2], True, 100, (0,1), options.min, options.max)
    else:
        plot1D([h], [ROOT.kBlack], [t[1]], t[0], 'Events', t[1]+' - '+t[2], False, 100, (0,1), options.min, options.max)

        


# # Plot 1D of normalized amp
# #ROOT.gStyle.SetOptFit(1)
# c = ROOT.TCanvas("c","c",1000,1000)
# ROOT.gPad.SetLeftMargin(0.12)
# ROOT.gPad.SetRightMargin(0.05)
# ROOT.gPad.SetTopMargin(0.05)
# ROOT.gPad.SetBottomMargin(0.12)
# ROOT.gPad.SetTicks(1,1)
# ROOT.TH1.SetDefaultSumw2()
# ROOT.gStyle.SetOptStat(0)
# #ROOT.gPad.SetLogx()
# ROOT.gPad.SetLogy()

# h1 = getHisto(f, "ampRank1", 5, ROOT.kBlack)
# h2 = getHisto(f, "ampRank2", 5, ROOT.kOrange+2)
# h3 = getHisto(f, "ampRank3", 5, ROOT.kGreen+2)
# h4 = getHisto(f, "ampRank4", 5, ROOT.kRed)
# h5 = getHisto(f, "ampRank5", 5, ROOT.kBlue)
# h6 = getHisto(f, "ampRank6", 5, ROOT.kGray+1)

# #h6.Draw('hists')
# h5.Draw('hists')
# h4.Draw('hists same')
# h3.Draw('hists same')
# h2.Draw('hists same')
# h1.Draw('hists same')

# legend = ROOT.TLegend(0.6,0.65,0.9,0.88);
# legend.SetBorderSize(0)
# legend.SetTextSize(0.04)
# legend.AddEntry(h1, "Strip Rank 1")
# legend.AddEntry(h2, "Strip Rank 2")
# legend.AddEntry(h3, "Strip Rank 3")
# legend.AddEntry(h4, "Strip Rank 4")
# legend.AddEntry(h5, "Strip Rank 5")
# #legend.AddEntry(h6, "Strip Rank 6")
# legend.Draw();

# h5.SetTitle("")
# h5.GetXaxis().SetTitle("Amplitude [mV]")
# h5.GetYaxis().SetTitle("A.U.")
# h5.SetMinimum(0.0005)
# h5.GetXaxis().SetRangeUser(0.0,200.0)


# name = "ampRankPlot"
# c.Print("%s.png"%(name))
# c.Print("%s.gif"%(name))
# c.Print("%s.pdf"%(name))

