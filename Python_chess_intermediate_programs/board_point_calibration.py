import cv2
import numpy as np 
import os

dir_path = os.path.dirname(os.path.realpath(__file__))+"/numpy_saved"

ix = -1
iy = -1
img = 0
print("==================================================")

def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),2,(255,0,0),-1)
        ix,iy = x,y

def get_points(img):
    # img = cv2.imread("Python_Chess_initial_programs/Images/1.jpg")
    img = cv2.resize(img,(800,800))
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)

    i,j = 0,0
    points = np.zeros((9,9,2),dtype=int)
    while(True):
        cv2.imshow("image",img)
        k = cv2.waitKey(1)
        if(k == ord('a')):
            cv2.putText(img,"({},{})".format(ix,iy),(ix,iy+20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
            if(i == 9):
                break
            points[i][j][0]=ix
            points[i][j][1]=iy
            if(j == 8):
                i = (i+1)
            j = (j+1)%9

    np.savez(dir_path+"/chess_board_points.npz",points = points)
    # points = np.load('Python_chess_intermediate_programs/cess_board_points.npz')['points']
    print("Points save successfully")
    print("==================================================")

