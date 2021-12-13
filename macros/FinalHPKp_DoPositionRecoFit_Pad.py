from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,TF1,gStyle,gROOT
import ROOT
import os
import optparse
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptStat(0)
gStyle.SetOptFit(0)

## Defining Style
myStyle.ForceStyle()

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-f','--file', dest='file', default = "myoutputfile.root", help="File name (or path from ../test/)")
parser.add_option('-s','--sensor', dest='sensor', default = "HPK C2", help="Type of sensor (HPK C2, HPK B2, ...)")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 180, help="Bias Voltage value in [V]")
options, args = parser.parse_args()

file = options.file
sensor = options.sensor
bias = options.biasvolt

inputfile = TFile("../test/"+file)

#Get x vs aleft/(aleft+aright) hist
AmpLeftOverAmpLeftandRightTop_vs_x = inputfile.Get("AmpLeftOverAmpLeftandRightTop_vs_x")
AmpLeftOverAmpLeftandRightBot_vs_x = inputfile.Get("AmpLeftOverAmpLeftandRightBot_vs_x")
AmpTopOverAmpTopandBotRight_vs_y = inputfile.Get("AmpTopOverAmpTopandBotRight_vs_y")
AmpTopOverAmpTopandBotLeft_vs_y = inputfile.Get("AmpTopOverAmpTopandBotLeft_vs_y")

AmpRatio_list = [AmpLeftOverAmpLeftandRightTop_vs_x,AmpLeftOverAmpLeftandRightBot_vs_x,AmpTopOverAmpTopandBotRight_vs_y,AmpTopOverAmpTopandBotLeft_vs_y]     

#Define profile hist
AmpLeftOverAmpLeftandRightTop_vs_x_profile = AmpLeftOverAmpLeftandRightTop_vs_x.ProjectionY().Clone("AmpLeftOverAmpLeftandRightTop_vs_x_profile")
AmpLeftOverAmpLeftandRightBot_vs_x_profile = AmpLeftOverAmpLeftandRightBot_vs_x.ProjectionY().Clone("AmpLeftOverAmpLeftandRightBot_vs_x_profile")
AmpTopOverAmpTopandBotRight_vs_y_profile = AmpTopOverAmpTopandBotRight_vs_y.ProjectionY().Clone("AmpTopOverAmpTopandBotRight_vs_y_profile")
AmpTopOverAmpTopandBotLeft_vs_y_profile = AmpTopOverAmpTopandBotLeft_vs_y.ProjectionY().Clone("AmpTopOverAmpTopandBotLeft_vs_y_profile")

AmpRatio_profile_list = [AmpLeftOverAmpLeftandRightTop_vs_x_profile,AmpLeftOverAmpLeftandRightBot_vs_x_profile,AmpTopOverAmpTopandBotRight_vs_y_profile,AmpTopOverAmpTopandBotLeft_vs_y_profile]  

AmpRatio_Gaus_list = [0,0,0,0]
AmpRatio_Fit_list = [0,0,0,0] 

