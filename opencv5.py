import  cv2
import numpy  as np
print(cv2.__version__)

#kernel =np.ones((5,5),np.uint8)
faceCascade = cv2.CascadeClassifier('ressources/haarcascade_frontalface_default.xml')
img = cv2.imread("ressources/BTS.jpg")
faces = faceCascade.detectMultiScale(img,1.02,3)
print(faces)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0)),
cv2.imshow('lena',img)
cv2.waitKey(0)
#print(np.shape(img))
#imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#print(np.shape(imgGray))
#imgGray = cv2.cvtColor(imgGray,cv2.COLOR_BGR2RGB)
#print(np.shape(imgGray))
#while True:
 #   success,img = img.read()
 #   faces = faceCascade.detectMultiScale(imgGray,1.1,3)
 #   for(x,y,w,h) in faces:
  #      cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0)),
#roi = img[120:260,110:270].copy()
#roiGray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
#roiGray = cv2.cvtColor(roiGray,cv2.COLOR_BGR2RGB)
#img[120:260,110:270] = roiGray

#cv2.imshow('lena',img)
#cv2.imshow('lena',imgGray)
#cv2.imshow('lenaROI',roi)
#cv2.imshow('lenaROIGeay',roiGray)
#cv2.waitKey(0)