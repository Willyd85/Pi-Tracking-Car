import RPi.GPIO as GPIO
import time
import threading
from vehicle import *

main_function = vehicle()
count = 1
check = 1
def main():
    while count == 1:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        trig1 = 40
        echo1 = 38

        GPIO.setup(trig1,GPIO.OUT)
        GPIO.output(trig1, 0)

        GPIO.setup(echo1,GPIO.IN)
        if check == 0:
            time.sleep(1)

        print ("starting measurement...")

        GPIO.output(trig1,1)
        time.sleep(0.00001)
        GPIO.output(trig1,0)

        while GPIO.input(echo1) == 0:
            start = time.time()
        while GPIO.input(echo1) == 1:
            stop = time.time()

        tot_time = stop - start
        distance = tot_time / .000058

        print (distance)
        if distance < 15:
            check == 0
        else:
            main_function.forward()
            check == 1
        GPIO.cleanup()
main()