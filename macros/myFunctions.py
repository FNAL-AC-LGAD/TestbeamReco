import ROOT
import myStyle

# Get list of all pairs of indices saved in histograms
# with name <prename> in <inputfile>

def get_existing_indices(inputfile, prename, skip_extra_channel=True):
    list_indices = []
    # Loop over all possible names and save only those existing!
    for i in range(8):
        for j in range(8):
            channel = "%i%i"%(i, j)
            hname = "%s%s"%(prename, channel)
            hist = inputfile.Get(hname)
            if not hist:
                continue

            list_indices.append(channel)

    # Remove extra channel used in pads
    if skip_extra_channel:
        elements_per_row = elements_associated(list_indices, row=True, show_output=False)
        for row in elements_per_row:
            if elements_per_row[row] == 1:
                list_indices.remove(row+"0")

    return list_indices

def get_n_row_col(indices_list):
    # NOTE: This assumes all rows have the same length
    last_idx = indices_list[-1]
    n_row, n_col = int(last_idx[0]) + 1, int(last_idx[1]) +1

    return n_row, n_col

def get_edge_indices(indices_list):
    is_edge = True
    row, col = 9, int(indices_list[-1][1])
    edge_indices = []
    for idx in indices_list:
        # Left edge when moving to a new row
        if row != int(idx[0]):
            row = int(idx[0])
            is_edge = True
        # Right edge when in last column (!) assuming all rows have the same number (!)
        elif int(idx[1]) == col:
            is_edge = True
        else:
            is_edge = False

        if is_edge:
            edge_indices.append(idx)

    return edge_indices

def check_same_n_elements(dict_elements, row=True, show_output=True):
    same_numbers = True
    # Using the first column or row as reference
    n_subchannels = dict_elements["0"]
    for key in dict_elements:
        if dict_elements[key] != n_subchannels:
            prev = "Rows" if row else "Columns"
            post = "columns" if row else "rows"
            msg = " >> (Warning) %s with different number of %s."%(prev, post)
            if show_output:
                print(msg)
                print(dict_elements)
                # exit()
            same_numbers = False

    return same_numbers

def elements_associated(indices, row=True, show_output=False):
    # Create a dictionary to get the number of columns (rows) associated with
    # each row (column)
    n_channels_paired_with = {}
    for i, j in indices:
        key = i if row else j

        if key not in n_channels_paired_with:
            n_channels_paired_with[key] = 0
        n_channels_paired_with[key]+= 1

    if show_output:
        same_elem = check_same_n_elements(n_channels_paired_with, row)

    return n_channels_paired_with

def get_central_channel_position(inputfile, direction="x"):
    # Get total number of channels used
    indices = get_existing_indices(inputfile, "stripBoxInfo")

    dict_associated = elements_associated(indices, (direction=="x"))
    n_subchannels = dict_associated["0"]
    if not check_same_n_elements(dict_associated, (direction=="x")):
        n_subchannels = dict_associated["1"]

    stripBox = "stripBoxInfo" if direction == "x" else "stripBoxInfoY"
    # Even number of columns
    if (n_subchannels%2 == 0):
        central_idx = round(n_subchannels/2)
        pairL = "0%i"%(central_idx-1) if direction is "x" else "%i0"%(central_idx-1)
        pairR = "0%i"%(central_idx) if direction is "x" else "%i0"%(central_idx)
        l_channel = inputfile.Get("%s%s"%(stripBox, pairL)).GetMean(1)
        r_channel = inputfile.Get("%s%s"%(stripBox, pairR)).GetMean(1)
        position_center = (l_channel + r_channel)/2
    # Odd number of columns
    else:
        central_idx = round((n_subchannels-1)/2)
        pair = "0%i"%(central_idx) if direction is "x" else "%i0"%(central_idx)
        position_center = inputfile.Get("%s%s"%(stripBox, pair)).GetMean(1)

    return position_center

# Get limits to draw th2 projection properly aligned w.r.t. channel's boxes drawn
def get_shifted_limits(th2, center_position):
    xmin, xmax = th2.GetXaxis().GetXmin(), th2.GetXaxis().GetXmax()

    zero_bin = th2.GetXaxis().FindBin(0.0)
    central_bin = th2.GetXaxis().FindBin(center_position)
    bin_diff = central_bin - zero_bin

    bin_width = th2.GetXaxis().GetBinWidth(zero_bin)

    # Move distribution so that the bin with the center of
    # the central channel is at zero
    # print("Zero bin: %i, Real center: %i; Diff: %i"%(zero_bin, central_bin, bin_diff))
    if (bin_diff != 0.0):
        xmin-= bin_width*bin_diff
        xmax-= bin_width*bin_diff

    # Even number of bins have 0.0 as lowedge in zero bin.
    # Slightly move this bin to make it look symmetric
    # TODO: Re-run with this line commented out and check differences
    if (th2.GetXaxis().GetBinLowEdge(zero_bin) == 0.0):
        xmin-= bin_width/2.
        xmax-= bin_width/2.

    return xmin, xmax

def is_inside_limits(this_bin, hist, xmax, xmin=0):
    symmetric = not xmin
    if symmetric:
        xmin = -xmax
    bin_min = hist.GetXaxis().FindBin(xmin)
    bin_max = hist.GetXaxis().FindBin(xmax)

    # Avoid asymmetry when value is in bin limit
    if symmetric:
        max_low_limit = hist.GetXaxis().GetBinLowEdge(bin_max)
        if round(xmax, 3) == round(max_low_limit, 3):
            bin_min-= 1

    return (bin_min < this_bin) and (this_bin < bin_max)

