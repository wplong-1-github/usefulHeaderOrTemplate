#include <TFile.h>
#include <vector>
#include "TMath.h"
#include "TVector3.h"
#define BRN 6 // branch number
#define BRNTTBAR 3

int readPlotDeltaEtaVsDeltaPhi() {

  gStyle->SetOptStat(0);

  TCanvas *c1 = new TCanvas("c1", "different scales hists", 600, 400);
  
  TFile *f = new TFile("../dihiggsProject/submitDir/data-myOutput/mc15_13TeV.342619.aMcAtNloHerwigppEvtGen_UEEE5_CTEQ6L1_CT10ME_hh_4b.merge.DAOD_EXOT8.e4419_s2608_r6869_r6282_p2438.root");
  TTree* tree = (TTree*)f->Get("tree");

  TH *bDeltaEtaVsDeltaPhith = new TH1F("bDeltaEtaVsDeltaPhi", "bDeltaEtaVsDeltaPhi", 200, -10, 10);

  double bDeltaEtaVsDeltaPhi[BRN];

  std::vector<TBranch *> branch(BRN);

  branch[0] = tree->GetBranch("b1Eta");
  branch[1] = tree->GetBranch("b2Eta");
  branch[2] = tree->GetBranch("b3Eta");
  branch[3] = tree->GetBranch("b4Eta");

  for (int i=0; i<BRN; i++)
    branch[i]->SetAddress(&bDeltaEtaVsDeltaPhi[i]);

  int nevent = tree->GetEntries();
  int nselected = 0;
  int nb = 0;

  for(int i=0; i<nevent; i++) {
    nb += tree->GetEntry(i);
    nselected++;
   
    for (int j=0; j<BRN; j++)
      bDeltaEtaVsDeltaPhith->Fill(bDeltaEtaVsDeltaPhi[j]);
  }

  bDeltaEtaVsDeltaPhith->SetFillStyle(3003);
  bDeltaEtaVsDeltaPhith->SetLineColor(kRed);
  bDeltaEtaVsDeltaPhith->GetXaxis()->SetTitle("DeltaEtaVsDeltaPhi");
  bDeltaEtaVsDeltaPhith->GetYaxis()->SetTitle("counts");
  //bDeltaEtaVsDeltaPhith->GetYaxis()->SetLabelOffset(1.40);
  // bDeltaEtaVsDeltaPhith->SetStats(0);
  bDeltaEtaVsDeltaPhith->Draw();
  //how is it normalized when drawnormalized
  c1->Update();



















  //----------------------
  TFile *f = new TFile("./mc15_Valid/submitDir/data-myOutput/mc15_valid.410000.PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad.recon.AOD.e3698_s2608_s2183_r6655.root.root");
  TTree* tree = (TTree*)f->Get("tree");

  TH2D *bDeltaEtaVsDeltaPhith = new TH2D("bDeltaEtaVsDeltaPhi", "bDeltaEtaVsDeltaPhi", 120, 0, 3.5, 100, 0, 3);

  double bDeltaEtaVsDeltaPhi[BRN];

  std::vector<TBranch *> branch(BRN);

  // branch name
  branch[0] = tree->GetBranch("b1Eta");
  branch[1] = tree->GetBranch("b2Eta");
  branch[2] = tree->GetBranch("b1b2DeltaPhi");

  for (int i=0; i<BRN; i++)
    branch[i]->SetAddress(&bDeltaEtaVsDeltaPhi[i]);

  int nevent = tree->GetEntries();
  int nselected = 0;
  int nb = 0;

  for(int i=0; i<nevent; i++) {
    nb += tree->GetEntry(i);
    nselected++;
    
    bDeltaEtaVsDeltaPhith->Fill(TMath::Abs(bDeltaEtaVsDeltaPhi[0] - bDeltaEtaVsDeltaPhi[1]), bDeltaEtaVsDeltaPhi[2]);
  }

  bDeltaEtaVsDeltaPhith->Draw("COLZ");


  return 0;
}
