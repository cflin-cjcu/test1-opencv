import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('test.jpg',1)
b = cv2.imread('test.jpg',1)
b[100:200,100:200,0]=0
b[300:500,600:800,1]=0
b[500:600,300:500,2]=0
print(b)

# roi=img[77:122,640:788]
# img[149:194,460:608]=roi
# roi=img[200:400, 200:400]
# img[100:300,100:300]=roi

# img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# plt.imshow(img1) 
# plt.xticks([]), plt.yticks([]) 
# plt.show()

cv2.namedWindow('test',cv2.WINDOW_NORMAL)
cv2.imshow('test',img)
cv2.imshow('b',b)


cv2.waitKey(0)
cv2.destroyAllWindows()