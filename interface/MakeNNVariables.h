#ifndef MakeNNVariables_h
#define MakeNNVariables_h

#include <TH1D.h>
#include <TH2D.h>
#include <TEfficiency.h>
#include <TTree.h>

#include <map>
#include <string>

class NTupleReader;
class MiniTupleMaker;

class MakeNNVariables{

public :
   std::map<std::string, std::shared_ptr<TH1D>>  my_histos;
   std::map<std::string, std::shared_ptr<TH2D>>  my_2d_histos;
   std::map<std::string, std::shared_ptr<TEfficiency>>  my_efficiencies;

   MakeNNVariables();
   ~MakeNNVariables(){};

   void     Loop(NTupleReader& tr, int maxevents = -1);
   void     InitHistos();
   void     WriteHistos(TFile* outfile); 

   MiniTupleMaker *myMiniTupleTrain;
   MiniTupleMaker *myMiniTupleTest;
   MiniTupleMaker *myMiniTupleVal;

   TTree          *myTreeTrain;
   TTree          *myTreeTest;
   TTree          *myTreeVal;
};

#endif
