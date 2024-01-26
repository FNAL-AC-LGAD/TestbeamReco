#ifndef PREPNTUPLEVARS_H
#define PREPNTUPLEVARS_H

#include <numeric>
#include "TestbeamReco/interface/Utility.h"
#include <TRandom3.h>
#include <chrono>

class PrepNTupleVars
{
private:
    std::vector<std::shared_ptr<TProfile2D>> v_timeDiff_coarse_vs_xy_channel;
    float xSlope_;
    float ySlope_;
    float xIntercept_;
    float yIntercept_;

    bool doAmpSmearing_;
    mutable int seed;

    double getSmear(double mean, double sigma) const
    {
        seed+=1;
        double smear = 1.0;
        if(doAmpSmearing_)
        {
            auto rNG = TRandom3(seed);
            smear = rNG.Gaus(mean, sigma);
            smear = (smear < 0.0) ? -1.0*smear : smear;
        }
        return smear;
    }

    void fillAmplitudeVec(NTupleReader& tr, std::string var_name, std::vector<std::vector<int>> list_indices) const
    {
        const auto& corrAmp = tr.getVec<double>("corrAmp");
        const auto& noiseAmpThreshold = tr.getVar<double>("noiseAmpThreshold");
        const auto& enablePositionReconstructionPad = tr.getVar<bool>("enablePositionReconstructionPad");
        // auto& new_amp = tr.createDerivedVec<double>("amp_row", corrAmp.size());
        // auto& new_amp = tr.createDerivedVec<double>("amp_col", corrAmp.size());
        auto& new_amp = tr.createDerivedVec<double>(var_name, corrAmp.size());

        // Skip calculation if not needed
        if (!enablePositionReconstructionPad)
        {
            for (unsigned int i = 0; i < corrAmp.size(); i++)
            {
                new_amp.at(i) = corrAmp.at(i);
            }
        }
        else
        {
            for (const auto& group : list_indices)
            {
                double amp_sum = 0.0, amp_sqrsum = 0.0;
                bool negValue = false, overThreshold = false;
                for (const auto& idx : group)
                {
                    if (corrAmp.at(idx) < 0.0) negValue = true;
                    if (corrAmp.at(idx) >= noiseAmpThreshold) overThreshold = true;

                    amp_sum+= corrAmp.at(idx);
                    amp_sqrsum+= corrAmp.at(idx)*corrAmp.at(idx);
                }
                bool quadSum = negValue || !overThreshold;
                // Fill
                for (const auto& idx : group)
                {
                    double value = amp_sum;
                    if (quadSum) value = std::sqrt(amp_sqrsum);
                    new_amp.at(idx) = value;
                }
            }
            // Use single value if sum of row/column is not possible (ex. Photek)
            for (unsigned int i = 0; i < new_amp.size(); i++)
            {
                if (!new_amp.at(i)) new_amp.at(i) = corrAmp.at(i);
            }
        }
    }

    void addAmplitudeRowCol(NTupleReader& tr) const
    {
        const auto& geometry = tr.getVar<std::vector<std::vector<int>>>("geometry");
        const auto& extraChannelIndex  = tr.getVar<int>("extraChannelIndex");
        // const auto& n_row = tr.getVar("n_row")
        const auto& n_col = tr.getVar<int>("n_col");
        // example: geometry -- list_rows -- list_columns
        // ex. {{3,1,0}, {4,5,6}, {7}}; -- {{3,1,0}, {4,5,6}}; -- {{3,4}, {1,5}, {0,6}};
        // ex. {{1,0},{2,3},{4,5},{7}}; (4 is extraChannel) -- {{1,0},{2,3}}; -- {{1,2}, {0,3}};
        std::vector<std::vector<int>> list_rows;
        std::vector<std::vector<int>> list_cols(n_col);
        // Fill lists with indices
        for (const auto& row : geometry)
        {
            if (row.size() < 2) continue;
            if (std::find(row.begin(), row.end(), extraChannelIndex) != row.end()) continue;

            list_rows.emplace_back(row);
            for(unsigned int i = 0; i < row.size(); i++)
            {
                list_cols[i].emplace_back(row[i]);
            }
        }
        fillAmplitudeVec(tr, "ampRow", list_rows);
        fillAmplitudeVec(tr, "ampCol", list_cols);
    }

