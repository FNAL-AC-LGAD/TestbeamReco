
################################################################################
# --------------------------  (!) 2023 Sensors (!)  -------------------------- #
################################################################################
##################################  Geometry  ##################################
# {<sensor name_long>, <sensor name_short/label>, <pitch [um]>, <width [um]>, <length [mm]>,
#  <Bias voltage [V]>, <thickness [um]>, <resistivity [Ohm/sq]>, <capacitance [pF/mm2]>}
geometry2023_default = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2": ["BNL_50um_1cm_450um_W3051", 500, 50, 10.0, 170, 50, "Null", "Null"],
    "BNL_50um_1cm_400um_W3051_1_4": ["BNL_50um_1cm_400um_W3051", 500, 100, 10.0, 160, 50, "Null", "Null"],
    "BNL_50um_1cm_450um_W3052_2_4": ["BNL_50um_1cm_450um_W3052", 500, 50, 10.0, 185, 50, "Null", "Null"],
    "BNL_20um_1cm_400um_W3074_1_4": ["BNL_20um_1cm_400um_W3074", 500, 100, 10.0, 95, 20 , "Null", "Null"],
    "BNL_20um_1cm_400um_W3075_1_2": ["BNL_20um_1cm_400um_W3075", 500, 100, 10.0, 80, 20, "Null", "Null"],
    "BNL_20um_1cm_450um_W3074_2_1": ["BNL_20um_1cm_450um_W3074", 500, 50, 10.0, 95, 20, "Null", "Null"],
    "BNL_20um_1cm_450um_W3075_2_4": ["BNL_20um_1cm_450um_W3075", 500, 50, 10.0, 80, 20, "Null", "Null"],
    "BNL_50um_2p5cm_mixConfig1_W3051_1_4": ["BNL_50um_2p5cm_mixConfig1_W3051", 500, 100, 25.0, 170, 50, "Null", "Null"],
    "BNL_50um_2p5cm_mixConfig2_W3051_1_4": ["BNL_50um_2p5cm_mixConfig2_W3051", 500, 50, 25.0, 170, 50, "Null", "Null"],

    # HPK pads (January)
    "HPK_20um_500x500um_2x2pad_E600_FNAL": ["HPK_20um_2x2pad", 500, 500, 0.5, 105, 20, "E", 600],
    "HPK_30um_500x500um_2x2pad_E600_FNAL": ["HPK_30um_2x2pad", 500, 500, 0.5, 140, 30, "E", 600],
    "HPK_50um_500x500um_2x2pad_E600_FNAL": ["HPK_50um_2x2pad", 500, 500, 0.5, 190, 50, "E", 600],

    # HPK pads (May)
    "HPK_W9_22_3_20T_500x500_150M_E600": ["HPK_W9_22_3_20T_500x500_150M_E600", 500, 150, 5.0, 112, 20, "E", 600],
    "HPK_W9_23_3_20T_500x500_300M_E600": ["HPK_W9_23_3_20T_500x500_300M_E600", 500, 300, 5.0, 112, 20, "E" , 600],
    "HPK_W11_22_3_20T_500x500_150M_C600": ["HPK_W11_22_3_20T_500x500_150M_C600", 500, 150, 5.0, 116, 20, "C", 600],
    "HPK_W8_1_1_50T_500x500_150M_C600": ["HPK_W8_1_1_50T_500x500_150M_C600", 500, 150, 5.0, 200, 50, "C", 600],
    "HPK_W5_1_1_50T_500x500_150M_E600": ["HPK_W5_1_1_50T_500x500_150M_E600", 500, 150, 5.0, 185, 50, "C", 600],

    # HPK strips
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": ["HPK_W8_18_2_50T_100M_C600", 500, 100, 10.0, 208, 50, "C", 600],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600": ["HPK_W8_17_2_50T_50M_C600", 500, 50, 10.0, 206, 50, "C", 600],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": ["HPK_W4_17_2_50T_1P0_500P_50M_C240", 500, 50, 10.0, 204, 50, "C", 240],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": ["HPK_W5_17_2_50T_1P0_500P_50M_E600", 500, 50, 10.0, 190, 50, "E", 600],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": ["HPK_W2_3_2_50T_1P0_500P_50M_E240", 500, 50, 10.0, 180, 50, "E", 240],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": ["HPK_W9_15_2_20T_1P0_500P_50M_E600", 500, 50, 10.0, 114, 20, "E", 600],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": ["HPK_W9_14_2_20T_1P0_500P_100M_E600", 500, 100, 10.0, 112, 20, "E", 600],
    "HPK_KOJI_50T_1P0_80P_60M_E240": ["HPK_50T_1P0_80P_60M_E240", 80, 60, 10.0, 190, 50, "E", 240],
    "HPK_KOJI_20T_1P0_80P_60M_E240": ["HPK_20T_1P0_80P_60M_E240", 80, 60, 10.0, 112, 20, "E", 240],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": ["HPK_W9_15_4_20T_0P5_500P_50M_E600", 500, 50, 5.0, 110, 20, "E", 600],
}

