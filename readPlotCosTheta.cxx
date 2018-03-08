#include <TFile.h>
#include <vector>
#include "TMath.h"
#include "TVector3.h"
#define BRN 12
#define BRNTTBAR 6


int readPlotCosTheta() {

  gStyle->SetOptStat(0);

  TCanvas *c1 = new TCanvas("c1", "different scales hists", 600, 400);

  TFile *f = new TFile("../dihiggsProject/submitDir/data-myOutput/mc15_13TeV.342619.aMcAtNloHerwigppEvtGen_UEEE5_CTEQ6L1_CT10ME_hh_4b.merge.DAOD_EXOT8.e4419_s2608_r6869_r6282_p2438.root");
  TTree* tree = (TTree*)f->Get("tree");

  TH1F *bCosThetath = new TH1F("CosTheta", "bCosTheta", 30, -1.5, 1.5);

  double bCosTheta[BRN];

  std::vector<TBranch *> branch(BRN);

  // branch name
  branch[0] = tree->GetBranch("b1Px");
  branch[1] = tree->GetBranch("b1Py");
  branch[2] = tree->GetBranch("b1Pz");
  branch[3] = tree->GetBranch("b2Px");
  branch[4] = tree->GetBranch("b2Py");
  branch[5] = tree->GetBranch("b2Pz");
  branch[6] = tree->GetBranch("b3Px");
  branch[7] = tree->GetBranch("b3Py");
  branch[8] = tree->GetBranch("b3Pz");
  branch[9] = tree->GetBranch("b4Px");
  branch[10] = tree->GetBranch("b4Py");
  branch[11] = tree->GetBranch("b4Pz");

  for (int i=0; i<BRN; i++)
    branch[i]->SetAddress(&bCosTheta[i]);

  std::vector<TVector3> bQuark(4);

  int nevent = tree->GetEntries();
  int nselected = 0;
  int nb = 0;

  for(int i=0; i<nevent; i++) {
    nb += tree->GetEntry(i);
    nselected++;
    
    bQuark.at(0).SetXYZ(bCosTheta[0], bCosTheta[1], bCosTheta[2]);
    bQuark.at(1).SetXYZ(bCosTheta[3], bCosTheta[4], bCosTheta[5]);
    bQuark.at(2).SetXYZ(bCosTheta[6], bCosTheta[7], bCosTheta[8]);
    bQuark.at(3).SetXYZ(bCosTheta[9], bCosTheta[10], bCosTheta[11]);
  
    bCosThetath->Fill( TMath::Cos( bQuark.at(0).Angle(bQuark.at(1)) ) );
    bCosThetath->Fill( TMath::Cos( bQuark.at(2).Angle(bQuark.at(3)) ) );
  }

  bCosThetath->SetFillStyle(3003);
  bCosThetath->SetLineColor(kRed);
  bCosThetath->GetXaxis()->SetTitle("Cos(Theta)");
  bCosThetath->GetYaxis()->SetTitle("counts");
  //bCosThetath->GetYaxis()->SetLabelOffset(1.40);
  // bCosThetath->SetStats(0);
  bCosThetath->Draw();
  //how is it normalized when drawnormalized
  c1->Update();

  
  TFile *ttbarF = new TFile("/scratch/users/peilongw/_small/ttbarBackgrounBbar/1/submitDir/data-myOutput/mc15_valid.410000.PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad.recon.AOD.e3698_s2608_s2183_r6655.root.root");
  TTree* ttbarTree = (TTree*)ttbarF->Get("tree");

  TH1F *ttbarBCosThetath = new TH1F("", "", 30, -1.5, 1.5);

  double ttbarBCosTheta[BRNTTBAR];

  std::vector<TBranch *> ttbarBranch(BRNTTBAR);

  // BRNTTBAR name
  ttbarBranch[0] = ttbarTree->GetBranch("b1Px");
  ttbarBranch[1] = ttbarTree->GetBranch("b1Py");
  ttbarBranch[2] = ttbarTree->GetBranch("b1Pz");
  ttbarBranch[3] = ttbarTree->GetBranch("b2Px");
  ttbarBranch[4] = ttbarTree->GetBranch("b2Py");
  ttbarBranch[5] = ttbarTree->GetBranch("b2Pz");

  for (int i=0; i<BRNTTBAR; i++) 
    ttbarBranch[i]->SetAddress(&ttbarBCosTheta[i]);

  std::vector<TVector3> ttbarBQuark(2);

  int ttbarNevent = ttbarTree->GetEntries();
  int ttbarNselected = 0;
  int ttbarNb = 0;
  
  for(int i=0; i<ttbarNevent; i++) {
    ttbarNb += ttbarTree->GetEntry(i);
    ttbarNselected++;
   
    ttbarBQuark.at(0).SetXYZ(ttbarBCosTheta[0], ttbarBCosTheta[1], ttbarBCosTheta[2]);
    ttbarBQuark.at(1).SetXYZ(ttbarBCosTheta[3], ttbarBCosTheta[4], ttbarBCosTheta[5]);
  
    ttbarBCosThetath->Fill( TMath::Cos( ttbarBQuark.at(0).Angle(ttbarBQuark.at(1)) ) );
  }

  ttbarBCosThetath->SetFillStyle(3008);
  ttbarBCosThetath->SetLineColor(kBlue);
  //ttbarBCosThetath->SetStats(0);
  ttbarBCosThetath->Draw("same");

  TLegend *legend = new TLegend(.75,.80,.95,.95);
  legend->AddEntry(bCosThetath,"hh->bbbb");
  legend->AddEntry(ttbarBCosThetath,"ttbar");
  legend->Draw();


  
  return 0;
}