    void applyAmplitudeCorrection(NTupleReader& tr) const
    {     
        const auto& ampCorrectionFactors = tr.getVar<std::map<int,double>>("amplitudeCorrectionFactor");
        auto& corrAmp = tr.createDerivedVec<double>("corrAmp");
        const auto& amp = tr.getVec<float>("amp");
        
        int counter = 0;
        for(auto thisAmp : amp) 
        {
            corrAmp.emplace_back(getSmear(1.0, 0.2)*thisAmp*ampCorrectionFactors.at(counter));
            counter++;
        }

        // Add amplitude in the same row/column
        addAmplitudeRowCol(tr);
    }

    // Translate hit position from tracker's coordinates to local/sensor's frame by rotating around lab axes Z(alpha) -> Y(beta) -> X(gamma)
    // * xyz_tracker gives the laboratory hit position relative to sensorCenter, sensorCenterY, z_center
    void getXYOnSensor(std::vector<double>* xyz_tracker, double& xFinal, double& yFinal, const float z_center=0.0, const float alpha=0.0, const float beta=0.0,
                        const float gamma=0.0, const float x_center=0.0, const float y_center=0.0, const bool isHorizontal=false)
    {
        double xI=xIntercept_, yI=yIntercept_, xS=xSlope_, yS=ySlope_;

        // Use correct track parameters, given the axes defined such that the strips are always perpendicular to the x-axis 
        if (isHorizontal)
        {
            xI = yIntercept_;
            yI = -xIntercept_;
            xS = ySlope_;
            yS = -xSlope_;
        }

        double degreesToRad = 3.14159/180.0;
        double alpha_rad = alpha*degreesToRad;
        double beta_rad = beta*degreesToRad;
        double gamma_rad = gamma*degreesToRad;

        // Define angles' dependent factors used in the next expression for the laboratory z position of the hit in the sensor
        double nx_nz = cos(alpha_rad)*tan(beta_rad) + sin(alpha_rad)*tan(gamma_rad)/cos(beta_rad);
        double ny_nz = sin(alpha_rad)*tan(beta_rad) - cos(alpha_rad)*tan(gamma_rad)/cos(beta_rad);

        double z_lab = (z_center - nx_nz*(xI - x_center) - ny_nz*(yI - y_center)) / (1 + nx_nz*xS + ny_nz*yS);

        // Coordinates of the hit w.r.t. sensor's center in the lab frame
        double lx = xI + z_lab*xS - x_center;
        double ly = yI + z_lab*yS - y_center;
        double lz = z_lab - z_center;

        // Express the hit position in the local/sensor's frame
        // First rotation around z-lab axis
        double x_r1 = cos(alpha_rad)*lx + sin(alpha_rad)*ly;
        double y_r1 = -sin(alpha_rad)*lx + cos(alpha_rad)*ly;
        double z_r1 = lz;

        // Second rotation around y-lab axis
        double x_r2 = cos(beta_rad)*x_r1 - sin(beta_rad)*z_r1;
        double y_r2 = y_r1;
        double z_r2 = sin(beta_rad)*x_r1 + cos(beta_rad)*z_r1;

        // Third rotation around x-lab axis (z component is always zero)
        double x_r3 = x_r2;
        double y_r3 = cos(gamma_rad)*y_r2 + sin(gamma_rad)*z_r2;
        // double z_r3 = -sin(gamma_rad)*y_r2 + cos(gamma_rad)*z_r2; // z_r3 = 0;

        // Save local/sensor hit's position when the tracker worked
        xFinal = (xI==0 && xS==0) ? -9999 : x_r3;
        yFinal = (yI==0 && yS==0) ? -9999 : y_r3;

        if (xyz_tracker)
        {
            xyz_tracker->at(0) = (xI==0 && xS==0) ? -9999 : lx;
            xyz_tracker->at(1) = (yI==0 && yS==0) ? -9999 : ly;
            xyz_tracker->at(2) = (xI==0 && xS==0 && yI==0 && yS==0) ? -9999 : lz;
        }
    }

