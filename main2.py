import RPi.GPIO as GPIO
import time
import os
import signal
from time import sleep
import multiprocessing as multi
import cv2
import numpy as np
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_servokit import ServoKit
import adafruit_motor.servo as motor
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
controlPin1 = 17
controlPin2 = 27
controlPin3 = 22
controlPin4 = 23
controlPin5 = 24
controlPin6 = 25
controlPin7 = 16
controlPin8 = 26
GPIO.setup(controlPin1, GPIO.OUT)
GPIO.setup(controlPin2, GPIO.OUT)
GPIO.setup(controlPin3, GPIO.OUT)
GPIO.setup(controlPin4, GPIO.OUT)
GPIO.setup(controlPin5, GPIO.OUT)
GPIO.setup(controlPin6, GPIO.OUT)
GPIO.setup(controlPin7, GPIO.OUT)
GPIO.setup(controlPin8, GPIO.OUT)
def ultrasonic(b):
    while True:
        GPIO.setwarnings(False)
        trig1 = 21
        echo1 = 20

        GPIO.setup(trig1,GPIO.OUT)
        GPIO.output(trig1, 0)

        GPIO.setup(echo1,GPIO.IN)
        print ("starting measurement...")
        time.sleep(.5)
        GPIO.output(trig1,1)
        time.sleep(0.00001)
        GPIO.output(trig1,0)
        print ("no problem")
        while GPIO.input(echo1) == 0:
            start = time.time()
        while GPIO.input(echo1) == 1:
            stop = time.time()
        print ("no problem 2")
        tot_time = stop - start
        distance = tot_time / .000058

        print (distance)
        if distance < 15:
            b.put(1)
        else:
            b.put(0)
        GPIO.cleanup()
def movement(pipe, d, e):
    Seq = [[0,1,0,0],
    [0,1,0,1],
    [0,0,0,1],
    [1,0,0,1],
    [1,0,0,0],
    [1,0,1,0],
    [0,0,1,0],
    [0,1,1,0],]
    p1_pid = pipe.recv()
    key = cv2.waitKey(1)
    c = 0
    a = d.get()
    b = e.get()
    #forward
    while True:
        if(d.empty() != True):
            a = d.get()
        if(e.empty() != True):
            b = e.get()
        if(c == 1):
            break
        while a == 0 and b == 0:
            print ("forward|")
            for j in reversed(range(8)):
                if(d.empty() != True):
                    a = d.get()
                if(e.empty() != True):
                    b = e.get()
                if key == 27:
                    c = 1
                    break
                m = -j + 7
                setStep1(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
                setStep2(Seq[m][0], Seq[m][1], Seq[m][2], Seq[m][3])
                time.sleep(.003)
                if(b != 0 and a == 0):
                    continue
                else:
                    break
        #back
        if(c == 1):
            break
        while a == 1 and b == 0:
            #print ("back")
            for j in range(8):
                if(d.empty() != True):
                    a = d.get()
                if(e.empty() != True):
                    b = e.get()
                if key == 27:
                    c = 1
                    break
                m = -j + 7
                setStep1(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
                setStep2(Seq[m][0], Seq[m][1], Seq[m][2], Seq[m][3])
                time.sleep(.003)
                if(b != 0 and a == 1):
                    continue
                else:
                    break
        #left
        if(c == 1):
            break
        while a == 2 and b == 0:
            if key == 27:
                c = 1
                break
            print ("left")
            for j in reversed(range(8)):
                if(d.empty() != True):
                    a = d.get()
                if(e.empty() != True):
                    b = e.get()
                setStep1(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
                time.sleep(.005)
                if(b != 0 and a == 2):
                    continue
                else:
                    break
        #right
        if(c == 1):
            break
        while a == 3 and b == 0:
            if key == 27:
                c = 1
                break
            print ("right")
            for j in range(8):
                if(d.empty() != True):
                    a = d.get()
                if(e.empty() != True):
                    b = e.get()
                setStep2(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
                time.sleep(.005)
                if(b != 0 and a == 3):
                    continue
                else:
                    break
        #stop
        if(c == 1):
            break
        while a == 4 or b == 0:
            print ("stop")
            if(e.empty() != True):
                b = e.get()
            if(d.empty() != True):
                a = d.get()
            if key == 27:
                c = 1
                break
            if(a != 4 and b != 1):
                break
def camera(pipe, a):
    p2_pid = pipe.recv
    PCA = ServoKit(channels=8)
    PCA.frequency = 60
    cam = cv2.VideoCapture(0)
    _, frame = cam.read()
    flipped = cv2.flip(frame, flipCode=1)
    rows, cols, _ = frame.shape
    x_center = int(cols / 2)
    center = int(cols / 2)
    position = 90
    sleep(2)
    direction = 5
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
            #print (x)
        except:
            size = 0
        if key == 27:
            break
        if position < 10:
            position = 10
            if x_center  < center:
                position += 3
            PCA.servo[0].angle = position
            print (position)
        elif position > 170:
            position = 170
            if x_center > center:
                position -= 3
            PCA.servo[0].angle = position
            print (position)
        else:
            if x_center == center:
                position = position
            if x_center  < center - 40:
                position += 3
            elif x_center > center + 40:
                position -= 3
            PCA.servo[0].angle = position
        print (position)
        if position < 70 and size >= 200:
            a.put(2)
        elif position > 110 and size >= 200:
            a.put(3)
        elif size < 200 and size >=50:
            a.put(4)
        elif size < 50:
            a.put(1)
        else:
            a.put(0)
    cam.release()
    cv2.destroyAllWindows()
def setStep1(e1, e2, e3, e4):
    GPIO.output(controlPin1, e1)
    GPIO.output(controlPin2, e2)
    GPIO.output(controlPin3, e3)
    GPIO.output(controlPin4, e4)
def setStep2(e1, e2, e3, e4):
    GPIO.output(controlPin5, e1)
    GPIO.output(controlPin6, e2)
    GPIO.output(controlPin7, e3)
    GPIO.output(controlPin8, e4)
if __name__ == '__main__':
    a = multi.Queue()
    b = multi.Queue()
    a.put(4)
    b.put(0)
    conn1, conn2 = multi.Pipe()
    movement = multi.Process(target=movement, args=(conn2, a, b))
    camera = multi.Process(target=camera, args=(conn1, a))
    #ultra = multi.Process(targer=ultra, args=(b))
    camera.start()
    movement.start()
    conn1.send(movement.pid)
    conn2.send(camera.pid)
    
