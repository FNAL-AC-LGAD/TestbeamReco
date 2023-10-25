from ROOT import TFile, TTree, TCanvas, TH1F, TH2F, TProfile, TLatex, TMath, TEfficiency, TGraph, TGraphErrors, TGraphAsymmErrors, TMultiGraph, TLegend, TF1, gStyle, gROOT, TBox, TGraphAsymmErrors
import ROOT
import numpy as np
import myStyle
import optparse
import os


# run it like this:

# python3 GeneralSummaryPlots.py -y ymin -Y ymax -v y_axis_variable -g x_variable(geometical variable)
# python3 GeneralSummaryPlots.py -y 0 -Y 100 -v time_resolution -e time_resolution_E -g width
# The code takes the values for y from the dictionary resolutions202- located in myStyle.py
# The code takes the values for x from the dictionary geometry202- located in myStyle.py


def shiftOverlappingPoints(x_values, x_offset):

    unique_x_values = set(x_values)

    for x_val in unique_x_values:
        indices = [i for i, val in enumerate(x_values) if val == x_val]

        if len(indices) > 1:
            if len(indices) % 2 == 0:
                for i, j in enumerate(indices):
                    shift = x_offset*(-len(indices)/2 + i + 0.5)
                    x_values[j] = x_val + shift
            else:
                for i, j in enumerate(indices):
                    shift = x_offset*(-int(len(indices)/2) + i)
                    x_values[j] = x_val + shift


# Generae a list with all the sensors that obey certain conditions
# sensorDic: dictionary with the sensor (sensorsGeom2023)
# conditions: dictionary with the conditions ex: {"length":10, "manufacturer":"HPK"}
def GetSensorList(sensorDic, conditions):

    returnList = []
    for sensor, geometry in sensorDic.items():

        counter = 0
        if sensor[-1] == "V":  # remove same sensors with different BV
            continue

        for condition, value in conditions.items():

            if condition == "manufacturer":
                if value in sensor:
                    counter += 1
                continue

            if geometry[condition] == value:
                counter += 1

        if counter == len(conditions):
            returnList.append(sensor + "_" + str(geometry["BV"]) + "V")

    if len(returnList) == 0:
        print("The list is empty, there is no sensor with that geometry")
    return returnList


myStyle.ForceStyle()
gStyle.SetOptStat(0)
organized_mode = True
gROOT.SetBatch(True)
tsize = myStyle.GetSize()

ROOT.gROOT.ForceStyle()
colors = myStyle.GetColors(True)

# dict_resolutions = myStyle.resolutions2023
outdir = myStyle.getOutputDir("Paper2023")
os.makedirs(outdir + "/SummaryPlots", exist_ok=True)

axis_label_dic = {
    "pitch": "Pitch [\mum]",
    "length": "Strip length [mm]",
    "width": "Metal width [\mum]",
    "capacitance": "Capacitance [pC]",
    "thickness": "Thickness [\mum]",
    "resistivity": "Resistivity [\Omega\\\square]",
    "time_resolution": "Time resolution [ps]",
    "time_resolution_m": "Time resolution metal [ps]",
    "time_resolution_g": "Time resolution gap [ps]",
    "spatial_resolution": "Spatial resolution [ps]",
    "spatial_resolution_m": "Spatial resolution metal [ps]",
    "spatial_resolution_g": "Spatial resolution gap [ps]",
    "jitter": "Jitter [ps]",
    "jitter_m": "Jitter metal [ps]",
    "jitter_g": "Jitter gap [ps]",
    "rise_time": "Rise Time [ps]",
    "rise_time_m": "Rise Time metal [ps]",
    "rise_time_g": "Rise Time gap [ps]",
    "amp_max": "Amp max [mV]",
    "amp_max_m": "Amp max [mV]",
    "amp_max_g": "Amp max [mV]",
    "charge": "Charge [fC]",
    "charge_m": "Charge metal [fC]",
    "charge_g": "Charge gap [fC]",
    "baseline_rms": "BaseLine RMS [mv]",
    "baseline_rms_m": "BaseLine RMS metal [mv]",
    "baseline_rms_g": "BaseLine RMS gap [mv]",
    "efficiency_twoStrip": "Two strip efficiency",
    "efficiency_twoStrip_m": "Two strip efficiency metal",
    "efficiency_twoStrip_g": "Two strip efficiency gap",
    "efficiency_oneStrip": "One strip efficiency",
    "efficiency_oneStrip_m": "One strip efficiency metal",
    "efficiency_oneStrip_g": "One strip efficiency gap"
}

