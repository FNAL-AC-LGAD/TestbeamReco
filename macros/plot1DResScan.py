import ROOT
import optparse
ROOT.gROOT.SetBatch(True)
from array import array

def cosmetic_tgraph(graph):
        # graph.SetLineColor(colors[colorindex])
        # graph.SetMarkerColor(colors[colorindex])
        graph.SetMarkerSize(0.75)
        graph.SetMarkerStyle(20)

def plot1D(hists, colors, labels, name, xlab, ylab, bins=100, arange=(0,1)):
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
        h.GetXaxis().SetTitle(ylab)
        h.GetYaxis().SetTitle(xlab)
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



# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('--runPad', dest='runPad', action='store_true', default = False, help="run fits or not")
options, args = parser.parse_args()

f = ROOT.TFile('../test/myoutputfile.root')
#f2 = ROOT.TFile('../test/myoutputfile_chi2lt3_newfitv2_nplanes14_slopelt0001.root')

channelMap = [(0,0),(0,1),(1,0),(1,1)] if options.runPad else [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5)]

hists=[]
for i in range(35):
        hists.append(('deltaX_var%i'%i,'deltaX_variant_%i'%i,"tracker"))
z_values = [51., 48., 45., 42., 39., 36., 33., 30., 27., 24., 21., 18., 15., 12., 9., 6., 3., 0., -3., -6., -9., -12., -15., -18., -21., -24., -27., -30., -33., -36., -39., -42., -45., -48., -51.]

resolutions=[]
res_errs=[]
for ivar,t in enumerate(hists):
        h = f.Get(t[0])
        resolution,error = plot1D([h], [ROOT.kBlack], [t[1]], t[0], 'Events', t[1]+' - '+t[2])
        resolutions.append(resolution)
        res_errs.append(error)
        print("res:%0.2f, z: %0.f "%(resolutions[-1],z_values[ivar]))


# z_values = [5.,4.5,4.,3.5,3.,2.5,2.,1.5,1.,0.5,0.,-0.5,-1.,-1.5,-2.,-2.5,-3.,-3.5,-4.,-4.5,-5.,-5.5,-6.]
# z_values = [16., 14., 12., 10., 8., 6., 4., 2., 0., -2., -4., -6., -8., -10., -12., -14., -16., -18., -20., -22., -24.]
resolution_vs_z = ROOT.TGraphErrors(len(z_values),array("d",z_values),array("d",resolutions),array("d",[0.01 for i in z_values]),array("d",res_errs))
resolution_vs_z.SetTitle(";Assigned Z position [mm];Resolution [microns]")
cosmetic_tgraph(resolution_vs_z)


#c.Print("%s.pdf"%("scan_summary"))

#resolutions=[]
#res_errs=[]
#for ivar,t in enumerate(hists):
#        h = f2.Get(t[0])
#        resolution,error = plot1D([h], [ROOT.kBlack], [t[1]], t[0], 'Events', t[1]+' - '+t[2])
#        resolutions.append(resolution)
#        res_errs.append(error)
#        print("res:%0.2f, z: %0.f "%(resolutions[-1],z_values[ivar]))
#
#
## z_values = [5.,4.5,4.,3.5,3.,2.5,2.,1.5,1.,0.5,0.,-0.5,-1.,-1.5,-2.,-2.5,-3.,-3.5,-4.,-4.5,-5.,-5.5,-6.]
## z_values = [16., 14., 12., 10., 8., 6., 4., 2., 0., -2., -4., -6., -8., -10., -12., -14., -16., -18., -20., -22., -24.]
#resolution_vs_z_noslope = ROOT.TGraphErrors(len(z_values),array("d",z_values),array("d",resolutions),array("d",[0.01 for i in z_values]),array("d",res_errs))
#resolution_vs_z_noslope.SetTitle(";Assigned Z position [mm];Resolution [microns]")
#cosmetic_tgraph(resolution_vs_z_noslope)
#resolution_vs_z_noslope.SetMarkerColor(ROOT.kRed+1)
#resolution_vs_z_noslope.SetLineColor(ROOT.kRed+1)
c = ROOT.TCanvas("c","c",1000,600)

resolution_vs_z.Draw("aep")
#resolution_vs_z_noslope.Draw("ep same")
#
c.Print("%s.pdf"%("scan_summary_overlay"))

