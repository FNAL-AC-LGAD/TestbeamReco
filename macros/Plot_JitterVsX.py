from ROOT import TFile,TTree,TCanvas,TH1F,TH1D,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gPad,gStyle, kWhite, TF1, TPaveStats
import langaus
from stripBox import getStripBox
import optparse
import myStyle
import myFunctions as mf

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)
colors = myStyle.GetColors(True)

## Defining Style
myStyle.ForceStyle()


class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, yMax=150,
                 xlabel="", ylabel="Amplitude [mV]",
                 sensor="", center_position = 0.0):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.yMax = yMax
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.sensor = sensor
        self.center_position = center_position
        if("KOJI" in sensor):
            self.th2 = self.getTH2(f, inHistoName, sensor).RebinX(2)
            print(" (!!) Using RebinX(2) to handle low stat bins!")
        else:
            self.th2 = self.getTH2(f, inHistoName, sensor)
        self.th1 = self.getTH1(outHistoName)

    def getTH2(self, f, name, sensor, axis='zx'):
        th3 = f.Get(name)
        th2 = th3.Project3D(axis)

        return th2

    def getTH1(self, hname):
        htitle = ";%s;%s"%(self.xlabel, self.ylabel)
        nxbin = self.th2.GetXaxis().GetNbins()
        xmin, xmax = mf.get_shifted_limits(self.th2, self.center_position)

        # Create and define th1 default style
        th1 = TH1D(hname, htitle, nxbin, xmin, xmax)
        # th1.SetStats(0)
        th1.SetMinimum(0.1)
        th1.SetMaximum(self.yMax)
        # th1.SetLineWidth(3)
        # th1.SetLineColor(kBlack)
        # # th1.GetXaxis().SetRangeUser(-xlength,xlength)

        return th1


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 2.5, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 100, help="Max jitter value in final plot")
parser.add_option('-m', dest='minCut_user', default = 1000.0, help="Minimum events requirement")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")
parser.add_option('-t', dest='useTight', action='store_true', default = False, help="Use tight cut for pass")
options, args = parser.parse_args()

dataset = options.Dataset
outdir = myStyle.getOutputDir(dataset)
inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch = sensor_Geometry['pitch']

minCut_user = float(options.minCut_user)
fit = langaus.LanGausFit()
xlength = float(options.xlength)
ylength = float(options.ylength)
debugMode = options.debugMode

is_tight = options.useTight

# Get position of the central channel in the "x" direction
position_center = mf.get_central_channel_position(inputfile, "x")

outdir = myStyle.GetPlotsDir(outdir, "Jitter/")

# Save list with histograms to draw
list_overall_htitles = [
    # [hist_input_name, short_output_name, y_axis_title]
    ["weighted2_jitter_vs_xy", "jitter_vs_x", "MPV signal amplitude [mV]"],
]

# Use tight cut histograms
if (is_tight):
    print(" >> Using tight cuts!")
    for titles in list_overall_htitles:
        titles[0]+= "_tight"

# List with histograms using HistoInfo class
all_histoInfos = []
for titles in (list_overall_htitles):
    hname, outname, ytitle = titles
    if not (inputfile.Get(hname)):
        print(" >> Histogram %s does not exist! Skipping."%hname)
        continue
    info_obj = HistoInfo(hname, inputfile, outname, yMax=ylength, ylabel=ytitle,
                         sensor=dataset, center_position=position_center)
    all_histoInfos.append(info_obj)

canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
gStyle.SetOptStat(0)

if debugMode:
    outdir_q = myStyle.CreateFolder(outdir, "Jitter_vs_X_fits0/")

nbins = all_histoInfos[0].th2.GetXaxis().GetNbins()

plot_xlimit = abs(inputfile.Get("stripBoxInfo00").GetMean(1) - position_center)
if ("pad" not in dataset) and ("500x500" not in dataset):
    plot_xlimit-= pitch/(2. * 1000)

print("Setting up Langaus")
fit = langaus.LanGausFit()
print("Setup Langaus")

