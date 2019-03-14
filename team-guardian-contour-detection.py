import numpy as np
import cv2 as cv

im = cv.imread('emitter.png')

# using this additional blur
# provides more reliable results with other images
im = cv.medianBlur(im, 5)

# the second threshold eliminates the shorter edges
edges = cv.Canny(im, 0, 200)

# merge the edges that are close to each other 
kernel = np.ones((10, 10), np.uint8)
edgesclosed = cv.morphologyEx(edges, cv.MORPH_CLOSE, kernel)

contours, hierarchy = cv.findContours(edgesclosed, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for i, contour in enumerate(contours):
    
    # solidity works well for recognizing circle-like shapes
    area = cv.contourArea(contour)
    hull = cv.convexHull(contour)
    hullArea = cv.contourArea(hull)
    
    # eliminate division by zero bugs
    if hullArea != 0:
        solidity = area / float(hullArea)

        if solidity > 0.8:
            (x,y), radius = cv.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            cv.circle(im, center, radius,(0, 0, 255), 2)
            
            # the final result: coordinates of the blob
            print(center)

cv.imshow('emitter with contours', im)
cv.waitKey(0)