for l in range(len(AmpRatio_list)) : 

    AmpRatio = AmpRatio_list[l]
    AmpRatio_profile = AmpRatio_profile_list[l]
    
    canvas = TCanvas("cv"+str(l),"cv",800,800)
    
    #loop over  Amp1OverAmp1and2 bins
    for i in range(0, AmpRatio.GetYaxis().GetNbins() + 1):
        #print ("Bin " + str(i))
    
        ##For Debugging
        #if not (i==46 and j==5):
        #    continue
    
        tmpHist = AmpRatio.ProjectionX("px",i,i)
        myMean = tmpHist.GetMean()
        myRMS = tmpHist.GetRMS()
        nEntries = tmpHist.GetEntries()
        
        #if (l==2 or l==3) :
        #    tmpHist.Rebin(2)
        
        if(nEntries > 10.0):
            myGausFunction = TF1("mygaus","gaus(0)",-0.5,0.5);
            tmpHist.Fit(myGausFunction,"Q","",-0.5,0.5);
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
           
        AmpRatio_profile.SetBinContent(i,mean)
        AmpRatio_profile.SetBinError(i,meanErr)           
            
    # Save amplitude histograms

    if (l==0) :
        outputfile = TFile("positionRecoFitPlotsTop.root","RECREATE")   
    elif (l==1) :
        outputfile = TFile("positionRecoFitPlotsBot.root","RECREATE")  
    elif (l==2) :
        outputfile = TFile("positionRecoFitPlotsRight.root","RECREATE")
    else :
        outputfile = TFile("positionRecoFitPlotsLeft.root","RECREATE")
    
    xmin=0.18
    xmax=0.83
    ymin=-0.3
    ymax=0.3
   
    gStyle.SetOptFit(1011)
    fit = TF1("mainFit","pol3",xmin,xmax)
    AmpRatio_profile.Fit(fit,"","",xmin,xmax)

    htemp = TH1F("temp"+str(l),"",1,xmin,xmax)
    # htemp.GetYaxis().SetRangeUser(ymin,ymax)
    htemp.SetMaximum(ymax)
    htemp.SetMinimum(ymin)
    # htemp.GetXaxis().SetRangeUser(xmin,xmax)
    htemp.GetXaxis().SetTitle("Amplitude fraction")
    htemp.GetYaxis().SetTitle("Position [mm]")
    htemp.Draw("AXIS")
    
    stripWidth = 0.45
    pitch = 0.5
    boxes = []
    i=-0.25
    while i<=ymax+stripWidth/2:
        yt = i+stripWidth/2
        yl = i-stripWidth/2
        if yt>ymax: yt=ymax
        if yl<ymin: yl=ymin
        box = ROOT.TBox(xmin,yl, xmax,yt)
        box.SetFillColor(18)
        boxes.append(box)
        i+=pitch

    for box in boxes:
        box.Draw("same")
        
    fit.Draw("same")
    AmpRatio_profile.Draw("AXIS same")
    AmpRatio_profile.Draw("same")

    #line = TF1("line","0.0",xmin,1.0)
    #line.SetLineColor(ROOT.kBlack)
    #line.Draw("same")

    myStyle.BeamInfo()
    myStyle.SensorInfo(sensor, bias)
   
    if (l==0) : 
        canvas.SaveAs("PositionFitTop.pdf")
    elif (l==1)  :
        canvas.SaveAs("PositionFitBot.pdf")
    elif (l==2) :
        canvas.SaveAs("PositionFitRight.pdf")
    else :
        canvas.SaveAs("PositionFitLeft.pdf")

    AmpRatio_Gaus_list[l] = AmpRatio_profile   
    AmpRatio_Fit_list[l] = fit

    AmpRatio_profile.Write()
    fit.Write()
    outputfile.Close()

# #Graphing all four fit functioonss 
# canvas2 = TCanvas("cv2","cv2",800,800)

# xmin=0.18
# xmax=0.83

# outputfile = TFile("positionRecoFitPlotsAll.root","RECREATE")   

# AmpRatio_Gaus_list[0].SetMaximum(0.3)
# AmpRatio_Gaus_list[0].SetMinimum(-0.3)
# AmpRatio_Gaus_list[0].GetXaxis().SetRangeUser(xmin,xmax)
# AmpRatio_Gaus_list[0].SetLineColor(ROOT.kBlack)
# AmpRatio_Fit_list[0].SetLineColor(ROOT.kBlack)
# AmpRatio_Gaus_list[0].Draw()
# AmpRatio_Fit_list[0].Draw("same")


# AmpRatio_Gaus_list[1].SetLineColor(ROOT.kRed)
# AmpRatio_Fit_list[1].SetLineColor(ROOT.kRed)
# AmpRatio_Gaus_list[1].Draw("same")
# AmpRatio_Fit_list[1].Draw("same")

# AmpRatio_Gaus_list[2].SetLineColor(ROOT.kMagenta)
# AmpRatio_Fit_list[2].SetLineColor(ROOT.kMagenta)
# AmpRatio_Gaus_list[2].Draw("same")
# AmpRatio_Fit_list[2].Draw("same")

# AmpRatio_Gaus_list[3].SetLineColor(ROOT.kTeal-7)
# AmpRatio_Fit_list[3].SetLineColor(ROOT.kTeal-7)
# AmpRatio_Gaus_list[3].Draw("same")
# AmpRatio_Fit_list[3].Draw("same")

# leg = ROOT.TLegend(0.28, 0.2, 0.6, 0.3)
# leg.SetFillStyle(0)
# leg.SetBorderSize(0)
# leg.SetLineWidth(1)
# leg.SetNColumns(1)
# #leg.SetTextFont(42)
# leg.SetTextFont(font)
# leg.SetTextSize(tsize)
# leg.AddEntry(AmpRatio_Gaus_list[0], "AmpRight/(AmpRight+AmpLeft)_Top", "pl")
# leg.AddEntry(AmpRatio_Gaus_list[1], "AmpRight/(AmpRight+AmpLeft)_Bot", "pl")
# leg.AddEntry(AmpRatio_Gaus_list[2], "AmpTop/(AmpTop+AmpBottom)_Right", "pl")
# leg.AddEntry(AmpRatio_Gaus_list[3], "AmpTop/(AmpTop+AmpBottom)_Left", "pl")
# leg.Draw("same")


# canvas2.SaveAs("PositionFitAll.pdf")

# canvas2.Write()
# outputfile.Close()




