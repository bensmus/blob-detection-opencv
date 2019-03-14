import numpy as np
import cv2 as cv

im = cv.imread('emitter.png')

# second argument sorts edges by length?
edges = cv.Canny(im, 0, 200)

# make the edges that are close to each other closed
# this is so that blob detection is easier
kernel = np.ones((10, 10), np.uint8)
edgesclosed = cv.morphologyEx(edges, cv.MORPH_CLOSE, kernel)

contours, hierarchy = cv.findContours(edgesclosed, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for i, contour in enumerate(contours):
    '''
    x,y,w,h = cv.boundingRect(contour)
    aspect_ratio = float(w)/h
    print(aspect_ratio)
    '''
    # solidity works well for recognizing blobs
    area = cv.contourArea(contour)
    hull = cv.convexHull(contour)
    hullArea = cv.contourArea(hull)
    solidity = area / float(hullArea)
    print(solidity)

    if solidity > 0.8:
        #cv.drawContours(im, contours[i], -1, (0, 0, 255), 3)
        (x,y),radius = cv.minEnclosingCircle(contour)
        center = (int(x),int(y))
        print(center)
        radius = int(radius)
        cv.circle(im, center, radius,(0, 0, 255), 2)

print('number of contours', len(contours))

cv.imshow('emitter with contours', im)
cv.waitKey(0)
