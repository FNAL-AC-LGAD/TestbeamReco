import ROOT
import optparse
ROOT.gROOT.SetBatch(True)
from array import array
from AlignBinning import z_values, alpha_values, beta_values, gamma_values

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
     #   c.Print("%s.gif"%(name))
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
                print("\tres:%0.2f, %s: %0.1f "%(resolutions[-1],var,var_values[ivar]))
                # print("res:%0.2f, z: %0.2f, alpha: %0.2f, beta: %0.2f "%(resolutions[-1],z_values[ivar], alpha_values[], beta_values[]))


        resolution_vs_var = ROOT.TGraphErrors(len(var_values),array("d",var_values),array("d",resolutions),array("d",[0.01 for i in var_values]),array("d",res_errs))
        resolution_vs_var.SetTitle(";Assigned %s position [%s];Resolution [microns]"%(var_dict[var][0],var_dict[var][1]))
        cosmetic_tgraph(resolution_vs_var)

        c = ROOT.TCanvas("c","c",1000,600)

        # lmin = var_values[0]
        # lmax = var_values[-1]
        # if var in ["Z","A"]: lmin = var_values[0]
        # if var=="C" and (var_values[0]<=90 and 90<=var_values[-1]):
        #         lmin = var_values[0] #90
        #         lmax = 89.4

        fit_limits = {
                "Z": [var_values[0], var_values[-1]],
                "A": [var_values[0], var_values[-1]],
                "B": [var_values[0], -0.2],
                "C": [var_values[0], 89.4],
        }


        fitFunc = ROOT.TF1("","pol2",var_values[0], var_values[-1]);

        # fitFunc.SetParLimits(2,0,10000)
        results = resolution_vs_var.Fit(fitFunc,"Q","",fit_limits[var][0], fit_limits[var][1]);
        #results.Print("V")
        a = fitFunc.GetParameter(2)
        b = fitFunc.GetParameter(1)
        print(a, b)
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
        c.Print("./EIC_Scan/%s%s.pdf"%("scan_summary_overlay",var))



# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('--runPad', dest='runPad', action='store_true', default = False, help="run fits or not")
parser.add_option('-f','--file', dest='file_name', default = "EIC_W1_1cm_255V_0.root", help="input name file with extension")
options, args = parser.parse_args()

file_name = options.file_name

f = ROOT.TFile('../test/%s'%file_name)

out = ROOT.TFile('./EIC_Scan/output_Scan.root',"RECREATE")

createTGraph(f, out, z_values,       "Z")
createTGraph(f, out, alpha_values,   "A")
createTGraph(f, out, beta_values,    "B")
createTGraph(f, out, gamma_values,   "C")

out.Write()
out.Close()

# histsZ=[]
# for i in range(len(z_values)):
#         histsZ.append(('deltaX_varZ%i'%i,'deltaX_variant_%i'%i,"tracker"))

# histsA=[]
# for i in range(len(alpha_values)):
#         histsA.append(('deltaX_varA%i'%i,'deltaX_variant_%i'%i,"tracker"))

# histsB=[]
# for i in range(len(beta_values)):
#         histsB.append(('deltaX_varB%i'%i,'deltaX_variant_%i'%i,"tracker"))

# histsC=[]
# for i in range(len(gamma_values)):
#         histsC.append(('deltaX_varC%i'%i,'deltaX_variant_%i'%i,"tracker"))

# fix_alpha = 4
# fix_beta = 4
# fix_gamma = 4
# for i in range(len(z_values)):
#         i_z = fix_gamma + fix_beta*9 + fix_alpha*9*9 + i*9*9*9 # beta + alpha*Nbeta + z*Nalpha*Nbeta
#         # #if i%81 == 40:
#         hists.append(('deltaX_var%i'%i_z,'deltaX_variant_%i'%i_z,"tracker"))
#         print("Z: %0.2f, alpha: %0.2f, beta: %0.2f, gamma: %0.2f, i_z: %i"%(z_values[i], alpha_values[fix_alpha], beta_values[fix_beta], gamma_values[fix_gamma], i_z))
#         # for j in range(len(alpha_values)):
#         #         for k in range(len(beta_values)):
#                         # i_scan = k + j*9 + i*81 #fix_beta + fix_alpha*9 + i*81 # beta + alpha*Nbeta + z*Nalpha*Nbeta
#                         # #if i%81 == 40:
#                         # hists.append(('deltaX_var%i'%i_scan,'deltaX_variant_%i'%i_scan,"tracker"))
#                         # print("Z: %0.2f, alpha: %0.2f, beta: %0.2f"%(z_values[i], alpha_values[j], beta_values[k]))

