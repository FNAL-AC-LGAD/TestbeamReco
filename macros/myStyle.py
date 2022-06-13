import ROOT

## Define global variables
marg=0.05
font=43 # Helvetica
# tsize=32
tsize=38 #35

def getOutputDir(dataset):
    outdir = "../output/%s/" % dataset
    return outdir

def ForceStyle():
    ## Defining Style
    ROOT.gStyle.SetPadTopMargin(marg)    #0.05
    ROOT.gStyle.SetPadRightMargin(marg)  #0.05
    ROOT.gStyle.SetPadBottomMargin(2*marg)  #0.16
    ROOT.gStyle.SetPadLeftMargin(2*marg)   #0.16

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

def SensorInfo(sensor="Name", bias_voltage="X", write_bv=True,adjustleft=0):
    text = ROOT.TLatex()
    text.SetTextSize(tsize-4)
    text.SetTextAlign(31)
    if write_bv: text.DrawLatexNDC(1-marg-0.005-adjustleft,1-marg+0.01,"#bf{"+str(sensor) + ", "+str(bias_voltage)+"V}")
    else: text.DrawLatexNDC(1-marg-0.005-adjustleft,1-marg+0.01,"#bf{"+str(sensor)+"}")

def SensorInfoSmart(dataset):
    sensor ="Not defined"
    bias_voltage = "X"

    if dataset=="EIC_W1_1cm_255V":
        sensor = "EIC W1 1 cm, 300 um gaps"
        bias_voltage = "255"

    if dataset=="EIC_W1_0p5cm_500um_300um_gap_1_7_240V":
        sensor = "EIC W1 0.5 cm, 300 um gaps (1_7)"
        bias_voltage = "240"

    if dataset=="EIC_W1_0p5cm_500um_300um_gap_1_4_245V":
        sensor = "EIC W1 0.5 cm, 300 um gaps (1_4)"
        bias_voltage = "245"

    if dataset=="EIC_W1_2p5cm_UCSC_330V":
        sensor = "EIC W1 2.5 cm, 300 um gaps, UCSC"
        bias_voltage = "330"

    if dataset=="EIC_W2_1cm_500um_400um_gap_220V" or dataset=="EIC_W2_1cm_500um_400um_gap_220V_628":
        sensor = "EIC W2 1 cm, 400 um gaps"
        bias_voltage ="220"

    if dataset=="EIC_W1_2p5cm_215V":
        sensor = "EIC W1 2.5 cm, 300 um gaps"
        bias_voltage = "215"


    SensorInfo(sensor,bias_voltage,True,0.08)

def GetMargin():
    return marg

def GetFont():
    return font

def GetSize():
    return tsize

def GetPadCenter():
    return (1 + marg)/2

def GetColors(color_blind = False):
    strip_colors = [416+2, 432+2, 600, 880, 632, 400+2, 600-5]
    ## [#kGreen+2, #kCyan+2, #kBlue, #kViolet, #kRed, #kYellow+2, #kBlue-3]
    if color_blind:
        color_RGB = [[51,34,136],[51,187,238],[17,119,51],[153,153,51],[204,102,119],[136,34,85],[128,128,128]]
        # [indigo, cyan, green, olive, rose, wine]
        
        for i in range(0,len(strip_colors)):
            strip_colors[i] = ROOT.TColor.GetColor(color_RGB[i][0],color_RGB[i][1],color_RGB[i][2])

    return strip_colors

def GetGeometry(name):
    sensor_dict = {}
    if sensorsGeom2022[name]:
        sensor_dict = sensorsGeom2022[name]
    else:
        print("Sensor not found")
    return sensor_dict


sensorsGeom2022 = { "EIC_W2_1cm_500um_200um_gap_240V": {'sensor': "EIC_W2_1cm_500up_300uw", 'pitch': 500, 'stripWidth': 300, "BV": 240, "length": 10.0},
                    "EIC_W1_1cm_255V": {'sensor': "EIC_W1_1cm_500up_200uw", 'pitch': 500, 'stripWidth': 200, "BV": 255, "length": 10.0},
                    "EIC_W2_1cm_500um_400um_gap_220V": {'sensor': "EIC_W2_1cm_500up_100uw", 'pitch': 500, 'stripWidth': 100, "BV": 220, "length": 10.0},
                    "EIC_W1_1cm_100_multiPitch_240V": {'sensor': "EIC_W1_1cm_100up_50uw", 'pitch': 100, 'stripWidth': 50, "BV": 240, "length": 10.0},
                    "EIC_W1_1cm_200_multiPitch_240V": {'sensor': "EIC_W1_1cm_200up_100uw", 'pitch': 200, 'stripWidth': 100, "BV": 240, "length": 10.0},
                    "EIC_W1_1cm_300_multiPitch_240V": {'sensor': "EIC_W1_1cm_300up_150uw", 'pitch': 300, 'stripWidth': 150, "BV": 240, "length": 10.0},
                    "EIC_W1_2p5cm_UCSC_330V": {'sensor': "EIC_W1_2p5cm_UCSC_500up_200uw", 'pitch': 500, 'stripWidth': 200, "BV": 330, "length": 25.0},
                    "EIC_W1_2p5cm_215V": {'sensor': "EIC_W1_2p5cm_500up_200uw", 'pitch': 500, 'stripWidth': 200, "BV": 215, "length": 25.0},
                    "HPK_strips_Eb_45um_170V": {'sensor': "HPK_Eb_80up_45uw", 'pitch': 80, 'stripWidth': 45, "BV": 170, "length": 10.0},
                    "EIC_W1_0p5cm_500um_300um_gap_1_7_240V": {'sensor': "EIC_W1_1_7_0p5cm_500up_200uw", 'pitch': 500, 'stripWidth': 200, "BV": 240, "length": 5.0},
                    "EIC_W1_0p5cm_500um_300um_gap_1_4_245V": {'sensor': "EIC_W1_1_4_0p5cm_500up_200uw", 'pitch': 500, 'stripWidth': 200, "BV": 245, "length": 5.0},
                    "BNL_500um_squares_175V": {'sensor': "BNL_squares_1cm_500up_300uw", 'pitch': 500, 'stripWidth': 100, "BV": 175},
                    "BNL2021_2022_medium_285V": {'sensor': "BNL2021_V2_1cm_150up_80uw", 'pitch': 150, 'stripWidth': 80, "BV": 285},
                    "IHEP_W1_I_185V": {'sensor': "IHEP_W1_I_1cm_150up_80uw", 'pitch': 150, 'stripWidth': 80, "BV": 185},
}
