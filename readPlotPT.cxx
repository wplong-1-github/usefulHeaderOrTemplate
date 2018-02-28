#include <TFile.h>
#include <vector>
#define BRN 4
#define BRNTTBAR 2
int readPlotPT() {

  gStyle->SetOptStat(0);

  TCanvas *c1 = new TCanvas("c1", "different scales hists", 600, 400);
  
  TFile *f = new TFile("/scratch/users/peilongw/_small/dihiggsProject/submitDir/data-myOutput/mc15_13TeV.342619.aMcAtNloHerwigppEvtGen_UEEE5_CTEQ6L1_CT10ME_hh_4b.merge.DAOD_EXOT8.e4419_s2608_r6869_r6282_p2438.root");
  TTree* tree = (TTree*)f->Get("tree");

  TH1F *bPTth = new TH1F("bPT", "bPT", 100, 0, 600);

  double bPT[BRN];

  std::vector<TBranch *> branch(BRN);

  branch[0] = tree->GetBranch("b1PT");
  branch[1] = tree->GetBranch("b2PT");
  branch[2] = tree->GetBranch("b3PT");
  branch[3] = tree->GetBranch("b4PT");

  for (int i=0; i<BRN; i++)
    branch[i]->SetAddress(&bPT[i]);

  int nevent = tree->GetEntries();
  int nselected = 0;
  int nb = 0;

  for(int i=0; i<nevent; i++) {
    nb += tree->GetEntry(i);
    nselected++;
   
    for (int j=0; j<BRN; j++)
      bPTth->Fill(bPT[j]);
  }

  bPTth->SetFillStyle(3003);
  bPTth->SetLineColor(kRed);
  bPTth->GetXaxis()->SetTitle("pT");
  bPTth->GetYaxis()->SetTitle("counts");
  //bPTth->GetYaxis()->SetLabelOffset(1.40);
  // bPTth->SetStats(0);
  bPTth->SetMaximum(10000);
  bPTth->Draw();
  //how is it normalized when drawnormalized
  c1->Update();
  
  
  TFile *ttbarF = new TFile("/scratch/users/peilongw/_small/ttbarBackgrounBbar/1/submitDir/data-myOutput/mc15_13TeV.410000.PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad.merge.AOD.e3698_s2608_s2183_r7773_r7676.root");

  //"/scratch/users/peilongw/_small/ttbarBackgrounBbar/1/submitDir/data-myOutput/mc15_valid.410000.PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad.recon.AOD.e3698_s2608_s2183_r6655.root");

  TTree* ttbarTree = (TTree*)ttbarF->Get("tree");

  TH1F *ttbarBPTth = new TH1F("ttbarbPT", "ttbarbPT", 100, 0, 600);

  double ttbarBPT[BRNTTBAR];

  std::vector<TBranch *> ttbarBranch(BRNTTBAR);

  ttbarBranch[0] = ttbarTree->GetBranch("b1PT");
  ttbarBranch[1] = ttbarTree->GetBranch("b2PT");

  for (int i=0; i<BRNTTBAR; i++) 
    ttbarBranch[i]->SetAddress(&ttbarBPT[i]);

  int ttbarNevent = ttbarTree->GetEntries();
  int ttbarNselected = 0;
  int ttbarNb = 0;
  
  for(int i=0; i<ttbarNevent; i++) {
    ttbarNb += ttbarTree->GetEntry(i);
    ttbarNselected++;
   
    for (int j=0; j<BRNTTBAR; j++)
      ttbarBPTth->Fill(ttbarBPT[j]);
  }

  ttbarBPTth->SetFillStyle(3008);
  ttbarBPTth->SetLineColor(kBlue);
  //ttbarBPTth->SetStats(0);
  ttbarBPTth->SetMaximum(10000);
  ttbarBPTth->Draw("same");

  TLegend *legend = new TLegend(.75,.80,.95,.95);
  legend->AddEntry(bPTth,"hh->bbbb");
  legend->AddEntry(ttbarBPTth,"ttbar");
  legend->Draw();
  
  return 0;
}
