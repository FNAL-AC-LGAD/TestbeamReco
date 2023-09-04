import ROOT
#import os

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gStyle.SetLabelFont(42,"xyz")
ROOT.gStyle.SetLabelSize(0.04,"xyz")
#ROOT.gStyle.SetTitleFont(42)
ROOT.gStyle.SetTitleFont(42,"xyz")
ROOT.gStyle.SetTitleFont(42,"t")
#ROOT.gStyle.SetTitleSize(0.05)
ROOT.gStyle.SetTitleSize(0.05,"xyz")
ROOT.gStyle.SetTitleSize(0.05,"t") 
ROOT.gStyle.SetPadBottomMargin(0.14)
ROOT.gStyle.SetPadLeftMargin(0.14)
ROOT.gStyle.SetPadRightMargin(0.25)
ROOT.gStyle.SetTitleOffset(1,'y')
ROOT.gStyle.SetLegendTextSize(0.035)
ROOT.gStyle.SetGridStyle(3)
ROOT.gStyle.SetGridColor(14)
ROOT.gStyle.SetOptFit(1)
ROOT.gStyle.SetOptStat(0)
one = ROOT.TColor(2001,0.906,0.153,0.094)
two = ROOT.TColor(2002,0.906,0.533,0.094)
three = ROOT.TColor(2003,0.086,0.404,0.576)
four =ROOT.TColor(2004,0.071,0.694,0.18)
five =ROOT.TColor(2005,0.388,0.098,0.608)
six=ROOT.TColor(2006,0.906,0.878,0.094)
colors = [1,2001,2002,2003,2004,2005,2006,6,2,3,4,6,7,5,1,8,9,29,38,46,1,2001,2002,2003,2004,2005,2006]

filename = "root://cmseos.fnal.gov//store/group/cmstestbeam/2021_CMSTiming_ETL/LecroyScope/RecoData/TimingDAQRECO/RecoWithTracks/v2/confInfo/run_scope34631_info.root"
event_number = 5594
chanlist =[1,2,3,4]

chain = ROOT.TChain("pulse")
chain.Add(filename)

canvas = ROOT.TCanvas("c1","",1000,600)
canvas.SetGridy()
canvas.SetGridx()

chain.SetLineWidth(2)
leg = ROOT.TLegend(0.8,0.6,0.99,0.9)


waves = []
dummy = ROOT.TH2F("dum","",100,-235,-185,100,-150,40)
dummy.SetTitle("Event %i;Time [ns]; Amplitude [mV];"%event_number)


dummy.Draw()

chain.SetLineColor(colors[0])
chain.Draw("channel[0]:1e9*time[0]>>hchan0","i_evt==%i"%event_number,"L same")
leg.AddEntry(ROOT.hchan0,"DC ring","L")
chain.SetLineColor(colors[1])
chain.Draw("channel[1]:1e9*time[0]>>hchan1","i_evt==%i"%event_number,"L same")
leg.AddEntry(ROOT.hchan1,"Top Right","L")
chain.SetLineColor(colors[2])
chain.Draw("channel[2]:1e9*time[0]>>hchan2","i_evt==%i"%event_number,"L same")
leg.AddEntry(ROOT.hchan2,"Top Left","L")
chain.SetLineColor(colors[3])
chain.Draw("channel[3]:1e9*time[0]>>hchan3","i_evt==%i"%event_number,"L same")
leg.AddEntry(ROOT.hchan3,"Bottom Left","L")
chain.SetLineColor(colors[4])
chain.Draw("channel[4]:1e9*time[0]>>hchan4","i_evt==%i"%event_number,"L same")
leg.AddEntry(ROOT.hchan4,"Bottom Right","L")

# for i,chan in enumerate(chanlist):
# 	# waves.append(ROOT.TH2F("chan%i"%chan,"",100,-230,-180,100,-500,50))
# 	# waves[i].SetLineColor(colors[chan])
# 	# waves[i].SetLineWidth(2)
# 	chain.SetLineColor(colors[chan])
# 	chain.Draw("channel[%i]:1e9*time[0]>>hchan"%(chan),"i_evt==%i"%event_number,"L same")
# 	# waves.append(ROOT.hchan)
# 	leg.AddEntry(ROOT.hchan,"Channel %i"%chan,"L")

leg.Draw("same")
canvas.Print("display_%i.pdf"%event_number)
