import  cv2
import numpy  as np
print(cv2.__version__)

kernel =np.ones((5,5),np.uint8)

img = cv2.imread("ressources/lena[1].png")
Gaussian= cv2.GaussianBlur(img,(7,7),0)
Canny =cv2.Canny(img,100,100)

Dilation = cv2.dilate(Canny,kernel,iterations=1)

cv2.imshow('lena',img)
cv2.imshow('lenaBlur',Gaussian)
cv2.imshow('lenaCanny',Canny)
cv2.imshow('lenaDilate',Dilation)
cv2.waitKey(0)