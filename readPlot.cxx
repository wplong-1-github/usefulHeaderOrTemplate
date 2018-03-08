#include <TFile.h>

int readPlot() {
  
  //  TCanvas* c2 = new TCanvas("theCanvas", "theCanvas", 800, 600);
  
  TFile *f1 = new TFile("./submitDir/hist-mc15_13TeV.342619.aMcAtNloHerwigppEvtGen_UEEE5_CTEQ6L1_CT10ME_hh_4b.merge.DAOD_EXOT8.e4419_s2608_r6869_r6282_p2438.root");
  /*
  f1->ls();

  TH1F *bPT = (TH1F*)f1->Get("h4_bEnergy");
  bPT->GetXaxis()->SetTitle("b-jet pT / Gev");
  bPT->GetXaxis()->CenterTitle();
  bPT->GetYaxis()->SetTitle("count");
  bPT->GetYaxis()->CenterTitle();
  //  c2->cd();
  bPT->Draw();
  */

  //  TCanvas* c3 = new TCanvas("theCanvas", "theCanvas", 800, 600);

  f1->ls();
  TH1F *Phi = (TH1F*)f1->Get("h3_bPhi");

  

  Phi->SetTitle("phi between higgs and its two daughter partiles(b-jets)");
  Phi->SetAxisRange(-4.,4.);
  Phi->GetXaxis()->SetTitle("phi between higgs and two b-jets)");
  Phi->GetXaxis()->CenterTitle();
  Phi->GetYaxis()->SetTitle("count");
  Phi->GetYaxis()->CenterTitle();
  //  c3->cd();
  Phi->Draw();

  TF1 *fit1 = new TF1("fit1", "expo");
  fit1->SetRange(0., 3.);
  fit1->SetLineColor(2);
  Phi->Fit("fit1","R");
  

  /*
  TH1D *pol = new TH1D("polarHist", "polarHist", 20, 0., 2.*TMath:Pi());
  double theta;

  for (int i=0; i<
  */




  gStyle->SetOptStat(0);


  TFile *f = new TFile("./submitDir/data-myOutput/mc15_13TeV.342619.aMcAtNloHerwigppEvtGen_UEEE5_CTEQ6L1_CT10ME_hh_4b.merge.DAOD_EXOT8.e4419_s2608_r6869_r6282_p2438.root");
  TTree* t4 = (TTree*)f->Get("tree");

  TH2D *bPhi = new TH2D("phi_Value", "b jet pT value", 100, -TMath::Pi(), TMath::Pi(), 1, 0, 1);

  double theta;//, r;

  /*
  for(int i=1; i<=bPhi->GetNbinsX(); i++)
    {
      theta = bPhi->GetXaxis()->GetBinCenter(i);
      //      for(int j=1; j<=bPhi->GetNbinsY(); j++)
      //{
      //	  r = bPhi->GetYaxis()->GetBinCenter(j);
	  bPhi->SetBinContent(i, j, r*cos(2.*theta) );
	  //}
    }
  */


  double phi1, phi2, phi3, phi4;

  TBranch *branch1 = t4->GetBranch("temp1");
  TBranch *branch2 = t4->GetBranch("temp2");
  TBranch *branch3 = t4->GetBranch("temp3");
  TBranch *branch4 = t4->GetBranch("temp4");

  branch1->SetAddress(&phi1);
  branch2->SetAddress(&phi2);
  branch3->SetAddress(&phi3);
  branch4->SetAddress(&phi4);

  int nevent = t4->GetEntries();
  int nselected = 0;
  int nb = 0;

  for(int i=0; i<nevent; i++) {
    nb += t4->GetEntry(i);
    nselected++;
   
    bPhi->Fill(phi1, 0.5);
    bPhi->Fill(phi2, 0.5);
    bPhi->Fill(phi3, 0.5);
    bPhi->Fill(phi4, 0.5);

  }


  TH2D* dummy_his = new TH2D("dummy", "phi between higgs and its two daughter partiles(b-jets)", 100, -1, 1, 100, -1, 1);

  TCanvas* c1 = new TCanvas("theCanvas", "theCanvas", 600, 600);

  c1->SetFrameLineColor(0);
  dummy_his->GetXaxis()->SetAxisColor(0);
  dummy_his->GetXaxis()->SetLabelColor(0);
  dummy_his->GetYaxis()->SetAxisColor(0);
  dummy_his->GetYaxis()->SetLabelColor(0);

  dummy_his->Draw("COL"); // draw the dummy histogram first

  bPhi->GetXaxis()->SetAxisColor(0);
  bPhi->GetXaxis()->SetLabelColor(0);
  bPhi->GetYaxis()->SetAxisColor(0);
  bPhi->GetYaxis()->SetLabelColor(0);


  bPhi->Draw("COLZA POL SAME");


  return 0;
}
