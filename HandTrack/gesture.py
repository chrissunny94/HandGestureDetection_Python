import cv2
import numpy as np
import math
cap = cv2.VideoCapture(0)
fgbg = cv2.BackgroundSubtractorMOG(history=3,nmixtures=4,backgroundRatio=0.5, noiseSigma=0.01) 
fbg = 0


while(cap.isOpened()):
    ret, img = cap.read()
    fbg = img
    history = 3
    fbg = fgbg.apply(img,learningRate=1.0/history)
    cv2.imshow('test',fbg)


    #Region inside which the hand is to be placed 
    cv2.rectangle(img,(0,0),(500,500),(0,255,0),0)
    grey = fbg[200:500, 200:500]
    crop_img =img[200:500, 200:500]
    fbg_crop = fbg[200:500, 200:500] 
    
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    #grey = cv2.cvtColor(crop_img, cv2.COLOR_GRAY2BGR)
    value = (35,35)
    
    thresh1 =crop_img
    blurred = cv2.GaussianBlur(grey, value, 0)
    
    _, thresh1 = cv2.threshold(blurred, 200, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    #cv2.imshow('Thresholded', thresh1)
    
    cv2.imshow('BackgroundSubtractor',fbg)

    #thresh1 = cv2.cvtColor(thresh1, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(fbg_crop.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    # max_area = -1
    # ci = 0
    # for i in range(len(contours)):
    #     cnt=contours[i]
    #     area = cv2.contourArea(cnt)
    #     if(area>max_area ):
    #         max_area=area
    #         print area
    #         ci=i
    #cnt=contours[ci]
    #x,y,w,h = cv2.boundingRect(cnt)

    #cv2.rectangle(crop_img,(x,y),(x+w,y+h),(0,0,255),0)
    #cv2.rectangle(fbg_crop,(x,y),(x+w,y+h),(0,0,255),0)
    #hull = cv2.convexHull(fbg_crop)
    

    
    #drawing = np.zeros(crop_img.shape,np.uint8)
    #cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
    #cv2.drawContours(drawing,[hull],0,(0,0,255),0)
    

    hull = cv2.convexHull(fbg_crop,2,1)
    defects = cv2.convexityDefects(cnt,hull)
    count_defects = 0
    cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
    
    
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
        
        if angle <= 90:
            
            count_defects += 1
            cv2.circle(crop_img,far,1,[0,0,255],-1)
            #dist = cv2.pointPolygonTest(cnt,far,True)
            
            cv2.line(crop_img,start,end,[0,255,0],2)
            cv2.circle(crop_img,far,5,[0,0,255],-1)
    

    if count_defects == 1 :
        cv2.putText(img,"2 fingers", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

    elif count_defects == 2:
        cv2.putText(img,"3 fingers", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        
    elif count_defects == 3:
        cv2.putText(img, "4 fingers", (5,50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)

    elif count_defects == 4:
        cv2.putText(img,"5 finger", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    
    elif count_defects == 5:
        cv2.putText(img,"This is 5", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    
    else:
        cv2.putText(img,"HandNotDetected", (50,50),cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    
    cv2.imshow('drawing', drawing)
    



    #cv2.imshow('end', crop_img)
    

    cv2.imshow('Gesture', img)
    all_img = np.hstack((drawing, crop_img))
    #cv2.imshow('Contours', all_img)
    k = cv2.waitKey(10)
    if k == 27:
        break