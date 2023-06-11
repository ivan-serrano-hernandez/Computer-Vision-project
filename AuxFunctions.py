import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

'''
This function reads all the bbox of the images of file filepath to check if our tracker is correct

@params:
file_path* -> file path to the file that contains the bounding boxes.
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
bboxReal -> Real bounding box.
'''
def getCorrectness(bboxPred, bboxReal):
    xp, yp, wp, hp = bboxPred
    xr,yr, wr,hr = bboxReal
    
    x_left = max(xp, xr)
    y_top = max(yp, yr)
    x_right = min(xp + wp, xr + wr)
    y_bottom = min(yp + hp, yr + hr)
    
    if x_right < x_left or y_bottom < y_top:
        return 0
    
    intersection = (x_right - x_left) * (y_bottom - y_top)
    
    areaP = wp * hp
    areaR = wr * hr
    union = areaP + areaR - intersection
    
    return intersection / union

#-----------------------------------------------------
'''
Function that represents the plot for a list of metrics

@params:
listOfMetrics -> List with values of the metric for each frame
'''
def plotResults(listOfMetrics):
    plt.plot(listOfMetrics)
    plt.xlabel("Frame")
    plt.ylabel("Percentage")
    yticks = mtick.PercentFormatter(symbol='%')
    ytick_positions = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    plt.yticks(ytick_positions)
    plt.gca().yaxis.set_major_formatter(yticks)
    plt.show()
