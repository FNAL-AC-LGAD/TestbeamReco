#ifndef Confg_h
#define Confg_h

#include "TestbeamReco/interface/NTupleReader.h"
#include "TestbeamReco/interface/Geometry.h"
#include "TestbeamReco/interface/PrepNTupleVars.h"
#include "TestbeamReco/interface/SignalProperties.h"
#include "TestbeamReco/interface/SpatialReconstruction.h"
#include "TestbeamReco/interface/Timing.h"
#include "TestbeamReco/interface/Utility.h"

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
        tr.registerDerivedVar("sensorConfigMap", g.sensorConfigMap);
        tr.registerDerivedVar("amplitudeCorrectionFactor", g.amplitudeCorrectionFactor);
        tr.registerDerivedVar("timeCalibrationCorrection", g.timeCalibrationCorrection);
        tr.registerDerivedVar("photekIndex", g.photekIndex);
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

        std::string runYear = "2021";
        tr.registerDerivedVar("runYear",runYear);

        const auto voltage = getVoltage(filetag);
        tr.registerDerivedVar("voltage", voltage);
        std::cout<<"Voltage: "<<voltage<<std::endl;
        
        if(filetag.find("BNL2020") != std::string::npos)
        {
            registerGeometry(tr, BNL2020Geometry());
        }
        else if(filetag.find("BNL2021") != std::string::npos)
        {
            registerGeometry(tr, BNL2021Geometry());
        }
        else if(filetag.find("HPK_pad_C2") != std::string::npos)
        {
            registerGeometry(tr, HPKPadC2Geometry());
        }
        else if(filetag.find("HPK_pad_B2") != std::string::npos)
        {
            registerGeometry(tr, HPKPadB2Geometry());
        }
        else if(filetag.find("HPK_strips") != std::string::npos)
        {
            registerGeometry(tr, HPKStripsC2WideMetalGeometry());
        }
        else if(filetag.find("Ron_wide") != std::string::npos)
        {
            registerGeometry(tr, RonStripsGeometry());
        }
        else if(filetag.find("BNL2021_quadpix") != std::string::npos)
        {
            registerGeometry(tr, BNLPixelHexGeometry());
        }
        else
        {
            registerGeometry(tr, DefaultGeometry());
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
        else
        {
            const std::vector<std::string> modulesList = {
                "PrepNTupleVars",
            };
            registerModules(tr, std::move(modulesList));
        }
    }
};

#endif
