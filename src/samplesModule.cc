#include "../interface/samples.h"

#include <string>
#include <iostream>
extern "C" {
    double SC_fixed_lumi(){ return AnaSamples::luminosity_2016; }
    AnaSamples::SampleSet* SS_new(char *ssfile)
    {
        return new AnaSamples::SampleSet(ssfile);
    }
    AnaSamples::SampleCollection* SC_new(AnaSamples::SampleSet* ss, char* scfile)
    {
        return new AnaSamples::SampleCollection(scfile, *ss); 
    }
    AnaSamples::SampleCollection* SSSC_new(char *ssfile, char* scfile)
    {
        AnaSamples::SampleSet *ss = new AnaSamples::SampleSet(ssfile);
        return new AnaSamples::SampleCollection(scfile, *ss); 
    }
    int SC_samples_size(AnaSamples::SampleCollection* sc, char *scn){ return (*sc)[std::string(scn)].size(); }
    char const ** SC_samples(AnaSamples::SampleCollection* sc, char *scn)
    {
        auto& sampleVec = (*sc)[std::string(scn)];
        const char **array = new const char*[sampleVec.size()];
        int i = 0;
        for(auto& sample : sampleVec)
        {
            std::string* s = new std::string (sample.filePath + "/" + sample.fileName);
            array[i++] = s->c_str();
        }
        return array;
    }
    char const ** SC_samples_names(AnaSamples::SampleCollection* sc, char *scn)
    {
        auto& sampleVec = sc->getSampleLabels(std::string(scn));
        const char **array = new const char*[sampleVec.size()];
        int i = 0;
        for(auto& sample : sampleVec)
        {
            array[i++] = sample.c_str();
        }
        return array;
    }
    int const * SC_samples_nEvts(AnaSamples::SampleCollection* sc, char *scn)
    {
        auto& sampleVec = (*sc)[std::string(scn)];
        int *array = new int[sampleVec.size()];
        int i = 0;
        for(auto& sample : sampleVec)
        {
            array[i++] = sample.nEvts;
        }
        return array;
    }
    char const ** SS_samples(AnaSamples::SampleSet* ss)
    {
        const char **array = new const char*[ss->size()];
        int i = 0;
        for(auto& sample : *ss)
        {
            std::string* s = new std::string (sample.second.filePath + "/" + sample.second.fileName);
            array[i++] = s->c_str();
        }
        return array;
    }
    char const ** SS_samples_names(AnaSamples::SampleSet* ss)
    {
        const char **array = new const char*[ss->size()];
        int i = 0;
        for(auto& sample : *ss)
        {
            array[i++] = sample.first.c_str();
        }
        return array;
    }
    int SC_samplecollection_size(AnaSamples::SampleCollection* sc, char *scn){ return sc->size(); }
    int SS_samples_size(AnaSamples::SampleCollection* ss){ return ss->size(); }
    char const ** SC_samplecollection_names(AnaSamples::SampleCollection* sc)
    {
        const char **array = new const char*[sc->size()];
        int i = 0;
        for(auto& sample : *sc)
        {
            array[i++] = sample.first.c_str();
        }
        return array;
    }
    double const * SC_samplecollection_lumis(AnaSamples::SampleCollection* sc)
    {
        double *array = new double[sc->size()];
        int i = 0;
        for(auto& sample : *sc)
        {
            array[i++] = sc->getSampleLumi(sample.first);
        }
        return array;
    }
}