color_dic = {
    'HPK_W8_18_2_50T_1P0_500P_100M_C600_208V': colors[0],
    'HPK_W9_14_2_20T_1P0_500P_100M_E600_112V': colors[0],
    'HPK_W8_17_2_50T_1P0_500P_50M_C600_206V': colors[1],
    'HPK_W5_17_2_50T_1P0_500P_50M_E600_190V': colors[1],
    'HPK_W4_17_2_50T_1P0_500P_50M_C240_204V': colors[2],
    'HPK_W2_3_2_50T_1P0_500P_50M_E240_180V': colors[2],
    'HPK_W9_15_2_20T_1P0_500P_50M_E600_114V': colors[3],
    'HPK_KOJI_50T_1P0_80P_60M_E240_190V': colors[4],
    'HPK_KOJI_20T_1P0_80P_60M_E240_112V': colors[4],

    "HPK_50um_500x500um_2x2pad_E600_FNAL_190V": colors[0],
    "HPK_30um_500x500um_2x2pad_E600_FNAL_140V": colors[1],
    "HPK_20um_500x500um_2x2pad_E600_FNAL_105V": colors[2],
}

marker_dic = {
    'HPK_W8_18_2_50T_1P0_500P_100M_C600_208V': 20,
    'HPK_W9_14_2_20T_1P0_500P_100M_E600_112V': 24,
    'HPK_W8_17_2_50T_1P0_500P_50M_C600_206V': 20,
    'HPK_W5_17_2_50T_1P0_500P_50M_E600_190V': 24,
    'HPK_W4_17_2_50T_1P0_500P_50M_C240_204V': 20,
    'HPK_W2_3_2_50T_1P0_500P_50M_E240_180V': 24,
    'HPK_W9_15_2_20T_1P0_500P_50M_E600_114V': 21,
    'HPK_KOJI_50T_1P0_80P_60M_E240_190V': 20,
    'HPK_KOJI_20T_1P0_80P_60M_E240_112V': 24,

    "HPK_50um_500x500um_2x2pad_E600_FNAL_190V": 20,
    "HPK_30um_500x500um_2x2pad_E600_FNAL_140V": 21,
    "HPK_20um_500x500um_2x2pad_E600_FNAL_105V": 24,
}

parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-y', '--ymin', dest='ymin', default=-140.0, type="float",
                  help="Lower limit of the y axes.")
parser.add_option('-Y', '--ymax', dest='ymax', default=0.0, type="float",
                  help="upper limit of the y axes.")
parser.add_option('-v', "--variable", dest='variable', default="",
                  help="variable of the y axes")
parser.add_option('-e', "--variableError", dest='variableError',
                  default="", help="variable of the y axes")
parser.add_option('-g', "--gvariable", dest='gvariable',
                  default="", help="geometical variable(x axis)")
options, args = parser.parse_args()

conditions = {"length": 10.0, "manufacturer": "HPK", "pitch": 500}

y_upper_limit = options.ymax
y_lower_limit = options.ymin
geometry_variable_name = options.gvariable
y_variable_name = options.variable
y_variable_error_name = options.variableError
# y_variable_name = "efficiency_twoStrip"
# y_variable_error_name = "efficiency_twoStrip_error"

# list_of_sensors = GetSensorList(myStyle.sensorsGeom2023, conditions)
list_of_sensors = [
    "HPK_50um_500x500um_2x2pad_E600_FNAL_190V",
    "HPK_30um_500x500um_2x2pad_E600_FNAL_140V",
    "HPK_20um_500x500um_2x2pad_E600_FNAL_105V",
]

geometry_variable = []


variable_value_list = []
variable_error_list = []
variable_metal_list = []
variable_gap_list = []

positionres_weighted_StdDev = []
positionres_weighteduncert = [0.5]*len(list_of_sensors)


for name in list_of_sensors:
    geometry_variable.append(myStyle.GetGeometry(name)[geometry_variable_name])
    sensor_info = myStyle.GetResolutions(name)

    y_variable = sensor_info[y_variable_name]
    y_variable_metal = sensor_info[y_variable_name + "_m"]
    y_variable_gap = sensor_info[y_variable_name + "_g"]
    try:
        y_variable_error = sensor_info[y_variable_error_name]
    except KeyError:
        y_variable_error = 0.

    variable_value_list.append(y_variable)
    variable_error_list.append(y_variable_error)
    variable_metal_list.append(y_variable_metal)
    variable_gap_list.append(y_variable_gap)

# for resistivity Plots
for i in range(len(geometry_variable)):

    if geometry_variable[i] == 'C':
        geometry_variable[i] = 400
    if geometry_variable[i] == 'E':
        geometry_variable[i] = 1600

geometry_variable = np.asarray(geometry_variable)
geometry_variable = geometry_variable.astype(float)
# empty = np.asarray([0]*len(list_of_sensors))

variable_value_array = np.asarray(variable_value_list)
variable_error_array = np.asarray(variable_error_list)
variable_metal_array = np.asarray(variable_metal_list)
variable_gap_array = np.asarray(variable_gap_list)

