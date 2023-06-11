'''
This function reads all the bbox of the images of file filepath to check if our tracker is correct

@params:

file_path* -> file path to the file taht contains the bounding boxes.
'''
def getBoundingBoxes(file_path):
    boundingBoxes = {}
    with open(file_path,'r') as file:
        for line in file:
            l = line.split(',')
            id,x1,y1,width,height,visible = list(map(int,l))
            #bbox = patches.Rectangle((x1, y1), width, height, linewidth=1, edgecolor='red', facecolor='none')
            boundingBoxes[id] = (x1,y1,width,height)
    return boundingBoxes

#-----------------------------------------------------

'''
Function to check if the prediction is correct, following the metric a. (A ∩ B)/(A U B)

@params:

bboxPred -> Predicted bounding box.
bboxReal -> Real bounging box.
'''
def getCorrectnes(bboxPred, bboxReal):
    xp, yp, wp, hp = bboxPred
    xr,yr, wr,hr = bboxReal
    
    
    x_left = max(xp, xr)
    y_top = max(yp, yr)
    x_right = min(xp + wp, xr + wr)
    y_bottom = min(yp + hp, yr + hr)
    
    if x_right < x_left or y_bottom < y_top:
      return 0
    
    intersection = (x_right - x_left) * (y_bottom - y_top)
    
    areaP = wp*hp
    areaR = wr*hr
    union = areaP + areaR - intersection
    
    return intersection / union