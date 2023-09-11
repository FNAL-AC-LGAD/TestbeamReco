import ROOT
import os

## Define global variables
marg=0.05
font=43 # Helvetica
# tsize=32
tsize=38 #35

### Paths and directories' functions
def getOutputDir(dataset):
    outdir = "../output/%s/" % dataset
    return outdir

def CreateFolder(outdir, title, overwrite = False):
    outdir2 = os.path.join(outdir,title)

    if overwrite:
        os.mkdir(outdir2)
    else:
        if not os.path.exists(outdir2):
            os.mkdir(outdir2)
        else:
            enum_folder(outdir2)
    print(outdir2,"created.")
    return outdir2

def enum_folder(mypath):
# Adds a sequential number to the path
    # Remove end slash and last digit
    if mypath[-1] == "/":
        mypath = mypath[0:-1]
    if (mypath[-1] == "0") or (mypath[-1] == "1"):
        mypath = mypath[0:-1]

    count = 0
    mypath+="0"
    # Rename until file number is not found
    while(os.path.exists(mypath)):
        # Remove number at the end
        idx = len(str(count))
        count+=1
        mypath = mypath[0:-idx] + str(count)

    os.makedirs(mypath)
    return mypath

def GetPlotsDir(outdir, macro_title):
    outdir_tmp = os.path.join(outdir, macro_title)
    if not (os.path.exists(outdir_tmp)):
        outdir_tmp = CreateFolder(outdir, macro_title, True)

    return outdir_tmp


### Style functions
def ForceStyle():
    ## Defining Style
    ROOT.gStyle.SetPadTopMargin(marg)       #0.05
    ROOT.gStyle.SetPadRightMargin(marg)     #0.05
    ROOT.gStyle.SetPadBottomMargin(2*marg)  #0.10
    ROOT.gStyle.SetPadLeftMargin(2*marg)    #0.10

    ROOT.gStyle.SetPadTickX(1)
    ROOT.gStyle.SetPadTickY(1)

    ROOT.gStyle.SetTextFont(font)
    ROOT.gStyle.SetLabelFont(font,"x")
    ROOT.gStyle.SetTitleFont(font,"x")
    ROOT.gStyle.SetLabelFont(font,"y")
    ROOT.gStyle.SetTitleFont(font,"y")
    ROOT.gStyle.SetLabelFont(font,"z")
    ROOT.gStyle.SetTitleFont(font,"z")

    ROOT.gStyle.SetTextSize(tsize)
    ROOT.gStyle.SetLabelSize(tsize-4,"x")
    ROOT.gStyle.SetTitleSize(tsize,"x")
    ROOT.gStyle.SetLabelSize(tsize-4,"y")
    ROOT.gStyle.SetTitleSize(tsize,"y")
    ROOT.gStyle.SetLabelSize(tsize-4,"z")
    ROOT.gStyle.SetTitleSize(tsize,"z")

    ROOT.gStyle.SetLegendFont(font)
    ROOT.gStyle.SetLegendTextSize(tsize)
    ROOT.gStyle.SetLegendBorderSize(0)
    ROOT.gStyle.SetLegendFillColor(0)

    ROOT.gStyle.SetTitleXOffset(1.0)
    ROOT.gStyle.SetTitleYOffset(1.0)
    ROOT.gStyle.SetOptTitle(0)
    # ROOT.gStyle.SetOptStat(0)

    ROOT.gStyle.SetHistLineWidth(4)

    ROOT.gStyle.SetGridColor(921)
    ROOT.gStyle.SetGridStyle()

    ROOT.gROOT.ForceStyle()


def BeamInfo():
    text = ROOT.TLatex()
    text.SetTextSize(tsize-4)
    text.DrawLatexNDC(2*marg+0.005,1-marg+0.01,"#bf{FNAL 120 GeV proton beam}")

def SensorInfo(sensor="Name", bias_voltage="", write_bv=True,adjustleft=0):
    text = ROOT.TLatex()
    text.SetTextSize(tsize-4)
    text.SetTextAlign(31)
    if bias_voltage:
        text.DrawLatexNDC(1-marg-0.005-adjustleft,1-marg+0.01,"#bf{"+str(sensor) + ", "+str(bias_voltage)+"}")
    else:
        text.DrawLatexNDC(1-marg-0.005-adjustleft,1-marg+0.01,"#bf{"+str(sensor)+"}")

def SensorInfoSmart(dataset, adjust=0.00):
    name ="Not defined"
    bias_voltage = "X"

    if GetGeometry(dataset):
        name = GetGeometry(dataset)['sensor']
        bias_voltage = GetBV(dataset)

    SensorInfo(name,bias_voltage,True,adjust)


### Return-value functions
def GetMargin():
    return marg

def GetFont():
    return font

def GetSize():
    return tsize

def GetPadCenter():
    return (1 + marg)/2


### Colors
def GetColors(color_blind = False):
    strip_colors = [416+2, 432+2, 600, 880, 632, 400+2, 600-5]
    ## [#kGreen+2, #kCyan+2, #kBlue, #kViolet, #kRed, #kYellow+2, #kBlue-3]
    if color_blind:
        color_RGB = [[51,34,136],[51,187,238],[17,119,51],[153,153,51],[204,102,119],[136,34,85],[128,128,128]]
        # [indigo, cyan, green, olive, rose, wine]
        
        for i in range(0,len(strip_colors)):
            strip_colors[i] = ROOT.TColor.GetColor(color_RGB[i][0],color_RGB[i][1],color_RGB[i][2])

    return strip_colors


### Names and strings
def GetGeometry(name):
    sensor_dict = {}

    this_name = RemoveBV(name)

    if (this_name in sensorsGeom2022):
        sensor_dict = sensorsGeom2022[this_name]
    elif (this_name in sensorsGeom2023):
        sensor_dict = sensorsGeom2023[this_name]
    else:
        print("Sensor not found in any dictionary :(")

    return sensor_dict

def RemoveBV(name):
    name_split=name.split('_')
    if name_split[-1][-1]=="V":
        name='_'.join(str(name_split[i]) for i in range(len(name_split)-1))
    return name

def GetBV(name):
    name_split=name.split('_')
    if name_split[-1][-1]=="V":
        return name_split[-1]
    else:
        return ""


