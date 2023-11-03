from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TH1D,TH2D,TLatex,TMath,\
    TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle
import os
import optparse
import myStyle
import langaus
import myFunctions as mf

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)
colors = myStyle.GetColors(True)

## Defining Style
myStyle.ForceStyle()
marginR = 3 * myStyle.GetMargin()
myStyle.ChangeMargins(mright=marginR)


class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, yMax=30.0, zmin=0.0, zmax=100.0,
                 xlabel="Track x position [mm]", ylabel="Track y position [mm]",
                 zlabel="", sensor="", center_position=0.0):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.yMax = yMax
        self.zmin = zmin
        self.zmax = zmax
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.zlabel = zlabel
        self.sensor = sensor
        self.center_position = center_position
        self.th3 = self.getTH3(f, inHistoName, sensor)
        self.th2 = self.getTH2(outHistoName)

    def getTH3(self, f, name, sensor):
        th3 = f.Get(name)

        # # Rebin low statistics sensors
        # if sensor=="BNL2020":
        #     th2.RebinX(5)
        # elif sensor=="BNL2021":
        #     th2.RebinX(10)
        # # if "1cm_500up_300uw" in sensor:
        # #     th2.RebinX(2)

        return th3

    def getTH2(self, hname):
        htitle = ";%s;%s;%s"%(self.xlabel, self.ylabel, self.zlabel)
        th2 = self.th3.Project3D("yx").Clone(hname)
        th2.SetTitle(htitle)

        th2.SetStats(0)
        th2.SetMinimum(self.zmin)
        th2.SetMaximum(self.zmax)

        # nxbin = self.th2.GetXaxis().GetNbins()
        # xmin, xmax = mf.get_shifted_limits(self.th2, self.center_position)
        # # Create and define th1 default style
        # th1 = TH1D(hname, htitle, nxbin, xmin, xmax)
        # # th1.SetStats(0)
        # th1.SetMinimum(0.0001)
        # th1.SetMaximum(self.yMax)
        # # th1.SetLineWidth(3)
        # # th1.SetLineColor(kBlack)
        # # # th1.GetXaxis().SetRangeUser(-xlength,xlength)

        return th2


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-z','--zmin', dest='zmin', default =   0.0, help="Set min Amp value in final plot")
parser.add_option('-Z','--zmax', dest='zmax', default = 120.0, help="Set max Amp value in final plot")
# parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")
parser.add_option('-t', dest='useTight', action='store_true', default = False, help="Use tight cut for pass")
options, args = parser.parse_args()

dataset = options.Dataset
outdir = myStyle.getOutputDir(dataset)
inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']

zmin = float(options.zmin)
zmax = float(options.zmax)
# debugMode = options.debugMode

is_tight = options.useTight

# # Get position of the central channel in the "x" direction
# position_center = mf.get_central_channel_position(inputfile, "x")

outdir = myStyle.GetPlotsDir(outdir, "Amplitude/")

# Save list with histograms to draw
list_htitles = [
    # [hist_input_name, short_output_name, y_axis_title]
    ["amplitude_vs_xy", "Amplitude", "MPV signal amplitude [mV]"],
    ["amplitudeDefault_vs_xy", "AmplitudeDefault", "MPV signal amplitude [mV]"],
]

# TODO: Add per channel plots
# indices = mf.get_existing_indices(inputfile, "amplitude_vs_xy_channel")
# for index in indices:
#     channel_element = ["amplitude_vs_xy_channel%s"%index, "deltaX_oneStripCh%s"%index, "tracker"]
#     list_htitles.append(channel_element)

# Use tight cut histograms
if (is_tight):
    print(" >> Using tight cuts!")
    for titles in list_htitles:
        titles[0]+= "_tight"

# List with histograms using HistoInfo class
all_histoInfos = []
for titles in list_htitles:
    hname, outname, ztitle = titles
    info_obj = HistoInfo(hname, inputfile, outname, zmin=zmin, zmax=zmax, zlabel=ztitle,
                         sensor=dataset) #, center_position=position_center)
    all_histoInfos.append(info_obj)

canvas = TCanvas("cv","cv",1000,800)
# canvas.SetGrid(0,1)
gStyle.SetOptStat(0)

# if debugMode:
#     outdir_q = myStyle.CreateFolder(outdir, "q_AmpVsXY0/")

# Get total number of bins in x-axis to loop over (all hists have the same number, in principle)
nXbins = all_histoInfos[0].th3.GetXaxis().GetNbins()
nYbins = all_histoInfos[0].th3.GetYaxis().GetNbins()

print("Setting up Langaus")
fit = langaus.LanGausFit()
print("Setup Langaus")

# Loop over X/Y bins
for i in range(1, nXbins+1):
    for j in range(1, nYbins+1):
        for info_entry in all_histoInfos:
            tmpHist = info_entry.th3.ProjectionZ("pz",i,i,j,j)
            myMean = tmpHist.GetMean()
            myRMS = tmpHist.GetRMS()
            value = myMean

            # #Do Langaus fit if histogram mean is larger than 10
            # #and mean is larger than RMS (a clear peak away from noise)
            # if (myMean > 10 and myMean > 0.5*myRMS):
            #     #use coarser bins when the signal is bigger
            #     if (myMean > 50):
            #         tmpHist.Rebin(10)
            #     else:
            #         tmpHist.Rebin(5)

            #     #myLanGausFunction = fit.fit(tmpHist, fitrange=(myMean-2*myRMS,myMean+3*myRMS))
            #     #myMPV = myLanGausFunction.GetParameter(1)
            #     #value = myMPV

            #     ##For Debugging
            #     #tmpHist.Draw("hist")
            #     #myLanGausFunction.Draw("same")
            #     #canvas.SaveAs(outdir+"q_"+str(i)+"_"+str(j)+".gif")

            info_entry.th2.SetBinContent(i,j, value)

# Define output file
output_path = "%sAmplitudeVsXY"%(outdir)
if (is_tight):
    output_path+= "_tight"
output_path+= ".root"

outputfile = TFile(output_path,"RECREATE")

for i,info_entry in enumerate(all_histoInfos):
    hist = info_entry.th2
    hist.Draw("colz")
    hist.Write()

    # myStyle.BeamInfo()
    myStyle.SensorInfoSmart(dataset)

    save_path = "%s%s_vs_xy"%(outdir, info_entry.outHistoName)
    if (is_tight):
        save_path+= "-tight"
    canvas.SaveAs("%s.gif"%save_path)
    canvas.SaveAs("%s.pdf"%save_path)

    canvas.Clear()

outputfile.Close()
