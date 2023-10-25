from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite, TF1, TList
import os
import EfficiencyUtils
import langaus
import optparse
import time
#from stripBox import getStripBox
import myStyle
import myFunctions as mf

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
marg = myStyle.GetMargin()


def fill_th1_amp_vs_axis(h1_fill, hist2d, ffit):
# Fill h1_fill histogram bin by bin from hist2d (which is amp vs axis)
    last_bin = int(h1_fill.GetXaxis().GetNbins())
    for i in range(1, last_bin + 1):

        tmpHist = hist2d.ProjectionY("py",i,i)
        myMean = tmpHist.GetMean()
        myRMS = tmpHist.GetRMS()

        value = myMean
        nEvents = tmpHist.GetEntries()

        # Make fit to obtain a better max amplitude value
        if(nEvents > 50):
            #use coarser bins when the signal is bigger
            if (myMean > 50):
                tmpHist.Rebin(5)
            else:
                tmpHist.Rebin(10)
            
            myLanGausFunction = ffit.fit(tmpHist, fitrange=(myMean-1*myRMS,myMean+3*myRMS))
            myMPV = myLanGausFunction.GetParameter(1)
            value = myMPV

            # For Debugging
            if (debugMode):
                cv = TCanvas("cv_debug","cv",1000,800)

                tmpHist.Draw("hist")
                myLanGausFunction.Draw("same")
                this_var = h1_fill.GetName().replace("amplitude_vs_", "")
                cv.SaveAs("%sq_PadCenter%s_%i.gif"%(outdir_q, this_var, i))
                msg_info = "Bin: %i (MPV = %.3f)"%(i, myMPV)
                print(msg_info)
                cv.Close()

        # Send to zero low populated bins (unwanted points)
        else:
            value = 0.0

        # Avoid negative values (just in case)
        if (value < 0.0):
            value = 0.0

        h1_fill.SetBinContent(i, value)


    return h1_fill

def findCenter(hist):
# Fit amp vs axis projection with a gaussian around max
    maxBin = hist.FindFirstBinAbove(0.999 * hist.GetMaximum())
    maxLoc = hist.GetBinCenter(maxBin)
    range_min = maxLoc - 0.4 * pitch/1000.
    range_max = maxLoc + 0.4 * pitch/1000.

    hname = hist.GetName()
    f1 = TF1("f1_%s"%(hname),"gaus",range_min,range_max)
    f1.SetParameter("Mean", maxLoc)
    hist.Fit(f1, "Q", "", range_min, range_max)

    fmean = f1.GetParameter("Mean")
    fsigma = f1.GetParameter("Sigma")
    print("Fit info of %s: Gauss center: %0.3f mm; Sigma: %0.3f mm;"%(hname, fmean, fsigma))

    return f1

def print_channel_info(list_position, indices, axis):
    # Position
    info_txt = " >> Position %s: {"%(axis.upper())
    for i, pos in enumerate(list_position):
        info_txt+= "{%s,%s}: %.3f, "%(indices[i][0], indices[i][1], pos)
    info_txt = "%s}"%(info_txt[:-2])
    print(info_txt)



# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")
options, args = parser.parse_args()

debugMode = options.debugMode

dataset = options.Dataset
outdir = myStyle.getOutputDir(dataset)
inputfile = TFile("%s%s_InitialAnalyzer.root"%(outdir,dataset)) 

if debugMode:
    outdir_q = myStyle.CreateFolder(outdir, "q_PadCenter/")

colors = myStyle.GetColors(True)

sensor_Geometry = myStyle.GetGeometry(dataset)
sensor = sensor_Geometry['sensor']
pitch  = sensor_Geometry['pitch']

indices = mf.get_existing_indices(inputfile, "amplitude_vs_xy_channel")

print("Setting up Langaus")
fit = langaus.LanGausFit()
print("Setup Langaus")

th1_amp_proj_vs = {"x": [], "y": []}
tf1_fit_vs = {"x": [], "y": []}
max_amp = {"x": 0.0, "y": 0.0}
for var, list_th1 in th1_amp_proj_vs.items():
    # Project th3 over x/y axis to get th2 with amp vs x/y
    for i, idx in enumerate(indices):
        section = "row" if var == "x" else "col"
        hname = "amplitude_vs_xy_%s_channel%s"%(section, idx)
        th3_amp_vs_xy_channel = inputfile.Get(hname)

        th2_amp_vs_axis = th3_amp_vs_xy_channel.Project3D("z%s"%(var))

        # Create empty hist
        htemp = th2_amp_vs_axis.ProjectionX().Clone("htemp")
        nbin = htemp.GetXaxis().GetNbins()
        xmin = htemp.GetXaxis().GetXmin()
        xmax = htemp.GetXaxis().GetXmax()

        # Fill th1 projection with amp values
        hname_temp = "amplitude_vs_%s_channel%s"%(var, idx)
        th1_amp_vs_axis = TH1F(hname_temp, "", nbin, xmin, xmax)
        th1_amp_vs_axis = fill_th1_amp_vs_axis(th1_amp_vs_axis, th2_amp_vs_axis, fit)

        th1_amp_vs_axis.SetLineWidth(2)
        th1_amp_vs_axis.SetLineColor(colors[i])

        tf1_fit = findCenter(th1_amp_vs_axis)
        tf1_fit.SetLineColor(colors[i])

        # Save histogram and fit
        list_th1.append(th1_amp_vs_axis)
        tf1_fit_vs[var].append(tf1_fit)

        # Get maximum amplitude registered
        max_value = th1_amp_vs_axis.GetMaximum()
        if max_value > max_amp[var]:
            max_amp[var] = max_value
    # Add a space in output line
    print()

canvas = TCanvas("cv","cv",1000,800)

for var, list_th1 in th1_amp_proj_vs.items():
    canvas.Clear()
    axis_temp = list_th1[0].GetXaxis()
    htemp = TH1F("htemp_%s"%var, "", 1, axis_temp.GetXmin(), axis_temp.GetXmax())
    htemp.SetStats(0)
    htemp.SetTitle("")
    htemp.GetXaxis().SetTitle("Track %s position [mm]"%var)
    htemp.GetYaxis().SetTitle("MPV signal amplitude [mV]")
    # htemp.SetLineWidth(2)
    htemp.SetMaximum(1.5 * max_amp[var])

    # Create legend
    legend = TLegend(2*marg + 0.02, 1-marg-0.02-0.2, 1-marg-0.02, 1-marg-0.02)
    legend.SetNColumns(3)
    legend.SetTextFont(myStyle.GetFont())
    legend.SetTextSize(myStyle.GetSize())
    legend.SetBorderSize(0)
    legend.SetFillColor(kWhite)

    # Save center positions to get final output line
    list_position = []

    htemp.Draw("AXIS")
    for i, th1_vs_axis in enumerate(list_th1):
        th1_vs_axis.Draw("hist same")
        legend.AddEntry(th1_vs_axis, "Channel %s"%(indices[i]))

        this_fit = tf1_fit_vs[var][i]
        this_fit.Draw("same")

        list_position.append(this_fit.GetParameter("Mean"))

    legend.Draw()

    myStyle.BeamInfo()
    myStyle.SensorInfoSmart(dataset)

    canvas.SaveAs("%sAmplitude_vs_%s-%s.pdf"%(outdir, var, sensor))

    print_channel_info(list_position, indices, var)
