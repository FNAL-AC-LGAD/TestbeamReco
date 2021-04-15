from ROOT import TFile,TTree,TCanvas,TF1,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors
import array

##########################
#2D Efficiency 
##########################
def Plot2DEfficiency( num, den, plotname, topTitle, xAxisTitle, xAxisRangeLow, xAxisRangeHigh, yAxisTitle, yAxisRangeLow, yAxisRangeHigh, effMin, effMax ) :

    c = TCanvas("cv","cv",800,800)    

    ratio = num.Clone("ratio")
    ratio.Divide(den)

    ratio.SetTitle("")
    ratio.Draw("colz")
    ratio.SetMaximum(effMax)
    ratio.SetMinimum(effMin)
    ratio.GetZaxis().SetTitle("Efficiency")
    ratio.GetZaxis().SetTitleSize(0.05)
    ratio.GetZaxis().SetTitleOffset(1.0)
    ratio.Draw("colz")
    ratio.SetStats(0)
    ratio.GetXaxis().SetTitle(xAxisTitle)
    ratio.GetXaxis().SetTitleSize(0.05)
    ratio.GetXaxis().SetTitleOffset(0.90)
    ratio.GetXaxis().SetLabelSize(0.03)
    ratio.GetXaxis().SetRangeUser(xAxisRangeLow,xAxisRangeHigh)
    ratio.GetYaxis().SetTitle(yAxisTitle)
    ratio.GetYaxis().SetTitleSize(0.05)
    ratio.GetYaxis().SetTitleOffset(1.05)
    ratio.GetYaxis().SetLabelSize(0.03)
    ratio.GetYaxis().SetRangeUser(yAxisRangeLow,yAxisRangeHigh)
    c.SetRightMargin(0.18)
    c.SetLeftMargin(0.12)

    title = TLatex()
    title.SetTextSize(0.05);
    #title.SetTextAlign(13);  
    title.DrawLatexNDC(.2,.93,topTitle);
    c.SaveAs(plotname+".gif")



def NoisePlusLandauGaus(x, par) :

    #p_noise comes from a template histogram and is normalized to 1.0
    p_noise = 0
    if (x[0] >= 0 and x[0] < 2):
        p_noise = 0.0219891
    elif (x[0] >= 2 and x[0] < 4):
        p_noise = 0.120234
    elif (x[0] >= 4 and x[0] < 6):
        p_noise = 0.201533
    elif (x[0] >= 6 and x[0] < 8):
        p_noise = 0.208594
    elif (x[0] >= 8 and x[0] < 10):
        p_noise = 0.150293
    elif (x[0] >= 10 and x[0] < 12):
        p_noise = 0.103087
    elif (x[0] >= 12 and x[0] < 14):
        p_noise = 0.0691951
    elif (x[0] >= 14 and x[0] < 16):
        p_noise = 0.0490216
    elif (x[0] >= 16 and x[0] < 18):
        p_noise = 0.0344967
    elif (x[0] >= 18 and x[0] < 20):
        p_noise = 0.0217874
    elif (x[0] >= 20 and x[0] < 22):
        p_noise = 0.0117006
    elif (x[0] >= 22and x[0] < 24):
        p_noise = 0.00484164
    else :
        p_noise = 0.003228

    
    #p_landau = TMath.Landau(x[0],par[2],par[3],False)

    invsq2pi = 0.3989422804014;   # (2 pi)^(-1/2)
    mpshift  = -0.22278298;       # Landau maximum location    
    np = 500.0;      # number of convolution steps
    sc =   5.0;      # convolution extends to +-sc Gaussian sigmas


    #integral result
    sum = 0.0;

    #MP shift correction
    mpc = par[2] - mpshift * par[3];

    #Range of convolution integral
    xlow = x[0] - sc * par[4];
    xupp = x[0] + sc * par[4];
    step = (xupp-xlow) / np;

    #Convolution integral of Landau and Gaussian by sum
    for i in range(1, int(np/2)+1):
         xx = xlow + (i-.5) * step;
         fland = TMath.Landau(xx,mpc,par[3]) / par[3];
         sum += fland * TMath.Gaus(x[0],xx,par[4]);

         xx = xupp - (i-.5) * step;
         fland = TMath.Landau(xx,mpc,par[3]) / par[3];
         sum += fland * TMath.Gaus(x[0],xx,par[4]);

    p_landauGaus = step * sum * invsq2pi / par[4];


    return par[0]*( (1-par[1])*p_noise + par[1]*p_landauGaus)





