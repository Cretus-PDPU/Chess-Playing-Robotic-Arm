import cv2

devicve = cv2.VideoCapture(0)

_,img = devicve.read()
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()