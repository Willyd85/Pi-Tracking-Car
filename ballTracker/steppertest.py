import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Seq = [[0,1,0,0],
[0,1,0,1],
[0,0,0,1],
[1,0,0,1],
[1,0,0,0],
[1,0,1,0],
[0,0,1,0],
[0,1,1,0],]
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
def backward(steps):
    for i in range(steps):
        for j in range(8):
            m = -j + 7
            setStep1(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            setStep2(Seq[m][0], Seq[m][1], Seq[m][2], Seq[m][3])
            time.sleep(.001)
def forward(steps):
    for i in range(steps):
        for j in reversed(range(8)):
            m = -j + 7
            setStep1(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            setStep2(Seq[m][0], Seq[m][1], Seq[m][2], Seq[m][3])
            time.sleep(.001)
def left(steps):
    for i in range(steps):
        for j in reversed(range(8)):
            setStep1(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(.002)
def right(steps):
    for i in range(steps):
        for j in (range(8)):
            setStep2(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(.002)
if __name__ =='__main__':
    while True:
        forward(50)
        time.sleep(1)
        backward(50)
        time.sleep(1)
        left(50)
        time.sleep(1)
        right(50)
        time.sleep(1)
GPIO.cleanup();