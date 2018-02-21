from glob import glob

import ROOT
from ROOT import TH1F, gStyle, TCanvas, TLegend, TFile, gROOT, TPad, TLatex, TF1

import copy
from math import sqrt
from array import array

def getHistogram(oneHistName):
    inputDir="/home/peilong/Downloads/hist_generated/*.root"
    # /afs/cern.ch/user/p/pewang/public/Project/VHbbTruthAnalysis2/run/hist_generated/*.root"

    hists = []
    for i,filename in enumerate(sorted(glob(inputDir))):
        print filename
        f1=TFile(filename, 'R')
        h=f1.Get(oneHistName)
        hists.append(copy.deepcopy(h))
    return hists


def getFracError(histName):
    if "2tag2jet_150ptv_" in histName:    
        return 0.02
    if "2tag2jet_75_150ptv_" in histName:
        return 0.01
    if "2tag3jet_150ptv_" in histName:
        return 0.01
    if "2tag3jet_75_150ptv_" in histName:
        return 0.005



def getMergeBins(hist):
    FracError = getFracError(hist.GetName())

    integral = 0.0
    error2 = 0.0
    Nbins = hist.GetNbinsX()
    startbin = Nbins
    currentbin = Nbins
    binedges = [hist.GetBinCenter(Nbins) + hist.GetBinWidth(Nbins) / 2]

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


def getXRangeFromHist(hist):
    nOfBin = hist.GetNbinsX()
    if nOfBin == 1:
        lower = 0
        upper = 1000

    elif nOfBin >= 1:
        name = hist.GetName()

        if "_mBB_" in name:
            xmin = 0
            xmax = 450
        if "_pTV_" in name:
            xmin = 75
            xmax = 300
        if "_MET_" in name:
            xmin = 0
            xmax = 300
        if "_dPhiVBB_" in name:
            xmin = 2.5
            xmax = 3.14
        if "_dYWH_" in name:
            xmin = 0
            xmax = 2.90
        if "_Mtop_" in name:
            xmin = 100
            xmax = 240
        if "_mTW_" in name:
            xmin = 0
            xmax = 300
        if "_pTB1_" in name:
            xmin = 20
            xmax = 400
        if "_pTB2_" in name:
            xmin = 20
            xmax = 400

        upperbin = hist.GetXaxis().FindBin(xmax) - 1
        print "peilong: upperbin number ", upperbin
        lowerbin = hist.GetXaxis().FindBin(xmin) + 1
        print "peilong: lowerbin number ", lowerbin

    return lowerbin, upperbin
            

def makeComparisonHistogram(oneHistName, histograms):
    gStyle.SetOptStat(0)
    gROOT.SetBatch(ROOT.kTRUE)
    # canvas->SetBatch(kTRUE);
    # print type(histograms)
    # print len(histograms)
    print oneHistName

    c1 = TCanvas( 'c1', 'Example',700, 500 )
    colors = [2,1,3,4,6]
    leg = TLegend(0.7, 0.71, 0.9, 0.91)
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

    # plot shape comparison
    hNewHists = []

    for i, h in enumerate(histograms):
        hNew = h.Rebin(binnum,h.GetName(),edge)
        for bin in xrange(0,hNew.GetNbinsX()+1):
            hNew.SetBinContent(bin,hNew.GetBinContent(bin)/(hNew.GetBinWidth(bin)) ) 
            hNew.SetBinError(bin,hNew.GetBinError(bin)/(hNew.GetBinWidth(bin)) ) 

        hNew.SetLineColor(colors[i])
        hNew.SetMarkerColor(colors[i])
        hNew.Scale(1/hNew.Integral())
        # get x-axis range for the histograms
        physValueName = ["_mBB_", "_pTV_", "_MET_", "_dPhiVBB_", "_dYWH_", "_Mtop_", "_mTW_", "_pTB1_", "_pTB2_"]
        if "_WhfSR_" in oneHistName:
            if any(value in oneHistName for value in physValueName):
                xmin,xmax = getXRangeFromHist(hNew)
                print "xmin, xmax: ", xmin, xmax
                # hNew.GetXaxis().SetRangeUser(xmin, xmax)
                # 
                hNew.GetXaxis().SetRange(xmin, xmax)
        # get x-axis range for the histograms
        ymax = 1.4 * hNew.GetMaximum() 
        hNew.GetYaxis().SetRangeUser(0, ymax)

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
        if i != 1: # skip the norminal
            h.Divide(hNewHists[1])
            h.GetYaxis().SetTitle("ratio")
            # ratioYMax = 1.2 * h.GetMaximum() 
            # ratioYMin = 1.2 * h.GetMinimum() 
            # h.GetYaxis().SetRangeUser(ratioYMin, ratioYMax)

            h.GetYaxis().SetRangeUser(0.8, 1.23)

            option="" if i==0 else "same"
            h.Draw(option)


    # define fit fuction for mBB and pTV from EPS 2017
    fitFunctionmBB = "x<500 ? [0] + [1] * exp([2] * x) : [0] + [1] * exp([2] * 500)"
    fitFunctionpTV = "x<500 ? [0] + [1] * x : [0] + [1] * 500"

    # plot EPS shape
    if "_mBB_" in oneHistName:
        func=TF1("f_Systtbar_mBB_1lep", fitFunctionmBB, 0, 500)
        func.SetParameter(0, 0.917)
        func.SetParameter(1, 0.389)
        func.SetParameter(2, -0.0138) # in 1/GeV
        func.SetLineColor(1)
        func.SetLineStyle(2)
        leg.AddEntry(func,"EPS")
        func.Draw('same')

    if "_pTV_" in oneHistName:
        func=TF1("f_SysTTbarPTV_1lep", fitFunctionpTV, 0, 500)
        # the following are the initialization
        func.SetParameter(0, 1.09)
        func.SetParameter(1, -0.0005)# in 1/GeV
        func.SetLineColor(1)
        func.SetLineStyle(2)
        leg.AddEntry(func,"EPS")
        func.Draw('same')

    pad1.cd()
    leg.Draw("same")

    # if 'WhfSR' in oneHistName:
    # raw_input("Press enter to save the image")
    c1.SaveAs("./plot_comparison_generated/" + oneHistName + ".pdf")


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