sensorsGeom2023 = {}
for key, info in geometry2023_default.items():
    info_dict = {}
    info_dict["sensor"] = info[0]
    info_dict["pitch"] = info[1]
    info_dict["stripWidth"], info_dict["width"] = info[2], info[2]
    info_dict["length"] = info[3]
    info_dict["BV"], info_dict["voltage"] = info[4], info[4]
    info_dict["thickness"] = info[5]
    info_dict["resistivity"] = info[6]
    info_dict["capacitance"] = info[7]

    sensorsGeom2023[key] = info_dict

#########################  Resolutions and efficiency  #########################
# NOTE: Resolution values do NOT have tracker component removed
###############################---  Overall  ---################################
# <one strip reco RMS [um]>, <two strip reco fit [um]>, <time [ps]>, <efficiency one strip>, <efficiency two strip>
resolutions2023_Overall = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2": [],
    "BNL_50um_1cm_400um_W3051_1_4": [],
    "BNL_50um_1cm_450um_W3052_2_4": [],
    "BNL_20um_1cm_400um_W3074_1_4": [],
    "BNL_20um_1cm_400um_W3075_1_2": [],
    "BNL_20um_1cm_450um_W3074_2_1": [],
    "BNL_20um_1cm_450um_W3075_2_4": [],
    "BNL_50um_2p5cm_mixConfig1_W3051_1_4": [],
    "BNL_50um_2p5cm_mixConfig2_W3051_1_4": [],

    # HPK pads (January)
    "HPK_20um_500x500um_2x2pad_E600_FNAL": [],
    "HPK_30um_500x500um_2x2pad_E600_FNAL": [],
    "HPK_50um_500x500um_2x2pad_E600_FNAL": [],

    # HPK pads (May)
    "HPK_W9_22_3_20T_500x500_150M_E600": [],
    "HPK_W9_23_3_20T_500x500_300M_E600": [],
    "HPK_W11_22_3_20T_500x500_150M_C600": [],
    "HPK_W8_1_1_50T_500x500_150M_C600": [],
    "HPK_W5_1_1_50T_500x500_150M_E600": [],

    # HPK strips
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": [69.6, 31.1, 40.1, 8.7, 91.3],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600": [36.5, 27.0, 39.9, 3.6, 96.4],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": [44.1, 28.2, 37.4, 3.0, 97.0],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": [53.8, 14.0, 35.5, 4.4, 95.6],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": [36.4, 14.3, 35.3, 2.4, 97.6],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": [115.3, 22.4, 49.7, 67.9, 32.1],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": [123.8, 23.4, 43.8, 81.0, 19.0],
    "HPK_KOJI_50T_1P0_80P_60M_E240": [149.8, 9.6, 32.6, 12.3, 87.7],
    "HPK_KOJI_20T_1P0_80P_60M_E240": [107.5, 10.9, 30.0, 23.4, 76.6],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": [109.4, 20.2, 37.4, 63.9, 36.1],
}

################################---  Metal  ---#################################
# <one strip reco RMS [um]>, <two strip reco fit [um]>, <time [ps]>, <efficiency one strip>, <efficiency two strip>
resolutions2023_Metal = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2": [],
    "BNL_50um_1cm_400um_W3051_1_4": [],
    "BNL_50um_1cm_450um_W3052_2_4": [],
    "BNL_20um_1cm_400um_W3074_1_4": [],
    "BNL_20um_1cm_400um_W3075_1_2": [],
    "BNL_20um_1cm_450um_W3074_2_1": [],
    "BNL_20um_1cm_450um_W3075_2_4": [],
    "BNL_50um_2p5cm_mixConfig1_W3051_1_4": [],
    "BNL_50um_2p5cm_mixConfig2_W3051_1_4": [],

    # HPK pads (January)
    "HPK_20um_500x500um_2x2pad_E600_FNAL": [],
    "HPK_30um_500x500um_2x2pad_E600_FNAL": [],
    "HPK_50um_500x500um_2x2pad_E600_FNAL": [],

    # HPK pads (May)
    "HPK_W9_22_3_20T_500x500_150M_E600": [],
    "HPK_W9_23_3_20T_500x500_300M_E600": [],
    "HPK_W11_22_3_20T_500x500_150M_C600": [],
    "HPK_W8_1_1_50T_500x500_150M_C600": [],
    "HPK_W5_1_1_50T_500x500_150M_E600": [],

    # HPK strips
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": [27.9, 40.6, 39.4, 28.4, 71.6],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600": [14.9, 26.7, 38.4, 21.6, 78.4],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": [15.2, 25.7, 36.3, 18.2, 81.8],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": [13.8, 18.3, 33.0, 25.2, 74.8],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": [13.6, 15.6, 32.9, 17.7, 82.3],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": [16.4, 52.9, 29.6, 97.5, 2.5],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": [30.0, 222.2, 31.1, 98.9, 1.1],
    "HPK_KOJI_50T_1P0_80P_60M_E240": [20.1, 9.6, 33.6, 16.0, 84.0],
    "HPK_KOJI_20T_1P0_80P_60M_E240": [33.1, 11.3, 30.2, 30.0, 70.0],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": [19.7, 27.1, 24.9, 97.2, 2.8],
}