# print("Sensors : ", list_of_sensors)
print(geometry_variable_name, geometry_variable)

shift = (np.max(geometry_variable)-np.min(geometry_variable))/75

shiftOverlappingPoints(geometry_variable, shift)
print(geometry_variable_name + " shifted", geometry_variable)
print(y_variable_name, variable_value_array)
print(y_variable_name + " on metal", variable_metal_array)
print(y_variable_name + " on gap", variable_gap_array)


c1 = ROOT.TCanvas("c1", "c1", 1080, 800)
c1.SetGrid(0, 1)

multiGraph = TMultiGraph()


ROOT.gPad.SetTicks(1, 1)
ROOT.gStyle.SetOptStat(0)


hdummy = ROOT.TH1D("", "", 1, 0.9*geometry_variable.min(),
                   1.05*geometry_variable.max())
hdummy.GetXaxis().SetTitle(axis_label_dic[geometry_variable_name])
hdummy.GetYaxis().SetTitle(axis_label_dic[y_variable_name])
hdummy.GetYaxis().SetTitleOffset(1.01)
# hdummy.SetMaximum(90.0)
hdummy.SetMaximum(y_upper_limit)
print(y_upper_limit)
hdummy.SetMinimum(y_lower_limit)
hdummy.Draw("AXIS SAME")

# leg = ROOT.TLegend(2*myStyle.GetMargin()+0.01, 1-myStyle.GetMargin() -
# 0.01-0.24, 2*myStyle.GetMargin()+0.01+1.35, 1-myStyle.GetMargin()-0.01)
leg = ROOT.TLegend(2*myStyle.GetMargin()+0.01, 1-myStyle.GetMargin() -
                   0.01-0.34, .93, 1-myStyle.GetMargin()-0.01)
leg.SetTextFont(myStyle.GetFont())
leg.SetTextSize(myStyle.GetSize()-12)


leg.SetBorderSize(1)  # No border
leg.SetTextFont(42)   # Text font (adjust as needed)
leg.SetTextSize(0.033)  # Text size (adjust as needed)
leg.SetFillColor(0)   # Transparent background
leg.SetLineColor(1)   # No line around the leg
leg.SetLineWidth(1)   # No line around the leg
leg.SetMargin(0.25)   # Margin between leg and entries


for i, sensor in enumerate(list_of_sensors):

    variable_graph = ROOT.TGraphAsymmErrors()
    variable_graph.SetPoint(
        0, geometry_variable[i], variable_value_array[i])
    # erros are the difference from the overall value and metal/midgap
    if variable_metal_array[i] < variable_value_array[i]:
        variable_graph.SetPointError(
            0, 0.0, 0.0, abs(variable_metal_array[i]-variable_value_array[i]), abs(variable_gap_list[i]-variable_value_array[i]))
    elif variable_metal_array[i] > variable_value_array[i]:
        variable_graph.SetPointError(
            0, 0.0, 0.0, abs(variable_gap_list[i]-variable_value_array[i]), abs(variable_metal_array[i]-variable_value_array[i]))
    variable_graph.SetMarkerColor(color_dic[sensor])
    variable_graph.SetMarkerStyle(marker_dic[sensor])
    variable_graph.SetMarkerSize(2)
    variable_graph.SetLineColor(color_dic[sensor])
    leg.AddEntry(variable_graph,
                 sensor, "pl")

    multiGraph.Add(variable_graph)


multiGraph.Draw("epl")
# leg.AddEntry(variable_graph,
# axis_label_dic[y_variable_name], "pl")
# leg.AddEntry(position_weighted_StdDev_graph, "Effective resolution", "pl")

# leg.AddEntry(variable_graph, "Two strip reconstruction", "pl")

myStyle.BeamInfo()
text = ROOT.TLatex()
text.SetTextSize(myStyle.GetSize()-4)
text.SetTextAlign(31)
text.DrawLatexNDC(1-myStyle.GetMargin()-0.005, 1 -
                  myStyle.GetMargin()+0.01, "#bf{Varying " + geometry_variable_name + "}")

ROOT.gPad.RedrawAxis("g")
leg.Draw()
# Customize the leg appearance

# Create a TBox for the white background
# Adjust the box's position and size


# position_oneStrip_StdDev_graph.Draw("epl same")
# position_weighted_StdDev_graph.Draw("epl same")

filename = "{}_vs_{}.pdf".format(y_variable_name, geometry_variable_name)
filepath = "{}/SummaryPlots/{}".format(outdir, filename)
c1.SaveAs(filepath)
filename = "{}_vs_{}.png".format(y_variable_name, geometry_variable_name)
filepath = "{}/SummaryPlots/{}".format(outdir, filename)
c1.SaveAs(filepath)
