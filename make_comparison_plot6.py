from glob import glob

import ROOT
from ROOT import TH1F, gStyle, TCanvas, TLegend, TFile, gROOT, TPad, TLatex, TF1

import copy
from math import sqrt
from array import array

def getHistogram(oneHistName):
    inputDir="/afs/cern.ch/user/p/pewang/public/Project/VHbbTruthAnalysis2/run/hist_generated/*.root"

    hists = []
    for i,filename in enumerate(sorted(glob(inputDir))):
        print filename
        f1=TFile(filename, 'R')
        h=f1.Get(oneHistName)
        hists.append(copy.deepcopy(h))
    return hists


def getMergeBins(hist):
    FracError = 0.01
    integral = 0.0
    error2 = 0.0
    Nbins = hist.GetNbinsX()
    startbin = Nbins
    currentbin = Nbins
    binedges = [hist.GetBinCenter(Nbins) + hist.GetBinWidth(Nbins)]

    for iBin in range (Nbins,0,-1):
        integral += hist.GetBinContent(iBin)
        error2 += hist.GetBinError(iBin)**2
        if (integral == 0 or error2 == 0): continue
        if iBin == 1:
            binedges.append(hist.GetBinCenter(iBin) - hist.GetBinWidth(iBin) / 2)
        elif ((sqrt(error2)/integral) < FracError):
            binedges.append(hist.GetBinCenter(iBin) - hist.GetBinWidth(iBin) / 2)
            integral = 0.0
            error2 = 0.0

    binedges.sort()

    return binedges


def getRangeFromHist(hist):
    name = hist.GetName()
    xmin = 0
    xmax = 500
    if "2jet" in name:
        if "mBB" in name:
            xmax = 450
        elif "pTV" in name:
            xmin = 150
            xmax = 400
        elif "dRBB" in name:
            xmax = 6
    elif "3jet" in name:
        if "mBB" in name:
            xmax = 450
        elif "pTV" in name:
            xmin = 150
            xmax = 450
        elif "dRBB" in name:
            xmax = 6

    upperbin = hist.GetXaxis().FindBin(xmax)
    upper = hist.GetBinCenter(upperbin) + hist.GetBinWidth(upperbin) / 2

    lowerbin = hist.GetXaxis().FindBin(xmin)
    lower = hist.GetBinCenter(lowerbin) - hist.GetBinWidth(lowerbin) / 2

    return lower,upper


def makeComparisonHistogram(oneHistName, histograms):
    gStyle.SetOptStat(0)
