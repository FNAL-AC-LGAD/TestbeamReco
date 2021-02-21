#ifndef Confg_h
#define Confg_h

#include "TestbeamReco/interface/NTupleReader.h"
#include "TestbeamReco/interface/PrepNTupleVars.h"

class Config
{
private:
    void registerModules(NTupleReader& tr, const std::vector<std::string>&& modules) const
    {
        for(const auto& module : modules)
        {
            if     (module=="PrepNTupleVars")     tr.emplaceModule<PrepNTupleVars>();
            //else if(module=="PartialUnBlinding")  tr.emplaceModule<PartialUnBlinding>();
        }
    }

public:
    Config() 
    {
    }

    void setUp(NTupleReader& tr) const
    {
        //Get and make needed info
        //const auto& filetag = tr.getVar<std::string>("filetag");
        const auto& analyzer = tr.getVar<std::string>("analyzer");

        std::string runYear = "2021";
        tr.registerDerivedVar("runYear",runYear);

        //Register Modules that are needed for each Analyzer
        if (analyzer=="AnalyzeTest")
        {
            const std::vector<std::string> modulesList = {
                "PrepNTupleVars",
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
