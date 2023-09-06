import ROOT

# Get list of all pairs of indices saved in histograms
# with name <prename> in <inputfile>
def get_existing_indices(inputfile, prename):
    list_indices = []
    # Loop over all possible names and save only those existing!
    for i in range(8):
        for j in range(8):
            channel = "%i%i"%(i, j)
            hname = "%s%s"%(prename, channel)
            hist = inputfile.Get(hname)
            if not hist:
                continue

            list_indices.append(channel)

    return list_indices

def get_central_channel_position(inputfile, direction="x"):
    # Get total number of channels used
    indices = get_existing_indices(inputfile, "stripBoxInfo")

    # Create a dictionary to get the number of columns (rows) associated with
    # each row (column). The later is chosen with the input <direction>.
    n_channels_paired_with = {}
    for i,j in indices:
        if direction is "x":
            key = i
        elif direction is "y":
            key = j
        else:
            print(" >> Choose a correct direction ('x' or 'y').")
            exit()

        if key not in n_channels_paired_with:
            n_channels_paired_with[key] = 0
        n_channels_paired_with[key]+= 1

    # Using the first column or row as reference
    n_subchannels = n_channels_paired_with["0"]
    for key in n_channels_paired_with:
        # TODO: Is this needed? Check
        if n_channels_paired_with[key] != n_subchannels:
            print(" >> Rows (columns) with different number of columns (rows).")
            print(n_channels_paired_with)
            exit()

    # Even number of columns
    if (n_subchannels%2 == 0):
        central_idx = round(n_subchannels/2)
        l_channel = inputfile.Get("stripBoxInfo0%i"%(central_idx-1)).GetMean(1)
        r_channel = inputfile.Get("stripBoxInfo0%i"%(central_idx)).GetMean(1)
        position_center = (l_channel + r_channel)/2
    # Odd number of columns
    else:
        central_idx =  round((n_subchannels-1)/2)
        position_center = (inputfile.Get("stripBoxInfo0%i"%central_idx)).GetMean(1)

    return position_center
