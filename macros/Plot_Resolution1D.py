import ROOT
import optparse
import myStyle
import math
import myFunctions as mf

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


def correct_limits(hist, peak_bin, vmin, vmax):
    # Avoid limits to go beyond 20% of the peak (to avoid problems with the Gaussian fit)
    peak_value = hist.GetBinContent(peak_bin)

    # Correct left edge if needed
    bin_left = hist.FindBin(vmin)
    value_left = hist.GetBinContent(bin_left)
    str_limit_left = " >> Left limit: %2.4f"%(vmin)
    while (value_left < 0.2*peak_value):
        vmin = hist.GetBinLowEdge(bin_left+1)
        value_left = hist.GetBinContent(bin_left + 1)
        bin_left+= 1
        str_limit_left+= " -> %2.4f"%(vmin)
    # print(str_limit_left)

    # Correct right edge if needed
    bin_right = hist.FindBin(vmax)
    value_right = hist.GetBinContent(bin_right)
    str_limit_right = " >> Right limit: %2.4f"%(vmax)
    while (value_right < 0.2*peak_value):
        vmax = hist.GetBinLowEdge(bin_right)
        value_right = hist.GetBinContent(bin_right)
        bin_right-= 1
        str_limit_right+= " -> %2.4f"%(vmax)
    # print(str_limit_right)

    return vmin, vmax

def plot1D(hist, outpath, xTitle, yTitle="Events", pads=False, bins=100, arange=(0,1), fmin=-1, fmax=1, tracker_res=0.0):
    # ROOT.gStyle.SetOptFit(1)
    canvas = ROOT.TCanvas("canvas","canvas",1000,1000)
    ROOT.gPad.SetTicks(1,1)
    ROOT.TH1.SetDefaultSumw2()
    #ROOT.gPad.SetLogy()
    # ROOT.gROOT.ForceStyle()

    hname = hist.GetName()
    print("----------------------------------------")
    print(" Resolution: %s"%(hname))

    hist.Rebin(2)
    hist.GetXaxis().SetTitle(xTitle)
    hist.GetYaxis().SetTitle(yTitle)
    hist.Draw('hists e')
    myMean = hist.GetMean()
    myRMS = hist.GetRMS()
    myRMS_Error = hist.GetRMSError()
    # # Define fit limits
    # fit_min = myMean + fmin*myRMS
    # fit_max = myMean + fmax*myRMS

    # Make fit around peak of the distribution!
    peak_bin = hist.GetMaximumBin()
    peak = hist.GetBinCenter(peak_bin)
    # Define fit limits
    fit_min = peak + fmin*myRMS
    fit_max = peak + fmax*myRMS
    fit_min, fit_max = correct_limits(hist, peak_bin, fit_min, fit_max)

    fit = ROOT.TF1("fit", "gaus", fit_min, fit_max)
    fit.SetLineColor(ROOT.kRed)
    hist.Fit(fit, "Q", "", fit_min, fit_max)
    fit.Draw("same")

    # Print resolution value
    use_RMS = "oneStrip" in hname
    value_type = "from fit" if not use_RMS else "RMS"
    sigma = 1000.*fit.GetParameter(2) if not use_RMS else 1000.*myRMS
    sigma_error = 1000.*fit.GetParError(2) if not use_RMS else 1000.*myRMS_Error

    msg_resolution = " >> Value %s: %.2f +- %.2f"%(value_type, sigma, sigma_error)
    if (tracker_res < sigma):
        sigma = math.sqrt(sigma**2 - tracker_res**2)
        msg_resolution+= " (Removing %.1f from tracker: %.2f)"%(tracker_res, sigma)
    else:
        msg_resolution+= " (!) Value smaller than reference (!)"

    print(msg_resolution)

    # Save plots
    # canvas.SaveAs("%s.png"%(outpath))
    # canvas.SaveAs("%s.gif"%(outpath))
    canvas.SaveAs("%s.pdf"%(outpath))

    return hist


def getHisto(f, name, rebin, color):
    h = f.Get(name)
    h.Rebin(rebin)
    h.Scale(1.0/h.Integral())
    h.SetLineColor(color)
    h.SetLineWidth(2)
    return h

# Limits of the fits used in the deltaX one and two strip reconstruction methods
# The limits are defined such that [fmin, fmax] gives the limits --> [max_bin_center + (fmin)*myRMS, max_bin_center + (fmax)*myRMS]
fit_limits = {
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
    "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_W4_17_2_50T_1P0_500P_50M_C240_204V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_W9_14_2_20T_1P0_500P_100M_E600_112V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_KOJI_50T_1P0_80P_60M_E240_190V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_KOJI_20T_1P0_80P_60M_E240_112V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
    "HPK_W9_15_4_20T_0P5_500P_50M_E600_110V": {'one': [-2.0,2.0], 'two': [-1.1,1.1]},
}


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-a', dest='all_quantities', action='store_true', default = False, help="Draw all histograms (not only the most important ones)")
parser.add_option('-c', dest='each_channel', action='store_true', default = False, help="Draw one strip reco for each channel")
parser.add_option('-m', '--min', dest='min', default=-1.0, type="float", help="Low limit of the fit (fmin): max_bin_center + (fmin)*myRMS.")
parser.add_option('-M', '--max', dest='max', default=1.0, type="float", help="High limit of the fit (fmax): max_bin_center + (fmax)*myRMS.")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-t', dest='useTight', action='store_true', default = False, help="Use tight cut for pass")
options, args = parser.parse_args()

