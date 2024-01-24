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


def shrink_limits(hist, limit_min, limit_max, peak_percentage = 0.2):
    # Avoid limits to go beyond X% of the peak (to avoid problems with the Gaussian fit)
    peak_bin = hist.GetMaximumBin()
    peak_value = hist.GetBinContent(peak_bin)

    # Correct left edge if needed
    bin_left = hist.FindBin(limit_min)
    value_left = hist.GetBinContent(bin_left)
    str_limit_left = " >> Initial left limit: %2.4f"%(limit_min)
    while (value_left < peak_percentage*peak_value):
        limit_min = hist.GetBinLowEdge(bin_left+1)
        value_left = hist.GetBinContent(bin_left + 1)
        bin_left+= 1
    str_limit_left+= " >> Final left limit: %2.4f"%(limit_min)
    # print(str_limit_left)

    # Correct right edge if needed
    bin_right = hist.FindBin(limit_max)
    value_right = hist.GetBinContent(bin_right)
    str_limit_right = " >> Initial right limit: %2.4f"%(limit_max)
    while (value_right < peak_percentage*peak_value):
        limit_max = hist.GetBinLowEdge(bin_right)
        value_right = hist.GetBinContent(bin_right)
        bin_right-= 1
        str_limit_right+= " >> Final right limit: %2.4f"%(limit_max)
    # print(str_limit_right)

    return limit_min, limit_max

def plot1D(hist, outpath, fmin, fmax, xTitle="x [X]", yTitle="Events", pads=False, bins=100, arange=(0,1),
           tracker_res=0.0, fit_around_peak=False, shrink_range=False):
    canvas = ROOT.TCanvas("canvas","canvas",1000,1000)
    ROOT.gPad.SetTicks(1,1)
    ROOT.TH1.SetDefaultSumw2()

    hname = hist.GetName()

    hist.Rebin(2)
    hist.GetXaxis().SetTitle(xTitle)
    hist.GetYaxis().SetTitle(yTitle)
    hist.Draw('hists e')
    myMean = hist.GetMean()
    myRMS = hist.GetRMS()
    myRMS_Error = hist.GetRMSError()

    # Define fit limits
    fit_min = myMean + fmin*myRMS
    fit_max = myMean + fmax*myRMS
    # ... around peak
    if fit_around_peak:
        peak_bin = hist.GetMaximumBin()
        peak_x = hist.GetBinCenter(peak_bin)
        fit_min = peak_x + fmin*myRMS
        fit_max = peak_x + fmax*myRMS
    if shrink_range:
        fit_min, fit_max = shrink_limits(hist, fit_min, fit_max)

    fit = ROOT.TF1("fit", "gaus", fit_min, fit_max)
    fit.SetLineColor(ROOT.kRed)
    hist.Fit(fit, "Q", "", fit_min, fit_max)
    fit.Draw("same")

    show_output = True
    for sufix in ["_Metal", "_Gap", "_MidGap"]:
        if sufix in hname:
            show_output = False
            break
    # Print output with resolution value
    if show_output:
        use_fit = "oneStrip" not in hname

        print("----------------------------------------")
        msg_title = " Resolution: %s"%(hname)
        center = "mean" if not fit_around_peak else "peak"
        if use_fit:
            msg_title+= " > Range: [%s - %.2f*RMS, %s + %.2f*RMS]"%(center, abs(fmin), center, abs(fmax))
        print(msg_title)
        value_type = "from fit" if use_fit else "RMS"
        sigma = 1000.*fit.GetParameter(2) if use_fit else 1000.*myRMS
        sigma_error = 1000.*fit.GetParError(2) if use_fit else 1000.*myRMS_Error

        msg_resolution = " >> Value %s: %.2f +- %.2f"%(value_type, sigma, sigma_error)
        if (tracker_res > 0.0):
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


