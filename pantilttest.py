import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
servo = GPIO.PWM(4, 50)
servo.start(0)
sleep(2)

while True:
    duty = 2
    while duty <= 12:
        servo.ChangeDutyCycle(duty)
        angle = duty * 15
        print ("angle = ")
        print (angle)
        sleep(1)
        duty = duty + 1
    sleep(2)
    duty = 7
    servo.ChangeDutyCycle(duty)
    angle = duty * 15
    print ("angle = ")
    print (angle)
    sleep(2)
    duty = 4.5
    servo.ChangeDutyCycle(duty)
    angle = duty * 15
    print ("angle = ")
    print (angle)
    sleep(2)
    duty = 2
    servo.ChangeDutyCycle(duty)
    angle = duty * 15
    print ("angle = ")
    print (angle)
    sleep(2)