### 2022 Sensors' information dictionaries
# Dataset_name: {'sensor': <name>, 'pitch': [micron], 'stripWidth': [micron], "BV": [V], "length": [mm]},
sensorsGeom2022 = {
    "EIC_W2_1cm_500up_300uw": {'sensor': "BNL 10-300", 'pitch': 500, 'stripWidth': 300, "BV": 240, "length": 10.0},
    "EIC_W1_1cm_500up_200uw": {'sensor': "BNL 10-200", 'pitch': 500, 'stripWidth': 200, "BV": 255, "length": 10.0},
    "EIC_W2_1cm_500up_100uw": {'sensor': "BNL 10-100", 'pitch': 500, 'stripWidth': 100, "BV": 220, "length": 10.0},
    "EIC_W1_1cm_100up_50uw": {'sensor': "EIC_1cm_100up_50uw", 'pitch': 100, 'stripWidth': 50, "BV": 240, "length": 10.0},
    "EIC_W1_1cm_200up_100uw": {'sensor': "EIC_1cm_200up_100uw", 'pitch': 200, 'stripWidth': 100, "BV": 240, "length": 10.0},
    "EIC_W1_1cm_300up_150uw": {'sensor': "EIC_1cm_300up_150uw", 'pitch': 300, 'stripWidth': 150, "BV": 240, "length": 10.0},
    "EIC_W1_UCSC_2p5cm_500up_200uw": {'sensor': "EIC_2p5cm_UCSC_500up_200uw", 'pitch': 500, 'stripWidth': 200, "BV": 330, "length": 25.0},
    "EIC_W1_2p5cm_500up_200uw": {'sensor': "BNL 25-200", 'pitch': 500, 'stripWidth': 200, "BV": 215, "length": 25.0},
    "HPK_Eb_1cm_80up_45uw": {'sensor': "HPK_Eb_80up_45uw", 'pitch': 80, 'stripWidth': 45, "BV": 170, "length": 10.0},
    "EIC_W1_0p5cm_500up_200uw_1_7": {'sensor': "EIC_1_7_0p5cm_500up_200uw", 'pitch': 500, 'stripWidth': 200, "BV": 240, "length": 5.0},
    "EIC_W1_0p5cm_500up_200uw_1_4": {'sensor': "BNL 5-200", 'pitch': 500, 'stripWidth': 200, "BV": 245, "length": 5.0},
    "BNL_500um_squares_175V": {'sensor': "BNL_squares_1cm_500up_300uw", 'pitch': 500, 'stripWidth': 100, "BV": 175},
    "BNL2021_22_medium_150up_80uw": {'sensor': "BNL2021_V2_150up_80uw", 'pitch': 150, 'stripWidth': 80, "BV": 285},
    "IHEP_W1_I_150up_80uw": {'sensor': "IHEP_1cm_150up_80uw", 'pitch': 150, 'stripWidth': 80, "BV": 185},
}

# 'position_oneStrip': Std Dev from fit, 'position_oneStrip_E': Statistical error from fit, 'position_oneStripRMS': RMS WITH OnMetal cut,
# 'position_oneStrip_StdDev': RMS WITHOUT OnMetal cut (This is the value used in the paper)
resolutions2022 = {
    "EIC_W2_1cm_500up_300uw_240V": {'position_oneStrip'  : 75.92, 'position_oneStrip_E': 0.18, 'position_oneStripRMS': 78.11,
                                    'position_oneStrip_StdDev': 82.71,
                                    'position_twoStrip'  : 15.74, 'position_twoStrip_E': 0.08,
                                    'efficiency_oneStrip': 0.51, 'efficiency_twoStrip' : 0.49},
    "EIC_W1_1cm_500up_200uw_255V": {'position_oneStrip'  : 81.89, 'position_oneStrip_E': 0.08, 'position_oneStripRMS': 54.75,
                                    'position_oneStrip_StdDev': 81.86,
                                    'position_twoStrip'  : 18.49, 'position_twoStrip_E': 0.02,
                                    'efficiency_oneStrip': 0.43, 'efficiency_twoStrip' : 0.57},
    "EIC_W2_1cm_500up_100uw_220V": {'position_oneStrip'  : 66.03, 'position_oneStrip_E': 0.10, 'position_oneStripRMS': 27.84,
                                    'position_oneStrip_StdDev': 68.89,
                                    'position_twoStrip'  : 19.23, 'position_twoStrip_E': 0.02,
                                    'efficiency_oneStrip': 0.23, 'efficiency_twoStrip' : 0.77},
    "EIC_W1_2p5cm_500up_200uw_215V": {'position_oneStrip'  : 121.5, 'position_oneStrip_E': 0.10, 'position_oneStripRMS': 70.93,
                                      'position_oneStrip_StdDev': 128.10,
                                      'position_twoStrip'  : 31.32, 'position_twoStrip_E': 0.12,
                                      'efficiency_oneStrip': 0.82, 'efficiency_twoStrip' : 0.18},
    "EIC_W1_0p5cm_500up_200uw_1_4_245V": {'position_oneStrip'  : 59.39, 'position_oneStrip_E': 0.08, 'position_oneStripRMS': 51.79,
                                          'position_oneStrip_StdDev': 60.93,
                                          'position_twoStrip'  : 11.76, 'position_twoStrip_E': 0.02,
                                          'efficiency_oneStrip': 0.35, 'efficiency_twoStrip' : 0.65},
    "HPK_Eb_1cm_80up_45uw": {'position_oneStrip'  : 11.91, 'position_oneStrip_E': 0.00, 'position_oneStripRMS': 13.83,
                             'position_twoStrip'  :  9.36, 'position_twoStrip_E': 0.00,
                             'efficiency_oneStrip': 0.50, 'efficiency_twoStrip' : 0.50},
    "BNL2021_22_medium_150up_80uw_285V": {'position_oneStrip'  : 14.0, 'position_oneStrip_E': 0.00, 'position_oneStripRMS': 22.35,
                                          'position_twoStrip'  : 8.01, 'position_twoStrip_E': 0.00,
                                          'efficiency_oneStrip': 0.50, 'efficiency_twoStrip': 0.50},
}

