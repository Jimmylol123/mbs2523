# Save this file as OpenCV-Ex2-BounceBox.py

import cv2
#import numpy as np
print(cv2.__version__)
import random
color = "%03x" % random.randint(0, 0xFFF)

capture = cv2.VideoCapture(0)

capture.set(3,640)
capture.set(4,480)

x = 0
dx = 1
y = 0
dy = 1
# Start capturing and show frames on window named 'Frame'
while True:
    success, img = capture.read()
    cv2.rectangle(img, (x, y), (x + 60, y+60), (255, 50, 100), 4)
    x = x + dx
    y = y+ dy
    if x >= 580 or x <= 0:
        dx = dx * (-1)
    if y >= 420 or y <= 0:
        dy = dy * (-1)

    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()