    void prepNTupleVars(NTupleReader& tr)
    {
        // Create the eventCounter variable to keep track of processed events
        int w = 1;
        tr.registerDerivedVar<int>("eventCounter",w);

        // Correct the rotation angle for the x and y measurment
        xSlope_     = tr.getVar<float>("xSlope");
        ySlope_     = tr.getVar<float>("ySlope");
        xIntercept_ = tr.getVar<float>("xIntercept");
        yIntercept_ = tr.getVar<float>("yIntercept");
        const auto& sensorCenter = tr.getVar<double>("sensorCenter");
        const auto& sensorCenterY = tr.getVar<double>("sensorCenterY");
        const auto& z_dut = tr.getVar<double>("z_dut");
        const auto& alpha = tr.getVar<double>("alpha");
        const auto& beta  = tr.getVar<double>("beta");
        const auto& gamma = tr.getVar<double>("gamma");
        const auto& isHorizontal = tr.getVar<bool>("isHorizontal");

        // Define final telescope hit location on DUT based on track lines and hard coded parameters
        auto& x = tr.createDerivedVar<double>("x");
        auto& y = tr.createDerivedVar<double>("y");
        auto& xyz_tracker = tr.createDerivedVec<double>("xyz_tracker",3);
        getXYOnSensor(&xyz_tracker, x, y, z_dut, alpha, beta, gamma, sensorCenter, sensorCenterY, isHorizontal);

        // Create vectors of possible x,y locations by varying hard coded parameters
        const auto& zScan = tr.getVar<std::vector<double>>("zScan");
        const auto& alphaScan = tr.getVar<std::vector<double>>("alphaScan");
        const auto& betaScan = tr.getVar<std::vector<double>>("betaScan");
        const auto& gammaScan = tr.getVar<std::vector<double>>("gammaScan");

        auto& x_var = tr.createDerivedVec<double>("x_var",zScan.size());
        auto& y_var = tr.createDerivedVec<double>("y_var",zScan.size());
        auto& x_varA = tr.createDerivedVec<double>("x_varA",alphaScan.size());
        auto& y_varA = tr.createDerivedVec<double>("y_varA",alphaScan.size());
        auto& x_varB = tr.createDerivedVec<double>("x_varB",betaScan.size());
        auto& y_varB = tr.createDerivedVec<double>("y_varB",betaScan.size());
        auto& x_varC = tr.createDerivedVec<double>("x_varC",gammaScan.size());
        auto& y_varC = tr.createDerivedVec<double>("y_varC",gammaScan.size());

        for(unsigned int i = 0; i < zScan.size(); i++)
        {
            getXYOnSensor(nullptr, x_var[i], y_var[i], zScan[i], alpha, beta, gamma, sensorCenter, sensorCenterY, isHorizontal);
        }
        for(unsigned int i = 0; i < alphaScan.size(); i++)
        {
            getXYOnSensor(nullptr, x_varA[i], y_varA[i], z_dut, alphaScan[i], beta, gamma, sensorCenter, sensorCenterY, isHorizontal);
        }
        for(unsigned int i = 0; i < betaScan.size(); i++)
        {
            getXYOnSensor(nullptr, x_varB[i], y_varB[i], z_dut, alpha, betaScan[i], gamma, sensorCenter, sensorCenterY, isHorizontal);
        }
        for(unsigned int i = 0; i < gammaScan.size(); i++)
        {
            getXYOnSensor(nullptr, x_varC[i], y_varC[i], z_dut, alpha, beta, gammaScan[i], sensorCenter, sensorCenterY, isHorizontal);
        }

        // Correct amp and map raw amplitude
        const auto& amp = tr.getVec<float>("amp");
        const auto& extraChannelIndex = tr.getVar<int>("extraChannelIndex");
        const auto& rawAmpLGAD = utility::remapToLGADgeometry(tr, amp, "rawAmpLGAD");
        int n_row = rawAmpLGAD.size();
        if (extraChannelIndex > -1) {n_row = rawAmpLGAD.size() -1;}
        tr.registerDerivedVar("n_row", static_cast<int>(n_row));
        tr.registerDerivedVar("n_col", static_cast<int>(rawAmpLGAD[0].size()));

        applyAmplitudeCorrection(tr);

        double totRawAmpLGAD = 0.0;
        for(auto row : rawAmpLGAD){totRawAmpLGAD += std::accumulate(row.begin(), row.end(), 0.0);}
        tr.registerDerivedVar("totRawAmpLGAD", totRawAmpLGAD);

        // Check whether a hit was in the active region of the sensor or not
        const auto& sensorEdges = tr.getVar<std::vector<std::vector<double>>>("sensorEdges");
        const auto& sensorEdgesExtra = tr.getVar<std::vector<std::vector<double>>>("sensorEdgesExtra");
        const auto& sensorEdgesTight = tr.getVar<std::vector<std::vector<double>>>("sensorEdgesTight");

        bool hitSensor = sensorEdges[0][0] < x && x < sensorEdges[1][0] &&  sensorEdges[0][1] < y && y < sensorEdges[1][1];
        bool hitSensorExtra = sensorEdgesExtra[0][0] < x && x < sensorEdgesExtra[1][0] &&  sensorEdgesExtra[0][1] < y && y < sensorEdgesExtra[1][1];
        bool hitSensorTightY = sensorEdgesTight[0][1] < y && y < sensorEdgesTight[1][1] && sensorEdges[0][0] < x && x < sensorEdges[1][0]; // The x cut is added so that hits outside the sensor are not registered
        bool hitSensorTight = sensorEdgesTight[0][0] < x && x < sensorEdgesTight[1][0] &&  hitSensorTightY;

        tr.registerDerivedVar("hitSensor", hitSensor);
        tr.registerDerivedVar("hitSensorExtra", hitSensorExtra);
        tr.registerDerivedVar("hitSensorTightY", hitSensorTightY);
        tr.registerDerivedVar("hitSensorTight", hitSensorTight);

        // Check hits in the active region with different sensor's orientations (used in Alignment)
        auto& hitSensorZ = tr.createDerivedVec<bool>("hitSensorZ", zScan.size());
        auto& hitSensorA = tr.createDerivedVec<bool>("hitSensorA", alphaScan.size());
        auto& hitSensorB = tr.createDerivedVec<bool>("hitSensorB", betaScan.size());
        auto& hitSensorC = tr.createDerivedVec<bool>("hitSensorC", gammaScan.size());

        for(unsigned int i = 0; i < zScan.size(); i++)
        {
            hitSensorZ[i] = sensorEdges[0][0] < x_var[i] && x_var[i] < sensorEdges[1][0] &&  sensorEdges[0][1] < y_var[i] && y_var[i] < sensorEdges[1][1];
        }
        for(unsigned int i = 0; i < alphaScan.size(); i++)
        {
            hitSensorA[i] = sensorEdges[0][0] < x_varA[i] && x_varA[i] < sensorEdges[1][0] &&  sensorEdges[0][1] < y_varA[i] && y_varA[i] < sensorEdges[1][1];
        }
        for(unsigned int i = 0; i < betaScan.size(); i++)
        {
            hitSensorB[i] = sensorEdges[0][0] < x_varB[i] && x_varB[i] < sensorEdges[1][0] &&  sensorEdges[0][1] < y_varB[i] && y_varB[i] < sensorEdges[1][1];
        }
        for(unsigned int i = 0; i < gammaScan.size(); i++)
        {
            hitSensorC[i] = sensorEdges[0][0] < x_varC[i] && x_varC[i] < sensorEdges[1][0] &&  sensorEdges[0][1] < y_varC[i] && y_varC[i] < sensorEdges[1][1];
        }

        // Correct the time variable
        const auto& CFD_threshold = tr.getVar<int>("CFD_threshold");
        const auto& LP2 = tr.getVec<float>(Form("LP2_%i",CFD_threshold));
        const auto& LP2_30mV = tr.getVec<float>("LP2_30mV");
        const auto& timeCalibrationCorrection = tr.getVar<std::map<int,double>>("timeCalibrationCorrection");
        auto& corrTime = tr.createDerivedVec<double>("corrTime");
        auto& corrTime_30mV = tr.createDerivedVec<double>("corrTime_30mV");
        auto& corrTimeTracker = tr.createDerivedVec<double>("corrTimeTracker");

        const auto& CFD_list = tr.getVar<std::vector<std::string>>("CFD_list");
        std::vector<std::vector<float>> v_LP2_allCFD;
        std::vector<std::vector<double>*> v_corrTime_allCFD;
        for(auto cfd : CFD_list)
        {
            v_LP2_allCFD.emplace_back(tr.getVec<float>("LP2_"+cfd));
            v_corrTime_allCFD.emplace_back(&tr.createDerivedVec<double>("corrTime"+cfd+"Tracker"));
        }

        uint counter = 0;
        for(auto thisTime : LP2)
        {
            auto corr = (thisTime == 0.0) ? 0.0 : timeCalibrationCorrection.at(counter);
            auto tracker_corr = utility::getTrackerTimeCorr<TProfile2D>(x, y, thisTime, counter, v_timeDiff_coarse_vs_xy_channel);

            corrTime.emplace_back(1e9*(thisTime) + corr);
            corrTimeTracker.emplace_back(1e9*(thisTime) - tracker_corr + corr);

            int icfd =0;
            for(auto cfd : CFD_list)
            {
                v_corrTime_allCFD[icfd]->emplace_back(1e9*(v_LP2_allCFD[icfd][counter]) - tracker_corr + corr);
                icfd++;
            }

            counter++;
        }

        counter = 0;
        for(auto thisTime : LP2_30mV)
        {
            auto corr = (thisTime == 0.0) ? 0.0 : timeCalibrationCorrection.at(counter);
            corrTime_30mV.emplace_back(1e9*(thisTime) + corr);
            counter++;
        }

        utility::remapToLGADgeometry(tr, corrTime, "timeLGAD");
        utility::remapToLGADgeometry(tr, corrTime_30mV, "timeLGAD_30mV");
        utility::remapToLGADgeometry(tr, corrTimeTracker, "timeLGADTracker");
        int icfd =0;
        for(auto* corrTimeEachCFD: v_corrTime_allCFD )
        {
            utility::remapToLGADgeometry(tr, *corrTimeEachCFD, "time"+CFD_list[icfd]+"LGADTracker");
            icfd++;
        }

        // Baseline RMS
        const auto& baselineRMS = tr.getVec<float>("baseline_RMS");
        utility::remapToLGADgeometry(tr, baselineRMS, "baselineRMS");

        // Redefine Risetime
        const auto& corrAmp = tr.getVec<double>("corrAmp");
        const auto& risetime = tr.getVec<float>("risetime");
        auto& corrRisetime = tr.createDerivedVec<double>("corrRisetime",risetime.size());
        //auto& SlewRate = tr.createDerivedVec<float>("SlewRate",risetime.size());
        for(unsigned int i = 0; i < risetime.size(); i++)
        {
            corrRisetime[i] = 1e12*abs(0.8*corrAmp[i] / risetime[i]);
            //SlewRate[i] = 1e-9*abs(risetime[i]);
        }
        utility::remapToLGADgeometry(tr, corrRisetime, "risetimeLGAD");

        const auto& slewrate = tr.getVec<float>("risetime");
        auto& corrSlewrate = tr.createDerivedVec<double>("corrSlewrate", slewrate.size());
        auto& baselineRMSSlewRateRatio = tr.createDerivedVec<double>("baselineRMSSlewRateRatio",slewrate.size());
		for(unsigned int i = 0; i < slewrate.size(); i++)
        {
             corrSlewrate[i] = 1e-9*abs(slewrate[i]);
			 baselineRMSSlewRateRatio[i] = 1000*(baselineRMS[i]/corrSlewrate[i]);
        }
        utility::remapToLGADgeometry(tr, corrSlewrate, "slewrateLGAD");
        utility::remapToLGADgeometry(tr, baselineRMSSlewRateRatio, "baselineRMSSlewRateRatioLGAD");
        utility::remapToLGADgeometry(tr, baselineRMSSlewRateRatio, "jitterLGAD");
        //utility::remapToLGADgeometry(tr, SlewRate, "slewrateLGAD");
        //Charge, amp/charge ratio
        const auto& integral = tr.getVec<float>("integral");
        auto& charge = tr.createDerivedVec<double>("charge",integral.size());
        auto& AmpChargeRatio = tr.createDerivedVec<double>("AmpChargeRatio",integral.size());
        auto& SlewRateChargeRatio = tr.createDerivedVec<double>("SlewRateChargeRatio",integral.size());
		for(unsigned int i = 0; i < integral.size(); i++)
        {
            charge[i] = -1000*integral[i]*1e9*50/(1.4*4700); //FNAL / UCSC Q ratio is 1.4, using 4700 for both.
            AmpChargeRatio[i] = corrAmp[i]/charge[i];
            SlewRateChargeRatio[i] = corrSlewrate[i]/charge[i];
        }
        utility::remapToLGADgeometry(tr, charge, "chargeLGAD");
        utility::remapToLGADgeometry(tr, AmpChargeRatio, "ampChargeRatioLGAD");
        utility::remapToLGADgeometry(tr, SlewRateChargeRatio, "slewRateChargeRatioLGAD");
    }


public:

    PrepNTupleVars(const std::vector<std::shared_ptr<TProfile2D>>& histVec) : v_timeDiff_coarse_vs_xy_channel(histVec), xSlope_(0), ySlope_(0), xIntercept_(0), yIntercept_(0), doAmpSmearing_(false)
    {
    }

    void operator()(NTupleReader& tr)
    {
        prepNTupleVars(tr);
    }
};

#endif
