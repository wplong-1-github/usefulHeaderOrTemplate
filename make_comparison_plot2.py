from glob import glob

import ROOT
from ROOT import TH1F, gStyle, TCanvas, TLegend, TFile, gROOT

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
#    canvas->SetBatch(kTRUE);
    print type(histograms)
    print len(histograms)
    print oneHistName

    c1 = TCanvas( 'c1', 'Example',700, 500 )
    colors = [1,2,3,4,6]
    leg = TLegend(0.6, 0.6, 0.9, 0.9)
    sampleName=["ttbar 410225", "ttbar 410501", "ttbar 410511", "ttbar 410512", "ttbar 410525"]

    for i, h in enumerate(histograms):
        h.Rebin(20)
        h.SetLineColor(colors[i])
        h.SetMarkerColor(colors[i])
        h.Scale(1/h.Integral())
#        h.GetYaxis().SetRangeUser(0,0.09)
        leg.AddEntry(h,sampleName[i])
        option="" if i==0 else "same"
        h.Draw(option)
        c1.Update()
    leg.Draw("same")
    # if 'WhfSR' in oneHistName:
    #     raw_input("Press enter to save the image")
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
    histNameList = getHistName()
    for histName in histNameList:
        histList = getHistogram(histName)
        makeComparisonHistogram(histName, histList)


if __name__ == "__main__":
    main()


# for i,filename in enumerate(glob(inputDir)):
#     print filename
#     f1=TFile(filename, 'R')
#     h=f1.Get("hist_1Lep_ttbar_2tag3jet_75_150ptv_WhfSR_BDT_Nominal")
#     print type(h)
# #    h.SetName("hist_1Lep_ttbar_2tag3jet_75_150ptv_WhfSR_BDT_Nominal")


