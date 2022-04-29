"""
rpi motor lib tests

will + joe
"""


import RPi.GPIO as GPIO

from RpiMotorLib import RpiMotorLib
    

# All GPIO Pins
GPIO_pins = (-1, -1, -1)
l_motor_dir= 16
l_motor_step = 12

r_motor_dir= 25
r_motor_step = 24

l_motor = RpiMotorLib.A4988Nema(l_motor_dir, l_motor_step, GPIO_pins, "DRV8825")
r_motor = RpiMotorLib.A4988Nema(r_motor_dir, r_motor_step, GPIO_pins, "DRV8825")

# Run the motor for a set number of pulses
l_motor.motor_go(False, "Full" , 2000, .001, False, .05)
r_motor.motor_go(True, "Full" , 2000, .001, False, .05)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
