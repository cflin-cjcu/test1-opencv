import cv2
import numpy as np
def nothing(x):
    pass

img = cv2.imread('test1.jpg', 0)
cv2.imshow('image1', img)
edges = cv2.Canny(img, 50, 100)
cv2.namedWindow('image')
cv2.createTrackbar('minval', 'image', 0, 255, nothing)
cv2.createTrackbar('maxval', 'image', 0, 255, nothing)

while(1):
    cv2.imshow('image', edges)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    minval = cv2.getTrackbarPos('minval', 'image')
    maxval = cv2.getTrackbarPos('maxval', 'image')
    edges = cv2.Canny(img, minval, maxval)

cv2.destroyAllWindows()
