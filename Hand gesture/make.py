import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while( cap.isOpened() ) :
    
    ret,img = cap.read() #Returns the image and the System report on the same
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Converts the img into a grayscale image
    #cv2.imshow('grayscale',gray)
    blur = cv2.GaussianBlur(gray,(5,5),0)#Blurs the image to blur
    #cv2.imshow('after bluring',blur)
    ret,thresh1 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    drawing = np.zeros(img.shape,np.uint8)

    max_area=0
   


   #this is the part that calculates the max area part
   #we will have to skip this part as for the region of interest
    for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i
    cnt=contours[ci]
    hull = cv2.convexHull(cnt)
    moments = cv2.moments(cnt)
    if moments['m00']!=0:
                cx = int(moments['m10']/moments['m00']) # cx = M10/M00
                cy = int(moments['m01']/moments['m00']) # cy = M01/M00
              
    centr=(cx,cy)       
    cv2.circle(img,centr,5,[0,0,255],2)       
    cv2.drawContours(drawing,[cnt],0,(0,255,0),2) 
    cv2.drawContours(drawing,[hull],0,(0,0,255),2) 
          
    cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    hull = cv2.convexHull(cnt,returnPoints = False)
    
    if(1):
               defects = cv2.convexityDefects(cnt,hull)
               mind=0
               maxd=0
               for i in range(defects.shape[0]):
                    s,e,f,d = defects[i,0]
                    start = tuple(cnt[s][0])
                    end = tuple(cnt[e][0])
                    far = tuple(cnt[f][0])
                    dist = cv2.pointPolygonTest(cnt,centr,True)
                    cv2.line(img,start,end,[0,255,0],2)
                    
                    cv2.circle(img,far,5,[0,0,255],-1)
               print(i)
               i=0
    cv2.imshow('output',drawing+img)
    cv2.imshow('input',img)
                
    k = cv2.waitKey(10)
    if k == 27:
        break
