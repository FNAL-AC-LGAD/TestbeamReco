
################################################################################
# --------------------------  (!) 2023 Sensors (!)  -------------------------- #
################################################################################
##################################  Geometry  ##################################
# {<sensor name_long>, <sensor name_short/label>, <pitch [um]>, <width [um]>, <length [mm]>,
#  <Bias voltage [V]>, <thickness [um]>, <resistivity [Ohm/sq]>, <capacitance [pF/mm2]>, tag}
geometry2023_default = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2": ["BNL_50um_1cm_450um_W3051", 500, 50, 10.0, 170, 50, "G", "270", "SB1"],
    "BNL_50um_1cm_400um_W3051_1_4": ["BNL_50um_1cm_400um_W3051", 500, 100, 10.0, 160, 50, "G", "270", "SB2"],
    "BNL_50um_1cm_450um_W3052_2_4": ["BNL_50um_1cm_450um_W3052", 500, 50, 10.0, 185, 50, "G", "260", "SB3"],
    "BNL_20um_1cm_400um_W3074_1_4": ["BNL_20um_1cm_400um_W3074", 500, 100, 10.0, 95, 20, "Null", "Null", "Null"],
    "BNL_20um_1cm_400um_W3075_1_2": ["BNL_20um_1cm_400um_W3075", 500, 100, 10.0, 80, 20, "Null", "Null", "Null"],
    "BNL_20um_1cm_450um_W3074_2_1": ["BNL_20um_1cm_450um_W3074", 500, 50, 10.0, 95, 20, "Null", "Null", "Null"],
    "BNL_20um_1cm_450um_W3075_2_4": ["BNL_20um_1cm_450um_W3075", 500, 50, 10.0, 80, 20, "Null", "Null", "Null"],
    "BNL_50um_2p5cm_mixConfig1_W3051_1_4": ["BNL_50um_2p5cm_mixConfig1_W3051", 500, 100, 25.0, 170, 50, "Null", "Null", "Null"],
    "BNL_50um_2p5cm_mixConfig2_W3051_1_4": ["BNL_50um_2p5cm_mixConfig2_W3051", 500, 50, 25.0, 170, 50, "Null", "Null", "Null"],

    "BNL_30um_5mm_500um_W3104": ["BNL_30um_5mm_500um_W3104", 500, 100, 5.0, 90, 30, "Null", "Null", "Null"],
    "BNL_30um_5mm_700um_W3104": ["BNL_30um_5mm_700um_W3104", 700, 100, 5.0, 115, 30, "Null", "Null", "Null"],
    "BNL_20um_5mm_700um_W3080": ["BNL_20um_5mm_700um_W3080", 700, 100, 5.0, 80, 20, "Null", "Null", "Null"],
    "BNL_20um_5mm_500um_W3080": ["BNL_20um_5mm_500um_W3080", 500, 100, 5.0, 80, 20, "Null", "Null", "Null"],
    "BNL_30um_500x500_SmallSquare_W3104": ["BNL_30um_500x500_SmallSquare_W3104", 500, 500, 5.0, 115, 30, "Null", "Null", "PB1"],
    "BNL_20um_500x500_SmallSquare_W3080": ["BNL_20um_500x500_SmallSquare_W3080", 500, 500, 5.0, 76, 20, "Null", "Null", "Null"],
    "BNL_30um_500x500_LargeSquare_W3104": ["BNL_30um_500x500_LargeSquare_W3104", 500, 500, 5.0, 115, 30, "Null", "Null", "PB2"],
    "BNL_20um_500x500_LargeSquare_W3080": ["BNL_20um_500x500_LargeSquare_W3080", 500, 500, 5.0, 80, 20, "Null", "Null", "Null"],
    "BNL_30um_500x500_SquaredCircle_W3104": ["BNL_30um_500x500_SquaredCircle_W3104", 500, 500, 5.0, 110, 30, "Null", "Null", "PB3"],
    "BNL_20um_500x500_SquaredCircle_W3080": ["BNL_20um_500x500_SquaredCircle_W3080", 500, 500, 5.0, 85, 20, "Null", "Null", "Null"],
    "BNL_30um_500x500_Cross_W3104": ["BNL_30um_500x500_Cross_W3104", 500, 500, 5.0,115, 30, "Null", "Null", "PB4"],
    "BNL_20um_500x500_Cross_W3080": ["BNL_20um_500x500_Cross_W3080", 500, 500,5.0, 80, 20, "Null", "Null", "Null"],

    # HPK pads (January)
    "HPK_20um_500x500um_2x2pad_E600_FNAL": ["HPK_20um_2x2pad", 500, 450, 0.5, 105, 20, "E", 600, "PH1"],
    "HPK_30um_500x500um_2x2pad_E600_FNAL": ["HPK_30um_2x2pad", 500, 450, 0.5, 140, 30, "E", 600, "PH2"],
    "HPK_50um_500x500um_2x2pad_E600_FNAL": ["HPK_50um_2x2pad", 500, 450, 0.5, 190, 50, "E", 600, "PH3"],

    # HPK pads (May)
    "HPK_W9_22_3_20T_500x500_150M_E600": ["HPK_W9_22_3_20T_500x500_150M_E600", 500, 150, 5.0, 112, 20, "E", 600, "PH5"],
    "HPK_W9_23_3_20T_500x500_300M_E600": ["HPK_W9_23_3_20T_500x500_300M_E600", 500, 300, 5.0, 112, 20, "E", 600, "PH8"],
    "HPK_W11_22_3_20T_500x500_150M_C600": ["HPK_W11_22_3_20T_500x500_150M_C600", 500, 150, 5.0, 116, 20, "C", 600, "PH4"],
    "HPK_W8_1_1_50T_500x500_150M_C600": ["HPK_W8_1_1_50T_500x500_150M_C600", 500, 150, 5.0, 200, 50, "C", 600, "PH6"],
    "HPK_W5_1_1_50T_500x500_150M_E600": ["HPK_W5_1_1_50T_500x500_150M_E600", 500, 150, 5.0, 185, 50, "E", 600, "PH7"],

    # HPK strips
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": ["HPK_W8_18_2_50T_100M_C600", 500, 100, 10.0, 208, 50, "C", 600, "SH7"],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600": ["HPK_W8_17_2_50T_50M_C600", 500, 50, 10.0, 206, 50, "C", 600, "SH3"],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": ["HPK_W4_17_2_50T_1P0_500P_50M_C240", 500, 50, 10.0, 204, 50, "C", 240, "SH2"],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": ["HPK_W5_17_2_50T_1P0_500P_50M_E600", 500, 50, 10.0, 190, 50, "E", 600, "SH5"],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": ["HPK_W2_3_2_50T_1P0_500P_50M_E240", 500, 50, 10.0, 180, 50, "E", 240, "SH4"],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": ["HPK_W9_15_2_20T_1P0_500P_50M_E600", 500, 50, 10.0, 114, 20, "E", 600, "SH1"],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": ["HPK_W9_14_2_20T_1P0_500P_100M_E600", 500, 100, 10.0, 112, 20, "E", 600, "SH6"],
    "HPK_KOJI_50T_1P0_80P_60M_E240": ["HPK_50T_1P0_80P_60M_E240", 80, 60, 10.0, 190, 50, "E", 240, "SHN2"],
    "HPK_KOJI_20T_1P0_80P_60M_E240": ["HPK_20T_1P0_80P_60M_E240", 80, 60, 10.0, 112, 20, "E", 240, "SHN1"],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": ["HPK_W9_15_4_20T_0P5_500P_50M_E600", 500, 50, 5.0, 110, 20, "E", 600, "Null"],
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
    info_dict["resistivityNumber"] = 0
    if info[6] == "E":
        info_dict["resistivityNumber"] = 1600
    elif info[6] == "C":
        info_dict["resistivityNumber"] = 400
    elif info[6] == "G":
        info_dict["resistivityNumber"] = 1400
    info_dict["capacitance"] = info[7]
    if info[8] == "Null":
        info_dict["tag"] = info[0]
    else:
        info_dict["tag"] = info[8]

    sensorsGeom2023[key] = info_dict

