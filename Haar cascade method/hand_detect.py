import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt 
PINK_MIN = np.array([120, 50, 50], np.uint8)
PINK_MAX = np.array([180, 180, 200], np.uint8)
def color_detect(img):
    #img = cv2.flip(img, 1)
    #thresh = cv2.namedWindow('Threshold', cv2.WINDOW_NORMAL)
    #orig = cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
    #img = cv2.GaussianBlur(img, (15, 15), 0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    frame_threshed = cv2.inRange(hsv, PINK_MIN, PINK_MAX)
    #res = cv2.bitwise_and(img,img, mask= frame_threshed)
    #cv2.imshow('res',res)
    contours,hierarchy = cv2.findContours(frame_threshed, 1, 2)
    max_area = 250
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
        else:
            return img,0,0


def face_detect(image):
    cascPath = sys.argv[1]
    HaarCascade = cv2.CascadeClassifier(cascPath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = HaarCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    xx = 0
    yy = 0
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #cv2.circle(image,(x+w/2,y+h/2),2,0xff)
        xx = x+w/2
        yy = y+h/2
    return image,xx,yy;

def detector(image):
  img_rgb = image
  img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
  template = cv2.imread('template.jpg',0)
  w, h = template.shape[::-1]
  counter = 0
  res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
  threshold = 0.5
  loc = np.where( res >= threshold)
  for pt in zip(*loc[::-1]):
    #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    counter = 1
  return counter

def main():
    if len(sys.argv) == 2:
        #get image form video
  	counter = 0;
  	count = 0;
        video_capture = cv2.VideoCapture(0)
        img = np.zeros((512,512,3), np.uint8)
        oldx = oldy = 0
        x  = 0
        y= 0
        write = 0
        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()
            #if(counter%2 == 0):
            frame,x,y = color_detect(frame)
            if(x==0 & y==0):
            	count = count + 1;
            else:
                count = 0
            	cv2.circle(img,(x,y),35,0xff,-1)
                cv2.imshow('canvas',img)
                print('working')
            	if(write ==2):
            		write = 1
            	else:
            		write = 2
            if(count == 5):
                #print('should work')
            	#if(write == 1):
                result = detector(img)
                if(result == 1):
                    print("YOLO detected")
                else:
                    print("you")
            	write = 0
            	img = np.zeros((512,512,3), np.uint8)
                cv2.imshow('canvas',img)
            	count = 0
            cv2.imshow('Processed Video', frame)
            #cv2.imshow('name',img)
            oldx = x
            oldy = y
            counter = counter+1;
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        #release everything
        video_capture.release()
        cv2.destroyAllWindows()
    else:
        print("usage : python hand_detect.py [har CascadeClassifier file]")

if __name__ == '__main__':
    main()
