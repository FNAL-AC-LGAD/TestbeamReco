#include "../interface/samples.h"

#include <iostream>
#include <cstdio>

namespace AnaSamples
{
    void FileSummary::readFileList() const
    {
        if(filelist_.size()) filelist_.clear();
        
        std::string filePathAndName;
        if(filePath.size() > 0)
        {
            filePathAndName = filePath + "/" + fileName;
        }
        else
        {
            filePathAndName = fileName;
        }

        FILE *f = fopen(filePathAndName.c_str(), "r");
        char buff[1024];
        if(f)
        {
            while(!feof(f) && fgets(buff, 1023, f))
            {
                for(char* k = strchr(buff, '\n'); k != 0; k = strchr(buff, '\n')) *k = '\0';
                filelist_.push_back(buff);
            }
            fclose(f);
        }
        else std::cout << "In FileSummary::readFileList(): Filelist file \"" << filePathAndName << "\" not found!!!!!!!" << std::endl;
    }

    void FileSummary::addCollection(const std::string& colName)
    {
        collections_.insert(colName);
    }

    // modify weights to compare two MC samples
    double SampleSet::getCrossSectionRatio(const std::vector<std::string>& sampleTags1, const std::vector<std::string>& sampleTags2, bool verbose)
    {
        double sum_xsec1 = 0.0;
        double sum_xsec2 = 0.0;
        // add sample 1 cross sections
        for (unsigned int i = 0; i < sampleTags1.size(); i++)
        {
            FileSummary fs = sampleSet_[sampleTags1[i]];
            double xsec = fs.kfactor * fs.xsec;
            sum_xsec1 += xsec;
        }
        // add sample 2 cross sections
        for (unsigned int i = 0; i < sampleTags2.size(); i++)
        {
            FileSummary fs = sampleSet_[sampleTags2[i]];
            double xsec = fs.kfactor * fs.xsec;
            sum_xsec2 += xsec;
        }
        // calculate cross section ratio
        double xsec_ratio = sum_xsec2 / sum_xsec1;
        if (verbose) 
        {
            printf("In SampleSet::getCrossSectionRatio():\n");
            printf("  k * sum_xsec1 = %f\n", sum_xsec1);
            printf("  k * sum_xsec2 = %f\n", sum_xsec2);
            printf("  xsec_ratio = %f / %f = %f\n", sum_xsec2, sum_xsec1, xsec_ratio);
        }
        return xsec_ratio; 
    }

    bool SampleSet::parseCfgLine(const char* buf)
    {
        char cDSname[256], cFPath[256], cfName[256], cTPath[256];
        double f1, f2, f3, f4;
        int nMatches = sscanf(buf, "%s %s %s %s %lf %lf %lf %lf", cDSname, cFPath, cfName, cTPath, &f1, &f2, &f3, &f4);
        if(nMatches == 8) //this is MC 
        {
            //                                                        xsec        NEvts+ NEvts-  kfactor
            if(!isCondor_) addSample(cDSname, cFPath, cfName, cTPath, f1,   lumi_, f2 -  f3,     f4,     kGreen);
            else           addSample(cDSname, "",     cfName, cTPath, f1,   lumi_, f2 -  f3,     f4,     kGreen);
            return true;
        }
        else if(nMatches == 6) //this is Data
        {
            //                                                        lumi  kfactor
            if(!isCondor_) addSample(cDSname, cFPath, cfName, cTPath, f1,   f2,     kBlack);
            else           addSample(cDSname, "",     cfName, cTPath, f1,   f2,     kBlack);
            return true;
        }

        return false;            
    }
    
    SampleSet::SampleSet(std::string file, bool isCondor, double lumi) : isCondor_(isCondor), lumi_(lumi)
    {
        readCfg(file);
    }
    
    // modify weights to compare two MC samples
    double SampleCollection::getCrossSectionRatio(std::string& sampleTag1, std::string sampleTag2, bool verbose)
    {
        double sum_xsec1 = 0.0;
        double sum_xsec2 = 0.0;
        // add sample 1 cross sections
        for(const auto& fs : sampleSet_[sampleTag1])
        {
            double xsec = fs.kfactor * fs.xsec;
            sum_xsec1 += xsec;
        }
        // add sample 2 cross sections
        for(const auto& fs : sampleSet_[sampleTag2])
        {
            double xsec = fs.kfactor * fs.xsec;
            sum_xsec2 += xsec;
        }
        // calculate cross section ratio
        double xsec_ratio = sum_xsec2 / sum_xsec1;
        if (verbose) 
        {
            printf("In SampleSet::getCrossSectionRatio():\n");
            printf("  k * sum_xsec1 = %f\n", sum_xsec1);
            printf("  k * sum_xsec2 = %f\n", sum_xsec2);
            printf("  xsec_ratio = %f / %f = %f\n", sum_xsec2, sum_xsec1, xsec_ratio);
        }
        return xsec_ratio;
    }
    
    bool SampleCollection::parseCfgLine(const char* buf)
    {
        char rbuf[BUF_LEN_];
        std::vector<std::string> sampleSetNames;

        memcpy(rbuf, buf, strlen(buf) + 1);

        //Get sampleCollection name 
        char * pch;
        pch = strtok(rbuf," ");

        if(pch == NULL) return false;

        std::string collectionName(pch);
        while(pch != NULL)
        {
            pch = strtok(NULL, " \t");
            if(pch != NULL) 
            {
                sampleSetNames.push_back(pch);
            }
        }

        if(sampleSetNames.size())
        {
            addSampleSet(ss_, collectionName, sampleSetNames);
            return true;
        }
        
        return false;
    }

    SampleCollection::SampleCollection(const std::string& file, SampleSet& samples) : ss_(samples)
    {
        readCfg(file);
    }

    void SampleCollection::addSampleSet(SampleSet& samples, const std::string& name, const std::vector<std::string>& vss)
    {
        if(vss.size() > 1)
        {
            for(const std::string& sn : vss)
            {
                if(sn.compare(name) == 0)
                {
                    std::cout << "You have named a sampleCollection the same as one of its member sampleSets, but it has more than one sampleSet!!!! This is bad!!!  Stop!!! Stop now!!!  This collection will be skipped until it is properly named." << std::endl;
                    return;
                }
            }
        }

        auto& map = samples.getMap();

        for(const std::string& sn : vss)
        {
            map[sn].addCollection(name);
            sampleSet_[name].push_back(samples[sn]);
            nameVec_[name].push_back(sn);
            totalLumiMap_[name] += samples[sn].lumi;
        }
    }

    std::vector<std::string>& SampleCollection::getSampleLabels(std::string name)
    {
        return nameVec_[name];
    }

    bool operator< (const FileSummary& lhs, const FileSummary& rhs)
    {
        return lhs.filePath < rhs.filePath || lhs.treePath < rhs.treePath || lhs.tag < rhs.tag;
    }

    bool operator== (const FileSummary& lhs, const FileSummary& rhs)
    {
        return lhs.filePath == rhs.filePath && lhs.treePath == rhs.treePath && lhs.xsec == rhs.xsec && lhs.lumi == rhs.lumi && lhs.kfactor == rhs.kfactor && lhs.nEvts == rhs.nEvts;
    }

    bool operator!= (const FileSummary& lhs, const FileSummary& rhs)
    {
        return !(lhs == rhs);
    }
}
