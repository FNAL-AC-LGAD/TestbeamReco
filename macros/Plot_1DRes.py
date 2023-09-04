import ROOT
import optparse
import myStyle

ROOT.gROOT.SetBatch(True)

myStyle.ForceStyle()

ROOT.gStyle.SetOptFit(1)
ROOT.gStyle.SetPadRightMargin(2*myStyle.GetMargin())
ROOT.gStyle.SetTextSize(myStyle.GetSize()-5)
ROOT.gStyle.SetLabelSize(myStyle.GetSize()-10,"x")
ROOT.gStyle.SetLabelSize(myStyle.GetSize()-10,"y")
ROOT.gStyle.SetLabelSize(myStyle.GetSize()-10,"z")
ROOT.gStyle.SetHistLineWidth(2)
ROOT.gROOT.ForceStyle()

def plot1D(hists, colors, labels, name, yTitle, xTitle, pads=False, bins=100, arange=(0,1), fmin=-1, fmax=1):
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
    # Range used to reproduce Paper plots [myMean + (fmin)*myRMS, myMean + (fmax)*myRMS] -> [fmin, fmax]

    fitlow = myMean + fmin*myRMS
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

fit_range = {
    ## 2022 sensors
    "EIC_W2_1cm_500up_300uw_240V": {'one': [-2.7,2.7], 'two': [-0.8,0.8]},
    "EIC_W1_1cm_500up_200uw_255V": {'one': [-3.0,3.0], 'two': [-1.1,1.1]},
    "EIC_W2_1cm_500up_100uw_220V": {'one': [-2.7,2.7], 'two': [-1.4,1.4]},
    "EIC_W1_2p5cm_500up_200uw_215V": {'one': [-3.0,3.0], 'two': [-0.8,0.6]},
    "EIC_W1_0p5cm_500up_200uw_1_4_245V": {'one': [-4.0,4.0], 'two': [-1.1,1.1]},

    ## 2023 sensors (needs to be updated)
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2_170V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "BNL_50um_1cm_400um_W3051_1_4_160V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "BNL_50um_1cm_450um_W3052_2_4_185V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "BNL_20um_1cm_400um_W3074_1_4_95V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "BNL_20um_1cm_400um_W3075_1_2_80V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "BNL_20um_1cm_450um_W3074_2_1_95V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "BNL_20um_1cm_450um_W3075_2_4_80V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},

    # HPK pads
    "HPK_20um_500x500um_2x2pad_E600_FNAL_105V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_30um_500x500um_2x2pad_E600_FNAL_140V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_50um_500x500um_2x2pad_E600_FNAL_190V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},

    # HPK May 2023
    "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    # "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    # "HPK_W8_17_2_50T_1P0_500P_50M_C600_206V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_W4_17_2_50T_1P0_500P_50M_C240_204V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_W9_14_2_20T_1P0_500P_100M_E600_112V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_KOJI_50T_1P0_80P_60M_E240_190V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_KOJI_20T_1P0_80P_60M_E240_112V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
}


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('--runPad', dest='runPad', action='store_true', default = False, help="Is pad (True) or strip (False). Needed when -a=True.")
parser.add_option('-a', dest='plotAll', action='store_true', default = False, help="Draw all channels")
parser.add_option('-m', '--min', dest='min', default=-1.0, type="float", help="Low limit of the fit (fmin): myMean + (fmin)*myRMS.")
parser.add_option('-M', '--max', dest='max', default=1.0, type="float", help="High limit of the fit (fmax): myMean + (fmax)*myRMS.")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-t', dest='useTight', action='store_true', default = False, help="Use tight cut for pass")
options, args = parser.parse_args()

dataset = options.Dataset
runPad = options.runPad
fitmin = options.min
fitmax = options.max

useTight = options.useTight
tight_ext = "_tight" if useTight else ""

outdir=""
outdir = myStyle.getOutputDir(dataset)
inputfile = ROOT.TFile("%s%s_Analyze.root"%(outdir,dataset))

outdir = myStyle.GetPlotsDir(outdir, "Paper_1DRes/")

channelMap = [(0,0),(0,1),(1,0),(1,1)] if options.runPad else [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6)]

range_oneS = fit_range[dataset]['one']
range_twoS = fit_range[dataset]['two']

hists = [('deltaX%s'%tight_ext,'deltaX',"tracker",fitmin,fitmax),
        ('deltaX_oneStrip%s'%tight_ext,'deltaX_oneStrip',"tracker",range_oneS[0],range_oneS[1]),
        ('deltaX_oneStrip_onMetal%s'%tight_ext,'deltaX_oneStrip_onMetal',"tracker",range_oneS[0],range_oneS[1]),
        ('deltaX_twoStrips%s'%tight_ext,'deltaX_twoStrips',"tracker",range_twoS[0],range_twoS[1]), # ('deltaX_twoStrips_noMetal','deltaX_twoStrips_noMetal',"tracker"),
        ("timeDiff%s"%tight_ext,"time","photek",fitmin,fitmax), ("weighted2_timeDiff%s"%tight_ext,"weighted2Time","photek",fitmin,fitmax),
        ("timeDiffTracker%s"%tight_ext,"time_tracker","photek",fitmin,fitmax), ("weighted2_timeDiff_tracker%s"%tight_ext,"weighted2_time_tracker","photek",fitmin,fitmax),
        ('deltaY','deltaY','tracker',fitmin,fitmax),
        ('deltaY_oneStrip','deltaY_oneStrip','tracker',fitmin,fitmax),
        ('deltaY_twoStrips','deltaY_twoStrips','tracker',fitmin,fitmax),
]

hists += list(('deltaX_oneStrip{0}{1}'.format(t[0],t[1]),'deltaX_oneStripCh0%i'%(t[1]),'tracker',range_oneS[0],range_oneS[1]) for t in channelMap)

if options.plotAll:
    hists += list(('weighted_timeDiff_channel{0}{1}'.format(t[0],t[1]),'weightedTime','photek') for t in channelMap)
    hists += list(('timeDiff_channel{0}{1}'.format(t[0],t[1]),'time','photek') for t in channelMap)
    hists += [("weighted_timeDiff","weightedTime","photek"), ("timeDiff_amp2","time","photek"), ("timeDiff_amp3","time","photek")]
    hists += [('deltaX_TopRow','deltaX_TopRow',"tracker"), ('deltaX_BotRow','deltaX_BotRow',"tracker"), ('deltaY_RightCol','deltaY_RightCol',"tracker"), ('deltaY_LeftCol','deltaY_LeftCol',"tracker")]
    hists += [("weighted_timeDiff_goodSig","weighted_goodSig","photek"), ("weighted2_timeDiff_goodSig","weighted2_goodSig","photek")]


nEntries = {}
for t in hists:
    h = inputfile.Get(t[0])
    if h:
        plot1D([h], [ROOT.kBlack], [t[1]], outdir+t[0], 'Events', t[1]+' - '+t[2], runPad, 100, (0,1), t[3], t[4])

        if (t[0] in ['deltaX_oneStrip%s'%tight_ext,'deltaX_twoStrips%s'%tight_ext]):
            # print("* Number of entries in",t[0],":",h.GetEntries())
            nEntries[t[0]] = h.GetEntries()

## Get fraction of events per reconstruction method
for reco_method in nEntries:
    print("\t* {0}: {1}/{2} ({3:.2f} %)".format(reco_method, nEntries[reco_method], sum(nEntries.values()), 100*nEntries[reco_method]/sum(nEntries.values())))

print()
