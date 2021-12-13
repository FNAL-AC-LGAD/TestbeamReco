import ROOT
import optparse
ROOT.gROOT.SetBatch(True)

## Defining Style
ROOT.gStyle.SetPadTopMargin(0.05)    #0.05
ROOT.gStyle.SetPadRightMargin(0.05)  #0.05
ROOT.gStyle.SetPadBottomMargin(0.1)  #0.16
ROOT.gStyle.SetPadLeftMargin(0.1)   #0.16

ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)

font=43 # Helvetica
tsize=28
ROOT.gStyle.SetTextFont(font)
ROOT.gStyle.SetLabelFont(font,"x")
ROOT.gStyle.SetTitleFont(font,"x")
ROOT.gStyle.SetLabelFont(font,"y")
ROOT.gStyle.SetTitleFont(font,"y")
ROOT.gStyle.SetLabelFont(font,"z")
ROOT.gStyle.SetTitleFont(font,"z")

ROOT.gStyle.SetTextSize(tsize)
ROOT.gStyle.SetLabelSize(tsize,"x")
ROOT.gStyle.SetTitleSize(tsize,"x")
ROOT.gStyle.SetLabelSize(tsize,"y")
ROOT.gStyle.SetTitleSize(tsize,"y")
ROOT.gStyle.SetLabelSize(tsize,"z")
ROOT.gStyle.SetTitleSize(tsize,"z")

ROOT.gStyle.SetTitleXOffset(1.0)
ROOT.gStyle.SetTitleYOffset(1.4)
ROOT.gStyle.SetOptTitle(0)
# ROOT.gStyle.SetOptStat(0)

ROOT.gStyle.SetGridColor(921)
ROOT.gStyle.SetGridStyle()

ROOT.gROOT.ForceStyle()

color_RGB = [[51,34,136],[51,187,238],[17,119,51],[153,153,51],[204,102,119],[136,34,85]]
# [indigo, cyan, green, olive, rose, wine]
color_list = []

for i in range(0,len(color_RGB)):
    c = ROOT.TColor.GetColor(color_RGB[i][0],color_RGB[i][1],color_RGB[i][2])
    color_list.append(c)

def plot1D(hists, colors, labels, name, xlab, ylab, pads=False, bins=100, arange=(0,1)):
        ROOT.gStyle.SetOptFit(1)
        c = ROOT.TCanvas("c","c",800,800)
        # ROOT.gPad.SetLeftMargin(0.12)
        # ROOT.gPad.SetRightMargin(0.15)
        # ROOT.gPad.SetTopMargin(0.08)
        # ROOT.gPad.SetBottomMargin(0.12)
        # ROOT.gPad.SetTicks(1,1)
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
parser.add_option('--runPad', dest='runPad', action='store_true', default = False, help="run fits or not")
parser.add_option('-f', dest='file', default = "myoutputfile.root", help="File name (or path from ../test/)")
options, args = parser.parse_args()

file = options.file

f = ROOT.TFile('../test/'+file,"READ")

channelMap = [(0,0),(0,1),(1,0),(1,1)] if options.runPad else [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5)]

# hists = list(('weighted_timeDiff_channel{0}{1}'.format(t[0],t[1]),'weightedTime','photek') for t in channelMap)
# hists += list(('timeDiff_channel{0}{1}'.format(t[0],t[1]),'time','photek') for t in channelMap)
# hists = [("weighted_timeDiff","weightedTime","photek"), ("timeDiff","time","photek"), ("timeDiff_amp2","time","photek"), ("timeDiff_amp3","time","photek"),('deltaX','deltaX',"tracker"),('deltaY','deltaY',"tracker")]
hists = [("timeDiff","time","photek"),('deltaX','deltaX',"tracker"),('deltaY','deltaY',"tracker")]
# hists += [('deltaX_TopRow','deltaX_TopRow',"tracker"),('deltaX_BotRow','deltaX_BotRow',"tracker"),('deltaY_RightCol','deltaY_RightCol',"tracker"),('deltaY_LeftCol','deltaY_LeftCol',"tracker")] 
# hists += [("weighted2_timeDiff","weighted2Time","photek"), ("weighted_timeDiff_goodSig","weighted_goodSig","photek"), ("weighted2_timeDiff_goodSig","weighted2_goodSig","photek")]
hists += [("weighted2_timeDiff","weighted2Time","photek")]

for t in hists:
    h = f.Get(t[0])
    plot1D([h], [ROOT.kBlack], [t[1]], t[0], 'Events', t[1]+' - '+t[2], True) if options.runPad else plot1D([h], [ROOT.kBlack], [t[1]], t[0], 'Events', t[1]+' - '+t[2])

        


# Plot 1D of normalized amp
#ROOT.gStyle.SetOptFit(1)
c = ROOT.TCanvas("c","c",800,800)
# ROOT.gPad.SetLeftMargin(0.12)
# ROOT.gPad.SetRightMargin(0.05)
# ROOT.gPad.SetTopMargin(0.05)
# ROOT.gPad.SetBottomMargin(0.12)
# ROOT.gPad.SetTicks(1,1)
ROOT.TH1.SetDefaultSumw2()
ROOT.gStyle.SetOptStat(0)
#ROOT.gPad.SetLogx()
ROOT.gPad.SetLogy()

h1 = getHisto(f, "ampRank1", 5, color_list[0])
h2 = getHisto(f, "ampRank2", 5, color_list[1])
h3 = getHisto(f, "ampRank3", 5, color_list[2])
h4 = getHisto(f, "ampRank4", 5, color_list[3])
h5 = getHisto(f, "ampRank5", 5, color_list[4])
h6 = getHisto(f, "ampRank6", 5, color_list[5])

#h6.Draw('hists')
h5.Draw('hists')
h4.Draw('hists same')
h3.Draw('hists same')
h2.Draw('hists same')
h1.Draw('hists same')

legend = ROOT.TLegend(0.63,0.68,0.93,0.90);
legend.SetBorderSize(0)
legend.SetFillStyle(0)
# legend.SetTextSize(0.04)
legend.AddEntry(h1, "Strip Rank 1")
legend.AddEntry(h2, "Strip Rank 2")
legend.AddEntry(h3, "Strip Rank 3")
legend.AddEntry(h4, "Strip Rank 4")
legend.AddEntry(h5, "Strip Rank 5")
#legend.AddEntry(h6, "Strip Rank 6")
legend.Draw();

h5.SetTitle("")
h5.GetXaxis().SetTitle("Amplitude [mV]")
h5.GetYaxis().SetTitle("Event/Total events")
h5.GetXaxis().SetRangeUser(0.0,200.0)
h5.GetYaxis().SetRangeUser(0.0005,1.0)


name = "ampRankPlot"
# c.Print("%s.png"%(name))
c.Print("%s.gif"%(name))
c.Print("%s.pdf"%(name))

