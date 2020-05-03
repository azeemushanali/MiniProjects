# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 05:32:43 2020

@author: Azeemushan
"""

import cv2
import time 
import numpy as np

classifier = cv2.CascadeClassifier(r'haarcascade_car.xml')
cap = cv2.VideoCapture('cars.avi')

while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cars = classifier.detectMultiScale(gray,1.3,3)
        for (x,y,w,h) in cars:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            cv2.imshow("Cars",frame)
        if cv2.waitKey(1) == 13:
            break
    else:
        print("Video Ended")
        break
cap.release()
cv2.destroyAllWindows()

