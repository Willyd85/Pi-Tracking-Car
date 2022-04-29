"""
Will + Joe
"""

import asyncio
import RPi.GPIO as GPIO

from RpiMotorLib import RpiMotorLib


class wheelMotor:
    """
    Defines a wheel motor
    """

    def __init__(self, _steppin: int, _dirpin: int):
        self.steppin = _steppin
        self.dirpin = _dirpin

        self.motor = RpiMotorLib.A4988Nema(self.dirpin, self.steppin, (-1, -1, -1), "DRV8825",)

    async def run(self, dir=True, step=2000, delay=0.001):
        """
        Runs the motor async
        """
        self.motor.motor_go(dir, "Full" , step, delay, False, .05,)
