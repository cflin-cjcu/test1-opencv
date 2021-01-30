import cv2
import numpy as np
def nothing(x):
    pass

img = cv2.imread('test27.jpg', 1)
img1 = img.copy()
cv2.imshow('image1', img)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(imgray, (11, 11), 0)
edges = cv2.Canny(img, 50, 100)
cv2.namedWindow('image')
cv2.createTrackbar('minval', 'image', 0, 255, nothing)
cv2.createTrackbar('maxval', 'image', 0, 255, nothing)

while(1):
    cv2.imshow('image', edges)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        print(len(contours))
        draw = cv2.drawContours(img1, contours, -1, (0, 255, 0), 2)
        show = draw.copy()
        cv2.imshow('contour', show)
    else:    
        minval = cv2.getTrackbarPos('minval', 'image')
        maxval = cv2.getTrackbarPos('maxval', 'image')
        edges = cv2.Canny(img, minval, maxval)    
cv2.destroyAllWindows()
