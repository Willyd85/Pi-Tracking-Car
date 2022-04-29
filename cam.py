import cv2
import numpy as np
import time
from time import sleep
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_servokit import ServoKit
import adafruit_motor.servo as motor
import RPi.GPIO as GPIO
PCA = ServoKit(channels=8)
PCA.frequency = 60
cam = cv2.VideoCapture(0)
_, frame = cam.read()
flipped = cv2.flip(frame, flipCode=1)
rows, cols, _ = frame.shape
x_center = int(cols / 2)
center = int(cols / 2)
position = 90
while True:
    _, frame = cam.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    low_red = np.array([161, 155, 84])
    high_red = np.array([179,255,255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    contours, _= cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        x_center = int((x + x + w) / 2)
        break
    cv2.line(frame, (x_center, 0), (x_center, 480), (0,255,0), 2)
    cv2.imshow("Frame", frame)
    cv2.imshow("mask", red_mask)
    
    key = cv2.waitKey(1)
    try:
        size = x
       # print (x)
    except:
        size = 0
    if key == 27:
        break
    if position < 10:
        position = 10
        if x_center  < center - 40 :
            position += 5
        PCA.servo[0].angle = position
        print (position)
    elif position > 170:
        position = 170
        if x_center > center + 40:
            position -= 5
        PCA.servo[0].angle = position
        print (position)
    else:
        if x_center == center:
            position = position
        if x_center  < center - 40:
            position += 5
        elif x_center > center + 40:
            position -= 5
        PCA.servo[0].angle = position
        print (position)
        if position < 40 and size >= 400:
            hi = 5
            #print ("left")
        elif position > 130 and size >= 400:
            hi = 5
            #print ("right")
        elif position < 400 and position >=300:
            #print ("stop")
            hi = 5
        elif size < 300:
            #print ("back")
            hi = 5
        else:
            hi = 5
            #print ("forward")
cam.release()
cv2.destroyAllWindows()