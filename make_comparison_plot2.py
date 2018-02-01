from glob import glob

import ROOT
from ROOT import TH1F, gStyle, TCanvas, TLegend, TFile, gROOT, TPad, TLatex, TF1

import copy

def getHistogram(oneHistName):
    inputDir="/afs/cern.ch/user/p/pewang/public/Project/VHbbTruthAnalysis/VHbbTruthFramework/macros/NtupleToHist/hist_generated/*.root"

    hists = []
    for i,filename in enumerate(glob(inputDir)):
        print filename
        f1=TFile(filename, 'R')
        h=f1.Get(oneHistName)
        hists.append(copy.deepcopy(h))
    print type(hists)
    return hists


def makeComparisonHistogram(oneHistName, histograms):
    gStyle.SetOptStat(0)
#    if 'WhfSR' not in oneHistName:
    gROOT.SetBatch(ROOT.kTRUE)
    # canvas->SetBatch(kTRUE);
    print type(histograms)
    print len(histograms)
    print oneHistName

    c1 = TCanvas( 'c1', 'Example',700, 500 )
    colors = [2,1,3,4,6]
    leg = TLegend(0.6, 0.6, 0.9, 0.9)
    sampleName=["aMc@NloPythia8EvtGen_A14N23LO_ttbar", "PowhegPythia8EvtGen_A14_ttbar_hdamp258p75 (nominal)", "PowhegPythia8EvtGen_ttbar_hdamp517p5", "PowhegPythia8EvtGen_ttbar_hdamp258p75", "PowhegHerwig7EvtGen_H7UE_tt_hdamp258p75"]

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

    for i, h in enumerate(histograms):
        h.Rebin(20)
        h.SetLineColor(colors[i])
        h.SetMarkerColor(colors[i])
        h.Scale(1/h.Integral())
        histNameTemp = h.GetName()
        if "_pTV" in histNameTemp:
            h.GetXaxis().SetRangeUser(0, 500)
        if "_mBB" in histNameTemp:
            h.GetXaxis().SetRangeUser(0, 400)
        h.SetTitle("")
        h.GetYaxis().SetTitle("arbitrary unit")
        h.GetYaxis().SetTitleOffset(1.0)
        leg.AddEntry(h,sampleName[i])
        option="" if i==0 else "same"
        h.Draw(option)
        c1.Update()

    lt = TLatex()     
    lt.SetNDC()     
    lt.SetTextSize(lt.GetTextSize() * 1.1)     
    titleName = oneHistName
    lt.DrawLatex(0.1275, 0.89, titleName[:-8])

    pad2.cd()
    
    ratios = []
    
    for i, h in enumerate(histograms):
        ratios.append(h.Clone())
        ratios[i].Divide(histograms[1])
        # ratios[i].SetTitle("")
        ratios[i].GetYaxis().SetTitle("ratio")
        ratios[i].GetYaxis().SetRangeUser(-0.3, 2.5)
        option="" if i==0 else "same"
        if i != 1: # skip the norminal
            ratios[i].Draw(option)


            
    for i, ratio in enumerate(ratios):
        if i == 1: continue
        ratioName = ratio.GetName()
        if "WhfCR" in ratioName:
            continue
        if "mBB" in ratioName:
            # the following are the initialization
            func=TF1("f_Systtbar_mBB_1lep", "x<500 ? [0] + [1] * exp([2] * x) - 1 : [0] + [1] * exp([2] * 500) - 1", 0, 500)
            func.SetParameter(0, 0.917)
            func.SetParameter(1, 0.389)
            func.SetParameter(2, -0.0138) # in 1/GeV
        elif "pTV" in ratioName:
            func=TF1("f_SysTTbarPTV_01lep", "x<500 ? [0] + [1] * x - 1 : [0] + [1] * 500 - 1", 0, 500)
            # the following are the initialization
            func.SetParameter(0, 1.09)
            func.SetParameter(1, -0.0005)# in 1/GeV
        else: continue

        func.SetLineColor(colors[i])
        print "Fitting to", ratioName
        ratio.Fit(func)

        if i != 1: # skip the norminal
            func.DrawCopy('same')

        print func.GetNDF()
        # if func.GetNDF() != 0:
        print "Chisquare", func.GetChisquare()/func.GetNDF()



    if "mBB" in oneHistName:
        func=TF1("f_Systtbar_mBB_1lep", "x<500 ? [0] + [1] * exp([2] * x) - 1 : [0] + [1] * exp([2] * 500) - 1", 0, 500)
        func.SetParameter(0, 0.917)
        func.SetParameter(1, 0.389)
        func.SetParameter(2, -0.0138) # in 1/GeV
        func.SetLineStyle(2)
        leg.AddEntry(func,"EPS")
        func.Draw('same')

    if "pTV" in oneHistName:
        func=TF1("f_SysTTbarPTV_01lep", "x<500 ? [0] + [1] * x - 1 : [0] + [1] * 500 - 1", 0, 500)
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
    c1.SaveAs("./comparison_plot_generated/" + oneHistName + ".eps")


def getHistName():
    nameSec0 = ['hist']
    nameSec1 = ['1Lep']
    nameSec2 = ['ttbar']
    nameSec3 = ['2tag2jet', '2tag3jet']
    nameSec4 = ['75_150ptv', '150ptv']
    nameSec5 = ['WhfSR', 'WhfCR']
    nameSec6 = ['BDT', 'mBB', 'pTV', 'Mtop', 'dRBB', 'pTB1', 'pTB2', 'MET', 'mTW', 'dPhiVBB', 'dPhiLBmin', 'dYWH', 'dPhiLepMET']
    # 'pTJ3' - program crashes with error:
    # AttributeError: 'TObject' object has no attribute 'Rebin'
    # 'mBBJ' - program crashes with error:
    # AttributeError: 'TObject' object has no attribute 'Rebin'

    nameSec7 = ['Nominal']

    histName = []
    for i0, i1, i2, i3, i4, i5, i6, i7 in [(i0, i1, i2, i3, i4, i5, i6, i7) for i0 in nameSec0 for i1 in nameSec1 for i2 in nameSec2 for i3 in nameSec3 for i4 in nameSec4 for i5 in nameSec5 for i6 in nameSec6 for i7 in nameSec7]:
        histName.append(i0 + "_" +  i1 + "_" + i2 + "_" + i3 + "_" + i4 + "_" + i5 + "_" + i6 + "_" + i7)
    return histName


def main():

    ROOT.gROOT.LoadMacro("./../AtlasStyleBase/AtlasStyle.C") 
    ROOT.gROOT.LoadMacro("./../AtlasStyleBase/AtlasUtils.C") 
    ROOT.SetAtlasStyle()

    histNameList = getHistName()
    for histName in histNameList:
        histList = getHistogram(histName)
        makeComparisonHistogram(histName, histList)


if __name__ == "__main__":
    main()