#################################---  Gap  ---##################################
# <one strip reco RMS [um]>, <two strip reco fit [um]>, <time [ps]>, <efficiency one strip>, <efficiency two strip>
resolutions2023_Gap = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2": [],
    "BNL_50um_1cm_400um_W3051_1_4": [],
    "BNL_50um_1cm_450um_W3052_2_4": [],
    "BNL_20um_1cm_400um_W3074_1_4": [],
    "BNL_20um_1cm_400um_W3075_1_2": [],
    "BNL_20um_1cm_450um_W3074_2_1": [],
    "BNL_20um_1cm_450um_W3075_2_4": [],
    "BNL_50um_2p5cm_mixConfig1_W3051_1_4": [],
    "BNL_50um_2p5cm_mixConfig2_W3051_1_4": [],

    # HPK pads (January)
    "HPK_20um_500x500um_2x2pad_E600_FNAL": [],
    "HPK_30um_500x500um_2x2pad_E600_FNAL": [],
    "HPK_50um_500x500um_2x2pad_E600_FNAL": [],

    # HPK pads (May)
    "HPK_W9_22_3_20T_500x500_150M_E600": [],
    "HPK_W9_23_3_20T_500x500_300M_E600": [],
    "HPK_W11_22_3_20T_500x500_150M_C600": [],
    "HPK_W8_1_1_50T_500x500_150M_C600": [],
    "HPK_W5_1_1_50T_500x500_150M_E600": [],

    # HPK strips
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": [116.1, 30.3, 41.5, 3.8, 96.2],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600": [56.0, 27.1, 40.0, 1.5, 98.5],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": [68.1, 28.5, 37.6, 1.3, 98.7],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": [83.6, 13.8, 35.7, 2.1, 97.9],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": [81.3, 14.2, 35.5, 0.7, 99.3],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": [124.5, 22.4, 53.2, 64.6, 35.4],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": [142.5, 23.4, 50.0, 76.2, 23.8],
    "HPK_KOJI_50T_1P0_80P_60M_E240": [399.0, 9.4, 32.6, 0.8, 99.2],
    "HPK_KOJI_20T_1P0_80P_60M_E240": [309.5, 5.5, 30.3, 4.2, 95.8],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": [118.7, 20.2, 39.6, 60.2, 39.8],

    # # Mid gap
    # "HPK_W8_18_2_50T_1P0_500P_100M_C600": [116.1, 30.3, 42.3, 1.2, 98.8],
    # "HPK_W8_17_2_50T_1P0_500P_50M_C600": [56.0, 27.1, 40.9, 0.2, 99.8],
    # "HPK_W4_17_2_50T_1P0_500P_50M_C240": [68.1, 28.5, 37.2, 0.1, 99.9],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600": [83.6, 13.8, 35.7, 0.3, 99.7],
    # "HPK_W2_3_2_50T_1P0_500P_50M_E240": [81.3, 14.2, 35.8, 0.2, 99.8],
    # "HPK_W9_15_2_20T_1P0_500P_50M_E600": [124.5, 22.4, 78.7, 20.1, 79.9],
    # "HPK_W9_14_2_20T_1P0_500P_100M_E600": [142.5, 23.4, 69.2, 36.1, 63.9],
    # "HPK_W9_15_4_20T_0P5_500P_50M_E600": [118.7, 20.2, 51.6, 12.1, 87.9],
    # "HPK_KOJI_50T_1P0_80P_60M_E240": [399.0, 9.4, 32.8, 0.7, 99.3],
    # "HPK_KOJI_20T_1P0_80P_60M_E240": [309.5, 5.5, 29.9, 3.5, 96.5],
}

