#ifndef Analyze_h
#define Analyze_h

#include <TH1D.h>
#include <TH2D.h>
#include <TH3D.h>
#include <TProfile2D.h>
#include <TEfficiency.h>
#include <TTree.h>

#include <map>
#include <string>

class NTupleReader;

class Analyze 
{
public:
    std::map<std::string, std::shared_ptr<TH1D>>  my_histos;
    std::map<std::string, std::shared_ptr<TH2D>>  my_2d_histos;
    std::map<std::string, std::shared_ptr<TH3D>>  my_3d_histos; 
    std::map<std::string, std::shared_ptr<TProfile2D>>  my_2d_prof;
    std::map<std::string, std::shared_ptr<TEfficiency>>  my_efficiencies;
    
    Analyze();
    ~Analyze(){};
    
    void Loop(NTupleReader& tr, int maxevents = -1);
    void InitHistos(const std::vector<std::vector<int>>& geometry, const std::map<std::string,double>& sensorConfigMap);
    void WriteHistos(TFile* outfile);
    std::pair<double,double> Rotate(double x0, double y0, double angle);
    std::map<std::string, double> GetSensorConfigMap(std::string sensorName);

};

#endif
