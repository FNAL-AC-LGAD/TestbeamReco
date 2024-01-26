import ROOT
from myFunctions import get_existing_indices

def getStripBox(f, ymin=0.0, ymax=100.0, getCenter=False, color=18,
                strips=True, shift=0.0, pitch=0.0, direction="x"):
    
    if (strips == True):
        stripBox = "stripBoxInfo" if (direction == "x") else "stripBoxInfoY"
        l_idx = get_existing_indices(f, stripBox)
        boxesInfo = []
        # NOTE: Pads use the first row position only
        for i in range(7):
            index = "0%i"%i if (direction == "x") else "%i0"%i
            if index not in l_idx:
                continue
            bname = stripBox + index
            if (f.Get(bname)):
                boxesInfo.append(f.Get(bname))
    else:
        boxesInfo = []
        boxesInfo.append(f.Get("stripBoxInfo00"))
        boxesInfo.append(f.Get("stripBoxInfo01"))
        print(" << WARNING >> Pads now follow the same treatment as strips.")
        
    widthPercent = 0.001 if getCenter else 0.5

    boxes = []
    for box in boxesInfo:
        if not box: 
            print("Warning: Issue getting stripBoxInfo")
            continue
        xCenter = box.GetMean(1) - shift
        # Use ideal position if pitch is given
        if pitch:
            position_ref = pitch if (len(boxesInfo)%2 == 1) else pitch/2
            xCenter = round(xCenter/position_ref) * position_ref
        width = box.GetMean(2)
        xmin = xCenter - (widthPercent*width)
        xmax = xCenter + (widthPercent*width)
        b = ROOT.TBox(xmin,ymin, xmax,ymax)
        b.SetFillColor(color)
        boxes.append(b)

    return boxes


def getStripBoxY(f, yampmin=0.0, yampmax=100.0, getCenter=False, color=18, shift=0.0):
    
    boxesInfo = []
    boxesInfo.append(f.Get("stripBoxInfoY00"))
    boxesInfo.append(f.Get("stripBoxInfoY10"))

    widthPercent = 0.001 if getCenter else 0.5

    boxes = []
    for box in boxesInfo:
        yCenter = box.GetMean(1) - shift
        width = box.GetMean(2)
        ymin = yCenter - (widthPercent*width)
        ymax = yCenter + (widthPercent*width)
        b = ROOT.TBox(ymin,yampmin, ymax,yampmax)
        b.SetFillColor(color)
        boxes.append(b)

    return boxes

def getStripBoxForRecoFit(stripWidth, pitch, ymax, xmax, xmin=0.5, color=18):
    boxes = []
    i=0
    while i<=ymax+stripWidth/2:
        yt = i+stripWidth/2
        yl = i-stripWidth/2
        if yt>ymax: yt=ymax
        if yl<0: yl=0.0
        box = ROOT.TBox(xmin,yl, xmax,yt)
        box.SetFillColor(color)
        boxes.append(box)
        i+=pitch

    return boxes
