import ROOT
import os
import mySensorInfo as msi

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
    key_name = RemoveBV(name)

    sensor_dict = {}
    if (key_name in msi.sensorsGeom2022):
        sensor_dict = msi.sensorsGeom2022[key_name]
    elif (key_name in msi.sensorsGeom2023):
        sensor_dict = msi.sensorsGeom2023[key_name]
    else:
        print("(!!!) Sensor not found in any dictionary :(")

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

def GetResolutions(name, per_channel=False):
    key_name = RemoveBV(name)

    reference_dict2022 = msi.resolutions2022 if not per_channel else msi.resolutions2022OneStripChannel
    reference_dict2023 = msi.resolutions2023 if not per_channel else msi.resolutions2023OneStripChannel

    sensor_dict = {}
    if (key_name in reference_dict2022):
        sensor_dict = reference_dict2022[key_name]
    elif (key_name in reference_dict2023):
        sensor_dict = reference_dict2023[key_name]
    else:
        print("(!!!) Sensor not found in any dictionary :(")
        exit()

    return sensor_dict

