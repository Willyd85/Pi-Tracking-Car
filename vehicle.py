import RPi.GPIO as GPIO
import time
import threading

class vehicle:
    def forward(self):
        controlPin = [11,13,15,16]
        for pin in controlPin:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
        seq1 = [
        [1,1,0,0],
        [0,1,1,0],
        [0,0,1,1],
        [1,0,0,1],]
        seq2 = [
        [1,1,0,0],
        [1,0,0,1],
        [0,0,1,1],
        [0,1,1,0],]
        for i in range(50):
            for fullstep in range(4):
                for pin in range(4):
                    GPIO.output(controlPin[pin], seq1[fullstep][pin])
                    time.sleep(0.004)
    def backward(self):
        movement = 0
    def left(self):
        movement = 0
    def right(self):
        movement = 0
    def idle(self):
        movement = 0
    