# Limits of the fits used in the deltaX one and two strip reconstruction methods
# The limits are defined such that [fmin, fmax] gives the limits --> [max_bin_center + (fmin)*myRMS, max_bin_center + (fmax)*myRMS]
fit_limits = {
    ## 2022 sensors
    "EIC_W2_1cm_500up_300uw_240V": {'one': [-2.7,2.7], 'two': [-0.8,0.8]},
    "EIC_W1_1cm_500up_200uw_255V": {'one': [-3.0,3.0], 'two': [-1.1,1.1]},
    "EIC_W2_1cm_500up_100uw_220V": {'one': [-2.7,2.7], 'two': [-1.4,1.4]},
    "EIC_W1_2p5cm_500up_200uw_215V": {'one': [-3.0,3.0], 'two': [-0.8,0.6]},
    "EIC_W1_0p5cm_500up_200uw_1_4_245V": {'one': [-4.0,4.0], 'two': [-1.1,1.1]},
}


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-a', dest='all_quantities', action='store_true', default = False, help="Draw all histograms (not only the most important ones)")
parser.add_option('-c', dest='each_channel', action='store_true', default = False, help="Draw one strip reco for each channel")
parser.add_option('-m', '--min', dest='min', default=0.0, type="float", help="Low limit of the fit (fmin): max_bin_center + (fmin)*myRMS.")
parser.add_option('-M', '--max', dest='max', default=0.0, type="float", help="High limit of the fit (fmax): max_bin_center + (fmax)*myRMS.")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-t', dest='useTight', action='store_true', default = False, help="Use tight cut for pass")
options, args = parser.parse_args()

dataset = options.Dataset
fitmin = options.min
fitmax = options.max

plot_all_hists = options.all_quantities
use_each_channel = options.each_channel

is_tight = options.useTight

outdir = myStyle.getOutputDir(dataset)
inputfile = ROOT.TFile("%s%s_Analyze.root"%(outdir,dataset))

outdir = myStyle.GetPlotsDir(outdir, "Resolution1D/")

# Set default or input limits for the fits
rms_min = -1.5 if fitmin == 0.0 else fitmin
rms_max = 1.5 if fitmax == 0.0 else fitmax
# Use predefined fit limits for 2022 sensors only
if dataset in fit_limits:
    print(" >> Using limits defined in dictionary.")
    limits_one = fit_limits[dataset]['one']
    limits_two = fit_limits[dataset]['two']
else:
    limits_one = [rms_min, rms_max]
    limits_two = [rms_min, rms_max]

# Modify time reference (Photek) contribution to be removed in quadrature
# res_tracker = 5 # um # Position tracker contribution is NOT removed
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
        indices_one = mf.get_existing_indices(inputfile, "deltaX_oneStrip", False)

        for index in indices_one:
            channel_element = ["deltaX_oneStrip%s"%index, "deltaX_oneStripCh%s"%index, "tracker"]
            list_htitles.append(channel_element)

if plot_all_hists:
    # Skip if tight cuts are required
    if (is_tight):
        print(" >> Tight cut is not compatible with 'all histograms'. Skipping.")
    else:
        indices_time = mf.get_existing_indices(inputfile, "timeDiffTracker_channel", False)

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

    peak_reference = False
    # Use default fit limits
    fmin, fmax = rms_min, rms_max
    # Change default range to a given one for one or two strip reco if added in input
    if "deltaX_oneStrip" in hname:
        fmin, fmax = limits_one
    elif "deltaX_twoStrip" in hname:
        fmin, fmax = limits_two
        peak_reference = True

    # Value to remove in quadrature (only for time plots)
    tracker_component = res_photek if "photek" in ref else 0.0

    hist = inputfile.Get(hname)
    hfinal = plot1D(hist, out_path, fmin, fmax, xTitle=x_title, tracker_res=tracker_component, fit_around_peak=peak_reference, shrink_range=False)

    hfinal.Write()

outputfile.Close()
