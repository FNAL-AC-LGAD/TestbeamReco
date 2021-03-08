import argparse
import math
import os

import ROOT

################################################################################

class LanGausFit:
    """LanGausFit fits Landau convoluted with Gaussian to a ROOT histogram.

    A simple example:
    histogram = ROOT.TH1D("hist", "hist", 100, 0.0, 10.)
    # fill histogram
    fit = LanGausFit()
    func = fit.fit(histogram)
    func.Print()
    """
    def __init__(self):
        self._loadlib()
        self._tf1 = None

    def fit(self, histogram, fitrange=None, startwidth=None, startmpv=None, startnorm=None, startsigma=None):
        """Fit Lan+Gaus function to a histogram.
        
        histogram must be of type TH1D (the D is important, errors will be thrown with a TH1F.)
        You can optionally provide the starting fit parameters. If not provided they will be automatically calculated.
        """
        # get fit starting parameters and fit range
        startwidth, startmpv, startnorm, startsigma = self._getstartingparameters(histogram, startwidth, startmpv, startnorm, startsigma)
        if not fitrange:
            fitrange = self._autofitrange(histogram)
        # create function
        xlow, xhigh = fitrange
        tf1 = ROOT.TF1("landaugausfunction", ROOT.langaufun, xlow, xhigh, 4)
        tf1.SetParNames("LandauWidth","LandauMPV","Normalisation","GaussianSigma")
        tf1.SetParameters(startwidth, startmpv, startnorm, startsigma)
        # run fit
        histogram.Fit(tf1, "Q0L", "", xlow, xhigh)
        # store the function object and return it
        self._tf1 = tf1
        return tf1

    def _loadlib(self):
        try:
            #try to load the function
            ROOT.langaufun
        except AttributeError:
            #try to compile the function
            pkgdir = os.path.dirname(__file__)
            if len(pkgdir) == 0:
                pkgdir = "."
            path = os.sep.join((pkgdir, "langaus.C"))
            path = os.path.abspath(path)
            if not os.path.exists(path):
                raise Exception("ERROR: file does not exist ", path)
            ROOT.gROOT.ProcessLine(".L " + path +"+")
        return

    def _getstartingparameters(self, hist, startwidth, startmpv, startnorm, startsigma):
        rms = hist.GetRMS()
        peakpos = hist.GetXaxis().GetBinCenter(hist.GetMaximumBin())
        if startwidth is None:
            startwidth = rms / 5.0
        if startmpv is None:
            startmpv = peakpos
        if startnorm is None:
            startnorm = hist.Integral()
        if startsigma is None:
            startsigma = rms / 10.0
        return startwidth, startmpv, startnorm, startsigma

    def _findlevel(self, l, hist):
        for ii in xrange(hist.GetNbinsX()):
            if hist.GetBinContent(ii + 1) >= l:
                break
        return hist.GetXaxis().GetBinCenter(ii + 1)

    def _autofitrange(self, hist, lowpercentile=0.05, highpercentile=0.9):
        #calculate cumulative histogram
        cumhist = hist.Clone()
        cumhist.Set(hist.GetNbinsX() + 2, hist.GetIntegral())
        #find low and high percentile values
        xlow = self._findlevel(lowpercentile, cumhist)
        xhigh = self._findlevel(highpercentile, cumhist)
        return (xlow, xhigh)

################################################################################

def _generate(mpv, gaussigma, landauwidth, nevents, xlow, xhigh, seed=20313):
    hist = ROOT.TH1D("data", "data;x;num events", 100, xlow, xhigh)
    #fill histogram with random events
    rand = ROOT.TRandom3(seed)
    for _ in xrange(nevents):
        expected = rand.Landau(mpv, landauwidth)
        smeared = rand.Gaus(expected, gaussigma)
        hist.Fill(smeared)
    return hist

################################################################################

def _plot(data, func, outputfilename):
    canv = ROOT.TCanvas(outputfilename, outputfilename, 800, 600)
    data.Draw()
    func.Draw("SAME")
    canv.SaveAs(outputfilename)
    return

################################################################################

def _testfit(args):
    data = _generate(mpv=args.mpv, gaussigma=args.sigma, landauwidth=args.width, nevents=args.nevents, xlow=args.xlow, xhigh=args.xhigh)
    fitter = LanGausFit()
    func = fitter.fit(data)
    _plot(data, func, args.output)
    return

################################################################################

def parsecml():
    parser = argparse.ArgumentParser("Test script for LanGaus fit.")
    parser.add_argument("--mpv", help="Generate data with this Landau MPV", default=10.0, type=float)
    parser.add_argument("--sigma", help="Generate data with this Gaussian sigma", default=1.0, type=float)
    parser.add_argument("--width", help="Generate data with this Landau width.", default=1.0, type=float)
    parser.add_argument("--nevents", help="Generate this many events.", default=10000, type=int)
    parser.add_argument("--xlow", help="Plot min x value", default=0.0, type=float)
    parser.add_argument("--xhigh", help="Plot max x value", default=100.0, type=float)
    parser.add_argument("-o", "--output", help="Output plot file name.", default="testlangaus.eps", type=str)
    return parser.parse_args()

def main():
    args = parsecml()
    _testfit(args)
    return

if __name__ == "__main__":
    main()
