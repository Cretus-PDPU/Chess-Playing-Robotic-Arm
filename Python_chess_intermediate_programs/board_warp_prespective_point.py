import cv2
import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))+"/numpy_saved"

iix,iiy = -1,-1
image = 0
def draw_circle(event,x,y,flags,param):
    global iix,iiy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image,(x,y),5,(255,0,0),-1)
        iix,iiy = x,y

def warp_prespective(img):
    global image
    image = img
    image = cv2.resize(image,(800,800))
    width,height = 800,800

    cv2.namedWindow("image")
    cv2.setMouseCallback('image',draw_circle)

    point_a=[]
    point_b=[]
    point_c=[]
    point_d=[]

    while(True):
        cv2.imshow("image",image)
        k = cv2.waitKey(1)
        if(k == ord('a')):
            point_a.append([iix,iiy])
        elif(k == ord('b')):
            point_b.append([iix,iiy])
        elif(k == ord('c')):
            point_c.append([iix,iiy])
        elif(k == ord('d')):
            point_d.append([iix,iiy])
        elif(k == ord('q')):
            break

    # print(point_a[-1][0],point_a[-1][1])
    pts1 = np.float32([[point_a[-1][1],point_a[-1][0]],[point_b[-1][1],point_b[-1][0]],[point_d[-1][1],point_d[-1][0]],[point_c[-1][1],point_c[-1][0]]])
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

    np.savez(dir_path+"/chess_board_warp_prespective.npz",pts1=pts1,pts2=pts2)

    # matrix = cv2.getPerspectiveTransform(pts1,pts2)
    # result = cv2.warpPerspective(img,matrix,(width,height))
    # cv2.imshow("result Image",result)

    # cv2.waitKey(0)
    cv2.destroyAllWindows()
    # return img 
