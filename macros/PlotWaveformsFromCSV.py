from ROOT import TFile,TTree,TCanvas,TGraph,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,TH1
import ROOT
import optparse
import os
import myStyle
import pandas as pd 
import matplotlib.pyplot as plt

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")

options, args = parser.parse_args()

dataset = options.Dataset
outdir=""
outdir = myStyle.getOutputDir(dataset)

colors = myStyle.GetColors()
regions = ['stripCenter']
max_save = 10
FileSave = ['Strip-center'] # Although the region name is called near-strip in geometry and waveform names, the region is actually on the strip center, so the save name was changed

for region_iter in range(len(regions)):
    for waveform_iter in range(max_save):    
        filename = outdir+"/waveforms_gabriele/waveform_"+regions[region_iter]+"_"+str(waveform_iter)+".csv"
        df=pd.read_csv(filename, header=0)
        last_three_columns = df.iloc[:, -7:]
        min_row, min_column = last_three_columns.unstack().idxmin()
        print(min_row, min_column)
        plt.plot(df['Time[ns]'], df[min_row],label=str(waveform_iter+1))
    plt.title(str(max_save)+" leading channel waveforms from "+FileSave[region_iter])
    plt.xlabel("Time [ns]")
    plt.ylabel("Amplitude [mV]")
    plt.legend(title="Waveform number")
    plt.grid()
    plt.savefig(outdir+"/waveforms_gabriele/Plot"+FileSave[region_iter]+".png")
    plt.close()
