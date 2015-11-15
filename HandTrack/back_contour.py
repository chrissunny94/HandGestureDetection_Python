#The needed libraries OpenCV , Numpy & Math
import cv2
import numpy as np
import math
#Object for using the WebCam
cap = cv2.VideoCapture(0)
#Object for using the BackGroundSubtractor
#backSub = cv2.BackgroundSubtractorMOG2(history=3,nmixtures=5,backgroundRatio=0.5, noiseSigma=1) 
backSub = cv2.BackgroundSubtractorMOG2() 


while(cap.isOpened()):
        #Getting the image from the WebCam    Edit  on 7th-OCt 
        ret, img = cap.read()
    
    	#Applying the Background Subtractor Edit on 7th Oct 
        back_img = backSub.apply( img , learningRate = .7 )

		#Showing the Background Subtractor Edit on 7th Oct
        cv2.imshow( 'BackGroundSubtractor' , back_img )
        contours, hierarchy = cv2.findContours(back_img.clone(),cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        print contours , hierarchy
        max_area = -1
    for i in range(len(contours)) :
            cnt=contours[i]
            area = cv2.contourArea(cnt)
        if(area>max_area ):
        	max_area=area
            print area
            x,y,w,h = cv2.boundingRect(contours[i])
            cv2.rectangle(back_img,(x,y),(x+w,y+h),(0,0,255),0)
    

	#hull = cv2.convexHull(,2,1)
	


	k = cv2.waitKey(10)
    #if k == 27:
    #	break

