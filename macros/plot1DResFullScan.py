import ROOT
import os
import optparse
ROOT.gROOT.SetBatch(True)
from array import array
from AlignBinning import z_values, alpha_values, beta_values, gamma_values
import myStyle


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-c', dest='Copy_Binning', action='store_true', default = False, help="Copy AlignBinning file from /macro")
options, args = parser.parse_args()


dataset = options.Dataset
copy_binning = options.Copy_Binning


outdir=""
outdir = myStyle.getOutputDir(dataset)
inputfile = ROOT.TFile("%s%s_Align.root"%(outdir,dataset))

outdir = os.path.join(outdir,"Scan0/")

if not os.path.exists(outdir):
        print(outdir)
        os.mkdir(outdir)
else:
        i = 1
        while(os.path.exists(outdir)):
                outdir = outdir[0:-2] + str(i) + outdir[-1]
                i+=1
        os.mkdir(outdir)

if copy_binning: os.system("cp AlignBinning.py %s"%outdir)

outputfile=ROOT.TFile("%sScan_ZABC.root"%outdir,"RECREATE")


def cosmetic_tgraph(graph):
        # graph.SetLineColor(colors[colorindex])
        # graph.SetMarkerColor(colors[colorindex])
        graph.SetMarkerSize(0.75)
        graph.SetMarkerStyle(20)

def plot1D(hists, colors, labels, name, ylab, xlab, bins=100, arange=(0,1)):
        ROOT.gStyle.SetOptFit(1)
        c = ROOT.TCanvas("c","c",1000,1000)
        ROOT.gPad.SetLeftMargin(0.12)
        ROOT.gPad.SetRightMargin(0.15)
        ROOT.gPad.SetTopMargin(0.08)
        ROOT.gPad.SetBottomMargin(0.12)
        ROOT.gPad.SetTicks(1,1)
        ROOT.TH1.SetDefaultSumw2()
        #ROOT.gPad.SetLogy()

        h = hists[0]
        h.GetXaxis().SetTitle(xlab)
        h.GetYaxis().SetTitle(ylab)
        h.Draw('hists e')
        myMean = h.GetMean()
        myRMS = h.GetRMS()
        fitlow = myMean - 1.2*myRMS
        fithigh = myMean + myRMS

        fit = ROOT.TF1("fit", "gaus", fitlow, fithigh)    
        fit.SetLineColor(ROOT.kRed)
        #fit.Draw("same")
        h.Fit(fit,"Q", "", fitlow, fithigh)
        fit.Draw("same")    

        #c.Print("%s.png"%(name))
        #c.Print("%s.gif"%(name))
        return 1000.*fit.GetParameter(2),1000.*fit.GetParError(2)

def createTGraph(f, out, var_values, var):
        var_dict = {'Z': ["Z", "mm"], 'A': ["#alpha", "deg"], 'B': ["#beta", "deg"], 'C': ["#gamma", "deg"]}

        print("Running over %s var:"%var)
        hists=[]
        for i in range(len(var_values)):
                hists.append(('deltaX_var%s%i'%(var,i),'deltaX_variant_%i'%i,"tracker"))

        resolutions=[]
        res_errs=[]
        for ivar,t in enumerate(hists):
                h = f.Get(t[0])
                resolution,error = plot1D([h], [ROOT.kBlack], [t[1]], t[0], 'Events', t[1]+' - '+t[2])
                resolutions.append(resolution)
                res_errs.append(error)
                print("%i\tres:%0.2f, %s: %0.1f "%(ivar,resolutions[-1],var,var_values[ivar]))
                # print("res:%0.2f, z: %0.2f, alpha: %0.2f, beta: %0.2f "%(resolutions[-1],z_values[ivar], alpha_values[], beta_values[]))


        resolution_vs_var = ROOT.TGraphErrors(len(var_values),array("d",var_values),array("d",resolutions),array("d",[0.01 for i in var_values]),array("d",res_errs))
        resolution_vs_var.SetTitle(";Assigned %s position [%s];Resolution [microns]"%(var_dict[var][0],var_dict[var][1]))
        cosmetic_tgraph(resolution_vs_var)

        c = ROOT.TCanvas("c","c",1000,600)

        fit_limits = {
                "Z": [var_values[0], var_values[-1], -99, -99, -99], # -99, -99, -99],
                "A": [var_values[0], var_values[-1], -99, -99, -99],
                "B": [var_values[0], var_values[-1], -99, -99, -99],
                "C": [var_values[0], var_values[-1], -99, -99, -99], # 50.0, 50.0, 20.0],
        }


        fitFunc = ROOT.TF1("","pol2",var_values[0], var_values[-1]);

        # fitFunc.SetParLimits(0,0.0,1.e12)
        fitFunc.SetParLimits(2,0.0,10000)
        if fit_limits[var][2]!=-99: fitFunc.SetParameter(0,fit_limits[var][2])
        if fit_limits[var][3]!=-99: fitFunc.SetParameter(1,fit_limits[var][3])
        if fit_limits[var][4]!=-99: fitFunc.SetParameter(2,fit_limits[var][4])

        results = resolution_vs_var.Fit(fitFunc,"Q","",fit_limits[var][0], fit_limits[var][1]);
        #results.Print("V")
        a = fitFunc.GetParameter(2)
        b = fitFunc.GetParameter(1)
        print(a, b)
        if (a<=0.0):
                print("Not quadratic: a = 0.0")
        else:
                print("\tMinimum at: {}".format(-(b)/(2*a)))

        resolution_vs_var.SetName("TGraph_%s"%var)
        resolution_vs_var.Draw("aep")


        #mean = myGausFunction.GetParameter(1)
        #meanErr = myGausFunction.GetParError(1)
        #sigma = myGausFunction.GetParameter(2)
        fitFunc.Draw("same")

        resolution_vs_var.Write()
        fitFunc.Write("f_%s"%var)
        out.Write()

        c.SaveAs(outdir+"Scan_"+var+".gif")
        c.SaveAs(outdir+"Scan_"+var+".pdf")

        resolution_vs_var.GetYaxis().SetRangeUser(5.1, 20.9)
        # resolution_vs_var.GetYaxis().SetRangeUser(10.1, 49.9)
        # resolution_vs_var.GetYaxis().SetRangeUser(15.1, 24.9)
        c.SaveAs(outdir+"Scan_"+var+"_fixY.gif")
        c.SaveAs(outdir+"Scan_"+var+"_fixY.pdf")


createTGraph(inputfile, outputfile, z_values,       "Z")
createTGraph(inputfile, outputfile, alpha_values,   "A")
createTGraph(inputfile, outputfile, beta_values,    "B")
createTGraph(inputfile, outputfile, gamma_values,   "C")

outputfile.Write()
outputfile.Close()
