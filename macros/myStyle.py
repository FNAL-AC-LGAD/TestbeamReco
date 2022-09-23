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
            i = 1
            while(os.path.exists(outdir2)):
                    outdir2 = outdir2[0:-2] + str(i) + outdir2[-1]
                    i+=1
            os.mkdir(outdir2)
    print(outdir2,"created.")
    return outdir2

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

def SensorInfoSmart(dataset):
    name ="Not defined"
    bias_voltage = "X"

    if GetGeometry(dataset):
        name = GetGeometry(dataset)['sensor']
        bias_voltage = GetBV(dataset)

    SensorInfo(name,bias_voltage,True,0.00)


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
    if sensorsGeom2022[RemoveBV(name)]:
        sensor_dict = sensorsGeom2022[RemoveBV(name)]
    else:
        print("Sensor not found")
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


### Sensors' information dictionaries
sensorsGeom2022 = { "EIC_W2_1cm_500up_300uw": {'sensor': "BNL 10-300", 'pitch': 500, 'stripWidth': 300, "BV": 240, "length": 10.0},
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

resolutions2022 = {
    "EIC_W2_1cm_500up_300uw_240V": {'position_oneStrip'  : 75.92, 'position_oneStrip_E': 0.18, 'position_oneStripRMS': 78.11,
                                    'position_twoStrip'  : 15.74, 'position_twoStrip_E': 0.08,
                                    'efficiency_oneStrip': 0.51, 'efficiency_twoStrip' : 0.49},
    "EIC_W1_1cm_500up_200uw_255V": {'position_oneStrip'  : 81.89, 'position_oneStrip_E': 0.08, 'position_oneStripRMS': 54.75,
                                    'position_twoStrip'  : 18.49, 'position_twoStrip_E': 0.02,
                                    'efficiency_oneStrip': 0.43, 'efficiency_twoStrip' : 0.57},
    "EIC_W2_1cm_500up_100uw_220V": {'position_oneStrip'  : 66.03, 'position_oneStrip_E': 0.10, 'position_oneStripRMS': 27.84,
                                    'position_twoStrip'  : 19.23, 'position_twoStrip_E': 0.02,
                                    'efficiency_oneStrip': 0.23, 'efficiency_twoStrip' : 0.77},
    "EIC_W1_2p5cm_500up_200uw_215V": {'position_oneStrip'  : 121.5, 'position_oneStrip_E': 0.10, 'position_oneStripRMS': 70.93,
                                      'position_twoStrip'  : 31.32, 'position_twoStrip_E': 0.12,
                                      'efficiency_oneStrip': 0.82, 'efficiency_twoStrip' : 0.18},
    "EIC_W1_0p5cm_500up_200uw_1_4_245V": {'position_oneStrip'  : 59.39, 'position_oneStrip_E': 0.08, 'position_oneStripRMS': 51.79,
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

