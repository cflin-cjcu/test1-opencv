import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('test.jpg',1)

roi=img[77:122,640:788]
img[149:194,460:608]=roi
# roi=img[200:400, 200:400]
# img[100:300,100:300]=roi

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img1) 
plt.xticks([]), plt.yticks([]) 
plt.show()

# cv2.namedWindow('test',cv2.WINDOW_NORMAL)
# cv2.imshow('test',img)
# cv2.imwrite('test1.jpg',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()