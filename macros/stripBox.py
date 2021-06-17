import ROOT

def getStripBox(f, ymin=0.0, ymax=100.0):
    boxesInfo = []
    boxesInfo.append(f.Get("stripBoxInfo00"))
    boxesInfo.append(f.Get("stripBoxInfo01"))
    boxesInfo.append(f.Get("stripBoxInfo02"))
    boxesInfo.append(f.Get("stripBoxInfo03"))
    boxesInfo.append(f.Get("stripBoxInfo04"))
    boxesInfo.append(f.Get("stripBoxInfo05"))

    boxes = []
    for box in boxesInfo:
        xCenter = box.GetMean(1)
        width = box.GetMean(2)
        xmin = xCenter - (0.5*width)
        xmax = xCenter + (0.5*width)
        b = ROOT.TBox(xmin,ymin, xmax,ymax)
        #b.SetFillColor(ROOT.kGray);
        b.SetFillColor(18);
        boxes.append(b)
    return boxes

