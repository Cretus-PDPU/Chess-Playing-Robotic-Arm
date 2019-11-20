import cv2
import numpy as np
import os
dir_path = os.path.dirname(os.path.realpath(__file__))+"/numpy_saved"


def find_mask(img):
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower__w =  np.load(dir_path+"/chess_w_color_points.npz")['lower']
    upper__w = np.load(dir_path+"/chess_w_color_points.npz")['upper']
    lower__b =  np.load(dir_path+"/chess_b_color_points.npz")['lower']
    upper__b = np.load(dir_path+"/chess_b_color_points.npz")['upper']

    mask_w = cv2.inRange(img_hsv,lower__w,upper__w)
    mask_b = cv2.inRange(img_hsv,lower__b,upper__b)

    mask = cv2.bitwise_or(mask_b,mask_w)

    kernel = np.ones((3,3),np.uint8)

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)  

    return mask