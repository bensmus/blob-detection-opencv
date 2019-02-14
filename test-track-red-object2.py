''' sometimes, line 21 throws an error, other times it does not-
this does not seem to be the fault of the code '''

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

clicks = 0

while(True):

    # _ is a valid variable name
    # use it for variables that you do not need
    _, frame = cap.read()

    '''convert BGR (blue green red) to HSV (hue saturation value)
    if we ignore S and V components of HSV,
    we can treat H similarly to greyscale (algorithms like it)'''

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # recall the hue saturation value color cylinder
    # red is zero degrees

    # the next two if statements allow
    # searched color category to be changed on runtime
    if clicks % 18 == 0:
        low = 0
        high = 20

    if cv2.waitKey(1) & 0xFF == ord('d'):
        low += 20
        high += 20
        clicks += 1

    print(low, high)

    min_hsv = np.array([low, 100, 100])
    max_hsv = np.array([high, 255, 255])

    # find pixels in range
    mask = cv2.inRange(hsv, min_hsv, max_hsv)

    # show image with window title
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    # program terminates when q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
