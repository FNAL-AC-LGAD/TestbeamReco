import ROOT

def getStripBox(f, ymin=0.0, ymax=100.0, getCenter=False, color=18, strips=True):
    
    if strips == True :
        boxesInfo = []
        boxesInfo.append(f.Get("stripBoxInfo00"))
        boxesInfo.append(f.Get("stripBoxInfo01"))
        boxesInfo.append(f.Get("stripBoxInfo02"))
        boxesInfo.append(f.Get("stripBoxInfo03"))
        boxesInfo.append(f.Get("stripBoxInfo04"))
        boxesInfo.append(f.Get("stripBoxInfo05"))
    else :
        boxesInfo = []
        boxesInfo.append(f.Get("stripBoxInfo00"))
        boxesInfo.append(f.Get("stripBoxInfo01"))
        
    widthPercent = 0.001 if getCenter else 0.5

    boxes = []
    for box in boxesInfo:
        xCenter = box.GetMean(1)
        width = box.GetMean(2)
        xmin = xCenter - (widthPercent*width)
        xmax = xCenter + (widthPercent*width)
        b = ROOT.TBox(xmin,ymin, xmax,ymax)
        b.SetFillColor(color)
        boxes.append(b)

    return boxes


def getStripBoxY(f, yampmin=0.0, yampmax=100.0, getCenter=False, color=18):
    
    boxesInfo = []
    boxesInfo.append(f.Get("stripBoxInfoY00"))
    boxesInfo.append(f.Get("stripBoxInfoY10"))

    widthPercent = 0.001 if getCenter else 0.5

    boxes = []
    for box in boxesInfo:
        yCenter = box.GetMean(1)
        width = box.GetMean(2)
        ymin = yCenter - (widthPercent*width)
        ymax = yCenter + (widthPercent*width)
        b = ROOT.TBox(ymin,yampmin, ymax,yampmax)
        b.SetFillColor(color)
        boxes.append(b)

    return boxes

