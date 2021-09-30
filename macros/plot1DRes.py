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
        fitlow = myMean - 0.65*myRMS
        fithigh = myMean + 0.6*myRMS

    
            
        fit = ROOT.TF1("fit", "gaus", fitlow, fithigh)    
        fit.SetLineColor(ROOT.kRed)
        #fit.Draw("same")
        h.Fit(fit,"Q", "", fitlow, fithigh)
        fit.Draw("same")    

        c.Print("%s.png"%(name))
        c.Print("%s.gif"%(name))


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

        

