import cv2
import numpy as np

img=np.zeros((512,512,3), np.uint8) 


#Import only if not previously imported
# Coordinates must be a tuple - (x,y)
cv2.line(img,(0,0),(500,500),(255,0,255),5)
cv2.rectangle(img,(100,100),(300,300),(0,255,0),3)
cv2.circle(img,(200,200), 150, (100, 100, 100) ,5)   
points=np.array([[200, 200], [300, 100], [400, 200], [400, 400], [200, 400]], np.int32)
print(points)
cv2.polylines(img,[points],True,(0,0,100),5) 


cv2.imshow("Window Name", img)
cv2.waitKey(0)
cv2.destroyAllWindows()