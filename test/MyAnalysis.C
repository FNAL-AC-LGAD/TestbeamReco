#include "TestbeamReco/interface/samples.h"
#include "TestbeamReco/interface/SATException.h"
#include "TestbeamReco/interface/NTupleReader.h"
#include "TestbeamReco/interface/MiniTupleMaker.h"
#include "TestbeamReco/interface/MakeNNVariables.h"
#include "TestbeamReco/interface/Utility.h"
#include "TestbeamReco/interface/Analyze.h"
#include "TestbeamReco/interface/Align.h"
#include "TestbeamReco/interface/InitialAnalyzer.h"
#include "Config.h"
#include "TSystem.h"
#include "TH1D.h"
#include "TFile.h"
#include "TChain.h"
#include "TGraph.h"

#include <iostream>
#include <getopt.h>
#include <string>
#include <functional>
#include <unistd.h>

const std::string getFullPath(const std::string& file)
{
    char buf[512];
    int count = readlink(file.c_str(), buf, sizeof(buf));
    if(count >= 0)
    {
        buf[count] = '\0';
        return std::string(buf);
    }
    else
    {
        std::cout<<"Could not get full path of "<<file<<std::endl;
        return std::string();
    }
}

template<typename Analyze> void run(const std::set<AnaSamples::FileSummary>& vvf, 
                                    const int startFile, const int nFiles, const int maxEvts, 
                                    TFile* const outfile, const std::string& analyzer)
{
    std::cout << "Initializing..." << std::endl;
    Analyze a;
    bool firstFile = true;
    for(const auto& file : vvf)
    {
        // Define what is needed per sample set
        std::cout << "Running over sample " << file.tag << std::endl;
        TChain* ch = new TChain( (file.treePath).c_str() );
        file.addFilesToChain(ch, startFile, nFiles);
        NTupleReader tr(ch, {"i_evt"});
        tr.registerDerivedVar("filetag",file.tag);
        tr.registerDerivedVar("analyzer",analyzer);
        tr.registerDerivedVar("firstFile",firstFile);

        printf( "nFiles: %i startFile: %i maxEvts: %i \n",nFiles,startFile,maxEvts ); fflush( stdout );

        // Define classes/functions that add variables on the fly        
        Config c;
        c.setUp(tr);

        // Loop over all of the events and fill histos
        std::cout << "Starting event loop (in run)" << std::endl;
        a.Loop(tr, maxEvts);
        // Cleaning up dynamic memory
        delete ch;

        firstFile = false;
    }
    std::cout << "Writing histograms..." << std::endl;
    a.WriteHistos(outfile);
}

std::set<AnaSamples::FileSummary> setFS(const std::string& dataSets, const bool isCondor)
{
    AnaSamples::SampleSet        ss("sampleSets.cfg", isCondor);
    AnaSamples::SampleCollection sc("sampleCollections.cfg", ss);

    std::map<std::string, std::vector<AnaSamples::FileSummary>> fileMap;
    if(ss[dataSets] != ss.null())
    {
        fileMap[dataSets] = {ss[dataSets]};
        for(const auto& colls : ss[dataSets].getCollections())
        {
            fileMap[colls] = {ss[dataSets]};
        }
    }
    else if(sc[dataSets] != sc.null())
    {
        fileMap[dataSets] = {sc[dataSets]};
        int i = 0;
        for(const auto& fs : sc[dataSets])
        {
            fileMap[sc.getSampleLabels(dataSets)[i++]].push_back(fs);
        }
    }
    std::set<AnaSamples::FileSummary> vvf;
    for(auto& fsVec : fileMap) for(auto& fs : fsVec.second) vvf.insert(fs);    
    if(vvf.size() == 0) std::cout<< utility::color("No samples for \""+std::string(dataSets)+"\" in the sampleSet.cfg","red") <<std::endl;

    return vvf;
}

int main(int argc, char *argv[])
{
    int opt, option_index = 0;
    bool runOnCondor = false;
    std::string histFile = "myoutputfile.root", dataSets = "2016_TT", analyzer = "Analyze";
    int nFiles = -1, startFile = 0, maxEvts = -1;

    static struct option long_options[] = {
        {"condor",             no_argument, 0, 'c'},
        {"verbose",            no_argument, 0, 'v'},
        {"analyzer",     required_argument, 0, 'A'},
        {"histFile",     required_argument, 0, 'H'},
        {"dataSets",     required_argument, 0, 'D'},
        {"numFiles",     required_argument, 0, 'N'},
        {"startFile",    required_argument, 0, 'M'},
        {"numEvts",      required_argument, 0, 'E'},
    };

    // here is the options to run the codes / can add options
    while((opt = getopt_long(argc, argv, "cvA:H:D:N:M:E:", long_options, &option_index)) != -1)
    {
        switch(opt)
        {
            case 'c': runOnCondor       = true;              break;
            case 'A': analyzer          = optarg;            break;
            case 'H': histFile          = optarg;            break;
            case 'D': dataSets          = optarg;            break;
            case 'N': nFiles            = int(atoi(optarg)); break;
            case 'M': startFile         = int(atoi(optarg)); break;
            case 'E': maxEvts           = int(atoi(optarg)); break;
        }
    }

    bool organized_mode = true;
    if(organized_mode){
        TString outDir = Form("../output/%s/",dataSets.c_str());
        gSystem->mkdir("../output");
        gSystem->mkdir(outDir);

        char thistFile[128];
        sprintf(thistFile, "../output/%s/%s_%s.root", dataSets.c_str(),dataSets.c_str(), analyzer.c_str());
        histFile = thistFile;
    }

    if(runOnCondor)
    {
        char thistFile[128];
        sprintf(thistFile, "MyAnalysis_%s_%d.root", dataSets.c_str(), startFile);
        histFile = thistFile;
    }

    std::set<AnaSamples::FileSummary> vvf = setFS(dataSets, runOnCondor); 
    TFile* outfile = TFile::Open(histFile.c_str(), "RECREATE");

    std::vector<std::pair<std::string, std::function<void(const std::set<AnaSamples::FileSummary>&,const int,const int,const int,TFile* const,const std::string&)>>> AnalyzerPairVec = {
        {"Analyze",             run<Analyze>},
        {"Align",               run<Align>},
        {"InitialAnalyzer",     run<InitialAnalyzer>},
        {"MakeNNVariables",     run<MakeNNVariables>},
    }; 

    try
    {
        bool foundAnalyzer = false;
        for(auto& pair : AnalyzerPairVec)
        {
            if(pair.first==analyzer) 
            {
                std::cout<<"Running the " << analyzer << " Analyzer" <<std::endl;
                pair.second(vvf,startFile,nFiles,maxEvts,outfile,analyzer); 
                foundAnalyzer = true;
            }
        }

        if (!foundAnalyzer)
        {
            std::cout << utility::color("ERROR: The analyzer \"" + analyzer + "\" is not an analyzer option! Please add it to the MyAnalysis.C list.", "red") << std::endl;        
        }
        outfile->Close();
    }
    catch(const std::string e)
    {
        std::cout << e << std::endl;
        return 0;
    }
    catch(const SATException e)
    {
        std::cout << e << std::endl;
        return 0;
    }

    return 0;
}
