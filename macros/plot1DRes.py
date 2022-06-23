import ROOT
import optparse
import myStyle

ROOT.gROOT.SetBatch(True)

myStyle.ForceStyle()
organized_mode=True

ROOT.gStyle.SetOptFit(1)
ROOT.gStyle.SetPadRightMargin(2*myStyle.GetMargin())
ROOT.gStyle.SetTextSize(myStyle.GetSize()-5)
ROOT.gStyle.SetLabelSize(myStyle.GetSize()-10,"x")
ROOT.gStyle.SetLabelSize(myStyle.GetSize()-10,"y")
ROOT.gStyle.SetLabelSize(myStyle.GetSize()-10,"z")
ROOT.gStyle.SetHistLineWidth(2)
ROOT.gROOT.ForceStyle()

def plot1D(hists, colors, labels, name, yTitle, xTitle, pads=False, bins=100, arange=(0,1), fmin=1, fmax=1):
        # ROOT.gStyle.SetOptFit(1)
        c = ROOT.TCanvas("c","c",1000,1000)
        ROOT.gPad.SetTicks(1,1)
        ROOT.TH1.SetDefaultSumw2()
        #ROOT.gPad.SetLogy()
        # ROOT.gROOT.ForceStyle()

        h = hists[0]
        h.Rebin(2)
        h.GetXaxis().SetTitle(xTitle)
        h.GetYaxis().SetTitle(yTitle)
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
parser.add_option('-m', '--min', dest='min', default=1.0, type="float", help="Low limit of the fit (fmin): myMean - (fmin)*myRMS.")
parser.add_option('-M', '--max', dest='max', default=1.0, type="float", help="High limit of the fit (fmax): myMean + (fmax)*myRMS.")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()

dataset = options.Dataset
runPad = options.runPad
fitmin = options.min
fitmax = options.max

outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = ROOT.TFile("%s%s_Analyze.root"%(outdir,dataset))
else: 
    inputfile = ROOT.TFile("../test/myoutputfile.root")

outdir = myStyle.GetPlotsDir(outdir, "1DRes/")

channelMap = [(0,0),(0,1),(1,0),(1,1)] if options.runPad else [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5)]

hists = [('deltaX','deltaX',"tracker"), ('deltaX_oneStrip','deltaX_oneStrip',"tracker"), ('deltaX_twoStrips','deltaX_twoStrips',"tracker"),
        ('deltaX_oneStrip_onMetal','deltaX_oneStrip_onMetal',"tracker"), ('deltaX_twoStrips_noMetal','deltaX_twoStrips_noMetal',"tracker"),
        ("timeDiff","time","photek"), ("weighted2_timeDiff","weighted2Time","photek"),
        ("timeDiffTracker","time_tracker","photek"), ("weighted2_timeDiff_tracker","weighted2_time_tracker","photek")]
if options.plotAll:
        hists += list(('weighted_timeDiff_channel{0}{1}'.format(t[0],t[1]),'weightedTime','photek') for t in channelMap)
        hists += list(('timeDiff_channel{0}{1}'.format(t[0],t[1]),'time','photek') for t in channelMap)
        hists += [("weighted_timeDiff","weightedTime","photek"), ("timeDiff_amp2","time","photek"), ("timeDiff_amp3","time","photek"), ('deltaY','deltaY',"tracker")]
        hists += [('deltaX_TopRow','deltaX_TopRow',"tracker"), ('deltaX_BotRow','deltaX_BotRow',"tracker"), ('deltaY_RightCol','deltaY_RightCol',"tracker"), ('deltaY_LeftCol','deltaY_LeftCol',"tracker")] 
        hists += [("weighted_timeDiff_goodSig","weighted_goodSig","photek"), ("weighted2_timeDiff_goodSig","weighted2_goodSig","photek")]

for t in hists:
    h = inputfile.Get(t[0])
    plot1D([h], [ROOT.kBlack], [t[1]], outdir+t[0], 'Events', t[1]+' - '+t[2], runPad, 100, (0,1), fitmin, fitmax)

        