##############################  Characterization  ##############################
###############################---  Overall  ---################################
# <jitter [ps]>, <amp max [mV]>, <risetime [ps]>, <baseline_rms [mV]>, <charge [fC]>
characteristics2023_Overall = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2": [],
    "BNL_50um_1cm_400um_W3051_1_4": [],
    "BNL_50um_1cm_450um_W3052_2_4": [],
    "BNL_20um_1cm_400um_W3074_1_4": [],
    "BNL_20um_1cm_400um_W3075_1_2": [],
    "BNL_20um_1cm_450um_W3074_2_1": [],
    "BNL_20um_1cm_450um_W3075_2_4": [],
    "BNL_50um_2p5cm_mixConfig1_W3051_1_4": [],
    "BNL_50um_2p5cm_mixConfig2_W3051_1_4": [],

    # HPK pads (January)
    "HPK_20um_500x500um_2x2pad_E600_FNAL": [],
    "HPK_30um_500x500um_2x2pad_E600_FNAL": [],
    "HPK_50um_500x500um_2x2pad_E600_FNAL": [],

    # HPK pads (May)
    "HPK_W9_22_3_20T_500x500_150M_E600": [],
    "HPK_W9_23_3_20T_500x500_300M_E600": [],
    "HPK_W11_22_3_20T_500x500_150M_C600": [],
    "HPK_W8_1_1_50T_500x500_150M_C600": [],
    "HPK_W5_1_1_50T_500x500_150M_E600": [],

    # HPK strips
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": [38.36, 57.88, 628.99, 1.90, 30.68],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600": [38.11, 49.94, 619.22, 1.70, 11.57],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": [34.26, 57.49, 625.48, 1.77, 15.83],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": [25.11, 99.99, 650.37, 1.94, 34.82],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": [25.47, 92.08, 651.77, 1.85, 22.12],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": [52.75, 34.23, 561.01, 1.77, 15.71],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": [48.53, 32.19, 525.42, 1.80, 11.13],
    "HPK_KOJI_50T_1P0_80P_60M_E240": [23.19, 72.97, 574.50, 1.83, 16.93],
    "HPK_KOJI_20T_1P0_80P_60M_E240": [32.00, 38.44, 419.34, 1.76, 11.82],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": [],
}

################################---  Metal  ---#################################
# <jitter [ps]>, <amp max [mV]>, <risetime [ps]>, <baseline_rms [mV]>, <charge [fC]>
characteristics2023_Metal = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2": [],
    "BNL_50um_1cm_400um_W3051_1_4": [],
    "BNL_50um_1cm_450um_W3052_2_4": [],
    "BNL_20um_1cm_400um_W3074_1_4": [],
    "BNL_20um_1cm_400um_W3075_1_2": [],
    "BNL_20um_1cm_450um_W3074_2_1": [],
    "BNL_20um_1cm_450um_W3075_2_4": [],
    "BNL_50um_2p5cm_mixConfig1_W3051_1_4": [],
    "BNL_50um_2p5cm_mixConfig2_W3051_1_4": [],

    # HPK pads (January)
    "HPK_20um_500x500um_2x2pad_E600_FNAL": [],
    "HPK_30um_500x500um_2x2pad_E600_FNAL": [],
    "HPK_50um_500x500um_2x2pad_E600_FNAL": [],

    # HPK pads (May)
    "HPK_W9_22_3_20T_500x500_150M_E600": [],
    "HPK_W9_23_3_20T_500x500_300M_E600": [],
    "HPK_W11_22_3_20T_500x500_150M_C600": [],
    "HPK_W8_1_1_50T_500x500_150M_C600": [],
    "HPK_W5_1_1_50T_500x500_150M_E600": [],

    # HPK strips
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": [36.58, 66.12, 614.60, 1.89, 34.60],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600": [36.62, 57.86, 603.51, 1.69, 13.14],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": [33.26, 66.26, 611.92, 1.77, 17.60],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": [20.39, 128.58, 621.87, 1.94, 42.31],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": [21.38, 117.72, 625.00, 1.85, 26.48],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": [22.12, 50.25, 418.81, 1.77, 19.24],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": [26.44, 43.52, 428.26, 1.80, 13.31],
    "HPK_KOJI_50T_1P0_80P_60M_E240": [23.16, 74.35, 573.29, 1.83, 17.19],
    "HPK_KOJI_20T_1P0_80P_60M_E240": [31.84, 39.10, 415.80, 1.76, 12.04],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": [],
}

