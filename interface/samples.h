#ifndef ANASAMPLES_SAMPLES_H
#define ANASAMPLES_SAMPLES_H

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>

#include <cstring>
#include <algorithm>

namespace AnaSamples
{
  enum COLORS{kRed = 632, kGreen = 416, kBlack = 1, kMagenta = 616, kBlue = 600, kYellow = 400, kTeal = 840, kPink = 900, kOrange = 800, kSpring = 820, kWhite = 0, kGray = 0, kCyan = 432, kAzure = 860, kViolet = 880};

  class FileSummary
  {
   public:
    std::string tag;
    std::string filePath, fileName, treePath;
    double xsec, lumi, kfactor, nEvts;
    int color;
    bool isData_;
        
    FileSummary() {}
    FileSummary(const std::string& tag, const std::string& filePath, const std::string& fileName, const std::string& treePath, double xsec, double lumi, double nEvts, double kfactor, int color = kBlack) : tag(tag), filePath(filePath), fileName(fileName), treePath(treePath), xsec(xsec), lumi(lumi), kfactor(kfactor), nEvts(nEvts), color(color), isData_(false)
    {
      weight_ = xsec * lumi * kfactor / nEvts;
    }

    //Constructor which doesn't make a xsec*lumi weighted sample, e.g. for use with data.
    //Initialize xsec, lumi, nEvts to 1 so that the comparison operators still work
    //Need a record of the actual data lumi!
    FileSummary(const std::string& tag, const std::string& filePath, const std::string& fileName, const std::string& treePath, double lumi, double kfactor, int color = kBlack) : tag(tag), filePath(filePath), fileName(fileName), treePath(treePath), xsec(1), lumi(lumi), kfactor(kfactor), nEvts(1), color(color), isData_(true)
    {
      weight_ = kfactor;
    }

    double getWeight() const {return weight_;}
    const std::vector<std::string>& getFilelist() const {return filelist_;}
    template<class T> void addFilesToChain(T* chain, int startfile=0, int filerun=-1) const
    {
      if(filelist_.size() == 0) readFileList();
      if(filerun<0)filerun=filelist_.size();
      for(unsigned int fn = startfile; static_cast<int>(fn)<startfile+filerun && fn<filelist_.size(); fn++)
      {
        //printf("fn = %d, filelist_[fn]=%s\n", fn, filelist_[fn].c_str()); // testing
        chain->Add(filelist_[fn].c_str());
      }
    }
    mutable std::vector<std::string> filelist_;
    void addCollection(const std::string&);
    const std::set<std::string>& getCollections() const
    {
      return collections_;
    }
    void readFileList() const;

   private:
    double weight_;
    std::set<std::string> collections_;
  };

  bool operator< (const FileSummary& lhs, const FileSummary& rhs);
  bool operator== (const FileSummary& lhs, const FileSummary& rhs);
  bool operator!= (const FileSummary& lhs, const FileSummary& rhs);

  //May 5, 2019: Updated Luminosities from PostProcessed_StopTuple_V2.7.2
  static const double luminosity_2016           = 35922.0; // in pb-1 (Data_SingleMuon_2016)
  static const double luminosity_2017           = 41856.0; // in pb-1 (Data_SingleElectron_2017)
  static const double luminosity_2018           = 58905.0; // in pb-1 (Data_EGamma_2018)
  static const double luminosity_2018_AB        = 20757.0; // in pb-1 (Data_EGamma_2018 Periods A + B)
  static const double luminosity_2018_CD        = 38148.0; // in pb-1 (Data_EGamma_2018 Periods C + D)
  // lumi per sample when datasets had different lumis
  static const double luminosity_electron_2016  = 35860.0; // in pb-1 for Data_SingleElectron_2016
  static const double luminosity_muon_2016      = 35922.0; // in pb-1 for Data_SingleMuon_2016
  static const double luminosity_photon_2016    = 35922.0; // in pb-1 for Data_SinglePhoton_2016 
  static const double luminosity_electron_2017  = 41856.0; // in pb-1 for Data_SingleElectron_2017
  static const double luminosity_muon_2017      = 41856.0; // in pb-1 for Data_SingleMuon_2017
  static const double luminosity_photon_2017    = 41666.0; // in pb-1 for Data_SinglePhoton_2017 
  static const double luminosity_electron_2018  = 58905.0; // in pb-1 for Data_EGamma_2018
  static const double luminosity_muon_2018      = 59477.0; // in pb-1 for Data_SingleMuon_2018
  static const double luminosity_photon_2018    = 58905.0; // in pb-1 for Data_EGamma_2018
  