#########################  Resolutions and efficiency  #########################
# NOTE: Resolution values do NOT have tracker component removed
###############################---  Overall  ---################################
# <one strip reco RMS [um]>, <two strip reco fit [um]>, <time [ps]>, <efficiency one strip>, <efficiency two strip>
resolutions2023_Overall = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2": [48.5, 22.6, 44.8, 13.7, 86.3],
    "BNL_50um_1cm_400um_W3051_1_4": [51.0, 21.0, 43.7, 20.4, 79.6],
    "BNL_50um_1cm_450um_W3052_2_4": [],
    "BNL_20um_1cm_400um_W3074_1_4": [],
    "BNL_20um_1cm_400um_W3075_1_2": [],
    "BNL_20um_1cm_450um_W3074_2_1": [],
    "BNL_20um_1cm_450um_W3075_2_4": [106.1, 32.4, 47.1, 92.2, 7.8],
    "BNL_50um_2p5cm_mixConfig1_W3051_1_4": [],
    "BNL_50um_2p5cm_mixConfig2_W3051_1_4": [],

    # HPK pads (January)
    "HPK_20um_500x500um_2x2pad_E600_FNAL": [0.0, 0.0, 22.4, 0.0, 0.0],
    "HPK_30um_500x500um_2x2pad_E600_FNAL": [0.0, 0.0, 0.0, 0.0, 0.0],
    "HPK_50um_500x500um_2x2pad_E600_FNAL": [0.0, 0.0, 0.0, 0.0, 0.0],

    # HPK pads (May)
    "HPK_W11_22_3_20T_500x500_150M_C600": [61.4, 20.6, 22.9, 55.5, 44.5],
    "HPK_W9_22_3_20T_500x500_150M_E600": [72.9, 25.4, 32.8, 62.1, 37.9],
    "HPK_W8_1_1_50T_500x500_150M_C600": [56.4, 22.9, 32.0, 44.4, 55.6],
    "HPK_W5_1_1_50T_500x500_150M_E600": [60.5, 31.1, 33.7, 45.5, 54.5],
    "HPK_W9_23_3_20T_500x500_300M_E600": [96.2, 15.4, 23.2, 80.4, 19.6],

    # HPK strips
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": [69.6, 32.8, 42.0, 8.7, 91.3],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600": [36.7, 27.4, 40.3, 3.6, 96.4],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": [38.6, 28.3, 38.0, 6.2, 93.8],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": [53.9, 14.4, 36.4, 4.4, 95.6],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": [36.3, 14.7, 36.3, 2.4, 97.6],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": [115.9, 23.3, 53.9, 67.9, 32.1],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": [123.9, 23.8, 49.1, 80.6, 19.4],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": [109.7, 20.5, 40.3, 63.9, 36.1],
    "HPK_KOJI_20T_1P0_80P_60M_E240": [26.7, 11.1, 31.3, 23.4, 76.6],
    "HPK_KOJI_50T_1P0_80P_60M_E240": [17.5, 9.9, 33.2, 12.3, 87.7],

    # # HPK strips
    # "HPK_W8_18_2_50T_1P0_500P_100M_C600": [69.6, 31.2, 40.1, 8.7, 91.3],
    # "HPK_W8_17_2_50T_1P0_500P_50M_C600": [36.7, 27.0, 39.9, 3.6, 96.4],
    # "HPK_W4_17_2_50T_1P0_500P_50M_C240": [38.6, 28.2, 37.4, 6.2, 93.8],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600": [53.9, 13.9, 35.5, 4.4, 95.6],
    # "HPK_W2_3_2_50T_1P0_500P_50M_E240": [36.3, 14.3, 35.3, 2.4, 97.6],
    # "HPK_W9_15_2_20T_1P0_500P_50M_E600": [115.9, 22.3, 49.7, 67.9, 32.1],
    # "HPK_W9_14_2_20T_1P0_500P_100M_E600": [123.9, 22.9, 43.8, 80.6, 19.4],
    # "HPK_W9_15_4_20T_0P5_500P_50M_E600": [109.7, 20.2, 37.4, 63.9, 36.1],
    # "HPK_KOJI_20T_1P0_80P_60M_E240": [26.7, 11.1, 31.3, 23.4, 76.6],
    # "HPK_KOJI_50T_1P0_80P_60M_E240": [17.5, 9.9, 33.2, 12.3, 87.7],
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
    list_res = [resolutions2023_Overall[sensor], resolutions2023_Overall[sensor],
                resolutions2023_Metal[sensor], resolutions2023_Gap[sensor]]
    list_char = [characteristics2023_Overall[sensor], characteristics2023_Overall[sensor],
                 characteristics2023_Metal[sensor], characteristics2023_Gap[sensor]]
    for i, reg in enumerate(region):
        res = list_res[i]
        if not res:
            # print(" (!) Sensor %s resolution is empty (!)"%sensor)
            continue
        info_dict["position_oneStrip%s"%reg] = res[0]
        info_dict["position_oneStripRMS%s"%reg] = res[0]
        info_dict["res_one_strip%s"%reg] = res[0]
        info_dict["position_twoStrip%s"%reg] = res[1]
        info_dict["res_two_strip%s"%reg] = res[1]
        info_dict["time_resolution%s"%reg] = res[2]
        info_dict["res_time%s"%reg] = res[2]
        info_dict["efficiency_oneStrip%s"%reg] = res[3]
        info_dict["efficiency_one_strip%s"%reg] = res[3]
        info_dict["efficiency_twoStrip%s"%reg] = res[4]
        info_dict["efficiency_two_strip%s"%reg] = res[4]

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
    "BNL_50um_1cm_450um_W3051_2_2": [[51.4, 49.4, 49.5, 48.1, 49.3, 47.7, 55.2]],
    "BNL_50um_1cm_400um_W3051_1_4": [[48.9, 50.9, 52.2, 50.8, 50.3, 48.8, 54.5]],
    "BNL_50um_1cm_450um_W3052_2_4": [],
    "BNL_20um_1cm_400um_W3074_1_4": [],
    "BNL_20um_1cm_400um_W3075_1_2": [],
    "BNL_20um_1cm_450um_W3074_2_1": [],
    "BNL_20um_1cm_450um_W3075_2_4": [[110.6, 102.6, 103.2, 102.1, 105.2, 105.7, 95.4]],
    "BNL_50um_2p5cm_mixConfig1_W3051_1_4": [],
    "BNL_50um_2p5cm_mixConfig2_W3051_1_4": [],

    # HPK pads (January)
    "HPK_20um_500x500um_2x2pad_E600_FNAL": [[145.7, 128.7], [139.4, 127.6]],
    "HPK_30um_500x500um_2x2pad_E600_FNAL": [],
    "HPK_50um_500x500um_2x2pad_E600_FNAL": [],

    # HPK pads (May)
    "HPK_W9_22_3_20T_500x500_150M_E600": [[81.5, 69.9, 69.7], [81.8, 68.2, 70.3]],
    "HPK_W9_23_3_20T_500x500_300M_E600": [[96.1, 100.3], [96.3, 95.3]],
    "HPK_W11_22_3_20T_500x500_150M_C600": [[59.5, 59.9, 57.3], [62.0, 63.7, 63.5]],
    "HPK_W8_1_1_50T_500x500_150M_C600": [[58.3, 56.3, 55.4], [62.7, 56.5, 51.9]],
    "HPK_W5_1_1_50T_500x500_150M_E600": [[53.3, 62.6, 69.8], [52.4, 61.8, 64.8]],

    # HPK strips
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": [[68.0, 77.2, 75.9, 74.0, 55.8, 70.8, 74.1]],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600": [[37.0, 35.3, 38.9, 37.4, 35.1, 34.2, 49.0]],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": [[45.3, 40.4, 39.7, 39.3, 38.0, 38.6, 43.9]],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": [[49.5, 52.6, 53.3, 52.9, 56.3, 52.9, 55.6]],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": [[38.0, 37.1, 39.6, 35.1, 35.4, 36.9, 42.5]],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": [[110.9, 110.1, 111.3, 115.2, 118.1, 116.9, 114.1]],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": [[127.1, 124.4, 121.8, 125.7, 121.4, 125.3, 119.2]],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": [[114.8, 111.2, 110.6, 109.5, 108.8, 106.8, 109.9]],
    "HPK_KOJI_50T_1P0_80P_60M_E240": [[13.3, 11.6, 12.8, 11.4, 11.9, 11.9, 14.2]],
    "HPK_KOJI_20T_1P0_80P_60M_E240": [[14.2, 15.0, 14.3, 14.4, 14.6, 14.6, 14.5]],
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
        info_dict["resistivityNumber"] = 0
        if info[6] == "E":
            info_dict["resistivityNumber"] = 1600
        elif info[6] == "C":
            info_dict["resistivityNumber"] = 400
        info_dict["capacitance"] = info[7]
        info_dict["tag"] = info[8]

        new_key = "%s_%iV"%(key, volt)
        sensorsGeom2023_biasScan[new_key] = info_dict

