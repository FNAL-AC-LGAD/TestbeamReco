#ifndef Confg_h
#define Confg_h

#include "TestbeamReco/interface/NTupleReader.h"
#include "TestbeamReco/interface/Geometry.h"
#include "TestbeamReco/interface/Geometry2022.h"
#include "TestbeamReco/interface/PrepNTupleVars.h"
#include "TestbeamReco/interface/SignalProperties.h"
#include "TestbeamReco/interface/SpatialReconstruction.h"
#include "TestbeamReco/interface/Timing.h"
#include "TestbeamReco/interface/Utility.h"

#include <iostream>
#include <fstream>

class Config
{
private:
    void registerModules(NTupleReader& tr, const std::vector<std::string>&& modules) const
    {
        for(const auto& module : modules)
        {
            if     (module=="PrepNTupleVars")          tr.emplaceModule<PrepNTupleVars>();
            else if(module=="SignalProperties")        tr.emplaceModule<SignalProperties>();
            else if(module=="SpatialReconstruction")   tr.emplaceModule<SpatialReconstruction>();
            else if(module=="Timing")                  tr.emplaceModule<Timing>();
        }
    }

    template<typename T> void registerGeometry(NTupleReader& tr, const T& g) const
    {
        tr.registerDerivedVar("indexToGeometryMap", g.indexToGeometryMap);
        tr.registerDerivedVar("geometry", g.geometry);
        tr.registerDerivedVar("acLGADChannelMap", g.acLGADChannelMap);
        tr.registerDerivedVar("numLGADchannels", g.numLGADchannels);
        tr.registerDerivedVar("amplitudeCorrectionFactor", g.amplitudeCorrectionFactor);
        tr.registerDerivedVar("stripWidth",g.stripWidth);
        tr.registerDerivedVar("sensorCenter",g.sensorCenter); 
        tr.registerDerivedVar("sensorCenterY",g.sensorCenterY); 
        tr.registerDerivedVar("pitch",g.pitch); 
        tr.registerDerivedVar("stripCenterXPosition", g.stripCenterXPosition);
        tr.registerDerivedVar("stripCenterYPosition", g.stripCenterYPosition);
        tr.registerDerivedVar("timeCalibrationCorrection", g.timeCalibrationCorrection);
        tr.registerDerivedVar("photekIndex", g.photekIndex);
        tr.registerDerivedVar("lowGoodStripIndex", g.lowGoodStripIndex);
        tr.registerDerivedVar("highGoodStripIndex", g.highGoodStripIndex);
        tr.registerDerivedVar("sensorEdges", g.sensorEdges);
        tr.registerDerivedVar("alpha", g.alpha);
        tr.registerDerivedVar("beta",  g.beta);
        tr.registerDerivedVar("gamma", g.gamma);
        tr.registerDerivedVar("z_dut", g.z_dut);
        tr.registerDerivedVar("xmin", g.xmin);
        tr.registerDerivedVar("xmax", g.xmax);
        tr.registerDerivedVar("ymin", g.ymin);
        tr.registerDerivedVar("ymax", g.ymax);
        tr.registerDerivedVar("positionRecoMaxPoint", g.positionRecoMaxPoint);
        tr.registerDerivedVar("photekSignalThreshold", g.photekSignalThreshold);
        tr.registerDerivedVar("noiseAmpThreshold", g.noiseAmpThreshold);
        tr.registerDerivedVar("signalAmpThreshold", g.signalAmpThreshold);
        tr.registerDerivedVar("isPadSensor", g.isPadSensor);
        tr.registerDerivedVar("isHPKStrips", g.isHPKStrips);
        tr.registerDerivedVar("enablePositionReconstruction", g.enablePositionReconstruction);
        tr.registerDerivedVar("enablePositionReconstructionPad", g.enablePositionReconstructionPad);
        tr.registerDerivedVar("positionRecoPar", g.positionRecoPar);
        tr.registerDerivedVar("positionRecoParRight", g.positionRecoParRight);
        tr.registerDerivedVar("positionRecoParLeft", g.positionRecoParLeft);
        tr.registerDerivedVar("positionRecoParTop", g.positionRecoParTop);
        tr.registerDerivedVar("positionRecoParBot", g.positionRecoParBot);
        tr.registerDerivedVar("xSlices", g.xSlices);
        tr.registerDerivedVar("ySlices", g.ySlices);
        tr.registerDerivedVar("boxes_XY", g.boxes_XY);        
    }

