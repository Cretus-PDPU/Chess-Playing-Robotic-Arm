import serial
import time
import numpy as np

serialcomm = serial.Serial('COM6', 1000000)
serialcomm.timeout = 1

def set_angle(servo_ID,servo_angle):

    servo_ID = str(servo_ID)
    servo_angle = str(servo_angle)

    serialcomm.write(servo_ID.encode())
    time.sleep(0.5)
    print(serialcomm.readline())

    serialcomm.write(servo_angle.encode())
    time.sleep(0.5)
    print(serialcomm.readline())

Angle_array = np.zeros((64,4),dtype=int)
