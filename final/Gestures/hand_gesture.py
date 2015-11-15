import cv2
import sys
import numpy as np
import subprocess
import os
from matplotlib import pyplot as plt 
PINK_MIN = np.array([120, 50, 50], np.uint8)
PINK_MAX = np.array([180, 180, 200], np.uint8)
BLUE_MIN = np.array([100,150,0], np.uint8)
BLUE_MAX = np.array([140,255,255], np.uint8)
def color_detect(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #frame_threshed = cv2.inRange(hsv, PINK_MIN, PINK_MAX)
    frame_threshed = cv2.inRange(hsv, BLUE_MIN, BLUE_MAX)
    contours,hierarchy = cv2.findContours(frame_threshed, 1, 2)
    max_area = 350
    found = 0
    if contours:
        for i in contours:
            area = cv2.contourArea(i)
            if area > max_area:
                found = 1
                cnt = i
        if(found == 1):
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            centroid_x = (x + x+w)/2
            centroid_y = (y + y+h)/2
            cv2.circle(img, (centroid_x, centroid_y), 2, (0,0,255), 2)
            #cv2.imshow('Threshold', frame_threshed)
            #cv2.imshow('Original', img)
            return img,centroid_x,centroid_y    
    return img,0,0


def detector(image):
    img_rgb = image
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template1 = cv2.imread('template.jpg',0)
    template2 = cv2.imread('template_line.png',0)
    template3 = cv2.imread('template_line_horiz.png',0)
    counter = 0
    res1 = cv2.matchTemplate(img_gray,template1,cv2.TM_CCOEFF_NORMED)
    res2 = cv2.matchTemplate(img_gray,template2,cv2.TM_CCOEFF_NORMED)
    #res3 = cv2.matchTemplate(img_gray,template3,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    posloc1 = np.where( res1 >= threshold)
    for pt in zip(*posloc1[::-1]):
        #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        counter = 1
    posloc2 = np.where( res2 >= threshold)
    for pt in zip(*posloc2[::-1]):
        #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        counter = 2
    #posloc3 = np.where( res3 >= threshold)
    #for pt in zip(*posloc3[::-1]):
        #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
     #   counter = 3
    return counter

def main():
    if len(sys.argv) == 1:
  	counter = 0;
  	count = 0;
        video_capture = cv2.VideoCapture(0)
        img = np.zeros((512,512,3), np.uint8)
        oldx = oldy = 0
        x  = 0
        y= 0
        write = 0
        while True:
            ret, frame = video_capture.read()
            frame,x,y = color_detect(frame)
            if(frame == None or x==None or y==None):
                continue
            if(x==0 & y==0):
            	count = count + 1;
            else:
                count = 0
            	cv2.circle(img,(x,y),35,0xff,-1)
                cv2.imshow('canvas',img)
            	if(write ==2):
            		write = 1
            	else:
            		write = 2
            if(count == 5):
                #print('should work')
            	#if(write == 1):
                result = detector(img)
                if(result == 1):
                    print("Initiate Gesture")
                    os.system("xdotool key XF86AudioMute")
                if(result == 2):
                    print("gesture 2")
                    os.system("xdotool key XF86AudioPlay")
                if(result == 3):
                    print("Gesture 3")
                    os.system("xdotool key XF86AudioLowerVolume")
            	write = 0
            	img = np.zeros((512,512,3), np.uint8)
                cv2.imshow('canvas',img)
            	count = 0
            cv2.imshow('Processed Video', frame)
            oldx = x
            oldy = y
            counter = counter+1;
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
