import ROOT
import optparse
import myStyle
import math
import myFunctions as mf

ROOT.gROOT.SetBatch(True)

myStyle.ForceStyle()

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()

dataset = options.Dataset
outdir = myStyle.getOutputDir(dataset)

sensor_Geometry = myStyle.GetGeometry(dataset)
sensor_name = sensor_Geometry["sensor"]

regions = ["Overall", "Metal", "Gap", "MidGap"]

print(" >> Sensor info summary to be saved in mySensorInfo.py")

# Resolution values
# -----------------
outdir_res1d = "%s/Resolution1D/"%(outdir)
inputfile_res1d = ROOT.TFile("%sResolutionValues.root"%(outdir_res1d), "READ")
inputfile_res1d_tight = ROOT.TFile("%sResolutionValues_tight.root"%(outdir_res1d), "READ")

# Efficiency values
# -----------------
outdir_efficiency = "%s/Cutflow/"%(outdir)
inputfile_eff = ROOT.TFile("%sPlot_cutflow.root"%(outdir_efficiency), "READ")

# Order: <one strip reco RMS [um]>, <two strip reco fit [um]>, <time [ps]>,
# <efficiency one strip>, <efficiency two strip>

for reg in regions:
    # One strip resolution per channel (only once)
    if reg == "Overall":
        info_channels = []
        indices = mf.get_existing_indices(inputfile_res1d, "deltaX_oneStrip")
        for idx in indices:
            hres_onestrip = inputfile_res1d.Get("deltaX_oneStrip%s"%idx)
            value = 1000 * hres_onestrip.GetStdDev()
            info_channels.append(value)

        # Output line for mySensorInfo.py
        print("\tOne strip info per channel:")
        info_str = "\t\"%s\": ["%(myStyle.RemoveBV(dataset))
        for val in info_channels:
            info_str+= "%.1f, "%(val)
        info_str = info_str[:-2] + "],"
        print(info_str)

    info = {}
    print("    # %s region"%(reg))

    res_region = "_%s"%reg
    if reg == "MidGap":
        res_region = "_Gap"
    elif reg == "Overall":
        res_region = ""
    
    # Resolution
    name_onestrip = "deltaX_oneStrip%s"%(res_region)
    name_twostrip = "deltaX_twoStrips%s_tight"%(res_region)
    name_time = "weighted2_timeDiff_tracker_%s"%reg if reg != "Overall" else "weighted2_timeDiff_tracker_tight"
    inputfile_time = inputfile_res1d if reg != "Overall" else inputfile_res1d_tight

    info["one_res"] = 1000 * inputfile_res1d.Get(name_onestrip).GetStdDev()
    info["two_res"] = 1000 * inputfile_res1d_tight.Get(name_twostrip).GetFunction("fit").GetParameter(2)
    info["time_res"] = 1000 * inputfile_time.Get(name_time).GetFunction("fit").GetParameter(2)

    # Efficiency
    name_eff = "cut_flow_%s"%(reg)
    hist_eff = inputfile_eff.Get(name_eff)
    bin_pass = hist_eff.GetXaxis().FindBin(reg)
    bin_one = hist_eff.GetXaxis().FindBin("OneStripReco")
    bin_two = hist_eff.GetXaxis().FindBin("TwoStripsReco")

    value_pass = hist_eff.GetBinContent(bin_pass)
    value_one = hist_eff.GetBinContent(bin_one)
    value_two = hist_eff.GetBinContent(bin_two)

    info["one_eff"] = 100 * value_one / value_pass
    info["two_eff"] = 100 * value_two / value_pass
    
    # Output line for mySensorInfo.py
    info_str = "\t\"%s\": ["%(myStyle.RemoveBV(dataset))
    for key in ["one_res", "two_res", "time_res", "one_eff", "two_eff"]:
        info_str+= "%.1f, "%(info[key])
    info_str = info_str[:-2] + "],"
    print(info_str)

    # Ouput for Latex table
    info_tex = "\t%s & %.0f $\\pm$ 1 &"%(reg, info["time_res"])
    for key in ["one_res", "one_eff", "two_res", "two_eff"]:
        info_tex+= " %.1f &"%(info[key])
    print(info_tex)


inputfile_res1d.Close()
inputfile_res1d_tight.Close()
inputfile_eff.Close()
