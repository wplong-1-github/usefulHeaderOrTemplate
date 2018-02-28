#include <TFile.h>
#include <vector>
#define BRN 4
#define BRNTTBAR 2
int readPlotEta() {

  gStyle->SetOptStat(0);

  TCanvas *c1 = new TCanvas("c1", "different scales hists", 600, 400);
  
  TFile *f = new TFile("../dihiggsProject/submitDir/data-myOutput/mc15_13TeV.342619.aMcAtNloHerwigppEvtGen_UEEE5_CTEQ6L1_CT10ME_hh_4b.merge.DAOD_EXOT8.e4419_s2608_r6869_r6282_p2438.root");
  TTree* tree = (TTree*)f->Get("tree");

  TH1F *bEtath = new TH1F("bEta", "bEta", 200, -10, 10);

  double bEta[BRN];

  std::vector<TBranch *> branch(BRN);

  branch[0] = tree->GetBranch("b1Eta");
  branch[1] = tree->GetBranch("b2Eta");
  branch[2] = tree->GetBranch("b3Eta");
  branch[3] = tree->GetBranch("b4Eta");

  for (int i=0; i<BRN; i++)
    branch[i]->SetAddress(&bEta[i]);

  int nevent = tree->GetEntries();
  int nselected = 0;
  int nb = 0;

  for(int i=0; i<nevent; i++) {
    nb += tree->GetEntry(i);
    nselected++;
   
    for (int j=0; j<BRN; j++)
      bEtath->Fill(bEta[j]);
  }

  bEtath->SetFillStyle(3003);
  bEtath->SetLineColor(kRed);
  bEtath->GetXaxis()->SetTitle("Eta");
  bEtath->GetYaxis()->SetTitle("counts");
  //bEtath->GetYaxis()->SetLabelOffset(1.40);
  // bEtath->SetStats(0);
  bEtath->Draw();
  //how is it normalized when drawnormalized
  c1->Update();

  
  TFile *ttbarF = new TFile("/scratch/users/peilongw/_small/ttbarBackgrounBbar/1/submitDir/data-myOutput/mc15_valid.410000.PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad.recon.AOD.e3698_s2608_s2183_r6655.root.root");
  TTree* ttbarTree = (TTree*)ttbarF->Get("tree");

  TH1F *ttbarBEtath = new TH1F("", "", 200, -10, 10);

  double ttbarBEta[BRNTTBAR];

  std::vector<TBranch *> ttbarBranch(BRNTTBAR);

  ttbarBranch[0] = ttbarTree->GetBranch("b1Eta");
  ttbarBranch[1] = ttbarTree->GetBranch("b2Eta");

  for (int i=0; i<BRNTTBAR; i++) 
    ttbarBranch[i]->SetAddress(&ttbarBEta[i]);

  int ttbarNevent = ttbarTree->GetEntries();
  int ttbarNselected = 0;
  int ttbarNb = 0;
  
  for(int i=0; i<ttbarNevent; i++) {
    ttbarNb += ttbarTree->GetEntry(i);
    ttbarNselected++;
   
    for (int j=0; j<BRNTTBAR; j++)
      ttbarBEtath->Fill(ttbarBEta[j]);
  }

  ttbarBEtath->SetFillStyle(3008);
  ttbarBEtath->SetLineColor(kBlue);
  //ttbarBEtath->SetStats(0);
  ttbarBEtath->Draw("same");
  
  TLegend *legend = new TLegend(.75,.80,.95,.95);
  legend->AddEntry(bEtath,"hh->bbbb");
  legend->AddEntry(ttbarBEtath,"ttbar");
  legend->Draw();

  return 0;
}