#    if 'WhfSR' not in oneHistName:
    gROOT.SetBatch(ROOT.kTRUE)
    # canvas->SetBatch(kTRUE);
    # print type(histograms)
    # print len(histograms)
    print oneHistName

    c1 = TCanvas( 'c1', 'Example',700, 500 )
    colors = [2,1,3,4,6]
    leg = TLegend(0.6, 0.6, 0.9, 0.9)
    sampleName=["aMc@NloPythia8EvtGen_A14N23LO_ttbar 410225", "PowhegPythia8EvtGen_A14_ttbar_hdamp258p75 (nominal)", "PowhegPythia8EvtGen_ttbar_hdamp517p5 410511", "PowhegPythia8EvtGen_ttbar_hdamp258p75 410512", "PowhegHerwig7EvtGen_H7UE_tt_hdamp258p75 410525"]

    pad1 = TPad("pad1", "up", 0., 0.5, 1., 1.)
    pad1.SetBottomMargin(0)
    pad1.SetLeftMargin(0.11)
    pad1.SetGridy()
    pad1.SetGridx()
    pad1.Draw()

    pad2 = TPad("pad2", "down", 0., 0., 1., 0.5)
    pad2.SetTopMargin(0)
    pad2.SetBottomMargin(0.2)
    pad2.SetLeftMargin(0.11)
    pad2.SetGridy()
    pad2.SetGridx()
    pad2.Draw()
    
    pad1.cd()

    # get merging bin option from niminal
    bins=getMergeBins(histograms[1])
    binnum=len(bins)-1
    edge = array('d', bins)

    # get x-axis range for the histograms
    xmin,xmax = getRangeFromHist(histograms[0])

    # plot shape comparison
    hNewHists = []

    for i, h in enumerate(histograms):
        hNew = h.Rebin(binnum,h.GetName(),edge)
        hNew.SetLineColor(colors[i])
        hNew.SetMarkerColor(colors[i])
        hNew.Scale(1/hNew.Integral())
        print "xmin, xmax: ", xmin, xmax
        hNew.GetXaxis().SetRangeUser(xmin, xmax)
        # histNameTemp = hNew.GetName()
        # print histNameTemp
        # if "WhfSR_mBB" in histNameTemp:
        #     # hNew.GetXaxis().SetRangeUser(0, 300)
        #     hNew.GetYaxis().SetRangeUser(-0.001, 0.025)
        # if "WhfSR_pTV" in histNameTemp:
        #     # hNew.GetXaxis().SetRangeUser(0, 500)
        #     hNew.GetYaxis().SetRangeUser(-0.001, 0.040)
        # if "WhfSR_MET" in histNameTemp:
        #     # hNew.GetXaxis().SetRangeUser(0, 350)
        #     hNew.GetYaxis().SetRangeUser(-0.001, 0.020)
        hNew.SetTitle("")
        hNew.GetYaxis().SetTitle("arbitrary unit")
        hNew.GetYaxis().SetTitleOffset(1.0)
        hNewHists.append(hNew.Clone())

        leg.AddEntry(hNew,sampleName[i])
        option="" if i==0 else "same"
        hNew.Draw(option)
        c1.Update()

    lt = TLatex()     
    lt.SetNDC()     
    lt.SetTextSize(lt.GetTextSize() * 1.1)     
    titleName = oneHistName
    lt.DrawLatex(0.1275, 0.89, titleName[:-8])

    pad2.cd()

    # make ratio plot
    # hNewHists are copied from the last step; the settings from the last step are also copied
    for i, h in enumerate(hNewHists):
        hNewHists[i].GetYaxis().SetTitle("ratio")
        hNewHists[i].GetYaxis().SetRangeUser(0, 1.9)
        option="" if i==0 else "same"
        if i != 1: # skip the norminal
            h.Divide(hNewHists[1])
            h.Draw(option)


    # ratiosOld = []

    # for i, h in enumerate(histograms):
    #     ratiosOld.append(h.Clone())

    #     ratiosOld[i].Divide(histograms[1])
    #     # ratiosOld[i].SetTitle("")
    #     ratiosOld[i].GetYaxis().SetTitle("ratio")
    #     ratiosOld[i].GetYaxis().SetRangeUser(0.6, 1.55)
    #     option="" if i==0 else "same"
    #     if i != 1: # skip the norminal
    #         ratiosOld[i].Draw(option)


    # define fit fuction for mBB and pTV from EPS 2017
    fitFunctionmBB = "x<500 ? [0] + [1] * exp([2] * x) : [0] + [1] * exp([2] * 500)"
    fitFunctionpTV = "x<500 ? [0] + [1] * x : [0] + [1] * 500"

    # fit ratio plot
        
    # for i, ratio in enumerate(ratios):
    #     if i == 1: continue

    #     ratioName = ratio.GetName()
    #     if "WhfCR" in ratioName:
    #         continue

    #     # fitOpt = ROOT.Math.MinimizerOptions()
    #     # fitOpt.SetStrategy(2)

    #     if "mBB" in ratioName:
    #         # the following are the initialization
    #         func=TF1("f_Systtbar_mBB_1lep", fitFunctionmBB, 0, 500)
    #         func.SetParameter(0, 0.917)
    #         func.SetParameter(1, 0.389)
    #         func.SetParameter(2, -0.0138) # in 1/GeV
    #         # func.SetParLimits(1, -10, 10)
    #         # func.SetParLimits(
    #     elif "pTV" in ratioName:
    #         func=TF1("f_SysTTbarPTV_01lep", fitFunctionpTV, 0, 500)
    #         # the following are the initialization
    #         func.SetParameter(0, 1.09)
    #         func.SetParameter(1, -0.0005)# in 1/GeV
    #     else: continue

    #     func.SetLineColor(colors[i])

    #     colorNames = {1 : "black",
    #                   2 : "red",
    #                   3 : "green",
    #                   4 : "blue",
    #                   5 : "yellow",
    #                   6 : "pink",
    #                   }

    #     print "Fitting to", ratioName[:-8], colorNames[colors[i]]
    #     ratio.Fit(func)

    #     if i != 1: # skip the norminal
    #         func.DrawCopy('same')

    #     print func.GetNDF()
    #     if func.GetNDF() != 0:
    #         print "Chisquare", func.GetChisquare()/func.GetNDF()


    # plot EPS shape
    if "mBB" in oneHistName:
        func=TF1("f_Systtbar_mBB_1lep", fitFunctionmBB, 0, 1000)
        func.SetParameter(0, 0.917)
        func.SetParameter(1, 0.389)
        func.SetParameter(2, -0.0138) # in 1/GeV
        func.SetLineStyle(2)
        leg.AddEntry(func,"EPS")
        func.Draw('same')

    if "pTV" in oneHistName:
        func=TF1("f_SysTTbarPTV_1lep", fitFunctionpTV, 0, 1000)
        # the following are the initialization
        func.SetParameter(0, 1.09)
        func.SetParameter(1, -0.0005)# in 1/GeV
        func.SetLineStyle(2)
        leg.AddEntry(func,"EPS")
        func.Draw('same')

    pad1.cd()
    leg.Draw("same")

    # if 'WhfSR' in oneHistName:
    # raw_input("Press enter to save the image")
    c1.SaveAs("./plot_comparison_generated/" + oneHistName + ".eps")


