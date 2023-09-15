
# 2023 Sensors
# ------------

# Geometry
# --------
# {<sensor name_long>, <sensor name_short/label>, <pitch [um]>, <width [um]>, <length [mm]>,
#  <Bias voltage [V]>, <thickness [um]>, <resistivity [Ohm/sq]>, <capacitance [pF/mm2]>}

geometry2023_short = {
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
    # "HPK_W8_17_2_50T_1P0_500P_50M_C600": ["HPK_W8_17_2_50T_50M_C600", 500, 50, 10.0, 206, 50, "C", 600],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": ["HPK_W8_17_2_50T_50M_C600", 500, 50, 10.0, 200, 50, "C", 600],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": ["HPK_W4_17_2_50T_1P0_500P_50M_C240", 500, 50, 10.0, 204, 50, "C", 240],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": ["HPK_W5_17_2_50T_1P0_500P_50M_E600", 500, 50, 10.0, 190, 50, "E", 600],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_188V": ["HPK_W5_17_2_50T_1P0_500P_50M_E600", 500, 50, 10.0, 188, 50 , "E", 600],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_186V": ["HPK_W5_17_2_50T_1P0_500P_50M_E600", 500, 50, 10.0, 186, 50, "E", 600],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_192V": ["HPK_W5_17_2_50T_1P0_500P_50M_E600", 500, 50, 10.0, 192, 50, "E", 600],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_194V": ["HPK_W5_17_2_50T_1P0_500P_50M_E600", 500, 50, 10.0, 194, 50, "E", 600],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": ["HPK_W2_3_2_50T_1P0_500P_50M_E240", 500, 50, 10.0, 180, 50, "E", 240],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": ["HPK_W9_15_2_20T_1P0_500P_50M_E600", 500, 50, 10.0, 114, 20, "E", 600],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": ["HPK_W9_14_2_20T_1P0_500P_100M_E600", 500, 100, 10.0, 112, 20, "E", 600],
    "HPK_KOJI_50T_1P0_80P_60M_E240": ["HPK_50T_1P0_80P_60M_E240", 80, 60, 10.0, 190, 50, "E", 240],
    "HPK_KOJI_20T_1P0_80P_60M_E240": ["HPK_20T_1P0_80P_60M_E240", 80, 60, 10.0, 112, 20, "E", 240],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": ["HPK_W9_15_4_20T_0P5_500P_50M_E600", 500, 50, 5.0, 110, 20, "E", 600],
}

sensorsGeom2023 = {}
for key, info in geometry2023_short.items():
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


# Resolutions and efficiency
# --------------------------
# NOTE: Resolution values does NOT have tracker component removed
# Overall: <one strip reco RMS [um]>, <two strip reco fit [um]>, <time [ps]>, <efficiency one strip>, <efficiency two strip>
resolutions2023_Overall = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2_170V": [],
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
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": [],
    # "HPK_W8_17_2_50T_1P0_500P_50M_C600": [],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": [],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": [],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_188V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_186V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_192V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_194V": [],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": [],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": [],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": [],
    "HPK_KOJI_50T_1P0_80P_60M_E240": [],
    "HPK_KOJI_20T_1P0_80P_60M_E240": [],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": [],
}

# Metal: <one strip reco RMS [um]>, <two strip reco fit [um]>, <time [ps]>, <efficiency one strip>, <efficiency two strip>
resolutions2023_Metal = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2_170V": [],
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
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": [],
    # "HPK_W8_17_2_50T_1P0_500P_50M_C600": [],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": [],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": [],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_188V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_186V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_192V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_194V": [],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": [],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": [],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": [],
    "HPK_KOJI_50T_1P0_80P_60M_E240": [],
    "HPK_KOJI_20T_1P0_80P_60M_E240": [],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": [],
}

# Gap: <one strip reco RMS [um]>, <two strip reco fit [um]>, <time [ps]>, <efficiency one strip>, <efficiency two strip>
resolutions2023_Gap = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2_170V": [],
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
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": [],
    # "HPK_W8_17_2_50T_1P0_500P_50M_C600": [],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": [],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": [],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_188V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_186V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_192V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_194V": [],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": [],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": [],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": [],
    "HPK_KOJI_50T_1P0_80P_60M_E240": [],
    "HPK_KOJI_20T_1P0_80P_60M_E240": [],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": [],
}

# Characterization
# ----------------
# Overall: <jitter [ps]>, <amp max [mV]>, <risetime [ps]>, <baseline_rms [mV]>, <charge [-]>
characteristics2023_Overall = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2_170V": [],
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
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": [],
    # "HPK_W8_17_2_50T_1P0_500P_50M_C600": [],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": [],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": [],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_188V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_186V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_192V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_194V": [],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": [],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": [],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": [],
    "HPK_KOJI_50T_1P0_80P_60M_E240": [],
    "HPK_KOJI_20T_1P0_80P_60M_E240": [],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": [],
}

