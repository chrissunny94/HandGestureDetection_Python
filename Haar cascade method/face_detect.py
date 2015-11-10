import cv2
import sys
import numpy as np

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


def main():
    if len(sys.argv) == 2:
        #get image form video
  	counter = 0;
        video_capture = cv2.VideoCapture(0)
        img = np.zeros((512,512,3), np.uint8)
        oldx = oldy = 0
        x  = 0
        y= 0
        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()

            if(counter%2!=0):
            	frame,x,y = face_detect(frame)
            if(x==0 & y==0):
            	#cv2.imwrite("image.png",img)
            	img = np.zeros((512,512,3), np.uint8)
            cv2.imshow('Processed Video', frame)
            cv2.circle(img,(x,y),35,0xff,-1)
            cv2.imshow('name',img)
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