resolutions2022OneStripChannel = {
    "EIC_W2_1cm_500up_300uw_240V": {'resOneStrip': [-1.00, 81.75, 83.41, 83.40, 82.10, -1.00, -1.00], ## Std Dev
                                  # 'resOneStrip': [-1.00, 75.61, 75.73, 77.48, 77.80, -1.00, -1.00], ## Sigma fit
                                  # 'errOneStrip': [ 1.00, 00.47, 00.40, 00.39, 00.40,  1.00,  1.00}],## Sigma fit
                                    'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]},
    "EIC_W1_1cm_500up_200uw_255V": {'resOneStrip': [-1.00, 76.99, 81.69, 79.00, 82.88, 84.76, -1.00],
                                    'errOneStrip': [ 1.00, 00.23, 00.19, 00.10, 00.15, 00.16,  1.00]},
    "EIC_W2_1cm_500up_100uw_220V": {'resOneStrip': [-1.00, 66.17, 68.40, 66.86, 68.28, 72.04, -1.00], ## Std Dev
                                  # 'resOneStrip': [-1.00, 59.17, 63.30, 61.23, 64.21, 69.26, -1.00], ## Sigma fit
                                  # 'errOneStrip': [ 1.00, 00.32, 00.30, 00.20, 00.17,  0.19,  1.00]},## Sigma fit
                                    'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]},
    "EIC_W1_2p5cm_500up_200uw_215V": {'resOneStrip': [-1.00, 76.99, 81.69, 79.00, 82.88, 84.76, -1.00],
                                      'errOneStrip': [ 1.00, 00.23, 00.19, 00.10, 00.15, 00.16,  1.00]},
    "EIC_W1_0p5cm_500up_200uw_1_4_245V": {'resOneStrip': [-1.00, 76.99, 81.69, 79.00, 82.88, 84.76, -1.00],
                                          'errOneStrip': [ 1.00, 00.23, 00.19, 00.10, 00.15, 00.16,  1.00]},
    "HPK_Eb_1cm_80up_45uw": {'resOneStrip': [-1.00, 76.99, 81.69, 79.00, 82.88, 84.76, -1.00],
                             'errOneStrip': [ 1.00, 00.23, 00.19, 00.10, 00.15, 00.16,  1.00]},
    "BNL2021_22_medium_150up_80uw_285V": {'resOneStrip': [-1.00, 76.99, 81.69, 79.00, 82.88, 84.76, -1.00],
                                          'errOneStrip': [ 1.00, 00.23, 00.19, 00.10, 00.15, 00.16,  1.00]},
}

### 2023 Sensors' information dictionaries
# Dataset_name: {'sensor': <name>, 'pitch': [micron], 'stripWidth': [micron], "BV": [V], "length": [mm],
#               "thickness": [micron], "width": [micron], "resistivity": <letter>, "capacitance": [pF/mm2]},
sensorsGeom2023 = {
    "BNL_50um_1cm_450um_W3051_2_2": {'sensor': "BNL_50um_1cm_450um_W3051", 'pitch': 500, 'stripWidth': 50, "BV": 170, "length": 10.0, "thickness": 50 ,"width": 50, "resistivity": "Null", "capacitance": "Null" },
    "BNL_50um_1cm_400um_W3051_1_4": {'sensor': "BNL_50um_1cm_400um_W3051", 'pitch': 500, 'stripWidth': 100, "BV": 160, "length": 10.0, "thickness": 50  ,"width": 100, "resistivity": "Null", "capacitance": "Null" },
    "BNL_50um_1cm_450um_W3052_2_4": {'sensor': "BNL_50um_1cm_450um_W3052", 'pitch': 500, 'stripWidth': 50, "BV": 185, "length": 10.0, "thickness": 50 ,"width": 50, "resistivity": "Null", "capacitance": "Null"},
    "BNL_20um_1cm_400um_W3074_1_4": {'sensor': "BNL_20um_1cm_400um_W3074", 'pitch': 500, 'stripWidth': 100, "BV": 95, "length": 10.0, "thickness": 20 ,"width": 100, "resistivity": "Null", "capacitance": "Null"},
    "BNL_20um_1cm_400um_W3075_1_2": {'sensor': "BNL_20um_1cm_400um_W3075", 'pitch': 500, 'stripWidth': 100, "BV": 80, "length": 10.0, "thickness": 20,"width": 100, "resistivity": "Null", "capacitance": "Null"} ,
    "BNL_20um_1cm_450um_W3074_2_1": {'sensor': "BNL_20um_1cm_450um_W3074", 'pitch': 500, 'stripWidth': 50, "BV": 95, "length": 10.0, "thickness": 20,"width": 50, "resistivity": "Null", "capacitance": "Null"} ,
    "BNL_20um_1cm_450um_W3075_2_4": {'sensor': "BNL_20um_1cm_450um_W3075", 'pitch': 500, 'stripWidth': 50, "BV": 80, "length": 10.0, "thickness": 20,"width": 50, "resistivity": "Null", "capacitance": "Null"} ,
    "BNL_50um_2p5cm_mixConfig1_W3051_1_4": {'sensor': "BNL_50um_2p5cm_mixConfig1_W3051", 'pitch': 500, 'stripWidth': 100, "BV": 170, "length": 25.0 , "thickness": 50,"width": 100, "resistivity": "Null", "capacitance": "Null"},
    "BNL_50um_2p5cm_mixConfig2_W3051_1_4": {'sensor': "BNL_50um_2p5cm_mixConfig2_W3051", 'pitch': 500, 'stripWidth': 50, "BV": 170, "length": 25.0, "thickness": 50,"width": 50, "resistivity": "Null", "capacitance": "Null"},
    "HPK_20um_500x500um_2x2pad_E600_FNAL": {'sensor': "HPK_20um_2x2pad", 'pitch': 500, 'stripWidth': 500, "BV": 105, "length": 0.5, "thickness": 20, "width": 500, "resistivity": "E", "capacitance": 600},
    "HPK_30um_500x500um_2x2pad_E600_FNAL": {'sensor': "HPK_30um_2x2pad", 'pitch': 500, 'stripWidth': 500, "BV": 140, "length": 0.5, "thickness": 30, "width": 500, "resistivity": "E", "capacitance": 600 },
    "HPK_50um_500x500um_2x2pad_E600_FNAL": {'sensor': "HPK_50um_2x2pad", 'pitch': 500, 'stripWidth': 500, "BV": 190, "length": 0.5, "thickness": 50, "width": 500, "resistivity": "E", "capacitance": 600},

    "HPK_W8_18_2_50T_1P0_500P_100M_C600": {'sensor': "HPK_W8_18_2_50T_100M_C600", 'pitch': 500, 'stripWidth': 100, "BV": 208, "length": 10.0, "thickness": 50,"width": 100, "resistivity": "C", "capacitance": 600},

    "HPK_W8_17_2_50T_1P0_500P_50M_C600": {'sensor': "HPK_W8_17_2_50T_50M_C600", 'pitch': 500, 'stripWidth': 50, "BV": 206, "length": 10.0, "thickness": 50,"width": 50, "resistivity": "C", "capacitance": 600 },
    "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": {'sensor': "HPK_W8_17_2_50T_50M_C600", 'pitch': 500, 'stripWidth': 50, "BV": 200, "length": 10.0, "thickness": 50,"width": 50, "resistivity": "C", "capacitance": 600 },

    "HPK_W4_17_2_50T_1P0_500P_50M_C240": {'sensor': "HPK_W4_17_2_50T_1P0_500P_50M_C240", 'pitch': 500, 'stripWidth': 50, "BV": 204, "length": 10.0, "thickness": 50,"width": 50, "resistivity": "C", "capacitance": 240 },

    "HPK_W5_17_2_50T_1P0_500P_50M_E600": {'sensor': "HPK_W5_17_2_50T_1P0_500P_50M_E600", 'pitch': 500, 'stripWidth': 50, "BV": 190, "length": 10.0, "thickness": 50,"width": 50, "resistivity": "E", "capacitance": 600},
    "HPK_W5_17_2_50T_1P0_500P_50M_E600_188V": {'sensor': "HPK_W5_17_2_50T_1P0_500P_50M_E600", 'pitch': 500, 'stripWidth': 50, "BV": 188, "length": 10.0, "thickness": 50 ,"width": 50, "resistivity": "E", "capacitance": 600},
    "HPK_W5_17_2_50T_1P0_500P_50M_E600_186V": {'sensor': "HPK_W5_17_2_50T_1P0_500P_50M_E600", 'pitch': 500, 'stripWidth': 50, "BV": 186, "length": 10.0, "thickness": 50,"width": 50, "resistivity": "E", "capacitance": 600},
    "HPK_W5_17_2_50T_1P0_500P_50M_E600_192V": {'sensor': "HPK_W5_17_2_50T_1P0_500P_50M_E600", 'pitch': 500, 'stripWidth': 50, "BV": 192, "length": 10.0, "thickness": 50,"width": 50, "resistivity": "E", "capacitance": 600 },
    "HPK_W5_17_2_50T_1P0_500P_50M_E600_194V": {'sensor': "HPK_W5_17_2_50T_1P0_500P_50M_E600", 'pitch': 500, 'stripWidth': 50, "BV": 194, "length": 10.0, "thickness": 50,"width": 50, "resistivity": "E", "capacitance": 600 },

    "HPK_W9_15_2_20T_1P0_500P_50M_E600":{'sensor': "HPK_W9_15_2_20T_1P0_500P_50M_E600", 'pitch': 500, 'stripWidth': 50, "BV": 114, "length": 10.0, "thickness": 20,"width": 50 , "resistivity": "E", "capacitance": 600 },
    "HPK_W2_3_2_50T_1P0_500P_50M_E240":{'sensor': "HPK_W2_3_2_50T_1P0_500P_50M_E240", 'pitch': 500, 'stripWidth': 50, "BV": 180, "length": 10.0, "thickness": 50,"width": 50, "resistivity": "E", "capacitance":  240},
    "HPK_W9_14_2_20T_1P0_500P_100M_E600":{'sensor': "HPK_W9_14_2_20T_1P0_500P_100M_E600", 'pitch': 500, 'stripWidth': 100, "BV": 112, "length": 10.0, "thickness": 20, "width": 100, "resistivity": "E", "capacitance": 600},
    "HPK_KOJI_50T_1P0_80P_60M_E240":{'sensor': "HPK_50T_1P0_80P_60M_E240", 'pitch': 80, 'stripWidth': 60, "BV": 190, "length": 10.0, "thickness": 50, "width": 60, "resistivity": "E", "capacitance": 240},
    "HPK_KOJI_20T_1P0_80P_60M_E240":{'sensor': "HPK_20T_1P0_80P_60M_E240", 'pitch': 80, 'stripWidth': 60, "BV": 112, "length": 10.0, "thickness": 20, "width": 60, "resistivity": "E", "capacitance": 240},

    "HPK_W9_15_4_20T_0P5_500P_50M_E600" :{'sensor': "HPK_W9_15_4_20T_0P5_500P_50M_E600",'pitch': 500, 'stripWidth': 50, "BV": 110, "length": 5.0, "thickness": 20, "width": 50, "resistivity": "E", "capacitance":  600},
    "HPK_W9_22_3_20T_500x500_150M_E600" :{'sensor': "HPK_W9_22_3_20T_500x500_150M_E600",'pitch': 500, 'stripWidth': 150, "BV": 112, "length": 5.0, "thickness": 20, "width": 150, "resistivity": "E", "capacitance":  600},
    "HPK_W9_23_3_20T_500x500_300M_E600" :{'sensor': "HPK_W9_23_3_20T_500x500_300M_E600",'pitch': 500, 'stripWidth': 300, "BV": 112, "length": 5.0, "thickness": 20, "width": 300, "resistivity": "E" , "capacitance":  600},
    "HPK_W11_22_3_20T_500x500_150M_C600" :{'sensor': "HPK_W11_22_3_20T_500x500_150M_C600",'pitch': 500, 'stripWidth': 150, "BV": 116, "length": 5.0, "thickness": 20, "width": 150, "resistivity": "C", "capacitance": 600},
    "HPK_W8_1_1_50T_500x500_150M_C600" :{'sensor': "HPK_W8_1_1_50T_500x500_150M_C600",'pitch': 500, 'stripWidth': 150, "BV": 200, "length": 5.0, "thickness": 50, "width": 150, "resistivity": "C", "capacitance": 600},
    "HPK_W5_1_1_50T_500x500_150M_E600" :{'sensor': "HPK_W5_1_1_50T_500x500_150M_E600",'pitch': 500, 'stripWidth': 150, "BV": 185, "length": 5.0, "thickness": 50, "width": 150, "resistivity": "C", "capacitance": 600},
}

# NEED TO BE UPDATED! ONLY PLACEHOLDERS TO MAKE PAPER_PLOTS MACROS RUN
# 'position_oneStrip': Std Dev from fit, 'position_oneStrip_E': Statistical error from fit, 'position_oneStripRMS': RMS WITH OnMetal cut,
# 'position_oneStrip_StdDev': RMS WITHOUT OnMetal cut (This is the value used in the paper)
resolutions2023 = {
    "BNL_50um_1cm_450um_W3051_2_2_170V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 
                                          'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                          'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                          'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                          "time_resolution": 0.0, "time_resolution_E": 0.0,
                                          "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
                                          "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
                                          "jitter": 0.0,
                                          "jitter_m": 0.0,
                                          "jitter_g": 0.0,
                                          "amp_max":0.0 , "max_amp_E": 0.0,
                                          "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
                                          "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
                                          "rise_time": 0.0, "rise_time_E": 0.0,
                                          "rise_time_m": 0.0, "rise_time_n_E": 0.0,
                                          "rise_time_g": 0.0, "rise_time_g_E": 0.0,
                                          "baseline_rms": 0.0 , "baseline_rms": 0.0,
                                          "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
                                          "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
                                          "charge": 0.0, "charge_E":0.0,
                                          "charge_m": 0.0, "charge_m_E":0.0,
                                          "charge_g": 0.0, "charge_g_E":0.0,
                                        },

    "BNL_50um_1cm_400um_W3051_1_4_160V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
                                          'position_oneStripRMS': 0.00,'position_oneStrip_StdDev': 0.00,
                                          'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                          'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                          "time_resolution": 0.0, "time_resolution_E": 0.0,
                                          "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
                                          "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
                                          "jitter": 0.0,
                                          "jitter_m": 0.0,
                                          "jitter_g": 0.0,
                                          "amp_max": 0.0 , "max_amp_E": 0.0,
                                          "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
                                          "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
                                          "rise_time": 0.0, "rise_time_E": 0.0,
                                          "rise_time_m": 0.0, "rise_time_n_E": 0.0,
                                          "rise_time_g": 0.0, "rise_time_g_E": 0.0,
                                          "baseline_rms": 0.0 , "baseline_rms": 0.0,
                                          "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
                                          "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
                                          "charge": 0.0, "charge_E":0.0,
                                          "charge_m": 0.0, "charge_m_E":0.0,
                                          "charge_g": 0.0, "charge_g_E":0.0,
                                        },

    "BNL_50um_1cm_450um_W3052_2_4_185V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 
                                          'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                          'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                          'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                          "time_resolution": 0.0, "time_resolution_E": 0.0,
                                          "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
                                          "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
                                          "jitter": 0.0,
                                          "jitter_m": 0.0,
                                          "jitter_g": 0.0,
                                          "amp_max": 0.0 , "max_amp_E": 0.0,
                                          "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
                                          "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
                                          "rise_time": 0.0, "rise_time_E": 0.0,
                                          "rise_time_m": 0.0, "rise_time_n_E": 0.0,
                                          "rise_time_g": 0.0, "rise_time_g_E": 0.0,
                                          "baseline_rms": 0.0 , "baseline_rms": 0.0,
                                          "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
                                          "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
                                          "charge": 0.0, "charge_E":0.0,
                                          "charge_m": 0.0, "charge_m_E":0.0,
                                          "charge_g": 0.0, "charge_g_E":0.0,
                                        },

    "BNL_20um_1cm_400um_W3074_1_4_95V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
                                         'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                         'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                         'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                         "time_resolution": 0.0, "time_resolution_E": 0.0,
                                         "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
                                         "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
                                         "jitter": 0.0,
                                         "jitter_m": 0.0,
                                         "jitter_g": 0.0,
                                         "amp_max": 0.0 , "max_amp_E": 0.0,
                                         "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
                                         "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
                                         "rise_time": 0.0, "rise_time_E": 0.0,
                                         "rise_time_m": 0.0, "rise_time_n_E": 0.0,
                                         "rise_time_g": 0.0, "rise_time_g_E": 0.0,
                                         "baseline_rms": 0.0 , "baseline_rms": 0.0,
                                         "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
                                         "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
                                         "charge": 0.0, "charge_E":0.0,
                                         "charge_m": 0.0, "charge_m_E":0.0,
                                         "charge_g": 0.0, "charge_g_E":0.0,
                                        },

    "BNL_20um_1cm_400um_W3075_1_2_80V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
                                         'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                         'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                         'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                         "time_resolution": 0.0, "time_resolution_E": 0.0,
                                         "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
                                         "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
                                         "jitter": 0.0,
                                         "jitter_m": 0.0,
                                         "jitter_g": 0.0,
                                         "amp_max": 0.0 , "max_amp_E": 0.0,
                                         "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
                                         "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
                                         "rise_time": 0.0, "rise_time_E": 0.0,
                                         "rise_time_m": 0.0, "rise_time_n_E": 0.0,
                                         "rise_time_g": 0.0, "rise_time_g_E": 0.0,
                                         "baseline_rms": 0.0 , "baseline_rms": 0.0,
                                         "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
                                         "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
                                         "charge": 0.0, "charge_E":0.0,
                                         "charge_m": 0.0, "charge_m_E":0.0,
                                         "charge_g": 0.0, "charge_g_E":0.0,
                                        },

    "BNL_20um_1cm_450um_W3074_2_1_95V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 
                                         'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                         'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                         'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                         "time_resolution": 0.0, "time_resolution_E": 0.0,
                                         "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
                                         "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
                                         "jitter": 0.0,
                                         "jitter_m": 0.0,
                                         "jitter_g": 0.0,
                                         "amp_max": 0.0 , "max_amp_E": 0.0,
                                         "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
                                         "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
                                         "rise_time": 0.0, "rise_time_E": 0.0,
                                         "rise_time_m": 0.0, "rise_time_n_E": 0.0,
                                         "rise_time_g": 0.0, "rise_time_g_E": 0.0,
                                         "baseline_rms": 0.0 , "baseline_rms": 0.0,
                                         "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
                                         "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
                                         "charge": 0.0, "charge_E":0.0,
                                         "charge_m": 0.0, "charge_m_E":0.0,
                                         "charge_g": 0.0, "charge_g_E":0.0,
                                        },

    "BNL_20um_1cm_450um_W3075_2_4_80V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 
                                         'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                         'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                         'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                         "time_resolution": 0.0, "time_resolution_E": 0.0,
                                         "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
                                         "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
                                         "jitter": 0.0,
                                         "jitter_m": 0.0,
                                         "jitter_g": 0.0,
                                         "amp_max": 0.0 , "max_amp_E": 0.0,
                                         "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
                                         "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
                                         "rise_time": 0.0, "rise_time_E": 0.0,
                                         "rise_time_m": 0.0, "rise_time_n_E": 0.0,
                                         "rise_time_g": 0.0, "rise_time_g_E": 0.0,
                                         "baseline_rms": 0.0 , "baseline_rms": 0.0,
                                         "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
                                         "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
                                         "charge": 0.0, "charge_E":0.0,
                                         "charge_m": 0.0, "charge_m_E":0.0,
                                         "charge_g": 0.0, "charge_g_E":0.0,
                                        },

    "BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 
                                                 'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                                 'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                                 'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                                 "time_resolution": 0.0, "time_resolution_E": 0.0,
                                                 "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
                                                 "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
                                                 "jitter": 0.0,
                                                 "jitter_m": 0.0,
                                                 "jitter_g": 0.0,
                                                 "amp_max": 0.0 , "max_amp_E": 0.0,
                                                 "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
                                                 "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
                                                 "rise_time": 0.0, "rise_time_E": 0.0,
                                                 "rise_time_m": 0.0, "rise_time_n_E": 0.0,
                                                 "rise_time_g": 0.0, "rise_time_g_E": 0.0,
                                                 "baseline_rms": 0.0 , "baseline_rms": 0.0,
                                                 "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
                                                 "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
                                                 "charge": 0.0, "charge_E":0.0,
                                                 "charge_m": 0.0, "charge_m_E":0.0,
                                                 "charge_g": 0.0, "charge_g_E":0.0,
                                                },

    "BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
                                                 'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                                 'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                                 'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                                 "time_resolution": 0.0, "time_resolution_E": 0.0,
                                                 "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
                                                 "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
                                                 "jitter": 0.0,
                                                 "jitter_m": 0.0,
                                                 "jitter_g": 0.0,
                                                 "amp_max": 0.0 , "max_amp_E": 0.0,
                                                 "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
                                                 "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
                                                 "rise_time": 0.0, "rise_time_E": 0.0,
                                                 "rise_time_m": 0.0, "rise_time_n_E": 0.0,
                                                 "rise_time_g": 0.0, "rise_time_g_E": 0.0,
                                                 "baseline_rms": 0.0 , "baseline_rms": 0.0,
                                                 "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
                                                 "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
                                                 "charge": 0.0, "charge_E":0.0,
                                                 "charge_m": 0.0, "charge_m_E":0.0,
                                                 "charge_g": 0.0, "charge_g_E":0.0,
                                                },

    "HPK_20um_500x500um_2x2pad_E600_FNAL_105V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
                                                 'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                                 'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                                 'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                                 "time_resolution": 24.09, "time_resolution_E": 0.0,
                                                 "time_resolution_m": 23.53, "time_resolution_m_E": 0.0,
                                                 "time_resolution_g": 30.50, "time_resolution_g_E": 0.0,
                                                 "jitter": 0.0,
                                                 "jitter_m": 0.0,
                                                 "jitter_g": 0.0,
                                                 "amp_max": 0.0 , "max_amp_E": 0.0,
                                                 "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
                                                 "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
                                                 "rise_time": 0.0, "rise_time_E": 0.0,
                                                 "rise_time_m": 0.0, "rise_time_n_E": 0.0,
                                                 "rise_time_g": 0.0, "rise_time_g_E": 0.0,
                                                 "baseline_rms": 0.0 , "baseline_rms": 0.0,
                                                 "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
                                                 "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
                                                 "charge": 0.0, "charge_E":0.0,
                                                 "charge_m": 0.0, "charge_m_E":0.0,
                                                 "charge_g": 0.0, "charge_g_E":0.0,
                                                },

    "HPK_30um_500x500um_2x2pad_E600_FNAL_140V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
                                                 'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                                 'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                                 'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                                 "time_resolution": 28.31, "time_resolution_E": 0.0,
                                                 "time_resolution_m": 26.83, "time_resolution_m_E": 0.0,
                                                 "time_resolution_g": 39.26, "time_resolution_g_E": 0.0,
                                                 "jitter": 0.0,
                                                 "jitter_m": 0.0,
                                                 "jitter_g": 0.0,
                                                 "amp_max": 0.0 , "max_amp_E": 0.0,
                                                 "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
                                                 "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
                                                 "rise_time": 0.0, "rise_time_E": 0.0,
                                                 "rise_time_m": 0.0, "rise_time_n_E": 0.0,
                                                 "rise_time_g": 0.0, "rise_time_g_E": 0.0,
                                                 "baseline_rms": 0.0 , "baseline_rms": 0.0,
                                                 "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
                                                 "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
                                                 "charge": 0.0, "charge_E":0.0,
                                                 "charge_m": 0.0, "charge_m_E":0.0,
                                                 "charge_g": 0.0, "charge_g_E":0.0,
                                                },

    "HPK_50um_500x500um_2x2pad_E600_FNAL_190V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
                                                 'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                                 'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                                 'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                                 "time_resolution": 40.80, "time_resolution_E": 0.0,
                                                 "time_resolution_m": 38.99, "time_resolution_m_E": 0.0,
                                                 "time_resolution_g": 53.14, "time_resolution_g_E": 0.0,
                                                 "jitter": 0.0,
                                                 "jitter_m": 0.0,
                                                 "jitter_g": 0.0,
                                                 "amp_max": 0.0 , "max_amp_E": 0.0,
                                                 "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
                                                 "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
                                                 "rise_time": 0.0, "rise_time_E": 0.0,
                                                 "rise_time_m": 0.0, "rise_time_n_E": 0.0,
                                                 "rise_time_g": 0.0, "rise_time_g_E": 0.0,
                                                 "baseline_rms": 0.0 , "baseline_rms": 0.0,
                                                 "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
                                                 "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
                                                 "charge": 0.0, "charge_E":0.0,
                                                 "charge_m": 0.0, "charge_m_E":0.0,
                                                 "charge_g": 0.0, "charge_g_E":0.0,
                                                },


    "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
                                                'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                                'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                                'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                                "time_resolution": 41.22, "time_resolution_E": 0.0,
                                                "time_resolution_m": 40.27, "time_resolution_m_E": 0.0,
                                                "time_resolution_g": 42.82, "time_resolution_g_E": 0.0,
                                                "jitter": 38.36,
                                                "jitter_m": 36.58,
                                                "jitter_g": 38.81,
                                                "amp_max": 57.88 , "max_amp_E": 0.0,
                                                "amp_max_m": 66.12 , "max_amp_m_E": 0.0,
                                                "amp_max_g": 49.67 , "max_amp_g_E": 0.0,
                                                "rise_time": 628.99, "rise_time_E": 0.0,
                                                "rise_time_m": 614.6, "rise_time_n_E": 0.0,
                                                "rise_time_g": 652.93, "rise_time_g_E": 0.0,
                                                "baseline_rms": 1.9 , "baseline_rms_E": 0.0,
                                                "baseline_rms_m": 1.89 , "baseline_rms_m_E": 0.0,
                                                "baseline_rms_g": 1.9 , "baseline_rms_g_E": 0.0,
                                                "charge": 30.68, "charge_E":0.0,
                                                "charge_m": 34.60, "charge_m_E":0.0,
                                                "charge_g": 26.92, "charge_g_E":0.0,
                                                },


    "HPK_W8_17_2_50T_1P0_500P_50M_C600_206V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 'position_oneStripRMS': 0.00,
                                               'position_oneStrip_StdDev': 0.00,
                                               'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                               'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                               "time_resolution": 38.86, "time_resolution_E": 0.0,
                                               "time_resolution_m": 37.36, "time_resolution_m_E": 0.0,
                                               "time_resolution_g": 39.87, "time_resolution_g_E": 0.0,
                                               "jitter": 38.11,
                                               "jitter_m": 36.62,
                                               "jitter_g": 38.28,
                                               "amp_max": 49.94 , "max_amp_E": 0.0,
                                               "amp_max_m": 57.86 , "max_amp_m_E": 0.0,
                                               "amp_max_g": 42.48 , "max_amp_g_E": 0.0,
                                               "rise_time": 619.22, "rise_time_E": 0.0,
                                               "rise_time_m": 603.51, "rise_time_n_E": 0.0,
                                               "rise_time_g": 643.64, "rise_time_g_E": 0.0,
                                               "baseline_rms": 1.7 , "baseline_rms_E": 0.0,
                                               "baseline_rms_m": 1.69 , "baseline_rms_m_E": 0.0,
                                               "baseline_rms_g": 1.7 , "baseline_rms_g_E": 0.0,
                                               "charge": 11.57, "charge_E":0.0,
                                               "charge_m": 13.14, "charge_m_E":0.0,
                                               "charge_g": 10.5, "charge_g_E":0.0,
                                               },

    # "HPK_W8_17_2_50T_1P0_500P_50M_C600":,
    # "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V":,
    "HPK_W4_17_2_50T_1P0_500P_50M_C240_204V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
                                               'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                               'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                               'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                               "time_resolution": 36.01, "time_resolution_E": 0.0,
                                               "time_resolution_m": 34.94, "time_resolution_m_E": 0.0,
                                               "time_resolution_g": 36.94, "time_resolution_g_E": 0.0,
                                               "jitter": 34.26,
                                               "jitter_m": 33.26,
                                               "jitter_g": 34.37,
                                               "amp_max": 57.49 , "max_amp_E": 0.0,
                                               "amp_max_m": 66.26 , "max_amp_m_E": 0.0,
                                               "amp_max_g": 49.31 , "max_amp_g_E": 0.0,
                                               "rise_time": 625.48, "rise_time_E": 0.0,
                                               "rise_time_m": 611.92, "rise_time_n_E": 0.0,
                                               "rise_time_g": 644.22, "rise_time_g_E": 0.0,
                                               "baseline_rms": 1.77 , "baseline_rms_E": 0.0,
                                               "baseline_rms_m": 1.77 , "baseline_rms_m_E": 0.0,
                                               "baseline_rms_g": 1.76 , "baseline_rms_g_E": 0.0,
                                               "charge": 15.83, "charge_E":0.0,
                                               "charge_m": 17.60, "charge_m_E":0.0,
                                               "charge_g": 14.24, "charge_g_E":0.0,
                                               },
    
    "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
                                               'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                               'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                               'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                               "time_resolution": 34.54, "time_resolution_E": 0.0,
                                               "time_resolution_m": 32.17, "time_resolution_m_E": 0.0,
                                               "time_resolution_g": 35.04, "time_resolution_g_E": 0.0,
                                               "jitter": 25.11,
                                               "jitter_m": 20.39,
                                               "jitter_g": 24.76,
                                               "amp_max": 99.99 , "max_amp_E": 0.0,
                                               "amp_max_m": 128.58 , "max_amp_m_E": 0.0,
                                               "amp_max_g": 74.06 , "max_amp_g_E": 0.0,
                                               "rise_time": 650.37, "rise_time_E": 0.0,
                                               "rise_time_m": 621.87, "rise_time_n_E": 0.0,
                                               "rise_time_g": 685.18, "rise_time_g_E": 0.0,
                                               "baseline_rms": 1.94 , "baseline_rms_E": 0.0,
                                               "baseline_rms_m": 1.94 , "baseline_rms_m_E": 0.0,
                                               "baseline_rms_g": 1.93 , "baseline_rms_g_E": 0.0,
                                               "charge": 34.82, "charge_E":0.0,
                                               "charge_m": 42.31, "charge_m_E":0.0,
                                               "charge_g": 27.72, "charge_g_E":0.0,
                                               },
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600":,
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_188V":,
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_186V":,
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_192V":,
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_194V":,
    "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 'position_oneStripRMS': 0.00,
                                               'position_oneStrip_StdDev': 0.00,
                                               'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                               'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                               "time_resolution": 53.52, "time_resolution_E": 0.0,
                                               "time_resolution_m": 29.49, "time_resolution_m_E": 0.0,
                                               "time_resolution_g": 87.00, "time_resolution_g_E": 0.0,
                                               "jitter": 52.75,
                                               "jitter_m": 22.12,
                                               "jitter_g": 68.39,
                                               "amp_max": 34.23 , "max_amp_E": 0.0,
                                               "amp_max_m": 50.25 , "max_amp_m_E": 0.0,
                                               "amp_max_g": 23.76 , "max_amp_g_E": 0.0,
                                               "rise_time": 561.01, "rise_time_E": 0.0,
                                               "rise_time_m": 418.81, "rise_time_n_E": 0.0,
                                               "rise_time_g": 578.16, "rise_time_g_E": 0.0,
                                               "baseline_rms": 1.77 , "baseline_rms_E": 0.0,
                                               "baseline_rms_m": 1.77 , "baseline_rms_m_E": 0.0,
                                               "baseline_rms_g": 1.77 , "baseline_rms_g_E": 0.0,
                                               "charge": 15.71, "charge_E":0.0,
                                               "charge_m": 19.24, "charge_m_E":0.0,
                                               "charge_g": 12.37, "charge_g_E":0.0,
                                               },

    "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 
                                              'position_oneStripRMS': 0.00,
                                              'position_oneStrip_StdDev': 0.00,
                                              'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                              'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                              "time_resolution": 34.37, "time_resolution_E": 0.0,
                                              "time_resolution_m": 31.94, "time_resolution_m_E": 0.0,
                                              "time_resolution_g": 34.86, "time_resolution_g_E": 0.0,
                                              "jitter": 25.47,
                                              "jitter_m": 21.38,
                                              "jitter_g": 26.82,
                                              "amp_max": 92.08, "max_amp_E": 0.0,
                                              "amp_max_m": 117.72, "max_amp_m_E": 0.0,
                                              "amp_max_g": 68.98, "max_amp_g_E": 0.0,
                                              "rise_time": 651.77, "rise_time_E": 0.0,
                                              "rise_time_m": 625.00, "rise_time_n_E": 0.0,
                                              "rise_time_g": 683.51, "rise_time_g_E": 0.0,
                                              "baseline_rms": 1.85 , "baseline_rms_E": 0.0,
                                              "baseline_rms_m": 1.85 , "baseline_rms_m_E": 0.0,
                                              "baseline_rms_g": 1.85 , "baseline_rms_g_E": 0.0,
                                              "charge": 22.12, "charge_E":0.0,
                                              "charge_m": 26.48, "charge_m_E":0.0,
                                              "charge_g": 17.87, "charge_g_E":0.0,
                                              },

    "HPK_W9_14_2_20T_1P0_500P_100M_E600_112V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 
                                                'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                                'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                                'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                                "time_resolution": 47.15, "time_resolution_E": 0.0,
                                                "time_resolution_m": 30.44, "time_resolution_m_E": 0.0,
                                                "time_resolution_g": 53.0, "time_resolution_g_E": 0.0,
                                                "jitter": 48.53,
                                                "jitter_m": 26.44,
                                                "jitter_g": 76.63,
                                                "amp_max": 32.19, "max_amp_E": 0.0,
                                                "amp_max_m": 43.52, "max_amp_m_E": 0.0,
                                                "amp_max_g": 22.60, "max_amp_g_E": 0.0,
                                                "rise_time": 525.42, "rise_time_E": 0.0,
                                                "rise_time_m": 428.26, "rise_time_n_E": 0.0,
                                                "rise_time_g": 693.34, "rise_time_g_E": 0.0,
                                                "baseline_rms": 1.8 , "baseline_rms_E": 0.0,
                                                "baseline_rms_m": 1.8 , "baseline_rms_m_E": 0.0,
                                                "baseline_rms_g": 1.8 , "baseline_rms_g_E": 0.0,
                                                "charge": 11.13, "charge_E":0.0,
                                                "charge_m": 13.31, "charge_m_E":0.0,
                                                "charge_g": 8.67, "charge_g_E":0.0,
                                                },

    "HPK_KOJI_50T_1P0_80P_60M_E240_190V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
                                           'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                           'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                           'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                           "time_resolution": 31.41, "time_resolution_E": 0.0,
                                           "time_resolution_m":31.39 , "time_resolution_m_E": 0.0,
                                           "time_resolution_g": 31.47, "time_resolution_g_E": 0.0,
                                           "jitter": 23.19,
                                           "jitter_m": 23.16,
                                           "jitter_g": 21.37,
                                           "amp_max": 72.97, "max_amp_E": 0.0,
                                           "amp_max_m": 74.35, "max_amp_m_E": 0.0,
                                           "amp_max_g": 68.32, "max_amp_g_E": 0.0,
                                           "rise_time": 574.5, "rise_time_E": 0.0,
                                           "rise_time_m": 573.29, "rise_time_n_E": 0.0,
                                           "rise_time_g": 578.81, "rise_time_g_E": 0.0,
                                           "baseline_rms": 1.83 , "baseline_rms_E": 0.0,
                                           "baseline_rms_m": 1.83 , "baseline_rms_m_E": 0.0,
                                           "baseline_rms_g": 1.82 , "baseline_rms_g_E": 0.0,
                                           "charge": 16.93, "charge_E":0.0,
                                           "charge_m": 17.19, "charge_m_E":0.0,
                                           "charge_g": 16.01, "charge_g_E":0.0,
                                           },

    "HPK_KOJI_20T_1P0_80P_60M_E240_112V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
                                           'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
                                           'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
                                           'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
                                           "time_resolution": 29.91, "time_resolution_E": 0.0,
                                           "time_resolution_m": 29.9, "time_resolution_m_E": 0.0,
                                           "time_resolution_g": 29.55, "time_resolution_g_E": 0.0,
                                           "jitter": 32.0,
                                           "jitter_m": 31.84,
                                           "jitter_g": 32.45,
                                           "amp_max": 38.44, "max_amp_E": 0.0,
                                           "amp_max_m": 39.1, "max_amp_m_E": 0.0,
                                           "amp_max_g": 35.13, "max_amp_g_E": 0.0,
                                           "rise_time": 419.34, "rise_time_E": 0.0,
                                           "rise_time_m": 415.8, "rise_time_n_E": 0.0,
                                           "rise_time_g": 430.75, "rise_time_g_E": 0.0,
                                           "baseline_rms": 1.76 , "baseline_rms_E": 0.0,
                                           "baseline_rms_m": 1.76 , "baseline_rms_m_E": 0.0,
                                           "baseline_rms_g": 1.76 , "baseline_rms_g_E": 0.0,
                                           "charge": 11.82, "charge_E":0.0,
                                           "charge_m": 12.04, "charge_m_E":0.0,
                                           "charge_g": 10.97, "charge_g_E":0.0,
                                           },
}

