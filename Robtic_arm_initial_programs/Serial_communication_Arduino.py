import serial
import time

serialcomm = serial.Serial('COM6', 1000000)
serialcomm.timeout = 1

while True:
    i = str(input("Enter ID: ").strip())
    serialcomm.write(i.encode())
    time.sleep(1)
    print(serialcomm.readline())

    i = str(input("Enter angle: ").strip())
    serialcomm.write(i.encode())
    time.sleep(1)
    print(serialcomm.readline())

serialcomm.close()


