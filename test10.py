import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test1.jpg', 1)
# global thresholding
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Otsu's thresholding
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
# （9,9）为高斯核的大小，8 为标准差
blur = cv2.GaussianBlur(img, (5, 5), 2)
# 阈值一定要设为 0！
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("origin", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