##########################  Characterization overall  ##########################
# <time res [ps]>, <jitter [ps]>, <amp max [mV]>, <risetime [ps]>, <baseline_rms [mV]>, <charge [fC]>
characteristics2023_biasscan_Overall = {
    # HPK pads (January) - overall, stat mean
    "HPK_50um_500x500um_2x2pad_E600_FNAL_190V": [39.60, 9.88, 155.34, 566.60, 1.89, 39.37],
    "HPK_50um_500x500um_2x2pad_E600_FNAL_185V": [39.10, 11.53, 135.68, 564.67, 1.86, 26.24],
    "HPK_50um_500x500um_2x2pad_E600_FNAL_180V": [40.87, 12.81, 122.57, 567.66, 1.86, 21.80],
    "HPK_50um_500x500um_2x2pad_E600_FNAL_170V": [45.34, 14.91, 102.34, 576.85, 1.86, 16.80],
    "HPK_50um_500x500um_2x2pad_E600_FNAL_160V": [48.81, 16.91, 86.12, 592.30, 1.86, 13.82],

    "HPK_30um_500x500um_2x2pad_E600_FNAL_144V": [34.90, 7.94, 146.22, 405.92, 1.88, 0.0],
    "HPK_30um_500x500um_2x2pad_E600_FNAL_140V": [26.77, 9.93, 105.93, 397.64, 1.84, 15.87],
    "HPK_30um_500x500um_2x2pad_E600_FNAL_135V": [28.22, 11.31, 88.71, 398.11, 1.84, 10.38],
    "HPK_30um_500x500um_2x2pad_E600_FNAL_130V": [29.56, 12.47, 75.20, 400.59, 1.84, 8.04],
    "HPK_30um_500x500um_2x2pad_E600_FNAL_120V": [33.41, 15.42, 57.03, 412.12, 1.84, 5.61],
    "HPK_30um_500x500um_2x2pad_E600_FNAL_110V": [37.58, 19.86, 44.23, 431.87, 1.84, 4.18],

    "HPK_20um_500x500um_2x2pad_E600_FNAL_110V": [44.49, 9.11, 140.45, 383.23, 1.88, 0.0],
    "HPK_20um_500x500um_2x2pad_E600_FNAL_108V": [24.53, 10.29, 82.13, 363.51, 1.85, 13.66],
    "HPK_20um_500x500um_2x2pad_E600_FNAL_105V": [23.75, 11.30, 66.99, 357.87, 1.84, 7.50],
    "HPK_20um_500x500um_2x2pad_E600_FNAL_100V": [25.70, 13.88, 51.81, 360.31, 1.84, 4.76],
    "HPK_20um_500x500um_2x2pad_E600_FNAL_95V": [27.38, 17.29, 42.02, 369.59, 1.84, 3.46],
    "HPK_20um_500x500um_2x2pad_E600_FNAL_90V": [30.77, 21.54, 34.33, 383.27, 1.84, 2.73],
    "HPK_20um_500x500um_2x2pad_E600_FNAL_85V": [34.94, 25.71, 30.14, 399.14, 1.85, 2.23],
    "HPK_20um_500x500um_2x2pad_E600_FNAL_75V": [43.99, 31.85, 24.95, 428.53, 1.84, 1.26],

    # Made to explain the contradiction between the jitter plot and the time resolution plot:
    # "HPK_50um_500x500um_2x2pad_E600_FNAL_190V": [32.39, 7.49, 153.36, 572.27, 1.90, -59.16],
    # "HPK_50um_500x500um_2x2pad_E600_FNAL_185V": [37.07, 11.86, 133.83, 564.67, 1.86, 28.12],
    # "HPK_50um_500x500um_2x2pad_E600_FNAL_180V": [39.03, 13.06, 117.84, 567.66, 1.86, 23.34],
    # "HPK_50um_500x500um_2x2pad_E600_FNAL_170V": [44.03, 15.27, 93.99, 576.85, 1.86, 18.13],
    # "HPK_50um_500x500um_2x2pad_E600_FNAL_160V": [47.93, 16.70, 75.57, 592.30, 1.86, 14.84],
    # "HPK_30um_500x500um_2x2pad_E600_FNAL_144V": [33.51, 8.21, 124.30, 405.92, 1.88, -7.83],
    # "HPK_30um_500x500um_2x2pad_E600_FNAL_140V": [23.29, 7.36, 99.17, 395.06, 1.84, 16.61],
    # "HPK_30um_500x500um_2x2pad_E600_FNAL_135V": [25.49, 11.51, 79.04, 398.11, 1.84, 10.99],
    # "HPK_30um_500x500um_2x2pad_E600_FNAL_130V": [27.29, 12.51, 64.93, 400.59, 1.84, 8.31],
    # "HPK_30um_500x500um_2x2pad_E600_FNAL_120V": [31.40, 15.62, 45.15, 412.12, 1.84, 5.61],
    # "HPK_30um_500x500um_2x2pad_E600_FNAL_110V": [35.92, 18.29, 32.45, 431.87, 1.84, 4.06],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_110V": [30.62, 9.20, 99.81, 383.23, 1.88, 49.75],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_108V": [22.46, 10.36, 74.39, 363.51, 1.85, 14.42],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_105V": [20.58, 10.15, 57.73, 352.36, 1.84, 7.95],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_100V": [23.51, 13.69, 40.57, 360.31, 1.84, 4.62],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_95V": [25.26, 15.97, 30.03, 369.59, 1.84, 3.34],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_90V": [28.93, 19.72, 23.09, 383.27, 1.84, 2.66],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_85V": [32.79, 26.82, 19.53, 399.14, 1.85, 2.35],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_75V": [42.80, 35.88, 16.13, 428.53, 1.84, 2.03],

    # # Use the ampMax values from here: which is from new definition of hitOnMetal and LanGauss fit
    # # Metal region
    # "HPK_50um_500x500um_2x2pad_E600_FNAL_190V": [35.44, 10.31, 152.65, 569.97, 1.89, -4.04],
    # "HPK_50um_500x500um_2x2pad_E600_FNAL_185V": [34.49, 11.91, 131.68, 567.62, 1.85, 27.96],
    # "HPK_50um_500x500um_2x2pad_E600_FNAL_180V": [36.65, 13.15, 117.19, 569.22, 1.86, 23.13],
    # "HPK_50um_500x500um_2x2pad_E600_FNAL_170V": [40.70, 15.24, 94.15, 578.22, 1.85, 17.91],
    # "HPK_50um_500x500um_2x2pad_E600_FNAL_160V": [44.53, 17.16, 76.77, 592.72, 1.86, 14.65],
    # "HPK_30um_500x500um_2x2pad_E600_FNAL_144V": [32.70, 8.06, 125.76, 402.77, 1.88, -19287748567.46],
    # "HPK_30um_500x500um_2x2pad_E600_FNAL_140V": [25.33, 10.14, 100.19, 395.26, 1.84, 17.21],
    # "HPK_30um_500x500um_2x2pad_E600_FNAL_135V": [26.03, 11.53, 80.65, 395.22, 1.84, 11.35],
    # "HPK_30um_500x500um_2x2pad_E600_FNAL_130V": [27.26, 12.66, 66.23, 397.35, 1.84, 8.72],
    # "HPK_30um_500x500um_2x2pad_E600_FNAL_120V": [31.24, 15.17, 46.31, 409.66, 1.84, 5.97],
    # "HPK_30um_500x500um_2x2pad_E600_FNAL_110V": [36.11, 18.89, 33.57, 430.02, 1.84, 4.34],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_110V": [41.78, 8.53, 103.00, 372.40, 1.88, -147.72],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_108V": [23.05, 10.41, 75.61, 356.63, 1.85, 14.94],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_105V": [22.34, 11.43, 58.73, 352.04, 1.84, 8.28],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_100V": [24.27, 13.61, 41.70, 356.42, 1.84, 5.03],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_95V": [26.85, 16.38, 31.11, 367.54, 1.84, 3.54],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_90V": [30.14, 20.54, 23.88, 382.48, 1.84, 2.84],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_85V": [33.98, 25.58, 19.54, 398.59, 1.84, 2.31],
    # "HPK_20um_500x500um_2x2pad_E600_FNAL_75V": [43.76, 32.31, 16.25, 427.96, 1.84, 1.23],
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
    info_dict["resistivityNumber"] = 0
    if info[6] == "E":
        info_dict["resistivityNumber"] = 1600
    elif info[6] == "C":
        info_dict["resistivityNumber"] = 400
    info_dict["capacitance"] = info[7] if info[7] != "Null" else 0
    info_dict["tag"] = info[0]

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
