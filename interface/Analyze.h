#ifndef Analyze_h
#define Analyze_h

#include <TH1D.h>
#include <TH2D.h>
#include <TEfficiency.h>
#include <TTree.h>

#include <map>
#include <string>

class NTupleReader;
class BNL2020Geometry;

class Analyze 
{
public:
    std::map<std::string, std::shared_ptr<TH1D>>  my_histos;
    std::map<std::string, std::shared_ptr<TH2D>>  my_2d_histos;
    std::map<std::string, std::shared_ptr<TEfficiency>>  my_efficiencies;
    
    Analyze();
    ~Analyze(){};
    
    void Loop(NTupleReader& tr, int maxevents = -1);
    void InitHistos(const BNL2020Geometry& g);
    void WriteHistos(TFile* outfile);
    
};

#endif