#################################---  Gap  ---##################################
# <jitter [ps]>, <amp max [mV]>, <risetime [ps]>, <baseline_rms [mV]>, <charge [fC]>
characteristics2023_Gap = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2": [],
    "BNL_50um_1cm_400um_W3051_1_4": [],
    "BNL_50um_1cm_450um_W3052_2_4": [],
    "BNL_20um_1cm_400um_W3074_1_4": [],
    "BNL_20um_1cm_400um_W3075_1_2": [],
    "BNL_20um_1cm_450um_W3074_2_1": [],
    "BNL_20um_1cm_450um_W3075_2_4": [],
    "BNL_50um_2p5cm_mixConfig1_W3051_1_4": [],
    "BNL_50um_2p5cm_mixConfig2_W3051_1_4": [],

    # HPK pads (January)
    "HPK_20um_500x500um_2x2pad_E600_FNAL": [],
    "HPK_30um_500x500um_2x2pad_E600_FNAL": [],
    "HPK_50um_500x500um_2x2pad_E600_FNAL": [],

    # HPK pads (May)
    "HPK_W9_22_3_20T_500x500_150M_E600": [],
    "HPK_W9_23_3_20T_500x500_300M_E600": [],
    "HPK_W11_22_3_20T_500x500_150M_C600": [],
    "HPK_W8_1_1_50T_500x500_150M_C600": [],
    "HPK_W5_1_1_50T_500x500_150M_E600": [],

    # HPK strips
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": [38.81, 49.67, 652.93, 1.90, 26.92],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600": [38.28, 42.48, 643.64, 1.70, 10.50],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": [34.37, 49.31, 644.22, 1.76, 14.24],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": [24.76, 74.06, 685.18, 1.93, 27.72],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": [26.82, 68.98, 683.51, 1.85, 17.87],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": [68.39, 23.76, 578.16, 1.77, 12.37],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": [76.63, 22.60, 693.34, 1.80, 8.67],
    "HPK_KOJI_50T_1P0_80P_60M_E240": [21.37, 68.32, 578.81, 1.82, 16.01],
    "HPK_KOJI_20T_1P0_80P_60M_E240": [32.45, 35.13, 430.75, 1.76, 10.97],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": [],
}

# [Overall (default), Overall, Metal, Gap]
region = ["", "_o", "_m", "_g"]
resolutions2023 = {}
for sensor in resolutions2023_Overall:
    info_dict = {}
    list_res = [resolutions2023_Overall[sensor], resolutions2023_Overall[sensor], resolutions2023_Metal[sensor], resolutions2023_Gap[sensor]]
    list_char = [characteristics2023_Overall[sensor], characteristics2023_Overall[sensor], characteristics2023_Metal[sensor], characteristics2023_Gap[sensor]]
    for i, reg in enumerate(region):
        res = list_res[i]
        if not res:
            # print(" (!) Sensor %s resolution is empty (!)"%sensor)
            continue
        info_dict["position_oneStrip%s"%reg], info_dict["position_oneStripRMS%s"%reg] = res[0], res[0]
        info_dict["res_one_strip%s"%reg] = res[0]
        info_dict["position_twoStrip%s"%reg], info_dict["res_two_strip%s"%reg] = res[1], res[1]
        info_dict["time_resolution%s"%reg], info_dict["res_time%s"%reg] = res[2], res[2]
        info_dict["efficiency_oneStrip%s"%reg], info_dict["efficiency_one_strip%s"%reg] = res[3], res[3]
        info_dict["efficiency_twoStrip%s"%reg], info_dict["efficiency_two_strip%s"%reg] = res[4], res[4]

        char = list_char[i]
        if not char:
            # print(" (!) Sensor %s characteristic is empty (!)"%sensor)
            continue
        info_dict["jitter%s"%reg] = char[0]
        info_dict["amp_max%s"%reg] = char[1]
        info_dict["rise_time%s"%reg] = char[2]
        info_dict["baseline_rms%s"%reg] = char[3]
        info_dict["charge%s"%reg] = char[4]

    resolutions2023[sensor] = info_dict