def first_common_non_empty_x(list_histograms, first = True):
    # Find first or last (first = True or False) common non empty bin of the histograms listed
    nbins = list_histograms[0].GetXaxis().GetNbins()

    x_filled = 0.0
    at_least_one_empty = True
    infor = 1 if first else nbins
    endfor = nbins+1 if first else 0
    step = 1 if first else -1

    # Use first histogram as reference without loss of generality
    for i in range(infor, endfor, step):
        value = list_histograms[0].GetBinContent(i)
        if value > 0.0:
            # First non empty bin
            bin_non_empty = i
            x_filled = list_histograms[0].GetBinCenter(bin_non_empty)
            break

    while(at_least_one_empty):
        if (bin_non_empty >= nbins or bin_non_empty <= 0):
            print("Something went wrong :C All bins seem to be empty.")
            exit()

        # List with all values in bin non empty
        list_values = []
        for hist in list_histograms:
            ibin = hist.FindBin(x_filled)
            value = hist.GetBinContent(ibin)
            list_values.append(value)

        # Save value if all values are non zero
        if all(v > 0.0 for v in list_values):
            previous_bin = bin_non_empty - step
            x_filled = list_histograms[0].GetBinCenter(previous_bin)
            at_least_one_empty = False
        else:
            bin_non_empty+= step
            x_filled = list_histograms[0].GetBinCenter(bin_non_empty)

    return x_filled

def move_distribution(list_elements, new_center_pos, is_tgraph = False):
    for i, obj in enumerate(list_elements):
        new_min, new_max = get_shifted_limits(obj, new_center_pos)
        if is_tgraph:
            npoints = obj.GetN()
            for j in range(npoints):
                obj.SetPointX(j, obj.GetPointX(j)-new_center_pos)
            list_elements[i] = obj
        else:
            nxbin = obj.GetXaxis().GetNbins()
            hname = "%s_%i_%i"%(obj.GetName(), abs(new_center_pos/0.005), i)
            th1 = ROOT.TH1D(hname, "", nxbin, new_min, new_max)
            for j in range(1, nxbin+1):
                th1.SetBinContent(j, obj.GetBinContent(j))
                th1.SetBinError(j, obj.GetBinError(j))
            list_elements[i] = th1

    return list_elements

def same_limits_compare(list_histograms, xlimit = 0):
    nbins = list_histograms[0].GetXaxis().GetNbins()

    xfirst = abs(first_common_non_empty_x(list_histograms, True))
    xlast = abs(first_common_non_empty_x(list_histograms, False))
    x_simmetric_limit = xfirst if xfirst < xlast else xlast
    if xlimit and (xlimit < x_simmetric_limit):
        x_simmetric_limit = xlimit

    for hist in list_histograms:
        if hist.GetXaxis().GetNbins() != nbins:
            nbins = hist.GetXaxis().GetNbins()
            print(" (!) Beware, sensors with different binning are being compared!")
        for i in range(1, nbins+1):
            # Fill only when inside limits
            if is_inside_limits(i, hist, xmax=x_simmetric_limit):
                continue

            value = hist.GetBinContent(i)
            if value:
                hist.SetBinContent(i, 0.0)

    return list_histograms


# Return a list with the legends dependening on the sensors and variables
# receive a list of sensors and a list of variables as arguments
# example: [("HPK_W9_22_3_20T_500x500_150M_E600", "HPK_W9_23_3_20T_500x500_300M_E600",
#    "HPK_W8_1_1_50T_500x500_150M_C600"], ["resistivityNumber", "capacitance"]))
# The last entrie of the list is the legend header: "Varying (variables)"

def get_legend_comparation_plots(sensors, variables):
    # Define the units of each variable
    variablesUnits = {}
    variablesUnits["pitch"] = " #mum "
    variablesUnits["stripWidth"], variablesUnits["width"] = " #mum ", " #mum "
    variablesUnits["length"] = " mm "
    variablesUnits["BV"], variablesUnits["voltage"] = " mV ", " mV "
    variablesUnits["thickness"] = " #mum "
    variablesUnits["resistivity"] = ""
    variablesUnits["resistivityNumber"] = " #Omega/#Box "
    variablesUnits["capacitance"] = " pF/mm^{2} "

    # Define the name use in the legend of each variable
    variablesName = {}
    variablesName["pitch"] = "pitch"
    variablesName["stripWidth"], variablesName["width"] = " metal width ", " metal width "
    variablesName["length"] = "strip length"
    variablesName["BV"], variablesUnits["voltage"] = " voltage ", " voltage "
    variablesName["thickness"] = " active thickness"
    variablesName["resistivity"] = ""
    variablesName["resistivityNumber"] = " resistivity"
    variablesName["capacitance"] = " capacitance"
    variablesName["manufacturer"] = " manufacturer"

    # Generate the list of legend entries
    sensor_legend_list = []
    for sensor in sensors:
        sensor_legend = ""
        geometry = myStyle.GetGeometry(sensor)
        for variable in variables:
            # add the variables
            if variable == "manufacturer":
                sensor_legend+= sensor[:3] + " "
            else:
                sensor_legend+= str(geometry[variable]) + variablesUnits[variable]
        # add the tag of the sensor at the end
        sensor_legend += " (" + geometry['tag'] + ")"
        sensor_legend_list.append(sensor_legend)

    # Add the Legend header at the end of the list
    if "manufacturer" in variables:
        variables.remove("manufacturer")
    legendHeader = "Varying"
    for i, variable in enumerate(variables):
        legendHeader += variablesName[variable]
        if i == len(variables) - 2 and len(variables) > 1 :
            legendHeader += " and"
    legendHeader = "#bf{%s}"%legendHeader
    sensor_legend_list.append(legendHeader)

    return sensor_legend_list
