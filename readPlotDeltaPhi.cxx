#include <TFile.h>
#include <vector>
#define BRN 2
#define BRNTTBAR 1
int readPlotDeltaPhi() {

  gStyle->SetOptStat(0);

  TCanvas *c1 = new TCanvas("c1", "different scales hists", 600, 400);
  
  TFile *f = new TFile("../dihiggsProject/submitDir/data-myOutput/mc15_13TeV.342619.aMcAtNloHerwigppEvtGen_UEEE5_CTEQ6L1_CT10ME_hh_4b.merge.DAOD_EXOT8.e4419_s2608_r6869_r6282_p2438.root");
  TTree* tree = (TTree*)f->Get("tree");

  TH1F *bDeltaPhith = new TH1F("bDeltaPhi", "bDeltaPhi", 200, 0, 4);

  double bDeltaPhi[BRN];

  std::vector<TBranch *> branch(BRN);

  // branch name
  branch[0] = tree->GetBranch("b1b2DeltaPhi");
  branch[1] = tree->GetBranch("b3b4DeltaPhi");

  for (int i=0; i<BRN; i++)
    branch[i]->SetAddress(&bDeltaPhi[i]);

  int nevent = tree->GetEntries();
  int nselected = 0;
  int nb = 0;

  for(int i=0; i<nevent; i++) {
    nb += tree->GetEntry(i);
    nselected++;
   
    for (int j=0; j<BRN; j++)
      bDeltaPhith->Fill(bDeltaPhi[j]);
  }

  bDeltaPhith->SetFillStyle(3003);
  bDeltaPhith->SetLineColor(kRed);
  bDeltaPhith->GetXaxis()->SetTitle("Delta Phi");
  bDeltaPhith->GetYaxis()->SetTitle("counts");
  //bDeltaPhith->GetYaxis()->SetLabelOffset(1.40);
  // bDeltaPhith->SetStats(0);
  bDeltaPhith->Draw();
  //how is it normalized when drawnormalized
  c1->Update();
 

  
  TFile *ttbarF = new TFile("/scratch/users/peilongw/_small/ttbarBackgrounBbar/1/submitDir/data-myOutput/mc15_valid.410000.PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad.recon.AOD.e3698_s2608_s2183_r6655.root.root");
  TTree* ttbarTree = (TTree*)ttbarF->Get("tree");

  TH1F *ttbarBDeltaPhith = new TH1F("", "", 200, 0, 4);

  double ttbarBDeltaPhi[BRNTTBAR];

  std::vector<TBranch *> ttbarBranch(BRNTTBAR);

  ttbarBranch[0] = ttbarTree->GetBranch("b1b2DeltaPhi");

  for (int i=0; i<BRNTTBAR; i++) 
    ttbarBranch[i]->SetAddress(&ttbarBDeltaPhi[i]);

  int ttbarNevent = ttbarTree->GetEntries();
  int ttbarNselected = 0;
  int ttbarNb = 0;
  
  for(int i=0; i<ttbarNevent; i++) {
    ttbarNb += ttbarTree->GetEntry(i);
    ttbarNselected++;
   
    for (int j=0; j<BRNTTBAR; j++)
      ttbarBDeltaPhith->Fill(ttbarBDeltaPhi[j]);
  }

  ttbarBDeltaPhith->SetFillStyle(3008);
  ttbarBDeltaPhith->SetLineColor(kBlue);
  //ttbarBDeltaPhith->SetStats(0);
  ttbarBDeltaPhith->Draw("same");

  TLegend *legend = new TLegend(.75,.80,.95,.95);
  legend->AddEntry(bDeltaPhith,"hh->bbbb");
  legend->AddEntry(ttbarBDeltaPhith,"ttbar");
  legend->Draw();

  return 0;
}
