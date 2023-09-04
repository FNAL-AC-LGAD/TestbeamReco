from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TH1D,TH2D,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle
import os
import EfficiencyUtils
import langaus
import optparse
import time
from stripBox import getStripBox,getStripBoxY
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)
organized_mode=True

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.25)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 0, help="Bias Voltage value in [V]")
parser.add_option('-z','--zmin', dest='zmin', default =   0.0, help="Set min Amp value in final plot")
parser.add_option('-Z','--zmax', dest='zmax', default = 120.0, help="Set max Amp value in final plot")
parser.add_option('-p', dest='plot', default = "-1", help="Choose what to plot: amp(0), risetime(1), charge(2), amp/charge(3)")
options, args = parser.parse_args()

dataset = options.Dataset
zmin = float(options.zmin)
zmax = float(options.zmax)
what2plot = int(options.plot)

outdir=""
if organized_mode:
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")

sensor_Geometry = myStyle.GetGeometry(dataset)
sensor = sensor_Geometry['sensor']
bias   = sensor_Geometry['BV'] if options.biasvolt == 0 else options.biasvolt

outdir = myStyle.GetPlotsDir(outdir, "AmpCharge_XY/")

list_name3Dhist = ["amplitude_vs_xy", "risetime_vs_xy", "charge_vs_xy", "ampChargeRatio_vs_xy"]
list_namesOutput = ["Amplitude_vs_xy", "Risetime_vs_xy", "Charge_vs_xy", "AmpChargeRatio_vs_xy"]

z_limits = [[0.0,100.0], [0.0,1500.0], [0.0,150.0], [0.0,15.0]] # Default

if ("50um_1cm_450um" in dataset):
    z_limits = [[10.0,90.0], [400.0,1000.0], [1.0,30.0], [2.0,7.0]] # 50um_1cm
elif ("50um_2p5cm_mix" in dataset):
    z_limits = [[15.0,50.0], [400.0,1000.0], [1.0,15.0], [2.0,7.0]] # 2p5cm
elif ("20um_1cm_450um" in dataset):
    z_limits = [[15.0,35.0], [400.0,1000.0], [1.0,10.0], [2.0,7.0]] # 20um

# If you want to plot only one of the xy maps, or define a specific Z range for that one, use -p
if (what2plot != -1):
    list_name3Dhist = [list_name3Dhist[what2plot]]
    list_namesOutput = [list_namesOutput[what2plot]]
    z_limits = [z_limits[what2plot]]

#Get 3D histograms
channel_good_index = []
list_th3_vs_xy = []

for name3D in list_name3Dhist:
    list_good_ch_tmp = []
    list_th3_tmp = []
    for i in range(7):
        hname = "%s_channel0%i"%(name3D,i) # ex. "amplitude_vs_xy_channel0X"
        if inputfile.Get(hname):
            list_good_ch_tmp.append(i)
            list_th3_tmp.append(inputfile.Get(hname))

    # Add all channels first and the overall map at the end
    list_th3_tmp.append(inputfile.Get(name3D))

    channel_good_index.append(list_good_ch_tmp)
    list_th3_vs_xy.append(list_th3_tmp)


#Build amplitude histograms
# This only works if all histograms have the same XY binning! xyROI is used only to retrieve the nbins and axes limits
amplitude_th2_4binning = inputfile.Get("amplitude_vs_xyROI")
amplitude_vs_xy_temp = amplitude_th2_4binning.Project3D("yx")

# List of lists with all channels + overall map
list_XY_maps = []

for n,name3D in enumerate(list_name3Dhist):
    list_th2_tmp = []
    for i,ch in enumerate(channel_good_index[n]):
        list_th2_tmp.append(amplitude_vs_xy_temp.Clone("%s_channel0%i"%(name3D,ch)))

    list_th2_tmp.append(amplitude_vs_xy_temp.Clone(name3D))
    list_XY_maps.append(list_th2_tmp)


canvas = TCanvas("cv","cv",800,800)
fit = langaus.LanGausFit()

for i_name,this_list_XY in enumerate(list_XY_maps):
    # Run across X-bins. ROOT convention: bin 0 - underflow, nbins+1 - overflow bin
    for i in range(1, amplitude_vs_xy_temp.GetXaxis().GetNbins()+1):
        # Loop over Y-bins
        for j in range(1, amplitude_vs_xy_temp.GetYaxis().GetNbins()+1):
            for ch,this_xy in enumerate(this_list_XY):
                tmpHist = list_th3_vs_xy[i_name][ch].ProjectionZ("pz",i,i,j,j)
                myMean = tmpHist.GetMean()
                myRMS = tmpHist.GetRMS()
                value = myMean

                #Do Langaus fit if histogram mean is larger than 10
                #and mean is larger than RMS (a clear peak away from noise)
                if (myMean > 10 and myMean > 0.5*myRMS):                
                    # if ch==0: 
                    #     print(tmpHist.GetEntries(), myMean)
                    #use coarser bins when the signal is bigger
                    if (myMean > 50) :
                        tmpHist.Rebin(10)
                    else :
                        tmpHist.Rebin(5)

                    #myLanGausFunction = fit.fit(tmpHist, fitrange=(myMean-2*myRMS,myMean+3*myRMS))
                    #myMPV = myLanGausFunction.GetParameter(1)
                    #value = myMPV

                    ##For Debugging
                    #tmpHist.Draw("hist")
                    #myLanGausFunction.Draw("same")
                    #canvas.SaveAs("q_"+str(i)+"_"+str(j)+".gif")

                #print ("Bin : " + str(i) + " , " + str(j) + " -> " + str(value))
                # if tmpHist.GetEntries()>20: 
                this_xy.SetBinContent(i,j,value)
            
            

outputfile=TFile("%splotsAmpChargevsXY.root"%outdir,"RECREATE")

# Plot 2D histograms
for i_name,this_list_XY in enumerate(list_XY_maps):
    for ch,this_xy in enumerate(this_list_XY):

        this_xy.Draw("colz")
        this_xy.SetStats(0)
        this_xy.SetTitle("Channel %i"%ch)

        this_zmin = z_limits[i_name][0] if zmin == 0.0 else zmin
        this_zmax = z_limits[i_name][1] if zmax == 120.0 else zmax

        # this_zmin = zmin
        # this_zmax = zmax
        # if ("Ratio" in list_name3Dhist[i_name]):
        #     this_zmin = 1.0
        #     this_zmax = 10.0

        this_xy.SetMinimum(this_zmin)
        this_xy.SetMaximum(this_zmax)

        canvas.SetRightMargin(0.18)
        canvas.SetLeftMargin(0.12)
        myStyle.SensorInfoSmart(dataset,2.0*myStyle.GetMargin())

        name = list_namesOutput[i_name]
        if (ch != (len(this_list_XY)-1)):
            name += "_channel%i"%ch

        canvas.SaveAs(outdir+name+".gif")
        canvas.SaveAs(outdir+name+".pdf")
        this_xy.Write()


outputfile.Close()