# Loop over X bins
for i in range(1, nbins+1):
    for info_entry in all_histoInfos:
        totalEvents = info_entry.th2.GetEntries()
        tmpHist = info_entry.th2.ProjectionY("py",i,i)
        myTotalEvents=tmpHist.Integral()
        myRMS = tmpHist.GetRMS()
        myMean = tmpHist.GetMean()
        nEvents = tmpHist.GetEntries()
        value = myMean
	# Add empty error for the moment
        error = 0.0

        # Define minimum of bin's entries to be fitted
        minEvtsCut = myTotalEvents/nbins
        # if("20T" in dataset):
        #     minEvtsCut = 0.3*totalEvents/nbins
        if(is_tight):
            minEvtsCut = 0
        if (i == 1):
            msg_nentries = "%s: nEvents > %.2f "%(info_entry.inHistoName, minEvtsCut)
            msg_nentries+= "(Total events: %i)"%(totalEvents)
            print(msg_nentries)


        if(nEvents>minCut_user):
            tmpHist.Rebin(2)
            myLanGausFunction = fit.fit(tmpHist, fitrange=(myMean-1.5*myRMS,myMean+3*myRMS))
            myMPV = myLanGausFunction.GetParameter(1)
            value = myMPV
	    # gaussian = TF1("gaussian", "gaus")
            # gaussian.SetRange(myMean-2*myRMS,myMean+2*myRMS)
            # tmpHist.Fit(gaussian, "R")
            # myMean = gaussian.GetParameter(1)
            # mySigma = gaussian.GetParameter(2)
            # value = myMean

            # ##For Debugging Gaussian
            # tmpHist.Draw("hist")
            # gaussian.Draw("same")
            # outdir_tmp = myStyle.GetPlotsDir(outdir, "jitter_x_fits/")
            # canvas.SaveAs(outdir_tmp+"q_"+str(i)+".gif")
            #For Debugging Landau
            if(debugMode):
                tmpHist.Draw("hist")
                myLanGausFunction.Draw("same")
                canvas.SaveAs("%sq_%s%i.gif"%(outdir_q, info_entry.outHistoName, i))
                bin_center = info_entry.th1.GetXaxis().GetBinCenter(i)
                msg_amp = "Bin: %i (x center = %.3f)"%(i, bin_center)
                # msg_amp+= " -> Amplitude: %.3f mV"%(value)
                msg_amp+= " -> Entries: %.3f"%(tmpHist.GetEntries())
                print(msg_amp)
        else:
            value = 0.0
            error = 0.0

        value = value if (value>0.0) else 0.0

        # Fill only when inside limits
        if not mf.is_inside_limits(i, info_entry.th1, xmax=plot_xlimit):
            continue

        info_entry.th1.SetBinContent(i, value)
        info_entry.th1.SetBinError(i, error)

# Define output file
output_path = "%sJitterVsX"%(outdir)
if (is_tight):
    output_path+= "_tight"
output_path+= ".root"

outputfile = TFile(output_path,"RECREATE")

# Define hist for axes style
htemp = TH1F("htemp", "", 1, -xlength, xlength)
htemp.SetStats(0)
htemp.GetXaxis().SetTitle("Track x position [mm]")
htemp.GetYaxis().SetRangeUser(0.0, ylength)
htemp.GetYaxis().SetTitle("Weighted jitter [ps]")
htemp.SetLineColor(colors[2])

# Draw overall amplitude vs X
for i,info_entry in enumerate(all_histoInfos):
    hist = info_entry.th1
    hist.SetLineColor(colors[0])
    hist.SetLineWidth(2)

    ymin = hist.GetMinimum()
    ymax = hist.GetMaximum()

    haxis = htemp.Clone()
    haxis.SetMinimum(ymin)
    haxis.SetMaximum(ymax)

    haxis.Draw("AXIS")
    # Define and draw gray bars in the background (Position of metallic sections)
    boxes = getStripBox(inputfile, ymin=ymin, ymax=ymax, strips=True,
                        shift=position_center, pitch=pitch/1000.)
    for box in boxes:
        box.Draw()
    gPad.RedrawAxis("g")

    hist.Draw("hist e same")

    hist.Write()

    haxis.Draw("AXIS same")
    # legend.Draw()

    myStyle.BeamInfo()
    myStyle.SensorInfoSmart(dataset)

    save_path = "%s%s"%(outdir, info_entry.outHistoName)
    if (is_tight):
        save_path+= "_tight"
    canvas.SaveAs("%s.gif"%save_path)
    canvas.SaveAs("%s.pdf"%save_path)

    canvas.Clear()

outputfile.Close()
