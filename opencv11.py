# Save this file to your Github as OpenCV-11-Haar-face-video.py
import cv2
import numpy as np
print(cv2.__version__)

faceCascade = cv2.CascadeClassifier('ressources/haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture('ressources/guitar.mp4')
# capture = cv2.VideoCapture(0)
capture.set(3,640)
capture.set(4,480)

while True:
    success, img = capture.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 3)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Frame', img)
    #cv2.moveWindow('Frame', 100,20)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()