# resolutionsZ=[]
# res_errsZ=[]
# for ivar,t in enumerate(histsZ):
#         h = f.Get(t[0])
#         resolution,error = plot1D([h], [ROOT.kBlack], [t[1]], t[0], 'Events', t[1]+' - '+t[2])
#         resolutionsZ.append(resolution)
#         res_errsZ.append(error)
#         print("res:%0.2f, Z: %0.1f "%(resolutionsZ[-1],z_values[ivar]))
#         # print("res:%0.2f, z: %0.2f, alpha: %0.2f, beta: %0.2f "%(resolutions[-1],z_values[ivar], alpha_values[], beta_values[]))


# resolution_vs_z = ROOT.TGraphErrors(len(z_values),array("d",z_values),array("d",resolutionsZ),array("d",[0.01 for i in z_values]),array("d",res_errsZ))
# resolution_vs_z.SetTitle(";Assigned Z position [mm];Resolution [microns]")
# cosmetic_tgraph(resolution_vs_z)

# resolutionsA=[]
# res_errsA=[]
# for ivar,t in enumerate(histsA):
#         h = f.Get(t[0])
#         resolution,error = plot1D([h], [ROOT.kBlack], [t[1]], t[0], 'Events', t[1]+' - '+t[2])
#         resolutionsA.append(resolution)
#         res_errsA.append(error)
#         print("res:%0.2f, alpha: %0.2f "%(resolutionsA[-1],alpha_values[ivar]))


# resolution_vs_a = ROOT.TGraphErrors(len(alpha_values),array("d",alpha_values),array("d",resolutionsA),array("d",[0.01 for i in alpha_values]),array("d",res_errsA))
# resolution_vs_a.SetTitle(";Assigned #alpha position [deg];Resolution [microns]")
# cosmetic_tgraph(resolution_vs_a)

# resolutionsB=[]
# res_errsB=[]
# for ivar,t in enumerate(histsB):
#         h = f.Get(t[0])
#         resolution,error = plot1D([h], [ROOT.kBlack], [t[1]], t[0], 'Events', t[1]+' - '+t[2])
#         resolutionsB.append(resolution)
#         res_errsB.append(error)
#         print("res:%0.2f, beta: %0.2f "%(resolutionsB[-1],beta_values[ivar]))


# resolution_vs_b = ROOT.TGraphErrors(len(beta_values),array("d",beta_values),array("d",resolutionsB),array("d",[0.01 for i in beta_values]),array("d",res_errsB))
# resolution_vs_b.SetTitle(";Assigned #beta position [deg];Resolution [microns]")
# cosmetic_tgraph(resolution_vs_b)

# resolutionsC=[]
# res_errsC=[]
# for ivar,t in enumerate(histsC):
#         h = f.Get(t[0])
#         resolution,error = plot1D([h], [ROOT.kBlack], [t[1]], t[0], 'Events', t[1]+' - '+t[2])
#         resolutionsC.append(resolution)
#         res_errsC.append(error)
#         print("res:%0.2f, gamma: %0.2f "%(resolutionsC[-1],gamma_values[ivar]))


# resolution_vs_c = ROOT.TGraphErrors(len(gamma_values),array("d",gamma_values),array("d",resolutionsC),array("d",[0.01 for i in gamma_values]),array("d",res_errsC))
# resolution_vs_c.SetTitle(";Assigned #gamma position [deg];Resolution [microns]")
# cosmetic_tgraph(resolution_vs_c)

# c = ROOT.TCanvas("c","c",1000,600)

# fitFunc = ROOT.TF1("","pol2",z_values[0], z_values[-1]);
# results = resolution_vs_z.Fit(fitFunc,"Q","",z_values[0], z_values[-1]);
# #results.Print("V")
# a = fitFunc.GetParameter(2)
# b = fitFunc.GetParameter(1)
# print(a, b)
# print("Minimum at: {}".format(-(b)/(2*a)))


# resolution_vs_z.Draw("aep")


# #mean = myGausFunction.GetParameter(1)
# #meanErr = myGausFunction.GetParError(1)
# #sigma = myGausFunction.GetParameter(2)
# fitFunc.Draw("same")

# c.Print("%s.pdf"%("scan_summary_overlay"))

