import cv2
import numpy as np
import os
import chess_board_mask
import chess_board_contours
dir_path = os.path.dirname(os.path.realpath(__file__))+"/numpy_saved" 


def convert_to_bool(img):
    image = img
    mask = chess_board_mask.find_mask(image)
    required_contoures,required_contoures_mid_point,cnt_rectangle = chess_board_contours.find_conotours(mask)
    bool_position = np.zeros((8,8),dtype=int)
    boxes = np.load(dir_path+"/chess_board_Box.npz")["boxes"]
    for i in range(8):
        for j in range(8):
            # cv2.putText(img1,"{}".format(chess_board[i][j]),(int(boxes[i][j][2]-20),int(boxes[i][j][3])-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
            for mid_point in required_contoures_mid_point:
                if(chess_board_contours.rectContains(boxes[i][j],mid_point)):
                    # cv2.rectangle(img1,(int(boxes[i][j][0]),int(boxes[i][j][1])),(int(boxes[i][j][2]),int(boxes[i][j][3])),(255,0,0),2)
                    # cv2.putText(img1,"({},{})".format(i,j),(int(boxes[i][j][2]-70),int(boxes[i][j][3])-50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
                    bool_position[i][j] = 1
                    
    return bool_position

# device = cv2.VideoCapture("http://192.168.1.136:4812/video")
# ret , img = device.read()
# img  = img[582:582+1090,0:1078]
# img = cv2.resize(img,(800,800))
# print(convert_to_bool(img))

# cv2.imshow("img",img)
# cv2.waitKey(0)

# device = cv2.VideoCapture("http://192.168.1.136:4812/video")
# ret , img = device.read()
# img  = img[582:582+1090,0:1078]
# img = cv2.resize(img,(800,800))
# print(convert_to_bool(img))

# img = cv2.imread("Python_Chess_initial_programs/Images/4.jpg")
# img = cv2.resize(img,(800,800))
# print(convert_to_bool(img))

#     bool_position = np.zeros((8,8),dtype=int)
    # for i in range(8):
    #     for j in range(8):
    #         cv2.putText(img1,"{}".format(chess_board[i][j]),(int(boxes[i][j][2]-20),int(boxes[i][j][3])-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
    #         for mid_point in required_contoures_mid_point:
    #             if(rectContains(boxes[i][j],mid_point)):
    #                 cv2.rectangle(img1,(int(boxes[i][j][0]),int(boxes[i][j][1])),(int(boxes[i][j][2]),int(boxes[i][j][3])),(255,0,0),2)
    #                 cv2.putText(img1,"({},{})".format(i,j),(int(boxes[i][j][2]-70),int(boxes[i][j][3])-50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    #                 bool_position[i][j] = 1
    #                 continue
