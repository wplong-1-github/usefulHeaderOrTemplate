from ROOT import *
from glob import glob

gStyle.SetOptStat(0)

inputDir="/afs/cern.ch/user/p/pewang/public/Project/VHbbTruthAnalysis/VHbbTruthFramework/macros/NtupleToHist/hist_generated/*.root"

c1 = TCanvas( 'c1', 'Example',700, 500 )

colors=[1,2,3,4,6]
sampleName=["ttbar1", "ttbar2", "ttbar3", "ttbar4", "ttbar5", "ttbar6"]
val = 0

leg = TLegend(0.6, 0.6, 0.9, 0.9)

for i,filename in enumerate(glob(inputDir)):
    print filename
    f1=TFile(filename, 'R')
    hist=f1.Get("hist_1Lep_ttbar_2tag3jet_75_150ptv_WhfSR_BDT_Nominal")
    hist.SetName("hist_1Lep_ttbar_2tag3jet_75_150ptv_WhfSR_BDT_Nominal")
    hist.Rebin(20)
    hist.SetLineColor(colors[i])
    hist.SetMarkerColor(colors[i])
    hist.Scale(1/hist.Integral())
    option="" if i==0 else "same"
    hist.DrawCopy(option)
    leg.AddEntry(hist, sampleName[i])
    c1.Update()

    
leg.Draw("same")

raw_input("Press enter to save the image")
c1.SaveAs("example.eps")
