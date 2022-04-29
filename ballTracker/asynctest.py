import asyncio

from hardware.wheel_motor import wheelMotor


async def main():
    left_motor = wheelMotor(12, 16)
    right_motor = wheelMotor(24, 25)


    leftMotorTask = asyncio.create_task(
            left_motor.run())

    rightMotorTask = asyncio.create_task(
            right_motor.run())

    await leftMotorTask
    await rightMotorTask

asyncio.run(main())
