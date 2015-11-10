import cv2
import numpy as np
import cv2.cv as cv
img = cv2.imread('image.png')
img = cv2.medianBlur(img,5)

contours,hierarchy = cv2.findContours(img, 1, 2)

cnt = contours[0]
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2)

cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()