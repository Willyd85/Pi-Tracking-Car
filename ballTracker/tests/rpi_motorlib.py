"""
rpi motor lib tests

will + joe
"""


import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib
    
#define GPIO pins
GPIO_pins = (-1, -1, -1) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 16       # Direction -> GPIO Pin
step = 12      # Step -> GPIO Pin

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "DRV8825")


# call the function, pass the arguments
mymotortest.motor_go(False, "Full" , 2000, .001, False, .05)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
