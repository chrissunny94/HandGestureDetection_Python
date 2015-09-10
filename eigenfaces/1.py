import cv2
import numpy as np
image = 0
count = 0
import os
for subdir, dirs, files in os.walk('./gallery'):
    for file in files:
    	gray = cv2.cvtColor(cv2.imread(file), cv2.COLOR_BGR2GRAY)
    	image =image + gray
    	count=count+1
    	image=image/count
    	#cv2.imshow(image)
        #cv2.waitKey(0)
    	count=count+1
    	print file
    	#cv2.waitKey(0)


cv2.destroyAllWindows()
print(count)
print(np.shape(image))
print(np.max(image))
#print(image)
image=image/count
cv2.imwrite("test.=png",image)
#image = cv2.imread("test.png")
#cv2.imshow(image)
cv2.waitKey(0)
cv2.destroyAllWindows()




#print(image)