dataset = options.Dataset
fitmin = options.min
fitmax = options.max

plot_all_hists = options.all_quantities
use_each_channel = options.each_channel

is_tight = options.useTight

outdir=""
outdir = myStyle.getOutputDir(dataset)
inputfile = ROOT.TFile("%s%s_Analyze.root"%(outdir,dataset))

outdir = myStyle.GetPlotsDir(outdir, "Resolution1D/")

if dataset in fit_limits:
    limits_one = fit_limits[dataset]['one']
    limits_two = fit_limits[dataset]['two']
else:
    print(" >> Using default fit limits.")
    limits_one = [-2.0, 2.0]
    limits_two = [-1.1, 1.1]

# Modify tracker and time reference (Photek) contribution to be removed in quadrature
res_tracker = 5 # um
res_photek = 10 # ps

# Save list with histograms to draw
list_htitles = [
    # [hist_input_name, x_axis_title/output_name, reference]
    ["deltaX_oneStrip", "deltaX_oneStrip", "tracker"],
    ["deltaX_twoStrip", "deltaX_twoStrip", "tracker"],
    ["deltaX_oneStrip_Metal", "deltaX_oneStrip_Metal", "tracker"],
    ["deltaX_twoStrip_Metal", "deltaX_twoStrip_Metal", "tracker"],
    ["deltaX_oneStrip_Gap", "deltaX_oneStrip_Gap", "tracker"],
    ["deltaX_twoStrip_Gap", "deltaX_twoStrip_Gap", "tracker"],
    ["timeDiff", "time", "photek"],
    ["timeDiffTracker", "time_tracker", "photek"],
    ["weighted2_timeDiff", "weighted2Time", "photek"],
    ["weighted2_timeDiff_tracker", "weighted2_time_tracker", "photek"],
    # ["deltaY", "deltaY", "tracker"],
    # ["deltaY_oneStrip", "deltaY_oneStrip", "tracker"],
    # ["deltaY_twoStrip", "deltaY_twoStrip", "tracker"],
]

# Use tight cut histograms
if (is_tight):
    print(" >> Using tight cuts!")
    for titles in list_htitles:
        hname = titles[0]
        # Adding extension only to possible histograms (i.e. not deltaY)
        if "deltaY" not in hname:
            titles[0]+= "_tight"
            titles[1]+= "-tight"
else:
    list_htitles+= [
        ["weighted2_timeDiff_tracker_Overall", "weighted2_time_tracker_Overall", "photek"],
        ["weighted2_timeDiff_tracker_Metal", "weighted2_time_tracker_Metal", "photek"],
        ["weighted2_timeDiff_tracker_Gap", "weighted2_time_tracker_Gap", "photek"],
        ["weighted2_timeDiff_tracker_MidGap", "weighted2_time_tracker_MidGap", "photek"],
    ]


# Run over every single channel
if use_each_channel:
    # Skip if tight cuts are required
    if (is_tight):
        print(" >> Tight cut is not compatible with 'each channel'. Skipping.")
    else:
        indices_one = mf.get_existing_indices(inputfile, "deltaX_oneStrip")

        for index in indices_one:
            channel_element = ["deltaX_oneStrip%s"%index, "deltaX_oneStripCh%s"%index, "tracker"]
            list_htitles.append(channel_element)

if plot_all_hists:
    # Skip if tight cuts are required
    if (is_tight):
        print(" >> Tight cut is not compatible with 'all histograms'. Skipping.")
    else:
        indices_time = mf.get_existing_indices(inputfile, "timeDiffTracker_channel")

        for index in indices_time:
            channel_element = ["timeDiffTracker_channel%s"%index, "time_trackerCh%s"%index, "photek"]
            list_htitles.append(channel_element)

            channel_element = ["weighted2_timeDiff_tracker_channel%s"%index, "weighted2_time_trackerCh%s"%index, "photek"]
            list_htitles.append(channel_element)

# Define output file
output_path = "%sResolutionValues"%(outdir)
if (is_tight):
    output_path+= "_tight"
output_path+= ".root"

outputfile = ROOT.TFile(output_path,"RECREATE")

# Create plots
for info in list_htitles:
    hname, out_name, ref = info
    out_path = "%s%s"%(outdir, out_name)
    x_title = "%s - %s "%(out_name.replace("-tight", ""), ref)
    # Units
    x_title+= "[ns]" if "time" in hname else "[mm]"

    # Choose correct fit limits
    fmin, fmax = fitmin, fitmax
    if "deltaX_" in hname:
        if "oneStrip" in hname:
            fmin, fmax = limits_one[0], limits_one[1]
        elif "twoStrip" in hname:
            fmin, fmax = limits_two[0], limits_two[1]

    # Value to remove in quadrature
    tracker_component = res_photek if "photek" in ref else res_tracker

    hist = inputfile.Get(hname)
    hfinal = plot1D(hist, out_path, x_title, fmin=fmin, fmax=fmax, tracker_res=tracker_component)

    hfinal.Write()

outputfile.Close()
