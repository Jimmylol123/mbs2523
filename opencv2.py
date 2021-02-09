import cv2
import numpy  as np
print(cv2.__version__)

kernel =np.ones((5,5),np.uint8)

cap = cv2.VideoCapture('ressources/d.mp4')
while True:
    s, img = cap.read()
    Gaussian = cv2.GaussianBlur(img, (7, 7), 0)
    Canny = cv2.Canny(img, 100, 100)
    Dilation = cv2.dilate(Canny, kernel, iterations=1)
    cv2.imshow("d",img)

    cv2.imshow('dBlur', Gaussian)
    cv2.imshow('dCanny', Canny)
    cv2.imshow('dDilate', Dilation)
    if  cv2.waitKey(20) &  0xff ==ord('q'):
        break
cap.release()
cv2.destroyALLWindows()