  //static const std::string fileDir = "/eos/uscms/store/user/lpcsusyhad/PHYS14_720_Dec23_2014/";
  //static const std::string fileDir = "/eos/uscms/store/user/lpcsusyhad/PHYS14_720_Mar14_2014_v2/";
  //static const std::string fileDir = "/eos/uscms/store/user/lpcsusyhad/PHYS14_72X_July_2015_v1.1/";
  //static const std::string fileDir = "/eos/uscms/store/user/lpcsusyhad/Spring15_74X_July_2015_v1.1/";
  //static const std::string fileDir = "/eos/uscms/store/user/lpcsusyhad/Spring15_74X_Oct_2015_Ntp_v2X/";
  //static const std::string fileDir = "/eos/uscms/store/user/lpcsusyhad/";
  
  static const std::string fileDir = "/cms/data/store/user/lpcsusyhad/";

  template<class T>
  class SampleBase
  {
   public:
    SampleBase() : nullT_() {};
    const T& operator[](const std::string& key) const
    {
            auto iter = sampleSet_.find(key);
            if(iter != sampleSet_.end()) return iter->second;
            else                         return nullT_;
    }
    const T& null() const {return nullT_;}
    
   protected:
    std::map<std::string, T> sampleSet_;
    const T nullT_;
    static constexpr unsigned int BUF_LEN_ = 4096;

    virtual bool parseCfgLine(const char* buf) = 0;

    void readCfg(const std::string& file)
    {
        FILE *fin = fopen(file.c_str(), "r");

        if(fin != nullptr)
        {
            char buf[BUF_LEN_];
            int lineNum = 0;
            while(!feof(fin) && fgets(buf, BUF_LEN_-1, fin))
            {
                ++lineNum;

                //skip comments
                if(strlen(buf) <= 0 || buf[0] == '#') continue;

                //skip empty lines (is there a way not to copy?)
                std::string sbuf(buf);
                if(std::all_of(sbuf.cbegin(), sbuf.cend(), [](char c) { return std::isspace(c); })) continue;

                //strip out commas
                char *bufPtr = strchr(buf, ',');
                while(bufPtr)
                {
                    *bufPtr = ' ';
                    bufPtr = strchr(bufPtr + 1, ',');
                }

                //strip out newlines
                bufPtr = strchr(buf, '\n');
                if(bufPtr) *bufPtr = '\0';

                //parse line
                if(!parseCfgLine(buf))
                {
                    //if false is returned, the line was not parsed properly
                    printf("Malformed line: %s:%i\n", file.c_str(), lineNum);
                }
            }

            fclose(fin);
        }
        else
        {
            std::cout << "ERROR: Unable to open file " << file << std::endl;
        }
    }


   public:
    decltype(sampleSet_.cbegin()) begin() const { return sampleSet_.cbegin(); }
    decltype(sampleSet_.cend())     end() const { return sampleSet_.cend(); }
    decltype(sampleSet_.size())    size() const { return sampleSet_.size(); }
  };

  class SampleCollection;
  
  class SampleSet : public SampleBase<FileSummary>
  {
    friend class SampleCollection;
   
   public:
    SampleSet(std::string fDir = fileDir, bool isCondor = false, double lumi = luminosity_2016);
    void addSample(const std::string& tag, const std::string& filePath, const std::string& fileName, const std::string& treePath, double xsec, double lumi, double nEvts, double kfactor, int color = kBlack) 
    {
        sampleSet_[tag] = FileSummary(tag, filePath, fileName, treePath, xsec, lumi, nEvts, kfactor, color);
    }

    void addSample(const std::string& tag, const std::string& filePath, const std::string& fileName,  const std::string& treePath, double lumi, double kfactor, int color = kBlack) 
    {
        sampleSet_[tag] = FileSummary(tag, filePath, fileName, treePath, lumi, kfactor, color);
    }
    
    // modify weights to compare two MC samples
    double getCrossSectionRatio(const std::vector<std::string>& sampleTags1, const std::vector<std::string>& sampleTags2, bool verbose = false);
    

   private:
    std::string fDir_;
    bool isCondor_;
    double lumi_;
    
    std::map<std::string, FileSummary>& getMap() { return sampleSet_; }
    
    bool parseCfgLine(const char* buf);
  };

  class SampleCollection : public SampleBase<std::vector<FileSummary>>
  {
   public:
    SampleCollection(const std::string& file, SampleSet& samples);
    std::vector<std::string>& getSampleLabels(std::string name);
    inline double getSampleLumi(std::string name)
    {
      return totalLumiMap_[name];
    }
    
    // modify weights to compare two MC samples
    double getCrossSectionRatio(std::string& sampleTag1, std::string sampleTag2, bool verbose = false);

   private:
    std::map<std::string, double> totalLumiMap_;
    std::map<std::string, std::vector<std::string>> nameVec_;
    SampleSet& ss_;
    void addSampleSet(SampleSet& samples, const std::string& name, const std::vector<std::string>& vss);
    bool parseCfgLine(const char* buf);
  };
}

#endif