    int getVoltage(std::string name) const
    {
        std::vector<std::string> stringChunks;
        bool keepGoing = true;
        while(keepGoing)
        {
            const auto& first = utility::split("first", name, "_");
            const auto& last = utility::split("last", name, "_");
            stringChunks.emplace_back(first);
            if(last == "" || last == name)
            {
                keepGoing = false;
            }
            else 
            {
                name = last;
            }
        }

        std::string sVoltage;
        for(auto c : stringChunks)
        {
            sVoltage = utility::split("first", c, "V");
            if(sVoltage != c) break;
        }

        return std::stoi(sVoltage);;
    }

public:
    Config() 
    {
    }

    void setUp(NTupleReader& tr) const
    {
        //Get and make needed info
        const auto& filetag = tr.getVar<std::string>("filetag");
        const auto& analyzer = tr.getVar<std::string>("analyzer");
        const auto& firstFile = tr.getVar<bool>("firstFile");

        std::string runYear = "2021";
        tr.registerDerivedVar("runYear",runYear);
        
        //Define zScan values and save to a python file for later
        const auto voltage = getVoltage(filetag);
        tr.registerDerivedVar("voltage", voltage);
        std::cout<<"Voltage: "<<voltage<<std::endl;

        // FIND THE WAY TO ADD THESE VALUES TO IMPROVE THE SCAN!
        // THIS DOESN'T WORK BECAUSE WE HAVEN'T DEFINED THE GEOMETRIES YET... CAN WE JUST MOVE THIS DEFINITION BELLOW?
        // const auto& z_dut = tr.getVar<double>("z_dut");
        // const auto& alpha = tr.getVar<double>("alpha");
        // const auto& beta  = tr.getVar<double>("beta");
        // const auto& gamma = tr.getVar<double>("gamma");

        const auto& z_dut_def = 28.0;
        const auto& alpha_def = 0.0;
        const auto& beta_def  = 0.0;
        const auto& gamma_def = 90.0;

        //Define zScan // [-20.0, 20.0]
        double zMin = -20.0, zStep = 1.0;
        unsigned int nZBins = 41;
        std::vector<double> zScan(nZBins);
        std::string pythonBins = "z_values = [";
        for(unsigned int i = 0; i < nZBins; i++) 
        {        
            pythonBins += std::to_string(z_dut_def + zMin) +  ",";
            zScan[i]=z_dut_def + zMin;
            zMin+=zStep;
        }
        tr.registerDerivedVar<std::vector<double>>("zScan",zScan);
        pythonBins+="]\n";

        //Define alphaScan // [-2.0, 2.0]
        double alphaMin = -2.0, alphaStep = 0.1;
        unsigned int nAlphaBins = 41;
        std::vector<double> alphaScan(nAlphaBins);
        pythonBins+="alpha_values = [";
        for(unsigned int i = 0; i < nAlphaBins; i++) 
        {        
            pythonBins += std::to_string(alpha_def + alphaMin) +  ",";
            alphaScan[i]=alpha_def + alphaMin;
            alphaMin+=alphaStep;
        }
        tr.registerDerivedVar<std::vector<double>>("alphaScan",alphaScan);
        pythonBins+="]\n";

        //Define betaScan // [-2.0, 2.0]
        double betaMin = -2.0, betaStep = 0.1;
        unsigned int nbetaBins = 41;
        std::vector<double> betaScan(nbetaBins);
        pythonBins+="beta_values = [";
        for(unsigned int i = 0; i < nbetaBins; i++) 
        {        
            pythonBins += std::to_string(beta_def + betaMin) +  ",";
            betaScan[i]=beta_def + betaMin;
            betaMin+=betaStep;
        }
        tr.registerDerivedVar<std::vector<double>>("betaScan",betaScan);
        pythonBins+="]\n";

        //Define gammaScan // [-2.0, 2.0]
        double gammaMin = -2.0, gammaStep = 0.1;
        unsigned int ngammaBins = 41;
        std::vector<double> gammaScan(ngammaBins);
        pythonBins+="gamma_values = [";
        for(unsigned int i = 0; i < ngammaBins; i++) 
        {        
            pythonBins += std::to_string(gamma_def + gammaMin) +  ",";
            gammaScan[i]=gamma_def + gammaMin;
            gammaMin+=gammaStep;
        }
        tr.registerDerivedVar<std::vector<double>>("gammaScan",gammaScan);
        pythonBins+="]";

        //Save python file with for later
        if(firstFile)
        {
            std::ofstream overwriteFile("../macros/AlignBinning.py", std::ofstream::trunc);
            overwriteFile << pythonBins << std::endl;
            overwriteFile.close();
        }

        //Setup Sensor Geometry 
        if     (filetag.find("BNL2020")                        != std::string::npos) registerGeometry(tr, BNL2020Geometry(voltage));
        else if(filetag.find("BNL2021_wide")                   != std::string::npos) registerGeometry(tr, BNL2021WideGeometry(voltage));
        else if(filetag.find("BNL2021_medium")                 != std::string::npos) registerGeometry(tr, BNL2021MediumGeometry(voltage));
        else if(filetag.find("BNL2021_narrow")                 != std::string::npos) registerGeometry(tr, BNL2021NarrowGeometry(voltage));
        else if(filetag.find("HPK_pad_C2")                     != std::string::npos) registerGeometry(tr, HPKPadC2Geometry(voltage));
        else if(filetag.find("HPK_pad_B2")                     != std::string::npos) registerGeometry(tr, HPKPadB2Geometry(voltage));
        else if(filetag.find("HPK_strips_C2_45um")             != std::string::npos) registerGeometry(tr, HPKStripsC2WideMetalGeometry(voltage));
        else if(filetag.find("HPK_strips_C2_30um")             != std::string::npos) registerGeometry(tr, HPKStripsC2NarrowMetalGeometry(voltage));
        else if(filetag.find("Ron_wide")                       != std::string::npos) registerGeometry(tr, RonStripsGeometry(voltage));
        else if(filetag.find("BNL2021_hexpix")                 != std::string::npos) registerGeometry(tr, BNLPixelHexGeometry(voltage));
        else if(filetag.find("HPK2_DCLGAD_220V")               != std::string::npos) registerGeometry(tr, HPK2DCLGADGeometry(voltage));
        else if(filetag.find("EIC_W1_1cm_255V")                != std::string::npos) registerGeometry(tr, EIC1cmStripsGeometry(voltage));
        else if(filetag.find("EIC_W1_1cm_300_multiPitch_240V") != std::string::npos) registerGeometry(tr, EIC1cmStrips300Geometry(voltage));
        else if(filetag.find("EIC_W1_1cm_200_multiPitch_240V") != std::string::npos) registerGeometry(tr, EIC1cmStrips200Geometry(voltage));
        else if(filetag.find("EIC_W1_1cm_100_multiPitch_240V") != std::string::npos) registerGeometry(tr, EIC1cmStrips100Geometry(voltage));
        else if(filetag.find("EIC_W1_2p5cm_UCSC_340V")         != std::string::npos) registerGeometry(tr, EIC2p5cmStripsUCSCGeometry(voltage));
        else
        {
            registerGeometry(tr, DefaultGeometry(voltage));
            std::cout<<"Warning: Using DefaultGeometry, odds are this is not what you want"<<std::endl;
        }

        //Register Modules that are needed for each Analyzer
        if (analyzer=="Analyze")
        {
            const std::vector<std::string> modulesList = {
                "PrepNTupleVars",
                "SignalProperties",
                "SpatialReconstruction",
                "Timing",
            };
            registerModules(tr, std::move(modulesList));
        }
        else if (analyzer=="Align")
        {
            const std::vector<std::string> modulesList = {
                "PrepNTupleVars",
                "SignalProperties",
                "SpatialReconstruction",
                "Timing",
            };
            registerModules(tr, std::move(modulesList));
        }
        else
        {
            const std::vector<std::string> modulesList = {
                "PrepNTupleVars",
                "SignalProperties",
                "SpatialReconstruction",
                "Timing",
            };
            registerModules(tr, std::move(modulesList));
        }
    }
};

#endif