######################  One strip resolution per channel  ######################
# NOTE: Resolution values do NOT have tracker component removed
resolutions2023_onestrip = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2": [],
    "BNL_50um_1cm_400um_W3051_1_4": [],
    "BNL_50um_1cm_450um_W3052_2_4": [],
    "BNL_20um_1cm_400um_W3074_1_4": [],
    "BNL_20um_1cm_400um_W3075_1_2": [],
    "BNL_20um_1cm_450um_W3074_2_1": [],
    "BNL_20um_1cm_450um_W3075_2_4": [],
    "BNL_50um_2p5cm_mixConfig1_W3051_1_4": [],
    "BNL_50um_2p5cm_mixConfig2_W3051_1_4": [],

    # HPK pads (January)
    "HPK_20um_500x500um_2x2pad_E600_FNAL": [],
    "HPK_30um_500x500um_2x2pad_E600_FNAL": [],
    "HPK_50um_500x500um_2x2pad_E600_FNAL": [],

    # HPK pads (May)
    "HPK_W9_22_3_20T_500x500_150M_E600": [],
    "HPK_W9_23_3_20T_500x500_300M_E600": [],
    "HPK_W11_22_3_20T_500x500_150M_C600": [],
    "HPK_W8_1_1_50T_500x500_150M_C600": [],
    "HPK_W5_1_1_50T_500x500_150M_E600": [],

    # HPK strips
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": [0.0, 77.2, 75.9, 74.0, 55.8, 70.8, 0.0],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600": [0.0, 35.3, 38.9, 37.4, 35.1, 34.2, 0.0],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": [0.0, 48.0, 45.7, 43.2, 43.3, 43.2, 0.0],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": [0.0, 52.6, 53.3, 52.9, 56.3, 52.9, 0.0],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": [0.0, 37.1, 39.6, 35.1, 35.4, 36.9, 0.0],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": [0.0, 110.1, 111.3, 115.2, 118.1, 116.9, 0.0],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": [0.0, 124.3, 121.7, 125.5, 121.3, 125.2, 0.0],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": [0.0, 111.2, 110.6, 109.5, 108.8, 106.8, 0.0],
    "HPK_KOJI_50T_1P0_80P_60M_E240": [0.0, 22.8, 23.7, 20.4, 22.3, 22.5, 0.0],
    "HPK_KOJI_20T_1P0_80P_60M_E240": [0.0, 56.7, 45.1, 35.3, 33.6, 38.6, 0.0],
}

resolutions2023OneStripChannel = {}
for key, res_list in resolutions2023_onestrip.items():
    info_dict = {}
    # if not res_list:
    #     print(" (!) Sensor %s per channel resolution is empty (!)"%sensor)
    info_dict["resOneStrip"], info_dict["resolution_onestrip"] = res_list, res_list
    info_dict["errOneStrip"] = [-1.0] * len(res_list)

    resolutions2023OneStripChannel[key] = info_dict


################################################################################
# ----------------  (!) Bias scan January 2023 2x2 pads (!)  ----------------- #
################################################################################
##################################  Geometry  ##################################
# List with all voltages used in each sensor
geometry2023_biasscan = {
    # HPK pads (January)
    "HPK_20um_500x500um_2x2pad_E600_FNAL": [95, 100, 105, 110, 108, 90, 85, 75],
    "HPK_30um_500x500um_2x2pad_E600_FNAL": [144, 140, 135, 130, 120, 110],
    "HPK_50um_500x500um_2x2pad_E600_FNAL": [190, 185, 180, 170, 160],
}

sensorsGeom2023_biasScan = {}
for key, voltages in geometry2023_biasscan.items():
    info = geometry2023_default[key]
    for volt in voltages:
        info_dict = {}
        info_dict["sensor"] = "%s_%iV"%(info[0], volt)
        info_dict["pitch"] = info[1]
        info_dict["stripWidth"], info_dict["width"] = info[2], info[2]
        info_dict["length"] = info[3]
        info_dict["BV"], info_dict["voltage"] = volt, volt
        info_dict["thickness"] = info[5]
        info_dict["resistivity"] = info[6]
        info_dict["capacitance"] = info[7]

        new_key = "%s_%iV"%(key, volt)
        sensorsGeom2023_biasScan[new_key] = info_dict

