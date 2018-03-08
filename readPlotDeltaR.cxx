#include <TFile.h>
#include <vector>
#define BRN 8
#define BRNTTBAR 4

int readPlotDeltaR() {

  gStyle->SetOptStat(0);

  TCanvas *c1 = new TCanvas("c1", "different scales hists", 600, 400);
  
  TFile *f = new TFile("../dihiggsProject/submitDir/data-myOutput/mc15_13TeV.342619.aMcAtNloHerwigppEvtGen_UEEE5_CTEQ6L1_CT10ME_hh_4b.merge.DAOD_EXOT8.e4419_s2608_r6869_r6282_p2438.root");
  TTree* tree = (TTree*)f->Get("tree");

  TH1F *bDeltaRth = new TH1F("bDeltaR", "bDeltaR", 100, 0, 10);

  double bDeltaR[BRN];

  std::vector<TBranch *> branch(BRN);

  // branch name
  branch[0] = tree->GetBranch("b1Eta");
  branch[1] = tree->GetBranch("b2Eta");
  branch[2] = tree->GetBranch("b3Eta");
  branch[3] = tree->GetBranch("b4Eta");
  branch[4] = tree->GetBranch("b1Phi");
  branch[5] = tree->GetBranch("b2Phi");
  branch[6] = tree->GetBranch("b3Phi");
  branch[7] = tree->GetBranch("b4Phi");
 
  for (int i=0; i<BRN; i++)
    branch[i]->SetAddress(&bDeltaR[i]);

  int nevent = tree->GetEntries();
  int nselected = 0;
  int nb = 0;

  for(int i=0; i<nevent; i++) {
    nb += tree->GetEntry(i);
    nselected++;
   
    bDeltaR[0] =  bDeltaR[0] - bDeltaR[1] ; // delta Eta higgs 1
    bDeltaR[1] =  bDeltaR[2] - bDeltaR[3] ; // delta Eta higgs 2
    bDeltaR[2] =  bDeltaR[4] - bDeltaR[5] ; // delta Phi higgs 1
    bDeltaR[3] =  bDeltaR[6] - bDeltaR[7] ; // delta Phi higgs 2

    if ( bDeltaR[2] < -TMath::Pi() )
      bDeltaR[2] = 2*TMath::Pi() + bDeltaR[2];
    else if ( bDeltaR[2] > TMath::Pi() )
      bDeltaR[2] = 2*TMath::Pi() - bDeltaR[2];
    else
      bDeltaR[2] = std::abs( bDeltaR[2] );

    if ( bDeltaR[3] < -TMath::Pi() )
      bDeltaR[3] = 2*TMath::Pi() + bDeltaR[3];
    else if ( bDeltaR[3] > TMath::Pi() )
      bDeltaR[3] = 2*TMath::Pi() - bDeltaR[3];
    else
      bDeltaR[3] = std::abs( bDeltaR[3] );

    bDeltaR[0]  = TMath::Sqrt( bDeltaR[0] * bDeltaR[0] + bDeltaR[2] * bDeltaR[2] );
    bDeltaR[1]  = TMath::Sqrt( bDeltaR[1] * bDeltaR[1] + bDeltaR[3] * bDeltaR[3] );

    for (int j=0; j<2; j++)
      bDeltaRth->Fill(bDeltaR[j]);
  }

  bDeltaRth->SetFillStyle(3003);
  bDeltaRth->SetLineColor(kRed);
  bDeltaRth->GetXaxis()->SetTitle("Delta R");
  bDeltaRth->GetYaxis()->SetTitle("counts");
  //bCosThetath->GetYaxis()->SetLabelOffset(1.40);
  // bCosThetath->SetStats(0);
  bDeltaRth->Draw();
  //how is it normalized when drawnormalized
  c1->Update();
 
  

  TFile *ttbarF = new TFile("/scratch/users/peilongw/_small/ttbarBackgrounBbar/1/submitDir/data-myOutput/mc15_valid.410000.PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad.recon.AOD.e3698_s2608_s2183_r6655.root.root");
  TTree* ttbarTree = (TTree*)ttbarF->Get("tree");

  TH1F *ttbarBDeltaRth = new TH1F("", "", 100, 0, 10);
  
  double ttbarBDeltaR[BRNTTBAR];

  std::vector<TBranch *> ttbarBranch(BRNTTBAR);

  // branch name
  ttbarBranch[0] = ttbarTree->GetBranch("b1Eta");
  ttbarBranch[1] = ttbarTree->GetBranch("b2Eta");
  ttbarBranch[2] = ttbarTree->GetBranch("b1Phi");
  ttbarBranch[3] = ttbarTree->GetBranch("b2Phi");

  for (int i=0; i<BRNTTBAR; i++) 
    ttbarBranch[i]->SetAddress(&ttbarBDeltaR[i]);

  int ttbarNevent = ttbarTree->GetEntries();
  int ttbarNselected = 0;
  int ttbarNb = 0;
  
  for(int i=0; i<ttbarNevent; i++) {
    ttbarNb += ttbarTree->GetEntry(i);
    ttbarNselected++;
   
    ttbarBDeltaR[0] = ttbarBDeltaR[0] - ttbarBDeltaR[1]; // delta Eta of b1b2
    ttbarBDeltaR[1] = ttbarBDeltaR[2] - ttbarBDeltaR[3]; // delta Phi of b1b2

    if ( ttbarBDeltaR[1] < -TMath::Pi() )
      ttbarBDeltaR[1] = 2*TMath::Pi() + ttbarBDeltaR[1];
    else if ( ttbarBDeltaR[1] > TMath::Pi() )
      ttbarBDeltaR[1] = 2*TMath::Pi() - ttbarBDeltaR[1];
    else
      ttbarBDeltaR[1] = std::abs( ttbarBDeltaR[1] );

    ttbarBDeltaR[0]  = TMath::Sqrt( ttbarBDeltaR[0] * ttbarBDeltaR[0] + ttbarBDeltaR[1] * ttbarBDeltaR[1] );

    for (int j=0; j<BRNTTBAR/4; j++)
      ttbarBDeltaRth->Fill(ttbarBDeltaR[j]);
  }

  ttbarBDeltaRth->SetFillStyle(3008);
  ttbarBDeltaRth->SetLineColor(kBlue);
  //ttbarBDeltaRth->SetStats(0);
  ttbarBDeltaRth->Draw("same");

  TLegend *legend = new TLegend(.75,.80,.95,.95);
  legend->AddEntry(bDeltaRth,"hh->bbbb");
  legend->AddEntry(ttbarBDeltaRth,"ttbar");
  legend->Draw();

  return 0;
}
