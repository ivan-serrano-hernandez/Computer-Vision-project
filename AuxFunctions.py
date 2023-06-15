import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import math
import matplotlib.patches as patches
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
def getMetricIntesection(bboxPred, bboxReal):
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


'''
Function to check if the prediction is correct, using the euclidean distance between the centroids of the boxes

@params:
bboxPred -> Predicted bounding box.
bboxReal -> Real bounding box.
'''
def getMetricCentDist(bboxPred, bboxReal):
    xp, yp, wp, hp = bboxPred
    xr,yr, wr,hr = bboxReal
    
    p_x = xp + (wp / 2)
    p_y = yp + (hp / 2)
    
    r_x = xr + (wr / 2)
    r_y = yr + (hr / 2)
    
    distance = abs(math.sqrt((r_x - p_x)**2 + (r_y - p_y)**2))
    
    return distance

#-----------------------------------------------------
#-----------------------------------------------------
'''
Function that represents the plot for a list of metrics

@params:
listOfMetrics -> List with values of the metric for each frame
'''
def plotResults(intersecions, distances):
    fig, axs =plt.subplots(1,2)
    axs[0].plot(intersecions)
    axs[0].set_xlabel("Frame")
    axs[0].set_ylabel("Percentage")
    yticks = mtick.PercentFormatter(symbol='%')
    ytick_positions = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    axs[0].set_yticks(ytick_positions)
    axs[0].yaxis.set_major_formatter(yticks)
    
    axs[1].plot(distances)
    axs[1].set_xlabel("Frame")
    axs[1].set_ylabel("Distance")
    
    plt.show()

    
#-----------------------------------------------------
'''
Function that draws an image with the predicted and the real box

@params:
img -> Image 
bboxPred -> Predicted box( color red)
bboxReal -> Real box (color green)
'''
def drawBox(img,bboxPred, bboxReal):
    x1,y1,width,height = bboxPred
    predRect = patches.Rectangle((x1, y1), width, height, linewidth=1, edgecolor='red', facecolor='none')
    
    x2,y2,widt2,heigh2 = bboxReal
    realRect = patches.Rectangle((x2, y2), widt2, heigh2, linewidth=1, edgecolor='green', facecolor='none')
    
    fig,ax = plt.subplots()
    ax.imshow(img)
    ax.add_patch(predRect)
    ax.add_patch(realRect)
    plt.show()