##########################  Characterization overall  ##########################
# <time res [ps]>, <jitter [ps]>, <amp max [mV]>, <risetime [ps]>, <baseline_rms [mV]>, <charge [fC]>
characteristics2023_biasscan_Overall = {
    # HPK pads (January)
    "HPK_50um_500x500um_2x2pad_E600_FNAL_190V": [40.80, 9.88, 155.77, 566.57, 1.89, 40.10],
    "HPK_50um_500x500um_2x2pad_E600_FNAL_185V": [39.10, 11.53, 135.97, 564.69, 1.86, 26.26],
    "HPK_50um_500x500um_2x2pad_E600_FNAL_180V": [40.84, 12.81, 122.97, 567.54, 1.86, 21.80],
    "HPK_50um_500x500um_2x2pad_E600_FNAL_170V": [45.31, 14.91, 102.83, 576.93, 1.86, 16.80],
    "HPK_50um_500x500um_2x2pad_E600_FNAL_160V": [48.79, 16.92, 86.69, 591.97, 1.86, 13.83],

    "HPK_30um_500x500um_2x2pad_E600_FNAL_144V": [34.90, 7.94, 146.90, 405.85, 1.88, -70.01],
    "HPK_30um_500x500um_2x2pad_E600_FNAL_140V": [28.31, 9.93, 106.27, 397.49, 1.84, 15.89],
    "HPK_30um_500x500um_2x2pad_E600_FNAL_135V": [28.19, 11.31, 89.20, 397.99, 1.84, 10.45],
    "HPK_30um_500x500um_2x2pad_E600_FNAL_130V": [29.51, 12.48, 75.99, 400.48, 1.84, 8.11],
    "HPK_30um_500x500um_2x2pad_E600_FNAL_120V": [33.08, 15.43, 58.39, 411.65, 1.84, 5.70],
    "HPK_30um_500x500um_2x2pad_E600_FNAL_110V": [37.29, 19.87, 45.29, 431.27, 1.84, 4.22],

    "HPK_20um_500x500um_2x2pad_E600_FNAL_110V": [44.42, 9.10, 141.34, 382.94, 1.88, -12.32],
    "HPK_20um_500x500um_2x2pad_E600_FNAL_108V": [24.47, 10.29, 82.91, 363.15, 1.85, 13.84],
    "HPK_20um_500x500um_2x2pad_E600_FNAL_105V": [24.09, 11.32, 68.32, 357.18, 1.84, 7.69],
    "HPK_20um_500x500um_2x2pad_E600_FNAL_100V": [25.13, 13.89, 53.13, 359.53, 1.84, 4.83],
    "HPK_20um_500x500um_2x2pad_E600_FNAL_95V": [27.20, 17.29, 42.88, 368.93, 1.84, 3.48],
    "HPK_20um_500x500um_2x2pad_E600_FNAL_90V": [30.72, 21.49, 34.99, 382.81, 1.84, 2.78],
    "HPK_20um_500x500um_2x2pad_E600_FNAL_85V": [34.80, 25.45, 31.15, 398.58, 1.85, 2.40],
    "HPK_20um_500x500um_2x2pad_E600_FNAL_75V": [43.61, 30.98, 27.02, 427.56, 1.85, 1.87],
}

variableInfo2023_biasScan = {}
for key, values in characteristics2023_biasscan_Overall.items():
    info_dict = {}
    info_dict["time_resolution"] = values[0]
    info_dict["jitter"] = values[1]
    info_dict["amp_max"] = values[2]
    info_dict["risetime"] = values[3]
    info_dict["baseline"], info_dict["baseline_RMS"] = values[4], values[4]
    info_dict["charge"] = values[5]

    variableInfo2023_biasScan[key] = info_dict

# TODO: Add dictionary with Metal and Gap values when they are implemented in pads



################################################################################
# --------------------------  (!) 2022 Sensors (!)  -------------------------- #
################################################################################
##################################  Geometry  ##################################
# {<sensor name_long>, <sensor name_short/label>, <pitch [um]>, <width [um]>, <length [mm]>,
#  <Bias voltage [V]>, <thickness [um]>, <resistivity [Ohm/sq]>, <capacitance [pF/mm2]>}

geometry2022_default = {
    "EIC_W2_1cm_500up_300uw": ["BNL 10-300", 500, 300, 10.0, 240, 0.0, "Null", "Null"],
    "EIC_W1_1cm_500up_200uw": ["BNL 10-200", 500, 200, 10.0, 255, 0.0, "Null", "Null"],
    "EIC_W2_1cm_500up_100uw": ["BNL 10-100", 500, 100, 10.0, 220, 0.0, "Null", "Null"],
    "EIC_W1_1cm_100up_50uw": ["EIC_1cm_100up_50uw", 100, 50, 10.0, 240, 0.0, "Null", "Null"],
    "EIC_W1_1cm_200up_100uw": ["EIC_1cm_200up_100uw", 200, 100, 10.0, 240, 0.0, "Null", "Null"],
    "EIC_W1_1cm_300up_150uw": ["EIC_1cm_300up_150uw", 300, 150, 10.0, 240, 0.0, "Null", "Null"],
    "EIC_W1_UCSC_2p5cm_500up_200uw": ["EIC_2p5cm_UCSC_500up_200uw", 500, 200, 25.0, 330, 0.0, "Null", "Null"],
    "EIC_W1_2p5cm_500up_200uw": ["BNL 25-200", 500, 200, 25.0, 215, 0.0, "Null", "Null"],
    "HPK_Eb_1cm_80up_45uw": ["HPK_Eb_80up_45uw", 80, 45, 10.0, 170, 0.0, "Null", "Null"],
    "EIC_W1_0p5cm_500up_200uw_1_7": ["EIC_1_7_0p5cm_500up_200uw", 500, 200, 5.0, 240, 0.0, "Null", "Null"],
    "EIC_W1_0p5cm_500up_200uw_1_4": ["BNL 5-200", 500, 200, 5.0, 245, 0.0, "Null", "Null"],
    "BNL_500um_squares_175V": ["BNL_squares_1cm_500up_300uw", 500, 100, 0.0, 175, 0.0, "Null", "Null"],
    "BNL2021_22_medium_150up_80uw": ["BNL2021_V2_150up_80uw", 150, 80, 0.0, 285, 0.0, "Null", "Null"],
    "IHEP_W1_I_150up_80uw": ["IHEP_1cm_150up_80uw", 150, 80, 0.0, 185, 0.0, "Null", "Null"],
}

