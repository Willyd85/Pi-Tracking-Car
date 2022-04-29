"""
Will + Joe
"""

import asyncio
import RPi.GPIO as GPIO


class wheelMotor:
    """
    Defines a wheel motor
    """

    def __init__(self, _steppin: int, _dirpin: int):
        self.steppin = _steppin
        self.dirpin = _dirpin

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.steppin, GPIO.OUT)
        GPIO.setup(self.dirpin, GPIO.OUT)

    async def run(self, dir=True, step=2000, delay=0.001):
        """
        Runs the motor async
        """
        i=0
        
        while i<step: #TODO: CHANGEME
            GPIO.output(self.dirpin, dir)

            #TODO: Optimize this
            GPIO.output(self.steppin, True)
            await asyncio.sleep(delay)
            GPIO.output(self.steppin, False)
            await asyncio.sleep(delay)

            i=i+1