resolutions2023OneStripChannel = {
"BNL_50um_1cm_450um_W3051_2_2_170V": {  'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                        'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_50um_1cm_400um_W3051_1_4_160V": {  'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                        'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_50um_1cm_450um_W3052_2_4_185V": {  'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                        'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_20um_1cm_400um_W3074_1_4_95V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                        'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_20um_1cm_400um_W3075_1_2_80V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                        'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_20um_1cm_450um_W3074_2_1_95V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                        'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_20um_1cm_450um_W3075_2_4_80V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                        'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                                'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                                'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_20um_500x500um_2x2pad_E600_FNAL_105V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                                'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_30um_500x500um_2x2pad_E600_FNAL_140V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                                'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_50um_500x500um_2x2pad_E600_FNAL_190V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                                'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit

"HPK_W8_18_2_50T_1P0_500P_100M_C600_208V": {'resOneStrip': [-1.00, 43.5, 44.3, 38.1, 40.6, 35.1, -1.00],  ## Std Dev
                                       'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": {'resOneStrip': [-1.00, 23.3, 25.0, 26.0, 26.2, 24.8, -1.00],  ## Std Dev
                                       'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_W4_17_2_50T_1P0_500P_50M_C240_204V": {'resOneStrip': [-1.00, 25.8, 25.9, 26.8, 24.7, 25.9, -1.00],  ## Std Dev
                                      'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_W5_17_2_50T_1P0_500P_50M_E600_190V": {'resOneStrip': [-1.00, 18.7, 19.2, 21.4, 21.6, 20.2, -1.00],  ## Std Dev
                                      'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_W9_15_2_20T_1P0_500P_50M_E600_114V": {'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                      'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_W2_3_2_50T_1P0_500P_50M_E240_180V": {'resOneStrip': [-1.00, 16.7, 15.4, 16.3, 16.3, 15.3, -1.00],  ## Std Dev
                                          'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_W9_14_2_20T_1P0_500P_100M_E600_112V": {'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                       'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_W9_15_4_20T_0P5_500P_50M_E600_110V": {'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                       'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_KOJI_50T_1P0_80P_60M_E240_190V": {'resOneStrip': [-1.00, 10.2, 10.3, 10.2, 10.3, 10.6, -1.00],  ## Std Dev
                                  'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_KOJI_20T_1P0_80P_60M_E240_112V": {'resOneStrip': [-1.00, 14.4, 11.8, 11.8, 12.2, 15.1, -1.00],  ## Std Dev
                                  'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
}


