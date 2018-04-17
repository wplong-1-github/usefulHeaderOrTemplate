from glob import glob

import ROOT
from ROOT import TH1F, gStyle, TCanvas, TLegend, TFile, gROOT, TPad, TLatex, TF1

import copy

def getHistogram(oneHistName, inputDir):
    # print oneHistName
    # print inputDir

    hists = []
    for i,filename in enumerate(sorted(glob(inputDir))):
        # print filename
        f1=TFile(filename, 'R')
        h=f1.Get(oneHistName)
        hists.append(copy.deepcopy(h))

    # hists[1].Add(hists[2])
    # hists.pop()

    return hists

def countNtupleEventNumber(oneHistName, histograms):

    eventNumber = 0

    for h in histograms:
        eventNumber = eventNumber + h.GetEntries()
    print eventNumber

def main():

    # ROOT.gROOT.LoadMacro("../AtlasStyleBase/AtlasStyle.C") 
    # ROOT.gROOT.LoadMacro("../AtlasStyleBase/AtlasUtils.C") 
    # ROOT.SetAtlasStyle()

    histNameTemplate = 'h_Keep_SumAbsWeight_%d_1Lep'
    dsid = [410441, 410442, 410470, 410472, 410480, 410482, 410557, 410558]
    
    inputDirList = ['/afs/cern.ch/user/p/pewang/public/Project/VHbbTruthAnalysis3/ntuples/group.phys-higgs.mc15_13TeV.410441.aMcAtNloPythia8EvtGen_ttbar_SingleLep.evgen.EVNT.e6407.VHbb.BETA_v07_ttbar_1_Lep/group.phys-higgs.mc15_13TeV.410441.aMcAtNloPythia8EvtGen_ttbar_SingleLep.evgen.EVNT.e6407.VHbb.BETA_v07_ttbar_1_Lep', '/afs/cern.ch/user/p/pewang/public/Project/VHbbTruthAnalysis3/ntuples/group.phys-higgs.mc15_13TeV.410442.aMcAtNloPythia8EvtGen_A14N23LO_ttbar_dil.evgen.EVNT.e6407.VHbb.BETA_v07_ttbar_1_Lep/group.phys-higgs.mc15_13TeV.410442.aMcAtNloPythia8EvtGen_A14N23LO_ttbar_dil.evgen.EVNT.e6407.VHbb.BETA_v07_ttbar_1_Lep', '/afs/cern.ch/user/p/pewang/public/Project/VHbbTruthAnalysis3/ntuples/group.phys-higgs.mc15_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.evgen.EVNT.e6337.VHbb.BETA_v07_ttbarmc15_1_Lep/group.phys-higgs.mc15_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.evgen.EVNT.e6337.VHbb.BETA_v07_ttbarmc15_1_Lep', '/afs/cern.ch/user/p/pewang/public/Project/VHbbTruthAnalysis3/ntuples/group.phys-higgs.mc15_13TeV.410472.PhPy8EG_A14_ttbar_hdamp258p75_dil.evgen.EVNT.e6348.VHbb.BETA_v07_ttbarmc15_1_Lep/group.phys-higgs.mc15_13TeV.410472.PhPy8EG_A14_ttbar_hdamp258p75_dil.evgen.EVNT.e6348.VHbb.BETA_v07_ttbarmc15_1_Lep', '/afs/cern.ch/user/p/pewang/public/Project/VHbbTruthAnalysis3/ntuples/group.phys-higgs.mc15_13TeV.410480.PhPy8EG_A14_ttbar_hdamp517p5_SingleLep.evgen.EVNT.e6454.VHbb.BETA_v07_ttbarmc15_1_Lep/group.phys-higgs.mc15_13TeV.410480.PhPy8EG_A14_ttbar_hdamp517p5_SingleLep.evgen.EVNT.e6454.VHbb.BETA_v07_ttbarmc15_1_Lep', '/afs/cern.ch/user/p/pewang/public/Project/VHbbTruthAnalysis3/ntuples/group.phys-higgs.mc15_13TeV.410482.PhPy8EG_A14_ttbar_hdamp517p5_dil.evgen.EVNT.e6454.VHbb.BETA_v07_ttbarmc15_1_Lep/group.phys-higgs.mc15_13TeV.410482.PhPy8EG_A14_ttbar_hdamp517p5_dil.evgen.EVNT.e6454.VHbb.BETA_v07_ttbarmc15_1_Lep', '/afs/cern.ch/user/p/pewang/public/Project/VHbbTruthAnalysis3/ntuples/group.phys-higgs.mc15_13TeV.410557.PowhegHerwig7EvtGen_704_SingleLep.evgen.EVNT.e6366.VHbb.BETA_v07_ttbarmc15_1_Lep/group.phys-higgs.mc15_13TeV.410557.PowhegHerwig7EvtGen_704_SingleLep.evgen.EVNT.e6366.VHbb.BETA_v07_ttbarmc15_1_Lep', '/afs/cern.ch/user/p/pewang/public/Project/VHbbTruthAnalysis3/ntuples/group.phys-higgs.mc15_13TeV.410558.PowhegHerwig7EvtGen_hdamp258p75_704_dil.evgen.EVNT.e6366.VHbb.BETA_v07_ttbarmc15_1_Lep/group.phys-higgs.mc15_13TeV.410558.PowhegHerwig7EvtGen_hdamp258p75_704_dil.evgen.EVNT.e6366.VHbb.BETA_v07_ttbarmc15_1_Lep']

    for id, inputDir in zip(dsid, inputDirList):
        histName = histNameTemplate % id
        print histName
        histList = getHistogram(histName, inputDir + "/*")
        countNtupleEventNumber(histName, histList)


if __name__ == "__main__":
    main()
