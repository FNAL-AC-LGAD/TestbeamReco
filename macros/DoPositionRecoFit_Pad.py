from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,TF1,gStyle,gROOT
import ROOT
import os

gROOT.SetBatch( True )

#inputfile = TFile("/uscms/home/sxie/work/releases/testbeam/CMSSW_11_2_0_pre5/src/TestbeamReco/test/BNL2020_220V_output.root")
inputfile = TFile("../test/myoutputfile.root")

    #Get x vs aleft/(aleft+aright) hist
AmpLeftOverAmpLeftandRightTop_vs_x = inputfile.Get("AmpLeftOverAmpLeftandRightTop_vs_x")
AmpLeftOverAmpLeftandRightBot_vs_x = inputfile.Get("AmpLeftOverAmpLeftandRightBot_vs_x")

AmpLeftOverAmpLeftandRight_vs_x_list = [AmpLeftOverAmpLeftandRightTop_vs_x,AmpLeftOverAmpLeftandRightBot_vs_x]     

#Define profile hist
AmpLeftOverAmpLeftandRightTop_vs_x_profile = AmpLeftOverAmpLeftandRightTop_vs_x.ProjectionY().Clone("AmpLeftOverAmpLeftandRightTop_vs_x_profile")
AmpLeftOverAmpLeftandRightBot_vs_x_profile = AmpLeftOverAmpLeftandRightBot_vs_x.ProjectionY().Clone("AmpLeftOverAmpLeftandRightBot_vs_x_profile")

AmpLeftOverAmpLeftandRight_vs_x_profile_list = [AmpLeftOverAmpLeftandRightTop_vs_x_profile,AmpLeftOverAmpLeftandRightBot_vs_x_profile]   

for l in range(len(AmpLeftOverAmpLeftandRight_vs_x_list)) : 

    AmpLeftOverAmpLeftandRight_vs_x = AmpLeftOverAmpLeftandRight_vs_x_list[l]
    AmpLeftOverAmpLeftandRight_vs_x_profile = AmpLeftOverAmpLeftandRight_vs_x_profile_list[l]
    
    canvas = TCanvas("cv","cv",800,800)
    
    #loop over  Amp1OverAmp1and2 bins
    for i in range(0, AmpLeftOverAmpLeftandRight_vs_x.GetYaxis().GetNbins() + 1):
        #print ("Bin " + str(i))
    
        ##For Debugging
        #if not (i==46 and j==5):
        #    continue
    
        tmpHist = AmpLeftOverAmpLeftandRight_vs_x.ProjectionX("px",i,i)
        myMean = tmpHist.GetMean()
        myRMS = tmpHist.GetRMS()
        nEntries = tmpHist.GetEntries()
        
        if(nEntries > 0.0):
            myGausFunction = TF1("mygaus","gaus(0)",-0.4,0.4);
            tmpHist.Fit(myGausFunction,"Q","",-0.4,0.4);
            mean = myGausFunction.GetParameter(1)
            meanErr = myGausFunction.GetParError(1)
            sigma = myGausFunction.GetParameter(2)
            
            ###For Debugging
            #tmpHist.Draw("hist")
            #myGausFunction.Draw("same")
            #canvas.SaveAs("q_"+str(l)+"_"+str(i)+".gif")
            #print ("Bin : " + str(i) + " -> " + str(mean))
        else:
            mean=0.0
            meanErr=0.0
           
        AmpLeftOverAmpLeftandRight_vs_x_profile.SetBinContent(i,mean)
        AmpLeftOverAmpLeftandRight_vs_x_profile.SetBinError(i,meanErr)           
            
    # Save amplitude histograms

    if (l==0) :
        outputfile = TFile("positionRecoFitPlotsTop.root","RECREATE")   
    else :
        outputfile = TFile("positionRecoFitPlotsBot.root","RECREATE")   

    #AmpLeftOverAmpLeftandRight_vs_x_profile.Write()
    #outputfile.Close()
    
    xmin=0.18
    xmax=0.83
    
    gStyle.SetOptFit(1011)
    fit = TF1("mainFit","pol5",xmin,xmax)
    AmpLeftOverAmpLeftandRight_vs_x_profile.SetMaximum(0.3)
    AmpLeftOverAmpLeftandRight_vs_x_profile.SetMinimum(-0.3)
    AmpLeftOverAmpLeftandRight_vs_x_profile.GetXaxis().SetRangeUser(xmin,xmax)
    AmpLeftOverAmpLeftandRight_vs_x_profile.Fit(fit,"","",xmin,xmax)
    AmpLeftOverAmpLeftandRight_vs_x_profile.Draw()
    fit.Draw("same")
    AmpLeftOverAmpLeftandRight_vs_x_profile.Draw("same")
    
    line = TF1("line","0.0",xmin,1.0)
    line.SetLineColor(ROOT.kBlack)
    line.Draw("same")
   
    if (l==0) : 
        canvas.SaveAs("PositionFitTop.gif")
    else :
        canvas.SaveAs("PositionFitBot.gif")

    AmpLeftOverAmpLeftandRight_vs_x_profile.Write()
    fit.Write()
    outputfile.Close()
    