def Plot1DEfficiencyWithFit( tree, plotname, topTitle, xAxisTitle, xAxisRangeLow, xAxisRangeHigh ) :

    #make amp histogram
    c = TCanvas("c","c", 800,800)

    ampHist = TH1F("ampHist",";Amplitude [mV]; Number of Events", 25,0,50)
    tree.Draw("amp[3]>>ampHist"," x_dut[2] > 19.6 && x_dut[2] < 19.7 && y_dut[2] > 23.5 && y_dut[2] < 24.0 && ((t_peak[3] - t_peak[0])*1e9 > 6 && (t_peak[3] - t_peak[0])*1e9  < 16)")
    
# create function for fitting
    fitFunction = TF1("NoisePlusLandauGaus",NoisePlusLandauGaus,0,50,5)

    fitFunction.SetParameters(10, 0.95, 20.0, 2.5, 3.0)
    fitFunction.SetParNames("a", "f", "mpv", "sigmaLandau", "sigmaGaus")
    #fitFunction.SetParLimits(0,   -1,   -4)
    #fitFunction.SetParLimits(1, 0.01,  0.2)
    #fitFunction.SetParLimits(2,    0,    2)
    #fitFunction.SetParLimits(3,    0, 1000)

    ampHist.Fit("NoisePlusLandauGaus")
    

    c.SaveAs("fit.gif")
    

    return

    nbins = num.GetXaxis().GetNbins()
    x = list()
    y = list()
    xErrLow = list()
    xErrHigh = list()
    yErrLow = list()
    yErrHigh = list()


    for b in range(1,nbins):

        xtemp = num.GetXaxis().GetBinCenter(b+1)
        xerrlow =  num.GetXaxis().GetBinCenter(b+1) - num.GetXaxis().GetBinLowEdge(b+1)  
        xerrhigh = num.GetXaxis().GetBinUpEdge(b+1) - num.GetXaxis().GetBinCenter(b+1)  

        ratio = 0
        errLow = 0
        errHigh = 0

        n1 = int(num.GetBinContent(b+1));
        n2 = int(den.GetBinContent(b+1));
        print ("numerator: " + str(n1) + " and denominator: " + str(n2))
        if (n1 > n2):
            n1 = n2;

        if (n2>0) :
          ratio = float(n1)/float(n2);
          if (ratio > 1) :
              ratio = 1;
          errLow = ratio - TEfficiency.ClopperPearson(n2, n1, 0.68269, False);
          errHigh = TEfficiency.ClopperPearson(n2, n1, 0.68269, True) - ratio;
    

        print (" done bin " + str(b) + " " + str(xtemp) + " : " + str(n1) + "(" + str(num.GetBinContent(b+1)) + ")" + " / " + str(n2) + "(" + str(den.GetBinContent(b+1)) + ")" + " = " + str(ratio) + " " + str(errLow) + " " + str(errHigh))
        ytemp = ratio
        yerrlowtemp = errLow
        yerrhightemp = errHigh
      
        print ("x: " + str(xtemp) + " and y: " + str(ytemp))

        x.append(xtemp);  
        y.append(ytemp); 
        xErrLow.append(xerrlow);
        xErrHigh.append(xerrhigh);
        yErrLow.append(yerrlowtemp);
        yErrHigh.append(yerrhightemp);
    
    c = TCanvas("cv","cv",800,800)    
    c.SetLeftMargin(0.12)

    #must convert list into array for TGraphAsymmErrors to work
    xArr = array.array('f',x)
    yArr = array.array('f',y)
    xErrLowArr = array.array('f',xErrLow)
    xErrHighArr = array.array('f',xErrHigh)
    yErrLowArr = array.array('f',yErrLow)
    yErrHighArr = array.array('f',yErrHigh)

    effGraph = TGraphAsymmErrors(nbins, xArr, yArr, xErrLowArr, xErrHighArr, yErrLowArr,yErrHighArr );
    effGraph.Draw("APE")
    effGraph.SetTitle("")
    effGraph.GetXaxis().SetTitle(xAxisTitle)
    effGraph.GetXaxis().SetTitleSize(0.05)
    effGraph.GetXaxis().SetTitleOffset(0.90)
    effGraph.GetXaxis().SetLabelSize(0.03)
    effGraph.GetXaxis().SetRangeUser(xAxisRangeLow,xAxisRangeHigh)
    effGraph.GetYaxis().SetTitle("Efficiency")
    effGraph.GetYaxis().SetTitleSize(0.05)
    effGraph.GetYaxis().SetTitleOffset(1.05)
    effGraph.GetYaxis().SetLabelSize(0.03)

    title = TLatex()
    title.SetTextSize(0.05);
    title.DrawLatexNDC(.2,.93,topTitle);
    c.Update()
    c.SaveAs(plotname+".gif")


