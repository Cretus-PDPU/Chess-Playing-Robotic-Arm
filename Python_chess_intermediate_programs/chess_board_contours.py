# import cv2
# import numpy as np
# import os

# dir_path = os.path.dirname(os.path.realpath(__file__))+"/numpy_saved"

# def rectContains(rect,mid_point):
#     logic = rect[0]<mid_point[0]<rect[2] and rect[1]<mid_point[1]<rect[3]
#     return logic

# def find_conotours(mask):
#     mask__1 = mask
#     contours,_= cv2.findContours(mask__1,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#     required_contoures = []
#     required_contoures_mid_point = []
#     cnt_rect = []

#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if(area > 300):
#             (x, y, w, h) = cv2.boundingRect(cnt)
#             required_contoures.append(cnt)
#             required_contoures_mid_point.append([x+int(w/2),y+int(h/2)])
    
#     boxes = np.load(dir_path+"/chess_board_Box.npz")["boxes"]


#     bool_position = np.zeros((8,8),dtype=int)
#     for i in range(8):
#         for j in range(8):
#             cv2.putText(img1,"{}".format(chess_board[i][j]),(int(boxes[i][j][2]-20),int(boxes[i][j][3])-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
#             for mid_point in required_contoures_mid_point:
#                 if(rectContains(boxes[i][j],mid_point)):
#                     cv2.rectangle(img1,(int(boxes[i][j][0]),int(boxes[i][j][1])),(int(boxes[i][j][2]),int(boxes[i][j][3])),(255,0,0),2)
#                     cv2.putText(img1,"({},{})".format(i,j),(int(boxes[i][j][2]-70),int(boxes[i][j][3])-50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
#                     bool_position[i][j] = 1
#                     continue