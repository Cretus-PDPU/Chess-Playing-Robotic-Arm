import cv2
import numpy as np

def nothing(X):
    pass

cv2.namedWindow("calibration")
cv2.createTrackbar("H_L", "calibration", 0, 179, nothing)
cv2.createTrackbar("S_L", "calibration", 0, 255, nothing)
cv2.createTrackbar("V_L", "calibration", 0, 255, nothing)
cv2.createTrackbar("R_L", "calibration", 0, 255, nothing)
cv2.createTrackbar("G_L", "calibration", 0, 255, nothing)
cv2.createTrackbar("B_L", "calibration", 0, 255, nothing)

img = cv2.imread("Python_Chess/Images/1.jpg")
img = cv2.resize(img,(600,600))     

while True:
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    H = cv2.getTrackbarPos("H_L", "calibration")
    S = cv2.getTrackbarPos("S_L", "calibration")
    V = cv2.getTrackbarPos("V_L", "calibration")
    R = cv2.getTrackbarPos("R_L", "calibration")
    G = cv2.getTrackbarPos("G_L", "calibration")
    B = cv2.getTrackbarPos("B_L", "calibration")

    lower_1 = np.array([H,S,V])
    lower_2 = np.array([B,G,R])

    mask1 = cv2.inRange(HSV, lower_1, lower_2)

    res_1 = cv2.bitwise_and(img, img, mask=mask1)
    cv2.imshow("result",res_1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()