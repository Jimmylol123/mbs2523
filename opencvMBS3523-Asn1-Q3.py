# Save this file to your Github as OpenCV-11-Haar-face-video.py
import cv2
import numpy as np
import random
print(cv2.__version__)
car_cascade = cv2.CascadeClassifier('ressources/cars.xml')
pedestrians_cascade1 = cv2.CascadeClassifier('ressources/pedestrian.xml')

capture = cv2.VideoCapture('ressources/test5.mp4')

#capture = cv2.VideoCapture(0)
capture.set(3,640)
capture.set(4,480)

while True:

    success, img = capture.read()
    imgGray = cv2.cvtColor (img,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(imgGray, 1.10, 3)
    pedestrians = pedestrians_cascade1.detectMultiScale(imgGray, 1.08, 3)

    for (x, y, w, h) in cars:
        color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.rectangle(img, (x, y), (x + w, y + h), (color1), 2)
    for (x, y, w, h) in pedestrians:
        color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.rectangle(img, (x, y), (x + w, y + h), (color2), 2)

    cv2.imshow('Frame', img)
    #cv2.moveWindow('Frame', 100,20)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()