##############################################################################
#1D Efficiency including bkg subtraction with amplitude histogram
# We purify the signal sample by requiring that signals fall inside a window:
# ((t_peak[3] - t_peak[0])*1e9 > 6 && (t_peak[3] - t_peak[0])*1e9  < 16)
# The efficiency of the time window cut on signal is measured to be 98.9% - using large-sized signals
# From this dataset: /eos/uscms/store/user/cmstestbeam/2019_04_April_CMSTiming/KeySightScope/RecoData/TimingDAQRECO/RecoWithTracks/v6_CACTUSSkim/Completed/Data_CACTUSAnalog_Pixel5_3_16216-16263.root
# Using this command: 
# pulse->Draw("((t_peak[3] - t_peak[0])*1e9 > 6 && (t_peak[3] - t_peak[0])*1e9  < 16)","(x_dut[2] > 19.6 && x_dut[2] < 20.4 && y_dut[2] > 23.6 && y_dut[2] < 23.9) && amp[3] > 20")
# Therefore we increase the measured efficiency by 1.1% to correct for the inefficiency of the time window ct
##############################################################################

def Plot1DEfficiencyWithBkgSubtraction( tree, num, den, axis, pixel, plotname, topTitle, xAxisTitle, xAxisRangeLow, xAxisRangeHigh ) :

    #make amp histogram
    c = TCanvas("c","c", 800,800)

    #Each pixel has slightly different time distribution and efficiency of time window cut differs a bit
    #We derive corresponding efficiency corrections for each pixel 
    timeWindowCutEfficiency = 1.0
    if (pixel == "5_3"):
        timeWindowCutEfficiency = 0.989
    if (pixel == "5_4"):
        timeWindowCutEfficiency = 0.9478
    if (pixel == "5_10"):
        timeWindowCutEfficiency = 0.9643

    #ampHist = TH1F("ampHist",";Amplitude [mV]; Number of Events", 25,0,50)
    #tree.Draw("amp[3]>>ampHist"," x_dut[2] > 19.6 && x_dut[2] < 19.7 && y_dut[2] > 23.5 && y_dut[2] < 24.0 && ((t_peak[3] - t_peak[0])*1e9 > 6 && (t_peak[3] - t_peak[0])*1e9  < 16)")
    
    nbins = num.GetXaxis().GetNbins()
    x = list()
    y = list()
    xErrLow = list()
    xErrHigh = list()
    yErrLow = list()
    yErrHigh = list()

    for b in range(1,nbins):

        xtemp = num.GetXaxis().GetBinCenter(b+1)
        xerrlow =  num.GetXaxis().GetBinCenter(b+1) - num.GetXaxis().GetBinLowEdge(b+1)  
        xerrhigh = num.GetXaxis().GetBinUpEdge(b+1) - num.GetXaxis().GetBinCenter(b+1)  

        #Noise templates: 
        #Pixel 5,3 : amp <= 6mV gives 0.4417 of the total and has 0 signal contamination
        #Pixel 5,4 : amp <= 10mV gives 0.0404 of the total and has 0 signal contamination
        #Pixel 5,10 : amp < gives 0. of the total and has 0 signal contamination
        #We will assume that bins 0+1+2 (0-6mV) do not contain ANY signal.
        #We count the number of events in those bins and divide by 0.4417 to get
        #the total number of noise events. We subtract those from the numerator.

        #Noise template is made from this data (outside of sensor region AND outside of time window):  
        #/eos/uscms/store/user/cmstestbeam/2019_04_April_CMSTiming/KeySightScope/RecoData/TimingDAQRECO/RecoWithTracks/v6_CACTUSSkim/Completed/Data_CACTUSAnalog_Pixel5_3_16216-16263.root
        #pulse->Draw("amp[3]>>ampHist(25,0,50)","!(x_dut[2] > 19.4 && x_dut[2] < 20.6 && y_dut[2] > 23.4 && y_dut[2] < 24.1) && !((t_peak[3] - t_peak[0])*1e9 > 6 && (t_peak[3] - t_peak[0])*1e9  < 16)")

        noiseSelection = ""
        noiseSelectionCRFraction = 1
        xPositionSelection = ""
        yPositionSelection = ""
        if (pixel == "5_3"):
            noiseSelection = " && amp[3] <= 6"
            noiseSelectionCRFraction = 0.4417
            xPositionSelection = " && x_dut[2] > 19.5 && x_dut[2] < 20.5 "
            yPositionSelection = " && y_dut[2] > 23.5 && y_dut[2] < 24.0 "
        if (pixel == "5_4"):
            noiseSelection = " && amp[3] <= 14"
            noiseSelectionCRFraction = 0.4053
            xPositionSelection = " && x_dut[2] > 18.5 && x_dut[2] < 19.5 "
            yPositionSelection = " && y_dut[2] > 23.5 && y_dut[2] < 24.0 "
        if (pixel == "5_10"):
            noiseSelection = " && amp[3] <= 13"
            noiseSelectionCRFraction = 0.3802
            xPositionSelection = " && x_dut[2] > 19.5 && x_dut[2] < 20.5 "
            yPositionSelection = " && y_dut[2] > 23.0 && y_dut[2] < 23.5 "

        print ("noise selection = " + noiseSelection + " " + str(noiseSelectionCRFraction))

        positionSelectionString = ""
        if (axis == "x"):
            positionSelectionString = " && x_dut[2] > "+str(num.GetXaxis().GetBinLowEdge(b+1))+ " && x_dut[2] < " + str(num.GetXaxis().GetBinUpEdge(b+1)) + yPositionSelection
        if (axis == "y"):
            positionSelectionString = xPositionSelection + " && y_dut[2] > "+str(num.GetXaxis().GetBinLowEdge(b+1))+ " && y_dut[2] < " + str(num.GetXaxis().GetBinUpEdge(b+1)) + " "


        print ("numerator: " + "ntracks==1 && y_dut[0] > 0 && npix>0 && nback>0 " + positionSelectionString + " && ((t_peak[3] - t_peak[0])*1e9 > 6 && (t_peak[3] - t_peak[0])*1e9  < 16)")


        ampHist = TH1F("ampHist"+"_"+str(b),";Amplitude [mV]; Number of Events", 25,0,50)
        denominatorCount = tree.GetEntries("ntracks==1 && y_dut[0] > 0 && npix>0 && nback>0 " + positionSelectionString + " ")
        tmpNumeratorTotalCount = tree.GetEntries("ntracks==1 && y_dut[0] > 0 && npix>0 && nback>0 " + positionSelectionString + " && ((t_peak[3] - t_peak[0])*1e9 > 6 && (t_peak[3] - t_peak[0])*1e9  < 16)")
        tmpNumeratorNoiseControlRegionCount = tree.GetEntries("ntracks==1 && y_dut[0] > 0 && npix>0 && nback>0 " + positionSelectionString + " && ((t_peak[3] - t_peak[0])*1e9 > 6 && (t_peak[3] - t_peak[0])*1e9  < 16) " + noiseSelection)
        tmpNumeratorSignalCount = tmpNumeratorTotalCount - tmpNumeratorNoiseControlRegionCount / noiseSelectionCRFraction

        print ("ntracks==1 && y_dut[0] > 0 && npix>0 && nback>0 " + positionSelectionString + " && ((t_peak[3] - t_peak[0])*1e9 > 6 && (t_peak[3] - t_peak[0])*1e9  < 16) " + noiseSelection)

        ratio = 0
        errLow = 0
        errHigh = 0

        n1 = int(tmpNumeratorSignalCount);
        n2 = int(denominatorCount);
        print ("numerator: " + str(n1) + " and denominator: " + str(n2))
        if (n1 > n2):
            n1 = n2;

        if (n2>0) :
          ratio = float(n1)/float(n2);
          if (ratio > 1) :
              ratio = 1;
          errLow = ratio - TEfficiency.ClopperPearson(n2, n1, 0.68269, False);
          errHigh = TEfficiency.ClopperPearson(n2, n1, 0.68269, True) - ratio;
    

        print (" done bin " + str(b) + " : " + str(num.GetXaxis().GetBinLowEdge(b+1)) + " - " + str(num.GetXaxis().GetBinUpEdge(b+1)))
        print (" num = " + str(n1)+" = " + str(tmpNumeratorTotalCount) + " - " + str(tmpNumeratorNoiseControlRegionCount) + " / " + str(noiseSelectionCRFraction) + " | den = " + str(n2) )
        print ("ratio = " + str(ratio) + " " + str(errLow) + " " + str(errHigh))
        ytemp = ratio / timeWindowCutEfficiency #here we correct for the time window cut inefficiency
        yerrlowtemp = errLow
        yerrhightemp = errHigh
      
        print ("x: " + str(xtemp) + " and y: " + str(ytemp))

        x.append(xtemp);  
        y.append(ytemp); 
        xErrLow.append(xerrlow);
        xErrHigh.append(xerrhigh);
        yErrLow.append(yerrlowtemp);
        yErrHigh.append(yerrhightemp);
    
    c = TCanvas("cv","cv",800,800)    
    c.SetLeftMargin(0.12)

    #must convert list into array for TGraphAsymmErrors to work
    xArr = array.array('f',x)
    yArr = array.array('f',y)
    xErrLowArr = array.array('f',xErrLow)
    xErrHighArr = array.array('f',xErrHigh)
    yErrLowArr = array.array('f',yErrLow)
    yErrHighArr = array.array('f',yErrHigh)

    effGraph = TGraphAsymmErrors(nbins, xArr, yArr, xErrLowArr, xErrHighArr, yErrLowArr,yErrHighArr );
    effGraph.Draw("APE")
    effGraph.SetTitle("")
    effGraph.GetXaxis().SetTitle(xAxisTitle)
    effGraph.GetXaxis().SetTitleSize(0.05)
    effGraph.GetXaxis().SetTitleOffset(0.90)
    effGraph.GetXaxis().SetLabelSize(0.03)
    effGraph.GetXaxis().SetRangeUser(xAxisRangeLow,xAxisRangeHigh)
    effGraph.GetYaxis().SetTitle("Efficiency")
    effGraph.GetYaxis().SetTitleSize(0.05)
    effGraph.GetYaxis().SetTitleOffset(1.05)
    effGraph.GetYaxis().SetLabelSize(0.03)

    title = TLatex()
    title.SetTextSize(0.05);
    title.DrawLatexNDC(.2,.93,topTitle);
    c.Update()
    c.SaveAs(plotname+".gif")





