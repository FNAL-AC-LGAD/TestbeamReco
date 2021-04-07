from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors
import os
import EfficiencyUtils
import langaus


#inputfile = TFile("/uscms/home/sxie/work/releases/testbeam/CMSSW_11_2_0_pre5/src/TestbeamReco/test/BNL2020_220V_output.root")
inputfile = TFile("/afs/cern.ch/work/s/sixie/public/releases/testbeam/CMSSW_11_2_0_pre5/src/TestbeamReco/test/BNL2020_220V.20210405.root")

#Get 3D histograms 
th3_amplitude_vs_xy_channel00 = inputfile.Get("amplitude_vs_xy_channel00")
th3_amplitude_vs_xy_channel01 = inputfile.Get("amplitude_vs_xy_channel01")
th3_amplitude_vs_xy_channel02 = inputfile.Get("amplitude_vs_xy_channel02")
th3_amplitude_vs_xy_channel03 = inputfile.Get("amplitude_vs_xy_channel03")
th3_amplitude_vs_xy_channel04 = inputfile.Get("amplitude_vs_xy_channel04")
th3_amplitude_vs_xy_channel05 = inputfile.Get("amplitude_vs_xy_channel05")
list_th3_amplitude_vs_xy = []
list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel00)
list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel01)
list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel02)
list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel03)
list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel04)
list_th3_amplitude_vs_xy.append(th3_amplitude_vs_xy_channel05)


#Build 2D amp vs x histograms
amplitude_vs_x_channel00 = th3_amplitude_vs_xy_channel00.Project3D("zx")
amplitude_vs_x_channel01 = th3_amplitude_vs_xy_channel01.Project3D("zx")
amplitude_vs_x_channel02 = th3_amplitude_vs_xy_channel02.Project3D("zx")
amplitude_vs_x_channel03 = th3_amplitude_vs_xy_channel03.Project3D("zx")
amplitude_vs_x_channel04 = th3_amplitude_vs_xy_channel04.Project3D("zx")
amplitude_vs_x_channel05 = th3_amplitude_vs_xy_channel05.Project3D("zx")

list_th2_amplitude_vs_x = []
list_th2_amplitude_vs_x.append(amplitude_vs_x_channel00)
list_th2_amplitude_vs_x.append(amplitude_vs_x_channel01)
list_th2_amplitude_vs_x.append(amplitude_vs_x_channel02)
list_th2_amplitude_vs_x.append(amplitude_vs_x_channel03)
list_th2_amplitude_vs_x.append(amplitude_vs_x_channel04)
list_th2_amplitude_vs_x.append(amplitude_vs_x_channel05)


#Build amplitude histograms
amplitude_vs_x = th3_amplitude_vs_xy_channel00.ProjectionX().Clone("amplitude_vs_x")
amplitude_vs_x_channel00 = amplitude_vs_x.Clone("amplitude_vs_x_channel00")
amplitude_vs_x_channel01 = amplitude_vs_x.Clone("amplitude_vs_x_channel01")
amplitude_vs_x_channel02 = amplitude_vs_x.Clone("amplitude_vs_x_channel02")
amplitude_vs_x_channel03 = amplitude_vs_x.Clone("amplitude_vs_x_channel03")
amplitude_vs_x_channel04 = amplitude_vs_x.Clone("amplitude_vs_x_channel04")
amplitude_vs_x_channel05 = amplitude_vs_x.Clone("amplitude_vs_x_channel05")

print ("Amplitude vs X: " + str(amplitude_vs_x.GetXaxis().GetBinLowEdge(1)) + " -> " + str(amplitude_vs_x.GetXaxis().GetBinUpEdge(amplitude_vs_x.GetXaxis().GetNbins())))


list_amplitude_vs_x = []
list_amplitude_vs_x.append(amplitude_vs_x_channel00)
list_amplitude_vs_x.append(amplitude_vs_x_channel01)
list_amplitude_vs_x.append(amplitude_vs_x_channel02)
list_amplitude_vs_x.append(amplitude_vs_x_channel03)
list_amplitude_vs_x.append(amplitude_vs_x_channel04)
list_amplitude_vs_x.append(amplitude_vs_x_channel05)


print ("1")

fit = langaus.LanGausFit()
canvas = TCanvas("cv","cv",800,800)

print ("yes")

#loop over X,Y bins
for channel in range(0, len(list_amplitude_vs_x)):

        print("Channel : " + str(channel))

        for i in range(1, list_amplitude_vs_x[channel].GetXaxis().GetNbins()):

            print ("Bin " + str(i))

        ##For Debugging
        #if not (i==46 and j==5):
        #    continue

            tmpHist = list_th2_amplitude_vs_x[channel].ProjectionY("py",i,i)
            myMean = tmpHist.GetMean()
            myRMS = tmpHist.GetRMS()
            value = myMean
                
            #use coarser bins when the signal is bigger
            if (myMean > 50) :
                tmpHist.Rebin(10)
            else :
                tmpHist.Rebin(5)

            myLanGausFunction = fit.fit(tmpHist, fitrange=(myMean-1*myRMS,myMean+3*myRMS))
            myMPV = myLanGausFunction.GetParameter(1)
            value = myMPV

            ##For Debugging
            tmpHist.Draw("hist")
            myLanGausFunction.Draw("same")
            canvas.SaveAs("q_"+str(i)+".gif")

            print ("Bin : " + str(i) + " -> " + str(value))
            list_amplitude_vs_x[channel].SetBinContent(i,value)
            
            
            
outputfile = TFile("plots.root","RECREATE")



canvas = TCanvas("cv","cv",800,800)
#amplitude_vs_x_channel00.Draw("colz")
list_amplitude_vs_x[0].Draw("hist")
list_amplitude_vs_x[0].SetStats(0)
list_amplitude_vs_x[0].SetTitle("")
list_amplitude_vs_x[0].SetLineWidth(2)
list_amplitude_vs_x[1].SetLineWidth(2)
list_amplitude_vs_x[2].SetLineWidth(2)
list_amplitude_vs_x[3].SetLineWidth(2)
list_amplitude_vs_x[4].SetLineWidth(2)
list_amplitude_vs_x[5].SetLineWidth(2)
list_amplitude_vs_x[0].SetLineColor(416+2) #kGreen+2
list_amplitude_vs_x[1].SetLineColor(432+2) #kCyan+2
list_amplitude_vs_x[2].SetLineColor(600) #kBlue
list_amplitude_vs_x[3].SetLineColor(880) #kViolet
list_amplitude_vs_x[4].SetLineColor(632) #kRed
list_amplitude_vs_x[5].SetLineColor(400+2) #kYellow
list_amplitude_vs_x[1].Draw("histsame")
list_amplitude_vs_x[2].Draw("histsame")
list_amplitude_vs_x[3].Draw("histsame")
list_amplitude_vs_x[4].Draw("histsame")
list_amplitude_vs_x[5].Draw("histsame")

canvas.SaveAs("Amplitude_vs_x.gif")




# Save amplitude histograms
outputfile = TFile("plots.root","RECREATE")

for channel in range(0, len(list_amplitude_vs_x)):
    list_amplitude_vs_x[channel].Write()

outputfile.Close()





