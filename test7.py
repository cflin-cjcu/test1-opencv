import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('test.jpg',1)
b = cv2.imread('test.jpg',1)
img1 = b[600:700,100:300]
img2 = b[100:200,700:900]
print(img1)
print(img2)
dst=cv2.addWeighted(img1,0.3,img2,0.7,0)
b[100:200,700:900]=dst
cv2.namedWindow('test',cv2.WINDOW_NORMAL)
cv2.imshow('test',img)
cv2.imshow('b',b)


cv2.waitKey(0)
cv2.destroyAllWindows()