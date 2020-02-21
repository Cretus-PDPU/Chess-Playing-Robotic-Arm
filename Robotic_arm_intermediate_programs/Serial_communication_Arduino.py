import serial
import time

def send_data(angle1,angle2,angle3,angle4):
    serialcomm = serial.Serial('COM8', 1000000)
    time.sleep(3)

    angle1 = str(angle1)
    angle2 = str(angle2)
    angle3 = str(angle3)
    angle4 = str(angle4)

    i1 = "1"+angle1
    serialcomm.write(i1.encode())
    print("Data From arduino : ",serialcomm.readline())

    time.sleep(3)

    i2 = "2"+angle2
    serialcomm.write(i2.encode())
    print("Data From arduino : ",serialcomm.readline())

    time.sleep(3)

    i3 = "3"+angle3
    serialcomm.write(i3.encode())
    print("Data From arduino : ",serialcomm.readline())

    time.sleep(3)

    i4 = "4"+angle4
    serialcomm.write(i4.encode())
    print("Data From arduino : ",serialcomm.readline())
    
    time.sleep(3)

    serialcomm.close()


