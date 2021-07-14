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
        boxesInfo.append(f.Get("stripBoxInfo10"))
        boxesInfo.append(f.Get("stripBoxInfo11"))

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

