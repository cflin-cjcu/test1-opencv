import cv2
import numpy as np
img = cv2.imread('test.jpg',0)
print(img)
cv2.namedWindow('test',cv2.WINDOW_NORMAL)
cv2.imshow('test',img)
cv2.imwrite('test1.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()