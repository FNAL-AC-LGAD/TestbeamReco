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
marg = myStyle.GetMargin()

# Define functions
def fill_th1_amp_vs_axis(h1_fill, hist2d, ffit):
# Fill h1_fill histogram bin by bin from hist2d (which is amp vs axis)
    last_bin = int(h1_fill.GetXaxis().GetNbins())
    # Define variables to get max amplitude too
    amp_max, amp_pos = 0.0, 0.0
    for i in range(1, last_bin + 1):
        #print ("Bin " + str(i))

        ##For Debugging
        #if not (i==46):
        #    continue

        tmpHist = hist2d.ProjectionY("py",i,i)
        myTotalEvents=tmpHist.Integral()
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

            ##For Debugging
            #tmpHist.Draw("hist")
            #myLanGausFunction.Draw("same")
            #canvas.SaveAs(outdir+"q_"+str(i)+"_"+str(channel)+".gif")
        # Send to zero low populated bins (unwanted points)
        else:
            value = 0.0

        # Avoid negative values (just in case)
        if (value < 0.0):
            value = 0.0

        # Compute max amplitude
        if value > amp_max:
            amp_max = value
            amp_pos = h1_fill.GetXaxis().GetBinCenter(i)

        h1_fill.SetBinContent(i, value)
    
    # Print info about max amplitude
    print("Name: %s; Max amplitude = %0.2f mV in x position: %0.4f mm"%(h1_fill.GetName(), amp_max, amp_pos))

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
    print("%s; Gauss center: %0.3f mm, sigma: %0.3f mm"%(hname, fmean, fsigma))
    return f1

def print_channels_distance(list_distances):
    str_out = "\n  List of distance between centers in mm: ["
    for dist in list_distances:
        str_out+= "%.2f, "%dist
    # Remove last characters
    str_out = "%s]"%str_out[:-2]

    print(str_out)
    return str_out

def print_channels_position(list_positions):
    str_out = "\n  Position of channels = {"
    for p, pos in enumerate(list_positions):
        # Get row and column str values from list, saved as two chars
        row, col = list_channel_coord[p]
        str_out+= "{%s, %s}: %.3f; "%(row, col, pos)
    # Remove last characters
    str_out = "%s}\n"%str_out[:-2]

    print(str_out)
    return str_out


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()

dataset = options.Dataset
outdir=""
outdir = myStyle.getOutputDir(dataset)
inputfile = TFile("%s%s_InitialAnalyzer.root"%(outdir,dataset)) 

colors = myStyle.GetColors(True)

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch  = sensor_Geometry['pitch']

# Retrieve all channels of interest
list_channel_coord = []
list_th2_amplitude_vs_x = []
list_th2_amplitude_vs_y = []
# th3_amplitude_vs_xy_channels =[]
for i in range(7):
    for j in range(7):
        hname = "amplitude_vs_xy_channel%i%i"%(i,j)
        th3_amp_vs_xy_channel = inputfile.Get(hname)
        if th3_amp_vs_xy_channel:
            # th3_amplitude_vs_xy_channels.append(th3_amp_vs_xy_channel)
            # Project over zx, i.e. integrate y
            amp_vs_x_channel = th3_amp_vs_xy_channel.Project3D("zx")
            list_th2_amplitude_vs_x.append(amp_vs_x_channel)
            # Project over zy, i.e. integrate x
            amp_vs_y_channel = th3_amp_vs_xy_channel.Project3D("zy")
            list_th2_amplitude_vs_y.append(amp_vs_y_channel)

            list_channel_coord.append("%i%i"%(i,j))
        else:
            break

#Build amplitude vs x reference histograms
htmp_x = amp_vs_x_channel.ProjectionX().Clone("htmp_x")
xnbin = htmp_x.GetXaxis().GetNbins()
xmin = htmp_x.GetXaxis().GetXmin()
xmax = htmp_x.GetXaxis().GetXmax()

#Build amplitude vs y reference histograms
htmp_y = amp_vs_y_channel.ProjectionX().Clone("htmp_y")
ynbin = htmp_y.GetXaxis().GetNbins()
ymin = htmp_y.GetXaxis().GetXmin()
ymax = htmp_y.GetXaxis().GetXmax()

print("Setting up Langaus")
fit = langaus.LanGausFit()
print("Setup Langaus")
canvas = TCanvas("cv","cv",1000,800)

# Create and save filled amplitude histograms
list_amplitude_vs_x = []
list_amplitude_vs_y = []
for c, coord in enumerate(list_channel_coord):
    xhname = "amplitude_vs_x_channel%s"%(coord)
    hamp_vs_x = TH1F(xhname, "", xnbin, xmin, xmax)
    hamp_vs_x = fill_th1_amp_vs_axis(hamp_vs_x, list_th2_amplitude_vs_x[c], fit)
    list_amplitude_vs_x.append(hamp_vs_x)

    yhname = "amplitude_vs_y_channel%s"%(coord)
    hamp_vs_y = TH1F(yhname, "", ynbin, ymin, ymax)
    hamp_vs_y = fill_th1_amp_vs_axis(hamp_vs_y, list_th2_amplitude_vs_y[c], fit)
    list_amplitude_vs_y.append(hamp_vs_y)
            
