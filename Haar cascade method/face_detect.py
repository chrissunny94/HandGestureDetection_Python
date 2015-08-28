import cv2
import sys

def face_detect(image):
    cascPath = sys.argv[1]
    faceCascade = cv2.CascadeClassifier(cascPath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return image;


def main():
    if len(sys.argv) == 2:
        #get image form video
        video_capture = cv2.VideoCapture(0)
        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()

            frame = face_detect(frame)

            cv2.imshow('Processed Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        #release everything
        video_capture.release()
        cv2.destroyAllWindows()
    
    elif len(sys.argv) == 3:
        #get image from file
        print("detecting faces on image\n")
        image = cv2.imread(sys.argv[2])
        cv2.imshow("before detecting",image)
        image = face_detect(image)
        cv2.imshow("after detecting",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("usage : python face_detect.py [har CascadeClassifier file] <image path>")

if __name__ == '__main__':
    main()