def getHistName():
    nameSec0 = ['hist']
    nameSec1 = ['1Lep']
    nameSec2 = ['ttbar']
    nameSec3 = ['2tag2jet', '2tag3jet']
    nameSec4 = ['75_150ptv', '150ptv']
    nameSec5 = ['WhfSR', 'WhfCR']
    nameSec6 = ['BDT', 'mBB', 'pTV', 'Mtop', 'dRBB', 'pTB1', 'pTB2', 'MET', 'mTW', 'dPhiVBB', 'dPhiLBmin', 'dYWH']
    # 'pTJ3' - program crashes with error:
    # AttributeError: 'TObject' object has no attribute 'Rebin'
    # 'mBBJ' - program crashes with error:
    # AttributeError: 'TObject' object has no attribute 'Rebin'
    # 'dPhiLepMET' - not in the latest VHTruth framework

    nameSec7 = ['Nominal']

    histName = []
    for i0, i1, i2, i3, i4, i5, i6, i7 in [(i0, i1, i2, i3, i4, i5, i6, i7) for i0 in nameSec0 for i1 in nameSec1 for i2 in nameSec2 for i3 in nameSec3 for i4 in nameSec4 for i5 in nameSec5 for i6 in nameSec6 for i7 in nameSec7]:
        histName.append(i0 + "_" +  i1 + "_" + i2 + "_" + i3 + "_" + i4 + "_" + i5 + "_" + i6 + "_" + i7)
    return histName


def main():

    ROOT.gROOT.LoadMacro("./AtlasStyleBase/AtlasStyle.C") 
    ROOT.gROOT.LoadMacro("./AtlasStyleBase/AtlasUtils.C") 
    ROOT.SetAtlasStyle()

    histNameList = getHistName()
    for histName in histNameList:
        histList = getHistogram(histName)
        makeComparisonHistogram(histName, histList)


if __name__ == "__main__":
    main()

