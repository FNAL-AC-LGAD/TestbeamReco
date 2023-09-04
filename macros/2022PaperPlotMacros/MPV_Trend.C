#include <cmath>
#include <vector>
#include <Riostream.h>
#include <string>
#include <TH1D.h>
#include <TEfficiency.h>
#include <TH2D.h>
#include <TFile.h>
#include <TMath.h>
#include <math.h>
#include <TCanvas.h>
#include <TGraphErrors.h>
#include <TLegend.h>
#include <TMarker.h>
#include <TAttMarker.h>
#include <TF1.h>
#include <TStyle.h>

void graph(double arr225MPV[6], double arr225MPVerr[6], double arr220MPV[6], double arr220MPVerr[6], double arr210MPV[6], double arr210MPVerr[6], double arr200MPV[6], double arr200MPVerr[6]) {
    double xvalues200[6]= {-0.1, 0.9, 1.9, 2.9, 3.9, 4.9};
    double xvalues210[6]= {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
    double xvalues220[6]= {0.1, 1.1, 2.1, 3.1, 4.1 ,5.1};
    double xvalues225[6]= {0.2, 1.2, 2.2, 3.2, 4.2, 5.2};
    TGraphErrors* graph225 =new TGraphErrors(6, xvalues225, arr225MPV, {}, arr225MPVerr);
    TGraphErrors* graph220 =new TGraphErrors(6, xvalues220, arr220MPV, {}, arr220MPVerr);
    TGraphErrors* graph210 =new TGraphErrors(6, xvalues210, arr210MPV, {}, arr210MPVerr);
    TGraphErrors* graph200 =new TGraphErrors(6, xvalues200, arr200MPV, {}, arr200MPVerr);


       
    graph225->GetXaxis()->SetLimits(-1.0,6.0);
    graph225->GetYaxis()->SetLimits(0.9,1.1); 
    graph220->GetYaxis()->SetLimits(0.9,1.1); 
    graph210->GetYaxis()->SetLimits(0.9,1.1); 
    graph200->GetYaxis()->SetLimits(0.9,1.1); 


    graph225->SetTitle("Normalized Peak MPV;Channel (mm);Peak Bin MPV (mV); ");

    
    graph225->SetLineColor(kRed);
    graph220->SetLineColor(kBlue);
    graph210->SetLineColor(kMagenta);

    graph225->SetMarkerStyle(8);
    graph220->SetMarkerStyle(8);
    graph210->SetMarkerStyle(8);
    graph200->SetMarkerStyle(8);

    graph225->SetMarkerSize(1);
    graph220->SetMarkerSize(1);
    graph210->SetMarkerSize(1);
    graph200->SetMarkerSize(1);

    graph225->SetLineWidth(2);
    graph220->SetLineWidth(2);
    graph210->SetLineWidth(2);
    graph200->SetLineWidth(2);



    graph225->SetMarkerColor(kRed);
    graph220->SetMarkerColor(kBlue);
    graph210->SetMarkerColor(kMagenta);
    


    graph225->Draw("AP");
    graph220->Draw("Same P");
    graph210->Draw("Same P");
    graph200->Draw("Same P");



   auto legend = new TLegend(0.1, 0.7, 0.4, 0.9);
   legend->SetHeader("Bias Voltage");
   legend->AddEntry(graph225,"225V", "l");
   legend->AddEntry(graph220,"220V", "l");
   legend->AddEntry(graph210,"210V", "l");   
   legend->AddEntry(graph200,"200V", "l");
   legend->Draw();
    
}

double errcalc(double err1, double err2, double finalvalue){
    double errprop=sqrt(pow(err1,2)+pow(err2,2));
    return errprop*finalvalue;
}


void MPV_Trend(){
    TCanvas* c1= new TCanvas("c1","c1",1200,800);
    c1->cd();
    double MPV225Chan1=112.676179;
    double MPV220Chan1=100.855302;
    double MPV210Chan1=77.3320563;
    double MPV200Chan1=65.1788554;
    double arr225MPV[6]={111.223572/MPV225Chan1, 112.676179/MPV225Chan1, 112.52539/MPV225Chan1, 112.774402/MPV225Chan1,110.504359/MPV225Chan1, 113.712538/MPV225Chan1};
    double arr220MPV[6]={100.62829/MPV220Chan1, 100.855302/MPV220Chan1, 100.842062/MPV220Chan1, 101.20024/MPV220Chan1, 100.194178/MPV220Chan1, 100.970889/MPV220Chan1};
    double arr210MPV[6]={78.7911752/MPV210Chan1, 77.3320563/MPV210Chan1, 76.3778652/MPV210Chan1, 78.0445628/MPV210Chan1, 78.828064/MPV210Chan1, 78.3650632/MPV210Chan1};
    double arr200MPV[6]={62.0711108/MPV200Chan1, 65.1788554/MPV200Chan1, 61.9489015/MPV200Chan1, 65.2943433/MPV200Chan1, 61.6310508/MPV200Chan1, 64.8201014/MPV200Chan1}; 
    
    double arr225MPVerr[6]={};
    double arr225MPVRawerr[6]={1.1966466569605476/111.223572, 1.2484510139990956/112.676179, 1.4528481133426068/112.52539, 1.3217240409472157/112.774402, 1.3339641828406885/110.504359, 1.1141354320792627/113.712538};  
    for (int i = 0; i < 6; i++){
        arr225MPVerr[i]=errcalc(arr225MPVRawerr[i],arr225MPVRawerr[1],arr225MPV[i]);
    }   
 
    double arr220MPVerr[6]={};
    double arr220MPVRawerr[6]={1.019222296456741/100.62829, 1.0137566126813702/100.855302,0.9868324398786559/100.842062, 0.9370057772823038/101.20024, 0.9329792870326921/100.194178, 0.9732299624847564/100.970889};
    for (int i = 0; i < 6; i++){
        arr220MPVerr[i]=errcalc(arr220MPVRawerr[i],arr220MPVRawerr[1],arr220MPV[i]);
    }
    

    double arr210MPVerr[6]={};
    double arr210MPVRawerr[6]={1.16696764517/78.7911752, 1.01277175766/77.3320563, 0.93674046001/76.3778652, 1.014448736/78.0445628, 1.21719113631/78.828064, 1.03530912255/78.3650632};
    for (int i = 0; i < 6; i++){
        arr210MPVerr[i]=errcalc(arr210MPVRawerr[i],arr210MPVRawerr[1],arr210MPV[i]);
    }
 
    double arr200MPVerr[6]={};
    double arr200MPVRawerr[6]={1.0636452695280243/62.0711108, 1.2198452541221123/65.1788554, 0.9217740098589856/61.9489015, 1.1873005252615352/65.2943433, 0.9915679812904172/61.6310508, 1.0794284391636833/64.8201014};     
    for (int i = 0; i < 6; i++){
        arr200MPVerr[i]=errcalc(arr200MPVRawerr[i],arr200MPVRawerr[1],arr200MPV[i]);
    }

    std::cout<< arr225MPVerr[0]<< " "<< arr225MPVerr[1]<<" "<<arr225MPVerr[2]<<" "<<arr225MPVerr[3]<<" "<<arr225MPVerr[4]<<" "<<arr225MPVerr[5]<<std::endl;
    std::cout<< arr220MPVerr[0]<< " "<< arr220MPVerr[1]<<" "<<arr220MPVerr[2]<<" "<<arr220MPVerr[3]<<" "<<arr220MPVerr[4]<<" "<<arr220MPVerr[5]<<std::endl;
    std::cout<< arr210MPVerr[0]<< " "<< arr210MPVerr[1]<<" "<<arr210MPVerr[2]<<" "<<arr210MPVerr[3]<<" "<<arr210MPVerr[4]<<" "<<arr210MPVerr[5]<<std::endl;
    std::cout<< arr200MPVerr[0]<< " "<< arr200MPVerr[1]<<" "<<arr200MPVerr[2]<<" "<<arr200MPVerr[3]<<" "<<arr200MPVerr[4]<<" "<<arr200MPVerr[5]<<std::endl;


 



    graph(arr225MPV, arr225MPVerr,  arr220MPV, arr220MPVerr, arr210MPV, arr210MPVerr, arr200MPV, arr200MPVerr);

      
 

}
