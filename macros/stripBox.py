import ROOT

def getStripBox(f, ymin=0.0, ymax=100.0, getCenter=False, color=18, strips=True, shift=0.0):
    
    if strips == True :
        boxesInfo = []
        boxesInfo.append(f.Get("stripBoxInfo00"))
        boxesInfo.append(f.Get("stripBoxInfo01"))
        boxesInfo.append(f.Get("stripBoxInfo02"))
        boxesInfo.append(f.Get("stripBoxInfo03"))
        boxesInfo.append(f.Get("stripBoxInfo04"))
        boxesInfo.append(f.Get("stripBoxInfo05"))
        if (f.Get("stripBoxInfo06")): boxesInfo.append(f.Get("stripBoxInfo06"))
    else :
        boxesInfo = []
        boxesInfo.append(f.Get("stripBoxInfo00"))
        boxesInfo.append(f.Get("stripBoxInfo01"))
        
    widthPercent = 0.001 if getCenter else 0.5

    boxes = []
    for box in boxesInfo:
        xCenter = box.GetMean(1) - shift
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
