import cv2
import numpy as np

body_classifier = cv2.CascadeClassifier(r"haarcascade_fullbody.xml")
cap = cv2.VideoCapture(r"walking.avi")
while cap.isOpened():
    ret,frame = cap.read()
    frame = cv2.resize(frame,None,fx = 0.5, fy = 0.5,interpolation=cv2.INTER_LINEAR)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#    bodies = body_classifier.detectMultiScale(gray,1.2,3)
    bodies = body_classifier.detectMultiScale3(gray,1.2,3)
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow()
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()
