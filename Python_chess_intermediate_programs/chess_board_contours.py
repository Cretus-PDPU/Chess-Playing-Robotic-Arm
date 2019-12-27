import cv2
import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))+"/numpy_saved"

def rectContains(rect,mid_point):
    logic = rect[0]<mid_point[0]<rect[2] and rect[1]<mid_point[1]<rect[3]
    return logic

def find_conotours(mask):
    mask__1 = mask
    contours,_= cv2.findContours(mask__1,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    required_contoures = []
    required_contoures_mid_point = []
    cnt_rectangle = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if(area > 280):
            (x, y, w, h) = cv2.boundingRect(cnt)
            required_contoures.append(cnt)
            required_contoures_mid_point.append([x+int(w/2),y+int(h/2)])
            cnt_rectangle.append([x,y,w,h])
    
    boxes = np.load(dir_path+"/chess_board_Box.npz")["boxes"]
    return required_contoures,required_contoures_mid_point,cnt_rectangle

