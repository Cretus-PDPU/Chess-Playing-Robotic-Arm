import cv2

device = cv2.VideoCapture(1)

while True:
    ret,img = device.read()
    if ret:
        cv2.imshow("video",img)
        if cv2.waitKey(1) == ord('q'):
                break