##########################
#1D Efficiency 
##########################
def Plot1DEfficiency( num, den, plotname, topTitle, xAxisTitle, xAxisRangeLow, xAxisRangeHigh ) :

    nbins = num.GetXaxis().GetNbins()
    x = list()
    y = list()
    xErrLow = list()
    xErrHigh = list()
    yErrLow = list()
    yErrHigh = list()


    for b in range(1,nbins):

        xtemp = num.GetXaxis().GetBinCenter(b+1)
        xerrlow =  num.GetXaxis().GetBinCenter(b+1) - num.GetXaxis().GetBinLowEdge(b+1)  
        xerrhigh = num.GetXaxis().GetBinUpEdge(b+1) - num.GetXaxis().GetBinCenter(b+1)  

        ratio = 0
        errLow = 0
        errHigh = 0

        n1 = int(num.GetBinContent(b+1));
        n2 = int(den.GetBinContent(b+1));
        print ("numerator: " + str(n1) + " and denominator: " + str(n2))
        if (n1 > n2):
            n1 = n2;

        if (n2>0) :
          ratio = float(n1)/float(n2);
          if (ratio > 1) :
              ratio = 1;
          errLow = ratio - TEfficiency.ClopperPearson(n2, n1, 0.68269, False);
          errHigh = TEfficiency.ClopperPearson(n2, n1, 0.68269, True) - ratio;
    

        print (" done bin " + str(b) + " " + str(xtemp) + " : " + str(n1) + "(" + str(num.GetBinContent(b+1)) + ")" + " / " + str(n2) + "(" + str(den.GetBinContent(b+1)) + ")" + " = " + str(ratio) + " " + str(errLow) + " " + str(errHigh))
        ytemp = ratio
        yerrlowtemp = errLow
        yerrhightemp = errHigh
      
        print ("x: " + str(xtemp) + " and y: " + str(ytemp))

        x.append(xtemp);  
        y.append(ytemp); 
        xErrLow.append(xerrlow);
        xErrHigh.append(xerrhigh);
        yErrLow.append(yerrlowtemp);
        yErrHigh.append(yerrhightemp);
    
    c = TCanvas("cv","cv",800,800)    
    c.SetLeftMargin(0.12)

    #must convert list into array for TGraphAsymmErrors to work
    xArr = array.array('f',x)
    yArr = array.array('f',y)
    xErrLowArr = array.array('f',xErrLow)
    xErrHighArr = array.array('f',xErrHigh)
    yErrLowArr = array.array('f',yErrLow)
    yErrHighArr = array.array('f',yErrHigh)

    effGraph = TGraphAsymmErrors(nbins, xArr, yArr, xErrLowArr, xErrHighArr, yErrLowArr,yErrHighArr );
    effGraph.Draw("APE")
    effGraph.SetTitle("")
    effGraph.GetXaxis().SetTitle(xAxisTitle)
    effGraph.GetXaxis().SetTitleSize(0.05)
    effGraph.GetXaxis().SetTitleOffset(0.90)
    effGraph.GetXaxis().SetLabelSize(0.03)
    effGraph.GetXaxis().SetRangeUser(xAxisRangeLow,xAxisRangeHigh)
    effGraph.GetYaxis().SetTitle("Efficiency")
    effGraph.GetYaxis().SetTitleSize(0.05)
    effGraph.GetYaxis().SetTitleOffset(1.05)
    effGraph.GetYaxis().SetLabelSize(0.03)

    title = TLatex()
    title.SetTextSize(0.05);
    title.DrawLatexNDC(.2,.93,topTitle);
    c.Update()
    c.SaveAs(plotname+".gif")


