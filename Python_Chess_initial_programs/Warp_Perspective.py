import cv2
import numpy as np

img = cv2.imread("Python_Chess_initial_programs/Images/1.jpg")
img = cv2.resize(img,(800,800))

width,height = 800,800

ix,iy = -1,-1
def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(255,0,0),-1)
        ix,iy = x,y

cv2.namedWindow("image")
cv2.setMouseCallback('image',draw_circle)

point_a=[]
point_b=[]
point_c=[]
point_d=[]

while(True):
    cv2.imshow("image",img)
    k = cv2.waitKey(1)
    if(k == ord('a')):
        point_a.append([ix,iy])
    elif(k == ord('b')):
        point_b.append([ix,iy])
    elif(k == ord('c')):
        point_c.append([ix,iy])
    elif(k == ord('d')):
        point_d.append([ix,iy])
    elif(k == ord('q')):
        break
# print(point_a[-1][0],point_a[-1][1])
pts1 = np.float32([[point_a[-1][1],point_a[-1][0]],[point_b[-1][1],point_b[-1][0]],[point_d[-1][1],point_d[-1][0]],[point_c[-1][1],point_c[-1][0]]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
result = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("result Image",result)

cv2.waitKey(0)
cv2.destroyAllWindows()
