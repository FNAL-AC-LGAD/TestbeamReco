import ROOT
import optparse
import myStyle
import math
import myFunctions as mf

ROOT.gROOT.SetBatch(True)

myStyle.ForceStyle()


def same_in_sensor_info(name_dataset, new_info):
    saved_values = myStyle.GetResolutions(name_dataset)
    qty_to_update = ""
    list_2_compare = [["one_res", "res_one_strip"], ["two_res", "res_two_strip"]]
    list_2_compare+= [["time_res", "time_resolution"]]
    list_2_compare+= [["one_eff", "efficiency_one_strip"], ["two_eff", "efficiency_two_strip"]]
    for new_qty, ref_qty in list_2_compare:
        if format(new_info[new_qty], ".1f") != format(saved_values[ref_qty], ".1f"):
            qty_to_update+= "%s, "%(ref_qty)

    if qty_to_update:
        qty_to_update = qty_to_update[:-2]

    return qty_to_update

def same_onestrip_info(name_dataset, new_info):
    saved_values = myStyle.GetResolutions(name_dataset, per_channel=True)["resolution_onestrip"]
    out_msg = ""
    for r,row in enumerate(new_info):
        if len(new_info) != len(saved_values):
            out_msg = "Number of rows, "
            break
        for c,value in enumerate(row):
            if len(row) != len(saved_values[r]):
                out_msg = "Number of columns (%i), "%(c)
                break
            if format(value, ".1f") != format(saved_values[r][c], ".1f"):
                out_msg+= "Ch%i%i, "%(r,c)

    if out_msg:
        out_msg = out_msg[:-2]

    return out_msg


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-A', dest='AllRegions', action='store_true', default = False, help="Get results for all regions")
options, args = parser.parse_args()

dataset = options.Dataset
all_regions = options.AllRegions
outdir = myStyle.getOutputDir(dataset)

sensor_Geometry = myStyle.GetGeometry(dataset)
sensor_name = sensor_Geometry["sensor"]

res_photek = 10 # ps

regions = ["Overall_tight"]
if all_regions:
    regions+= ["Metal", "Gap", "MidGap"]

print("\n\t\tSensor %s summary info to be saved in mySensorInfo.py\n"%(myStyle.RemoveBV(dataset)))

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
    if "Overall" in reg:
        indices = mf.get_existing_indices(inputfile_res1d, "deltaX_oneStrip")
        edge_indices = mf.get_edge_indices(indices)

        n_row, n_col = mf.get_n_row_col(indices)
        info_channels = [[0] * n_col for i in range(n_row)]

        for idx in indices:
            hres_onestrip = inputfile_res1d.Get("deltaX_oneStrip%s"%idx)
            value = 1000 * hres_onestrip.GetStdDev()

            # Approximate appropriate std dev for edge channels (with only half of the channel info)
            if idx in edge_indices:
                mean = 1000 * hres_onestrip.GetMean()
                value = math.sqrt(value**2 + mean**2)
            r, c = int(idx[0]), int(idx[1])
            info_channels[r][c] = value

        # Output line for mySensorInfo.py
        info_str = " > One strip info per channel: ["
        for row in info_channels:
            info_str+= "["
            for v in row:
                info_str+= "%.1f, "%(v)
            info_str = info_str[:-2] + "], "
        info_str = info_str[:-2] + "],"
        # Check if current saved info is the same or if it has changed
        msg = same_onestrip_info(dataset, info_channels)
        if msg:
            info_str+= " --> (!!) Differences: %s (!!)"%msg
        print(info_str)

    info = {}
    print(" > %s region:"%(reg))

    res_region = "_%s"%reg
    if reg == "MidGap":
        res_region = "_Gap"
    elif "Overall" in reg:
        res_region = ""
    
    # Resolution
    # NOTE: One strip tight distribution might look assymetric for some sensors, but this is because of the tight
    # cut that removes half of the channels at the edges. Since we care about the RMS this does not impact the result.
    # Moreover, the RMS of the tight cut in the overall distribution matches in a much better way with each individual value per channel!
    name_onestrip = "deltaX_oneStrip%s_tight"%(res_region)
    name_twostrip = "deltaX_twoStrip%s_tight"%(res_region)
    name_time = "weighted2_timeDiff_tracker_tight" if "Overall" in reg else "weighted2_timeDiff_tracker_%s"%reg
    inputfile_time = inputfile_res1d_tight if "Overall" in reg else inputfile_res1d

    info["one_res"] = 1000 * inputfile_res1d_tight.Get(name_onestrip).GetStdDev()
    info["two_res"] = 1000 * inputfile_res1d_tight.Get(name_twostrip).GetFunction("fit").GetParameter(2)
    info["time_res"] = 1000 * inputfile_time.Get(name_time).GetFunction("fit").GetParameter(2)

    # Efficiency
    name_eff = "cut_flow_%s"%(reg)
    hist_eff = inputfile_eff.Get(name_eff)
    bin_pass = hist_eff.GetXaxis().FindBin(reg)
    if reg == "Overall_tight":
        bin_pass = hist_eff.GetXaxis().FindBin("Pass_tight")
    bin_one = hist_eff.GetXaxis().FindBin("OneStripReco")
    bin_two = hist_eff.GetXaxis().FindBin("TwoStripReco")

    value_pass = hist_eff.GetBinContent(bin_pass)
    value_one = hist_eff.GetBinContent(bin_one)
    value_two = hist_eff.GetBinContent(bin_two)

    info["one_eff"] = 100 * value_one / value_pass
    info["two_eff"] = 100 * value_two / value_pass

    # Output line for mySensorInfo.py
    info_str = "    - List format: ["
    for key in ["one_res", "two_res", "time_res", "one_eff", "two_eff"]:
        info_str+= "%.1f, "%(info[key])
    info_str = info_str[:-2] + "],"
    # Check if current saved info is the same or if it has changed
    info_to_update = same_in_sensor_info(dataset, info)
    if info_to_update:
        info_str+= " (!!) Update mySensorInfo.py --> %s (!!)"%(info_to_update)
    print(info_str)

    # # Output line for Excel (Check only two strip reco and time resolutions)
    # info_str = "    - Excel format: ["
    # for key in ["two_res", "time_res"]:
    #     info_str+= "%.1f, "%(info[key])
    # info_str = info_str[:-2] + "],"
    # print(info_str)

    # Ouput for Latex table (time has tracker contribution removed!)
    info["time_res"] = math.sqrt(info["time_res"]**2 - res_photek**2)
    info_tex = "    - LaTeX format: "
    if all_regions:
        info_tex+= "%s "%(reg)
    info_tex+= "& %.0f $\\pm$ 1 &"%(info["time_res"])
    for key in ["one_res", "one_eff", "two_res", "two_eff"]:
        info_tex+= " %.0f"%(info[key])
        if "eff" in key:
            info_tex+= "\\%"
        info_tex+= " &"
    info_tex+= " %%%% Time reference contribution removed (%.0f [ps])\n"%res_photek
    print(info_tex)

inputfile_res1d.Close()
inputfile_res1d_tight.Close()
inputfile_eff.Close()
