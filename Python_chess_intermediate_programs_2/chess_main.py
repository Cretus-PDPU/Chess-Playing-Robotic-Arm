###################################################################################
## Import Libraries
###################################################################################
import os
import chess
import chess.engine
import cv2
import numpy as np

###################################################################################
## Import files
###################################################################################
from design import design
from detect_points import get_points

###################################################################################
## Define Main Variables
###################################################################################
points = []    # contains chess board corners points
boxes = np.zeros((8,8,4),dtype=int)    # contains top-left and bottom-right point of chessboard boxes
fen_line = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR' # fen line of chess board
board = chess.Board(fen=fen_line) # object of chess board
dir_path = os.path.dirname(os.path.realpath(__file__))+"/numpy_saved" # path of current directory
device = cv2.VideoCapture(1) # set devidce for read image (1: for tacking input from usb-webcam)
img_resize = (800,800) # set o/p image size

###################################################################################
## camara position calibration
###################################################################################
while True:
    print("Do you want to set camara Position[y/n] : ",end=" ")
    answer = str(input())
    if answer == "y" or answer == "Y":
        while True:
            ## show frame from camera and set positon by moving camera
            flag , img = device.read()
            img = cv2.resize(img,img_resize)
            if flag:
                cv2.imshow("Set camera position",img)
                k = cv2.waitKey(1)
                if k == ord('q'):
                    cv2.destroyAllWindows()
                    break
        break
    elif answer == "n" or answer == "N":
        print("\nHope that camera position already set...\n")
        break
    else:
        print("Invalid Input ")



###################################################################################
## Image warp_presnpective
###################################################################################
while True:
    print("DO you want to warp prespective image[y/n] :",end=" ")
    answer = str(input())
    img = cv2.imread("Python_Chess_initial_programs/Images/1.jpg")
    img =   cv2.resize(img,(800,800))
    width,height = 800,800
    if answer == "y" or answer == "Y":
        warp_points = get_points(img,4)
        pts1 = np.float32([[warp_points[0][0],warp_points[0][1]],
                        [warp_points[1][0],warp_points[1][1]],
                        [warp_points[3][0],warp_points[3][1]],
                        [warp_points[2][0],warp_points[2][1]]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        np.savez(dir_path+"/chess_board_warp_prespective.npz",pts1=pts1,pts2=pts2)
        H,maks = cv2.findHomography(pts1,pts2)
        result = cv2.warpPerspective(img,H,(width,height))
        cv2.imshow("result",result)
        cv2.waitKey(0)