# Metal: <jitter [ps]>, <amp max [mV]>, <risetime [ps]>, <baseline_rms [mV]>, <charge [-]>
characteristics2023_Metal = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2_170V": [],
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
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": [],
    # "HPK_W8_17_2_50T_1P0_500P_50M_C600": [],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": [],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": [],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_188V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_186V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_192V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_194V": [],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": [],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": [],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": [],
    "HPK_KOJI_50T_1P0_80P_60M_E240": [],
    "HPK_KOJI_20T_1P0_80P_60M_E240": [],
    "HPK_W9_15_4_20T_0P5_500P_50M_E600": [],
}

# Gap: <jitter [ps]>, <amp max [mV]>, <risetime [ps]>, <baseline_rms [mV]>, <charge [-]>
characteristics2023_Gap = {
    # BNL strips
    "BNL_50um_1cm_450um_W3051_2_2_170V": [],
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
    "HPK_W8_18_2_50T_1P0_500P_100M_C600": [],
    # "HPK_W8_17_2_50T_1P0_500P_50M_C600": [],
    "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": [],
    "HPK_W4_17_2_50T_1P0_500P_50M_C240": [],
    "HPK_W5_17_2_50T_1P0_500P_50M_E600": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_188V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_186V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_192V": [],
    # "HPK_W5_17_2_50T_1P0_500P_50M_E600_194V": [],
    "HPK_W2_3_2_50T_1P0_500P_50M_E240": [],
    "HPK_W9_15_2_20T_1P0_500P_50M_E600": [],
    "HPK_W9_14_2_20T_1P0_500P_100M_E600": [],
    "HPK_KOJI_50T_1P0_80P_60M_E240": [],
    "HPK_KOJI_20T_1P0_80P_60M_E240": [],
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
        info_dict["position_oneStrip%s"%reg], info_dict["position_oneStripRMS%s"%reg] = res[0], res[0]
        info_dict["res_one_strip%s"%reg] = res[0]
        info_dict["position_twoStrip%s"%reg], info_dict["res_two_strip%s"%reg] = res[1], res[1]
        info_dict["time_resolution%s"%reg], info_dict["res_time%s"%reg] = res[2], res[2]
        info_dict["efficiency_oneStrip%s"%reg], info_dict["efficiency_one_strip%s"%reg] = res[3], res[3]
        info_dict["efficiency_twoStrip%s"%reg], info_dict["efficiency_two_strip%s"%reg] = res[4], res[4]

        char = list_char[i]
        info_dict["jitter%s"%reg] = char[0]
        info_dict["amp_max%s"%reg] = char[1]
        info_dict["rise_time%s"%reg] = char[2]
        info_dict["baseline_rms%s"%reg] = char[3]
        info_dict["charge%s"%reg] = char[4]

    resolutions2023[sensor] = info_dict


# # NOTE: Resolution values does NOT have tracker component removed
# # 'position_oneStrip': Std Dev from fit, 'position_oneStrip_E': Statistical error from fit, 'position_oneStripRMS': RMS WITH OnMetal cut,
# # 'position_oneStrip_StdDev': RMS WITHOUT OnMetal cut (This is the value used in the paper)
# resolutions2023 = {
#     "BNL_50um_1cm_450um_W3051_2_2_170V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 
#                                           'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                           'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                           'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                           "time_resolution": 0.0, "time_resolution_E": 0.0,
#                                           "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
#                                           "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
#                                           "jitter": 0.0,
#                                           "jitter_m": 0.0,
#                                           "jitter_g": 0.0,
#                                           "amp_max":0.0 , "max_amp_E": 0.0,
#                                           "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
#                                           "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
#                                           "rise_time": 0.0, "rise_time_E": 0.0,
#                                           "rise_time_m": 0.0, "rise_time_n_E": 0.0,
#                                           "rise_time_g": 0.0, "rise_time_g_E": 0.0,
#                                           "baseline_rms": 0.0 , "baseline_rms": 0.0,
#                                           "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
#                                           "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
#                                           "charge": 0.0, "charge_E":0.0,
#                                           "charge_m": 0.0, "charge_m_E":0.0,
#                                           "charge_g": 0.0, "charge_g_E":0.0,
#                                         },

#     "BNL_50um_1cm_400um_W3051_1_4_160V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
#                                           'position_oneStripRMS': 0.00,'position_oneStrip_StdDev': 0.00,
#                                           'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                           'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                           "time_resolution": 0.0, "time_resolution_E": 0.0,
#                                           "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
#                                           "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
#                                           "jitter": 0.0,
#                                           "jitter_m": 0.0,
#                                           "jitter_g": 0.0,
#                                           "amp_max": 0.0 , "max_amp_E": 0.0,
#                                           "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
#                                           "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
#                                           "rise_time": 0.0, "rise_time_E": 0.0,
#                                           "rise_time_m": 0.0, "rise_time_n_E": 0.0,
#                                           "rise_time_g": 0.0, "rise_time_g_E": 0.0,
#                                           "baseline_rms": 0.0 , "baseline_rms": 0.0,
#                                           "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
#                                           "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
#                                           "charge": 0.0, "charge_E":0.0,
#                                           "charge_m": 0.0, "charge_m_E":0.0,
#                                           "charge_g": 0.0, "charge_g_E":0.0,
#                                         },

#     "BNL_50um_1cm_450um_W3052_2_4_185V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 
#                                           'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                           'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                           'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                           "time_resolution": 0.0, "time_resolution_E": 0.0,
#                                           "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
#                                           "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
#                                           "jitter": 0.0,
#                                           "jitter_m": 0.0,
#                                           "jitter_g": 0.0,
#                                           "amp_max": 0.0 , "max_amp_E": 0.0,
#                                           "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
#                                           "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
#                                           "rise_time": 0.0, "rise_time_E": 0.0,
#                                           "rise_time_m": 0.0, "rise_time_n_E": 0.0,
#                                           "rise_time_g": 0.0, "rise_time_g_E": 0.0,
#                                           "baseline_rms": 0.0 , "baseline_rms": 0.0,
#                                           "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
#                                           "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
#                                           "charge": 0.0, "charge_E":0.0,
#                                           "charge_m": 0.0, "charge_m_E":0.0,
#                                           "charge_g": 0.0, "charge_g_E":0.0,
#                                         },

#     "BNL_20um_1cm_400um_W3074_1_4_95V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
#                                          'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                          'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                          'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                          "time_resolution": 0.0, "time_resolution_E": 0.0,
#                                          "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
#                                          "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
#                                          "jitter": 0.0,
#                                          "jitter_m": 0.0,
#                                          "jitter_g": 0.0,
#                                          "amp_max": 0.0 , "max_amp_E": 0.0,
#                                          "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
#                                          "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
#                                          "rise_time": 0.0, "rise_time_E": 0.0,
#                                          "rise_time_m": 0.0, "rise_time_n_E": 0.0,
#                                          "rise_time_g": 0.0, "rise_time_g_E": 0.0,
#                                          "baseline_rms": 0.0 , "baseline_rms": 0.0,
#                                          "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
#                                          "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
#                                          "charge": 0.0, "charge_E":0.0,
#                                          "charge_m": 0.0, "charge_m_E":0.0,
#                                          "charge_g": 0.0, "charge_g_E":0.0,
#                                         },

#     "BNL_20um_1cm_400um_W3075_1_2_80V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
#                                          'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                          'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                          'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                          "time_resolution": 0.0, "time_resolution_E": 0.0,
#                                          "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
#                                          "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
#                                          "jitter": 0.0,
#                                          "jitter_m": 0.0,
#                                          "jitter_g": 0.0,
#                                          "amp_max": 0.0 , "max_amp_E": 0.0,
#                                          "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
#                                          "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
#                                          "rise_time": 0.0, "rise_time_E": 0.0,
#                                          "rise_time_m": 0.0, "rise_time_n_E": 0.0,
#                                          "rise_time_g": 0.0, "rise_time_g_E": 0.0,
#                                          "baseline_rms": 0.0 , "baseline_rms": 0.0,
#                                          "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
#                                          "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
#                                          "charge": 0.0, "charge_E":0.0,
#                                          "charge_m": 0.0, "charge_m_E":0.0,
#                                          "charge_g": 0.0, "charge_g_E":0.0,
#                                         },

#     "BNL_20um_1cm_450um_W3074_2_1_95V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 
#                                          'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                          'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                          'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                          "time_resolution": 0.0, "time_resolution_E": 0.0,
#                                          "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
#                                          "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
#                                          "jitter": 0.0,
#                                          "jitter_m": 0.0,
#                                          "jitter_g": 0.0,
#                                          "amp_max": 0.0 , "max_amp_E": 0.0,
#                                          "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
#                                          "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
#                                          "rise_time": 0.0, "rise_time_E": 0.0,
#                                          "rise_time_m": 0.0, "rise_time_n_E": 0.0,
#                                          "rise_time_g": 0.0, "rise_time_g_E": 0.0,
#                                          "baseline_rms": 0.0 , "baseline_rms": 0.0,
#                                          "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
#                                          "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
#                                          "charge": 0.0, "charge_E":0.0,
#                                          "charge_m": 0.0, "charge_m_E":0.0,
#                                          "charge_g": 0.0, "charge_g_E":0.0,
#                                         },

#     "BNL_20um_1cm_450um_W3075_2_4_80V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 
#                                          'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                          'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                          'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                          "time_resolution": 0.0, "time_resolution_E": 0.0,
#                                          "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
#                                          "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
#                                          "jitter": 0.0,
#                                          "jitter_m": 0.0,
#                                          "jitter_g": 0.0,
#                                          "amp_max": 0.0 , "max_amp_E": 0.0,
#                                          "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
#                                          "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
#                                          "rise_time": 0.0, "rise_time_E": 0.0,
#                                          "rise_time_m": 0.0, "rise_time_n_E": 0.0,
#                                          "rise_time_g": 0.0, "rise_time_g_E": 0.0,
#                                          "baseline_rms": 0.0 , "baseline_rms": 0.0,
#                                          "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
#                                          "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
#                                          "charge": 0.0, "charge_E":0.0,
#                                          "charge_m": 0.0, "charge_m_E":0.0,
#                                          "charge_g": 0.0, "charge_g_E":0.0,
#                                         },

#     "BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 
#                                                  'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                                  'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                                  'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                                  "time_resolution": 0.0, "time_resolution_E": 0.0,
#                                                  "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
#                                                  "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
#                                                  "jitter": 0.0,
#                                                  "jitter_m": 0.0,
#                                                  "jitter_g": 0.0,
#                                                  "amp_max": 0.0 , "max_amp_E": 0.0,
#                                                  "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
#                                                  "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
#                                                  "rise_time": 0.0, "rise_time_E": 0.0,
#                                                  "rise_time_m": 0.0, "rise_time_n_E": 0.0,
#                                                  "rise_time_g": 0.0, "rise_time_g_E": 0.0,
#                                                  "baseline_rms": 0.0 , "baseline_rms": 0.0,
#                                                  "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
#                                                  "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
#                                                  "charge": 0.0, "charge_E":0.0,
#                                                  "charge_m": 0.0, "charge_m_E":0.0,
#                                                  "charge_g": 0.0, "charge_g_E":0.0,
#                                                 },

#     "BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
#                                                  'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                                  'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                                  'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                                  "time_resolution": 0.0, "time_resolution_E": 0.0,
#                                                  "time_resolution_m": 0.0, "time_resolution_m_E": 0.0,
#                                                  "time_resolution_g": 0.0, "time_resolution_g_E": 0.0,
#                                                  "jitter": 0.0,
#                                                  "jitter_m": 0.0,
#                                                  "jitter_g": 0.0,
#                                                  "amp_max": 0.0 , "max_amp_E": 0.0,
#                                                  "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
#                                                  "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
#                                                  "rise_time": 0.0, "rise_time_E": 0.0,
#                                                  "rise_time_m": 0.0, "rise_time_n_E": 0.0,
#                                                  "rise_time_g": 0.0, "rise_time_g_E": 0.0,
#                                                  "baseline_rms": 0.0 , "baseline_rms": 0.0,
#                                                  "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
#                                                  "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
#                                                  "charge": 0.0, "charge_E":0.0,
#                                                  "charge_m": 0.0, "charge_m_E":0.0,
#                                                  "charge_g": 0.0, "charge_g_E":0.0,
#                                                 },

#     "HPK_20um_500x500um_2x2pad_E600_FNAL_105V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
#                                                  'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                                  'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                                  'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                                  "time_resolution": 24.09, "time_resolution_E": 0.0,
#                                                  "time_resolution_m": 23.53, "time_resolution_m_E": 0.0,
#                                                  "time_resolution_g": 30.50, "time_resolution_g_E": 0.0,
#                                                  "jitter": 0.0,
#                                                  "jitter_m": 0.0,
#                                                  "jitter_g": 0.0,
#                                                  "amp_max": 0.0 , "max_amp_E": 0.0,
#                                                  "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
#                                                  "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
#                                                  "rise_time": 0.0, "rise_time_E": 0.0,
#                                                  "rise_time_m": 0.0, "rise_time_n_E": 0.0,
#                                                  "rise_time_g": 0.0, "rise_time_g_E": 0.0,
#                                                  "baseline_rms": 0.0 , "baseline_rms": 0.0,
#                                                  "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
#                                                  "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
#                                                  "charge": 0.0, "charge_E":0.0,
#                                                  "charge_m": 0.0, "charge_m_E":0.0,
#                                                  "charge_g": 0.0, "charge_g_E":0.0,
#                                                 },

#     "HPK_30um_500x500um_2x2pad_E600_FNAL_140V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
#                                                  'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                                  'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                                  'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                                  "time_resolution": 28.31, "time_resolution_E": 0.0,
#                                                  "time_resolution_m": 26.83, "time_resolution_m_E": 0.0,
#                                                  "time_resolution_g": 39.26, "time_resolution_g_E": 0.0,
#                                                  "jitter": 0.0,
#                                                  "jitter_m": 0.0,
#                                                  "jitter_g": 0.0,
#                                                  "amp_max": 0.0 , "max_amp_E": 0.0,
#                                                  "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
#                                                  "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
#                                                  "rise_time": 0.0, "rise_time_E": 0.0,
#                                                  "rise_time_m": 0.0, "rise_time_n_E": 0.0,
#                                                  "rise_time_g": 0.0, "rise_time_g_E": 0.0,
#                                                  "baseline_rms": 0.0 , "baseline_rms": 0.0,
#                                                  "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
#                                                  "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
#                                                  "charge": 0.0, "charge_E":0.0,
#                                                  "charge_m": 0.0, "charge_m_E":0.0,
#                                                  "charge_g": 0.0, "charge_g_E":0.0,
#                                                 },

#     "HPK_50um_500x500um_2x2pad_E600_FNAL_190V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
#                                                  'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                                  'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                                  'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                                  "time_resolution": 40.80, "time_resolution_E": 0.0,
#                                                  "time_resolution_m": 38.99, "time_resolution_m_E": 0.0,
#                                                  "time_resolution_g": 53.14, "time_resolution_g_E": 0.0,
#                                                  "jitter": 0.0,
#                                                  "jitter_m": 0.0,
#                                                  "jitter_g": 0.0,
#                                                  "amp_max": 0.0 , "max_amp_E": 0.0,
#                                                  "amp_max_m": 0.0 , "max_amp_m_E": 0.0,
#                                                  "amp_max_g": 0.0 , "max_amp_g_E": 0.0,
#                                                  "rise_time": 0.0, "rise_time_E": 0.0,
#                                                  "rise_time_m": 0.0, "rise_time_n_E": 0.0,
#                                                  "rise_time_g": 0.0, "rise_time_g_E": 0.0,
#                                                  "baseline_rms": 0.0 , "baseline_rms": 0.0,
#                                                  "baseline_rms_m": 0.0 , "baseline_rms_m": 0.0,
#                                                  "baseline_rms_g": 0.0 , "baseline_rms_g": 0.0,
#                                                  "charge": 0.0, "charge_E":0.0,
#                                                  "charge_m": 0.0, "charge_m_E":0.0,
#                                                  "charge_g": 0.0, "charge_g_E":0.0,
#                                                 },


#     "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
#                                                 'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                                 'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                                 'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                                 "time_resolution": 41.22, "time_resolution_E": 0.0,
#                                                 "time_resolution_m": 40.27, "time_resolution_m_E": 0.0,
#                                                 "time_resolution_g": 42.82, "time_resolution_g_E": 0.0,
#                                                 "jitter": 38.36,
#                                                 "jitter_m": 36.58,
#                                                 "jitter_g": 38.81,
#                                                 "amp_max": 57.88 , "max_amp_E": 0.0,
#                                                 "amp_max_m": 66.12 , "max_amp_m_E": 0.0,
#                                                 "amp_max_g": 49.67 , "max_amp_g_E": 0.0,
#                                                 "rise_time": 628.99, "rise_time_E": 0.0,
#                                                 "rise_time_m": 614.6, "rise_time_n_E": 0.0,
#                                                 "rise_time_g": 652.93, "rise_time_g_E": 0.0,
#                                                 "baseline_rms": 1.9 , "baseline_rms_E": 0.0,
#                                                 "baseline_rms_m": 1.89 , "baseline_rms_m_E": 0.0,
#                                                 "baseline_rms_g": 1.9 , "baseline_rms_g_E": 0.0,
#                                                 "charge": 30.68, "charge_E":0.0,
#                                                 "charge_m": 34.60, "charge_m_E":0.0,
#                                                 "charge_g": 26.92, "charge_g_E":0.0,
#                                                 },


#     "HPK_W8_17_2_50T_1P0_500P_50M_C600_206V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 'position_oneStripRMS': 0.00,
#                                                'position_oneStrip_StdDev': 0.00,
#                                                'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                                'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                                "time_resolution": 38.86, "time_resolution_E": 0.0,
#                                                "time_resolution_m": 37.36, "time_resolution_m_E": 0.0,
#                                                "time_resolution_g": 39.87, "time_resolution_g_E": 0.0,
#                                                "jitter": 38.11,
#                                                "jitter_m": 36.62,
#                                                "jitter_g": 38.28,
#                                                "amp_max": 49.94 , "max_amp_E": 0.0,
#                                                "amp_max_m": 57.86 , "max_amp_m_E": 0.0,
#                                                "amp_max_g": 42.48 , "max_amp_g_E": 0.0,
#                                                "rise_time": 619.22, "rise_time_E": 0.0,
#                                                "rise_time_m": 603.51, "rise_time_n_E": 0.0,
#                                                "rise_time_g": 643.64, "rise_time_g_E": 0.0,
#                                                "baseline_rms": 1.7 , "baseline_rms_E": 0.0,
#                                                "baseline_rms_m": 1.69 , "baseline_rms_m_E": 0.0,
#                                                "baseline_rms_g": 1.7 , "baseline_rms_g_E": 0.0,
#                                                "charge": 11.57, "charge_E":0.0,
#                                                "charge_m": 13.14, "charge_m_E":0.0,
#                                                "charge_g": 10.5, "charge_g_E":0.0,
#                                                },

#     # "HPK_W8_17_2_50T_1P0_500P_50M_C600":,
#     # "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V":,
#     "HPK_W4_17_2_50T_1P0_500P_50M_C240_204V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
#                                                'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                                'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                                'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                                "time_resolution": 36.01, "time_resolution_E": 0.0,
#                                                "time_resolution_m": 34.94, "time_resolution_m_E": 0.0,
#                                                "time_resolution_g": 36.94, "time_resolution_g_E": 0.0,
#                                                "jitter": 34.26,
#                                                "jitter_m": 33.26,
#                                                "jitter_g": 34.37,
#                                                "amp_max": 57.49 , "max_amp_E": 0.0,
#                                                "amp_max_m": 66.26 , "max_amp_m_E": 0.0,
#                                                "amp_max_g": 49.31 , "max_amp_g_E": 0.0,
#                                                "rise_time": 625.48, "rise_time_E": 0.0,
#                                                "rise_time_m": 611.92, "rise_time_n_E": 0.0,
#                                                "rise_time_g": 644.22, "rise_time_g_E": 0.0,
#                                                "baseline_rms": 1.77 , "baseline_rms_E": 0.0,
#                                                "baseline_rms_m": 1.77 , "baseline_rms_m_E": 0.0,
#                                                "baseline_rms_g": 1.76 , "baseline_rms_g_E": 0.0,
#                                                "charge": 15.83, "charge_E":0.0,
#                                                "charge_m": 17.60, "charge_m_E":0.0,
#                                                "charge_g": 14.24, "charge_g_E":0.0,
#                                                },
    
#     "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
#                                                'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                                'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                                'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                                "time_resolution": 34.54, "time_resolution_E": 0.0,
#                                                "time_resolution_m": 32.17, "time_resolution_m_E": 0.0,
#                                                "time_resolution_g": 35.04, "time_resolution_g_E": 0.0,
#                                                "jitter": 25.11,
#                                                "jitter_m": 20.39,
#                                                "jitter_g": 24.76,
#                                                "amp_max": 99.99 , "max_amp_E": 0.0,
#                                                "amp_max_m": 128.58 , "max_amp_m_E": 0.0,
#                                                "amp_max_g": 74.06 , "max_amp_g_E": 0.0,
#                                                "rise_time": 650.37, "rise_time_E": 0.0,
#                                                "rise_time_m": 621.87, "rise_time_n_E": 0.0,
#                                                "rise_time_g": 685.18, "rise_time_g_E": 0.0,
#                                                "baseline_rms": 1.94 , "baseline_rms_E": 0.0,
#                                                "baseline_rms_m": 1.94 , "baseline_rms_m_E": 0.0,
#                                                "baseline_rms_g": 1.93 , "baseline_rms_g_E": 0.0,
#                                                "charge": 34.82, "charge_E":0.0,
#                                                "charge_m": 42.31, "charge_m_E":0.0,
#                                                "charge_g": 27.72, "charge_g_E":0.0,
#                                                },
#     # "HPK_W5_17_2_50T_1P0_500P_50M_E600":,
#     # "HPK_W5_17_2_50T_1P0_500P_50M_E600_188V":,
#     # "HPK_W5_17_2_50T_1P0_500P_50M_E600_186V":,
#     # "HPK_W5_17_2_50T_1P0_500P_50M_E600_192V":,
#     # "HPK_W5_17_2_50T_1P0_500P_50M_E600_194V":,
#     "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 'position_oneStripRMS': 0.00,
#                                                'position_oneStrip_StdDev': 0.00,
#                                                'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                                'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                                "time_resolution": 53.52, "time_resolution_E": 0.0,
#                                                "time_resolution_m": 29.49, "time_resolution_m_E": 0.0,
#                                                "time_resolution_g": 87.00, "time_resolution_g_E": 0.0,
#                                                "jitter": 52.75,
#                                                "jitter_m": 22.12,
#                                                "jitter_g": 68.39,
#                                                "amp_max": 34.23 , "max_amp_E": 0.0,
#                                                "amp_max_m": 50.25 , "max_amp_m_E": 0.0,
#                                                "amp_max_g": 23.76 , "max_amp_g_E": 0.0,
#                                                "rise_time": 561.01, "rise_time_E": 0.0,
#                                                "rise_time_m": 418.81, "rise_time_n_E": 0.0,
#                                                "rise_time_g": 578.16, "rise_time_g_E": 0.0,
#                                                "baseline_rms": 1.77 , "baseline_rms_E": 0.0,
#                                                "baseline_rms_m": 1.77 , "baseline_rms_m_E": 0.0,
#                                                "baseline_rms_g": 1.77 , "baseline_rms_g_E": 0.0,
#                                                "charge": 15.71, "charge_E":0.0,
#                                                "charge_m": 19.24, "charge_m_E":0.0,
#                                                "charge_g": 12.37, "charge_g_E":0.0,
#                                                },

#     "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 
#                                               'position_oneStripRMS': 0.00,
#                                               'position_oneStrip_StdDev': 0.00,
#                                               'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                               'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                               "time_resolution": 34.37, "time_resolution_E": 0.0,
#                                               "time_resolution_m": 31.94, "time_resolution_m_E": 0.0,
#                                               "time_resolution_g": 34.86, "time_resolution_g_E": 0.0,
#                                               "jitter": 25.47,
#                                               "jitter_m": 21.38,
#                                               "jitter_g": 26.82,
#                                               "amp_max": 92.08, "max_amp_E": 0.0,
#                                               "amp_max_m": 117.72, "max_amp_m_E": 0.0,
#                                               "amp_max_g": 68.98, "max_amp_g_E": 0.0,
#                                               "rise_time": 651.77, "rise_time_E": 0.0,
#                                               "rise_time_m": 625.00, "rise_time_n_E": 0.0,
#                                               "rise_time_g": 683.51, "rise_time_g_E": 0.0,
#                                               "baseline_rms": 1.85 , "baseline_rms_E": 0.0,
#                                               "baseline_rms_m": 1.85 , "baseline_rms_m_E": 0.0,
#                                               "baseline_rms_g": 1.85 , "baseline_rms_g_E": 0.0,
#                                               "charge": 22.12, "charge_E":0.0,
#                                               "charge_m": 26.48, "charge_m_E":0.0,
#                                               "charge_g": 17.87, "charge_g_E":0.0,
#                                               },

#     "HPK_W9_14_2_20T_1P0_500P_100M_E600_112V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00, 
#                                                 'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                                 'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                                 'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                                 "time_resolution": 47.15, "time_resolution_E": 0.0,
#                                                 "time_resolution_m": 30.44, "time_resolution_m_E": 0.0,
#                                                 "time_resolution_g": 53.0, "time_resolution_g_E": 0.0,
#                                                 "jitter": 48.53,
#                                                 "jitter_m": 26.44,
#                                                 "jitter_g": 76.63,
#                                                 "amp_max": 32.19, "max_amp_E": 0.0,
#                                                 "amp_max_m": 43.52, "max_amp_m_E": 0.0,
#                                                 "amp_max_g": 22.60, "max_amp_g_E": 0.0,
#                                                 "rise_time": 525.42, "rise_time_E": 0.0,
#                                                 "rise_time_m": 428.26, "rise_time_n_E": 0.0,
#                                                 "rise_time_g": 693.34, "rise_time_g_E": 0.0,
#                                                 "baseline_rms": 1.8 , "baseline_rms_E": 0.0,
#                                                 "baseline_rms_m": 1.8 , "baseline_rms_m_E": 0.0,
#                                                 "baseline_rms_g": 1.8 , "baseline_rms_g_E": 0.0,
#                                                 "charge": 11.13, "charge_E":0.0,
#                                                 "charge_m": 13.31, "charge_m_E":0.0,
#                                                 "charge_g": 8.67, "charge_g_E":0.0,
#                                                 },

#     "HPK_KOJI_50T_1P0_80P_60M_E240_190V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
#                                            'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                            'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                            'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                            "time_resolution": 31.41, "time_resolution_E": 0.0,
#                                            "time_resolution_m":31.39 , "time_resolution_m_E": 0.0,
#                                            "time_resolution_g": 31.47, "time_resolution_g_E": 0.0,
#                                            "jitter": 23.19,
#                                            "jitter_m": 23.16,
#                                            "jitter_g": 21.37,
#                                            "amp_max": 72.97, "max_amp_E": 0.0,
#                                            "amp_max_m": 74.35, "max_amp_m_E": 0.0,
#                                            "amp_max_g": 68.32, "max_amp_g_E": 0.0,
#                                            "rise_time": 574.5, "rise_time_E": 0.0,
#                                            "rise_time_m": 573.29, "rise_time_n_E": 0.0,
#                                            "rise_time_g": 578.81, "rise_time_g_E": 0.0,
#                                            "baseline_rms": 1.83 , "baseline_rms_E": 0.0,
#                                            "baseline_rms_m": 1.83 , "baseline_rms_m_E": 0.0,
#                                            "baseline_rms_g": 1.82 , "baseline_rms_g_E": 0.0,
#                                            "charge": 16.93, "charge_E":0.0,
#                                            "charge_m": 17.19, "charge_m_E":0.0,
#                                            "charge_g": 16.01, "charge_g_E":0.0,
#                                            },

#     "HPK_KOJI_20T_1P0_80P_60M_E240_112V": {'position_oneStrip'  : 0.00, 'position_oneStrip_E': 0.00,
#                                            'position_oneStripRMS': 0.00, 'position_oneStrip_StdDev': 0.00,
#                                            'position_twoStrip'  : 0.00, 'position_twoStrip_E': 0.00,
#                                            'efficiency_oneStrip': 0.00, 'efficiency_twoStrip' : 0.00,
#                                            "time_resolution": 29.91, "time_resolution_E": 0.0,
#                                            "time_resolution_m": 29.9, "time_resolution_m_E": 0.0,
#                                            "time_resolution_g": 29.55, "time_resolution_g_E": 0.0,
#                                            "jitter": 32.0,
#                                            "jitter_m": 31.84,
#                                            "jitter_g": 32.45,
#                                            "amp_max": 38.44, "max_amp_E": 0.0,
#                                            "amp_max_m": 39.1, "max_amp_m_E": 0.0,
#                                            "amp_max_g": 35.13, "max_amp_g_E": 0.0,
#                                            "rise_time": 419.34, "rise_time_E": 0.0,
#                                            "rise_time_m": 415.8, "rise_time_n_E": 0.0,
#                                            "rise_time_g": 430.75, "rise_time_g_E": 0.0,
#                                            "baseline_rms": 1.76 , "baseline_rms_E": 0.0,
#                                            "baseline_rms_m": 1.76 , "baseline_rms_m_E": 0.0,
#                                            "baseline_rms_g": 1.76 , "baseline_rms_g_E": 0.0,
#                                            "charge": 11.82, "charge_E":0.0,
#                                            "charge_m": 12.04, "charge_m_E":0.0,
#                                            "charge_g": 10.97, "charge_g_E":0.0,
#                                            },
# }

resolutions2023OneStripChannel = {
"BNL_50um_1cm_450um_W3051_2_2_170V": {  'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                        'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_50um_1cm_400um_W3051_1_4_160V": {  'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                        'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_50um_1cm_450um_W3052_2_4_185V": {  'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                        'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_20um_1cm_400um_W3074_1_4_95V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                        'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_20um_1cm_400um_W3075_1_2_80V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                        'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_20um_1cm_450um_W3074_2_1_95V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                        'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_20um_1cm_450um_W3075_2_4_80V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                        'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                                'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                                'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_20um_500x500um_2x2pad_E600_FNAL_105V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                                'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_30um_500x500um_2x2pad_E600_FNAL_140V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                                'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_50um_500x500um_2x2pad_E600_FNAL_190V": {   'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                                'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit

"HPK_W8_18_2_50T_1P0_500P_100M_C600_208V": {'resOneStrip': [-1.00, 43.5, 44.3, 38.1, 40.6, 35.1, -1.00],  ## Std Dev
                                       'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": {'resOneStrip': [-1.00, 23.3, 25.0, 26.0, 26.2, 24.8, -1.00],  ## Std Dev
                                       'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_W4_17_2_50T_1P0_500P_50M_C240_204V": {'resOneStrip': [-1.00, 25.8, 25.9, 26.8, 24.7, 25.9, -1.00],  ## Std Dev
                                      'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_W5_17_2_50T_1P0_500P_50M_E600_190V": {'resOneStrip': [-1.00, 18.7, 19.2, 21.4, 21.6, 20.2, -1.00],  ## Std Dev
                                      'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_W9_15_2_20T_1P0_500P_50M_E600_114V": {'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                      'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_W2_3_2_50T_1P0_500P_50M_E240_180V": {'resOneStrip': [-1.00, 16.7, 15.4, 16.3, 16.3, 15.3, -1.00],  ## Std Dev
                                          'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_W9_14_2_20T_1P0_500P_100M_E600_112V": {'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                       'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_W9_15_4_20T_0P5_500P_50M_E600_110V": {'resOneStrip': [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],  ## Std Dev
                                       'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_KOJI_50T_1P0_80P_60M_E240_190V": {'resOneStrip': [-1.00, 10.2, 10.3, 10.2, 10.3, 10.6, -1.00],  ## Std Dev
                                  'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
"HPK_KOJI_20T_1P0_80P_60M_E240_112V": {'resOneStrip': [-1.00, 14.4, 11.8, 11.8, 12.2, 15.1, -1.00],  ## Std Dev
                                  'errOneStrip': [ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00]}, ## Sigma fit
}



