import cv2
print(cv2.__version__)

cap = cv2.VideoCapture(0)
while True:
    s ,img = cap.read()
    cv2.imshow("d",img)
    cv2.imshow('Dog',img)
    if  cv2.waitKey(20) &  0xff ==ord('q'):
        break
cap.release()
cv2.destroyALLWindows()