sensorsGeom2022 = {}
for key, info in geometry2022_default.items():
    info_dict = {}
    info_dict["sensor"] = info[0]
    info_dict["pitch"] = info[1]
    info_dict["stripWidth"], info_dict["width"] = info[2], info[2]
    info_dict["length"] = info[3]
    info_dict["BV"], info_dict["voltage"] = info[4], info[4]
    info_dict["thickness"] = info[5]
    info_dict["resistivity"] = info[6]
    info_dict["capacitance"] = info[7]

    sensorsGeom2022[key] = info_dict

#########################  Resolutions and efficiency  #########################
# NOTE: Resolution values do NOT have tracker component removed
# NOTE 2: Time resolution values were set according to paper's table. Missing numbers are set to 0.0
# <one strip reco RMS [um]>, <two strip reco fit [um]>, <time [ps]>, <efficiency one strip>, <efficiency two strip>
resolutions2022_Overall = {
    "EIC_W2_1cm_500up_300uw": [82.71, 15.74, 36.0, 0.51, 0.49],
    "EIC_W1_1cm_500up_200uw": [81.86, 18.49, 32.0, 0.43, 0.57],
    "EIC_W2_1cm_500up_100uw": [68.89, 19.23, 35.0, 0.23, 0.77],
    "EIC_W1_2p5cm_500up_200uw": [128.10, 31.32, 51.0, 0.82, 0.18],
    "EIC_W1_0p5cm_500up_200uw_1_4": [60.93, 11.76, 30.0, 0.35, 0.65],
    "HPK_Eb_1cm_80up_45uw": [13.83, 9.36, 0.0, 0.50, 0.50],
    "BNL2021_22_medium_150up_80uw": [22.35, 8.01, 0.0, 0.50, 0.50],
}

resolutions2022 = {}
for sensor in resolutions2022_Overall:
    info_dict = {}

    info_dict["position_oneStrip"], info_dict["position_oneStripRMS"] = res[0], res[0]
    info_dict["res_one_strip"] = res[0]
    info_dict["position_twoStrip"], info_dict["res_two_strip"] = res[1], res[1]
    info_dict["time_resolution"], info_dict["res_time"] = res[2], res[2]
    info_dict["efficiency_oneStrip"], info_dict["efficiency_one_strip"] = res[3], res[3]
    info_dict["efficiency_twoStrip"], info_dict["efficiency_two_strip"] = res[4], res[4]

    resolutions2022[sensor] = info_dict

######################  One strip resolution per channel  ######################
# NOTE: Resolution values do NOT have tracker component removed
resolutions2022_onestrip = {
    "EIC_W2_1cm_500up_300uw": [0.00, 81.75, 83.41, 83.40, 82.10, 0.00, 0.00],
    "EIC_W1_1cm_500up_200uw": [0.00, 76.99, 81.69, 79.00, 82.88, 84.76, 0.00],
    "EIC_W2_1cm_500up_100uw": [0.00, 66.17, 68.40, 66.86, 68.28, 72.04, 0.00],
    "EIC_W1_2p5cm_500up_200uw": [],
    "EIC_W1_0p5cm_500up_200uw_1_4": [],
    "HPK_Eb_1cm_80up_45uw": [],
    "BNL2021_22_medium_150up_80uw": [],
}

resolutions2022OneStripChannel = {}
for key, res_list in resolutions2022_onestrip.items():
    info_dict = {}
    # if not res_list:
    #    print(" (!) Sensor %s per channel resolution is empty (!)"%sensor)
    info_dict["resOneStrip"], info_dict["resolution_onestrip"] = res_list, res_list
    info_dict["errOneStrip"] = [1.0] * len(res_list)

    resolutions2022OneStripChannel[key] = info_dict

