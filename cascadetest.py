import cv2
import numpy as np

pothole_cascade = cv2.CascadeClassifier('E:/Vedant/Projects/Pothole Detection and Severity Prediction/cascade/cascade.xml')

img = cv2.imread("potholes.png")
cv2.imshow('img', img)
cv2.waitKey(0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

potholes = pothole_cascade.detectMultiScale(gray)

for (x,y,w,h) in potholes:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