def Make1DEfficiency( num, den, plotname, topTitle, xAxisTitle, xAxisRangeLow, xAxisRangeHigh ) :

    nbins = num.GetXaxis().GetNbins()
    x = list()
    y = list()
    xErrLow = list()
    xErrHigh = list()
    yErrLow = list()
    yErrHigh = list()


    for b in range(1,nbins):

        xtemp = num.GetXaxis().GetBinCenter(b+1)
        xerrlow =  num.GetXaxis().GetBinCenter(b+1) - num.GetXaxis().GetBinLowEdge(b+1)  
        xerrhigh = num.GetXaxis().GetBinUpEdge(b+1) - num.GetXaxis().GetBinCenter(b+1)  

        ratio = 0
        errLow = 0
        errHigh = 0

        n1 = int(num.GetBinContent(b+1));
        n2 = int(den.GetBinContent(b+1));
        print ("numerator: " + str(n1) + " and denominator: " + str(n2))
        if (n1 > n2):
            n1 = n2;

        if (n2>0) :
          ratio = float(n1)/float(n2);
          if (ratio > 1) :
              ratio = 1;
          errLow = ratio - TEfficiency.ClopperPearson(n2, n1, 0.68269, False);
          errHigh = TEfficiency.ClopperPearson(n2, n1, 0.68269, True) - ratio;
    

        print (" done bin " + str(b) + " " + str(xtemp) + " : " + str(n1) + "(" + str(num.GetBinContent(b+1)) + ")" + " / " + str(n2) + "(" + str(den.GetBinContent(b+1)) + ")" + " = " + str(ratio) + " " + str(errLow) + " " + str(errHigh))
        ytemp = ratio
        yerrlowtemp = errLow
        yerrhightemp = errHigh
      
        print ("x: " + str(xtemp) + " and y: " + str(ytemp))

        x.append(xtemp);  
        y.append(ytemp); 
        xErrLow.append(xerrlow);
        xErrHigh.append(xerrhigh);
        yErrLow.append(yerrlowtemp);
        yErrHigh.append(yerrhightemp);
    
    c = TCanvas("cv","cv",800,800)    
    c.SetLeftMargin(0.12)

    #must convert list into array for TGraphAsymmErrors to work
    xArr = array.array('f',x)
    yArr = array.array('f',y)
    xErrLowArr = array.array('f',xErrLow)
    xErrHighArr = array.array('f',xErrHigh)
    yErrLowArr = array.array('f',yErrLow)
    yErrHighArr = array.array('f',yErrHigh)

    effGraph = TGraphAsymmErrors(nbins-1, xArr, yArr, xErrLowArr, xErrHighArr, yErrLowArr,yErrHighArr );
    effGraph.Draw("APE")
    effGraph.SetTitle("")
    effGraph.GetXaxis().SetTitle(xAxisTitle)
    effGraph.GetXaxis().SetTitleSize(0.05)
    effGraph.GetXaxis().SetTitleOffset(0.90)
    effGraph.GetXaxis().SetLabelSize(0.03)
    effGraph.GetXaxis().SetRangeUser(xAxisRangeLow,xAxisRangeHigh)
    effGraph.GetYaxis().SetTitle("Efficiency")
    effGraph.GetYaxis().SetTitleSize(0.05)
    effGraph.GetYaxis().SetTitleOffset(1.05)
    effGraph.GetYaxis().SetLabelSize(0.03)

    title = TLatex()
    title.SetTextSize(0.05);
    title.DrawLatexNDC(.2,.93,topTitle);

    return effGraph
