import RPi.GPIO as GPIO
import time
count = 1
while count == 1:
    GPIO.setmode(GPIO.BCM)

    trig1 = 21
    echo1 = 20

    GPIO.setup(trig1,GPIO.OUT)
    GPIO.output(trig1, 0)

    GPIO.setup(echo1,GPIO.IN)

    time.sleep(0.5)

    print ("starting measurement...")

    GPIO.output(trig1,1)
    time.sleep(0.0001)
    GPIO.output(trig1,0)

    while GPIO.input(echo1) == 0:
        start = time.time()
    while GPIO.input(echo1) == 1:
        stop = time.time()

    tot_time = stop - start
    distance = tot_time / .00058
    print ("hi")
    print (distance)

    GPIO.cleanup()


