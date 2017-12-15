void root_draw_2d_hist()
{
  TCanvas *c1 = new TCanvas("c1", "c1",900,900);
  gStyle->SetOptStat(0);
  c1->cd();
  
  TFile *f = new TFile("/home/peilong/Downloads/hist-mc15_14TeV_vbf2600_FCal.root");
  f.ls();
  TH2D * h1 = (TH2D*)f.Get("rho_eta");
  h1->Draw("colz"); 

  TCanvas *c2 = new TCanvas("c2", "c2",900,900);
  gStyle->SetOptStat(0);
  c2->cd();
  
  TH2D * h2 = (TH2D*)f.Get("rho_eta_jet_uncorr");
  h2->Draw("colz"); 

  TCanvas *c3 = new TCanvas("c3", "c3",900,900);
  gStyle->SetOptStat(0);
  c3->cd();
  
  TH2D * h3 = (TH2D*)f.Get("rho_eta_jet_corr_sel");
  h3->Draw("colz"); 

  TCanvas *c4 = new TCanvas("c4", "c4",900,900);
  gStyle->SetOptStat(0);
  c4->cd();
  
  TH2D * h4 = (TH2D*)f.Get("rho_eta_jet_corr_rej");
  h4->Draw("colz"); 
  //
  
  /*  
  // Create, fill and project a 2D histogram.
  TH2D *h2 = new TH2D("h2","",40,-4,4,40,-20,20);
  Float_t px, py;
  
  for (Int_t i = 0; i < 25000; i++) {
    gRandom->Rannor(px,py);
    h2->Fill(px,5*py);
  }
  TH1D * projh2X = h2->ProjectionX();
  TH1D * projh2Y = h2->ProjectionY();

  // Drawing
  center_pad->cd();
  gStyle->SetPalette(1);
  h2->Draw("COL");

  top_pad->cd();
  projh2X->SetFillColor(kBlue+1);
  projh2X->Draw("bar");

  right_pad->cd();
  projh2Y->SetFillColor(kBlue-2);
  projh2Y->Draw("hbar");

  c1->cd();
  TLatex *t = new TLatex();
  t->SetTextFont(42);
  t->SetTextSize(0.02);
  t->DrawLatex(0.6,0.88,"This example demonstrate how to display");
  t->DrawLatex(0.6,0.85,"a histogram and its two projections.");
}

h2proj.C:1
  */


}
