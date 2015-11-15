#The needed libraries OpenCV , Numpy & Math
import cv2
import numpy as np
import math
#Object for using the WebCam
cap = cv2.VideoCapture(0)
#Object for using the BackGroundSubtractor
backSub = cv2.BackgroundSubtractorMOG(history=3,nmixtures=5,backgroundRatio=0.5, noiseSigma=1) 
backSub2 = cv2.BackgroundSubtractorMOG2() 


while(cap.isOpened()):
                #Getting the image from the WebCam    Edit  on 7th-OCt 
        ret, img = cap.read()
            #Applying the Background Subtractor Edit on 7th Oct 
        back_img = backSub.apply( img , learningRate = .7 )
        back_img2 = backSub2.apply( img , learningRate = .1 )
        

		#Showing the Background Subtractor Edit on 7th Oct
        cv2.imshow( 'BackGroundSubtractor' , back_img )
        cv2.imshow( 'BackGroundSubtractor2' , back_img )
        
        contours, hierarchy = cv2.findContours(back_img.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        max_area = -1
        for i in range(len(contours)) :
                cnt=contours[i]
                area = cv2.contourArea(cnt)
                if(area>max_area ):
                        max_area=area
                        x,y,w,h = cv2.boundingRect(contours[i])
                        temp=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),0)

        k = cv2.waitKey(10)
    