# Define style of histograms and fit curves
list_fit_functions_x = []
list_fit_functions_y = []
amp_max_x, amp_max_y = 0.0, 0.0
for c, coord in enumerate(list_channel_coord):
    # Save max value in amp vs x
    hamp_vs_x = list_amplitude_vs_x[c]
    if hamp_vs_x.GetMaximum() > amp_max_x:
        amp_max_x = hamp_vs_x.GetMaximum()

    list_fit_functions_x.append(findCenter(hamp_vs_x))
    hamp_vs_x.SetLineWidth(2)
    hamp_vs_x.SetLineColor(colors[c])
    list_fit_functions_x[c].SetLineColor(colors[c])

    # Save max value in amp vs y
    hamp_vs_y = list_amplitude_vs_y[c]
    if hamp_vs_y.GetMaximum() > amp_max_y:
        amp_max_y = hamp_vs_y.GetMaximum()
    
    list_fit_functions_y.append(findCenter(hamp_vs_y))
    hamp_vs_y.SetLineWidth(2)
    hamp_vs_y.SetLineColor(colors[c])
    list_fit_functions_y[c].SetLineColor(colors[c])


## Draw x canvas
canvas.Clear()
htmp_x = TH1F("htemp_x", "", 1, xmin, xmax)
htmp_x.Draw("hist")
htmp_x.SetStats(0)
htmp_x.SetTitle("")
htmp_x.GetXaxis().SetTitle("Track x position [mm]")
htmp_x.GetYaxis().SetTitle("MPV signal amplitude [mV]")
# htmp_x.SetLineWidth(2)
htmp_x.SetMaximum(1.5 * amp_max_x)

legend_x = TLegend(2*marg + 0.02, 1-marg-0.02-0.2, 1-marg-0.02, 1-marg-0.02)
legend_x.SetNColumns(3)
legend_x.SetTextFont(myStyle.GetFont())
legend_x.SetTextSize(myStyle.GetSize())
legend_x.SetBorderSize(0)
legend_x.SetFillColor(kWhite)

# Extract position of each channel and their distance
list_position_x = []
list_distance_x = []

htmp_x.Draw("AXIS same")
for c, coord in enumerate(list_channel_coord):
    list_amplitude_vs_x[c].Draw("hist same")
    list_fit_functions_x[c].Draw("same")
    legend_x.AddEntry(list_amplitude_vs_x[c], "Channel %s"%coord)

    # Get position and distance
    position = list_fit_functions_x[c].GetParameter("Mean")
    if list_position_x:
        prev_position = list_position_x[-1]
        list_distance_x.append(position - prev_position)
    list_position_x.append(position)
legend_x.Draw()

myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

canvas.SaveAs("%sAmplitude_vs_x-%s.gif"%(outdir, sensor))
# canvas.SaveAs("%sAmplitude_vs_x-%s.pdf"%(outdir, sensor))


## Draw y canvas
canvas.Clear()
htmp_y = TH1F("htemp_y", "", 1, ymin, ymax)
htmp_y.Draw("hist")
htmp_y.SetStats(0)
htmp_y.SetTitle("")
htmp_y.GetXaxis().SetTitle("Track y position [mm]")
htmp_y.GetYaxis().SetTitle("MPV signal amplitude [mV]")
# htmp_y.SetLineWidth(2)
htmp_y.SetMaximum(1.5 * amp_max_y)

legend_y = TLegend(2*marg + 0.02, 1-marg-0.02-0.2, 1-marg-0.02, 1-marg-0.02)
legend_y.SetNColumns(3)
legend_y.SetTextFont(myStyle.GetFont())
legend_y.SetTextSize(myStyle.GetSize())
legend_y.SetBorderSize(0)
legend_y.SetFillColor(kWhite)

# Extract position of each channel and their distance
list_position_y = []
list_distance_y = []

htmp_y.Draw("AXIS same")
for c, coord in enumerate(list_channel_coord):
    list_amplitude_vs_y[c].Draw("hist same")
    list_fit_functions_y[c].Draw("same")
    legend_y.AddEntry(list_amplitude_vs_y[c], "Channel %s"%coord)

    # Get position and distance
    position = list_fit_functions_y[c].GetParameter("Mean")
    if list_position_y:
        prev_position = list_position_y[-1]
        list_distance_y.append(position - prev_position)
    list_position_y.append(position)
legend_y.Draw()

myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

canvas.SaveAs("%sAmplitude_vs_y-%s.gif"%(outdir, sensor))
# canvas.SaveAs("%sAmplitude_vs_y-%s.pdf"%(outdir, sensor))

# Print output info
print("\n > Positions in Amplitude VS X")
print_channels_distance(list_distance_x)
print_channels_position(list_position_x)

print(" > Positions in Amplitude VS Y")
print_channels_distance(list_distance_y)
print_channels_position(list_position_y)

# Save amplitude histograms
outputfile = TFile("%sPlotAmplitudeVsXAndY.root"%(outdir),"RECREATE")

for c, coord in enumerate(list_channel_coord):
    list_amplitude_vs_x[c].Write()
    list_fit_functions_x[c].Write()
    list_amplitude_vs_y[c].Write()
    list_fit_functions_y[c].Write()
outputfile.Close()


