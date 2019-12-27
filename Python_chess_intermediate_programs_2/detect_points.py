import cv2
import numpy as np
# import os 

# dir_path = os.path.dirname(os.path.realpath(__file__))+"/numpy_saved"
ix,iy = -1,-1
img = 0 

def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),2,(255,0,0),-1)
        ix,iy = x,y

def get_points(image,numOfPoints):
    global img 
    img = image.copy()
    img = cv2.resize(img,(800,800))
    width, height = image.shape[:2]
    cv2.namedWindow("image")
    cv2.setMouseCallback("image",draw_circle)
    points = []
    while len(points) != numOfPoints:
        cv2.imshow("image",img)
        k = cv2.waitKey(1)
        if k == ord('a'):
            points.append([int(ix),int(iy)])

    cv2.destroyAllWindows()
    return list(points)
    # pts1 = np.float([[points[0][0],points[0][1]],
    #                 [points[1][0],points[1][1]],
    #                 [points[2][0],points[2][1]],
    #                 [points[3][0],points[3][1]]
    #                 ])
    # pts2 = np.float([[0,0],[width,0],[0,height],[width,height]])
    # np.savez(dir_path+"/chess_board_warp_prespective.npz",pts1=pts1,pts2=pts2)
    # H,maks = cv2.findHomography(pts1,pts2)
    # result = cv2.warpPerspective(img,H,(width,height))
    # print(result)