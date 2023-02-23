from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite, TF1
import os
import EfficiencyUtils
import langaus
import optparse
import time
#from stripBox import getStripBox
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
organized_mode=True


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()

dataset = options.Dataset
outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_InitialAnalyzer.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")   

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch  = sensor_Geometry['pitch']

num_strips=8

colors = myStyle.GetColors(True)


def sanitize_profile2D(profile2D):

    for ix in range(profile2D.GetNbinsX()+1):
        for iy in range(profile2D.GetNbinsY()+1):
            ibin = profile2D.GetBin(ix,iy)
            if profile2D.GetBinContent(ibin) == 0:
                profile2D.SetBinError(ibin,0)
                continue
            if profile2D.GetBinEntries(ibin)<20 or profile2D.GetBinError(ibin)/profile2D.GetBinContent(ibin) > 0.2: 
                profile2D.SetBinContent(ibin,0)
                profile2D.SetBinError(ibin,0)


list_th2_amplitude_vs_x = []


profile_timeDiff_coarse_vs_xy_channels =[]



for i in range(num_strips):
    th3_timeDiff_coarse_vs_xy_channel = inputfile.Get("timeDiff_coarse_vs_xy_channel0%i"%i)
    
    this_profile = th3_timeDiff_coarse_vs_xy_channel.Project3DProfile("yx")

    sanitize_profile2D(this_profile)

    profile_timeDiff_coarse_vs_xy_channels.append(this_profile)


outputfile = TFile(outdir+"delayCorrections.root","RECREATE")

for hist in profile_timeDiff_coarse_vs_xy_channels: hist.Write()
outputfile.Close()

##### in code, get delay for channel like this: timeDiff_coarse_vs_xy_channel03_pyx->Interpolate(X_tracker,Y_tracker)