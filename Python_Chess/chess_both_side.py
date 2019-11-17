import cv2
import numpy as np
import chess
import chess
import chess.engine

fen_line = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
board = chess.Board(fen=fen_line)

# chess_board = []
# past_player_position = []
# 
# for row in fen_line.split('/'):
#     for cell in list(row):
#         # print(cell,cell.isnumeric())
#         if cell.isnumeric():
#             for i in range(int(cell)):
#                 # print("0",end=" ")
#                 chess_board.append(str(1))
#                 past_player_position.append(0)
#         else:
#             # print(cell,end=" ")
#             chess_board.append(cell)
#             past_player_position.append(1)
#     # print(" ")
# print(chess_board)
# print(past_player_position)


# move = list(board.legal_moves)[1]
# board.push(move)
# fen = board.fen().split(" ")[0]
# print(fen)
# current_player_position = []
# chess_board_current = []

# for row in fen.split('/'):
#     for cell in list(row):
#         if cell.isnumeric():
#             for i in range(int(cell)):
#                 print("0",end=" ")
#                 chess_board_current.append(str(1))
#                 current_player_position.append(0)
#         else:
#             print(cell,end=" ")
#             chess_board_current.append(cell)
#             current_player_position.append(1)

# print(current_player_position)
# # print(current_player_position)

# diff_mat = [a_i - b_i for a_i, b_i in zip(current_player_position, past_player_position)]
# print(diff_mat)
# #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0]

img = cv2.imread("Python_Chess/Images/7.jpg")
img = cv2.resize(img,(800,800))
cv2.imshow("img",img)

HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


lower_1_w = np.array([16,25,179])
lower_2_w = np.array([255,255,255])

mask_w = cv2.inRange(HSV, lower_1_w, lower_2_w)
cv2.imshow("mask",mask_w)
cv2.waitKey(0)
lower_1_b = np.array([0,0,0])
lower_2_b = np.array([255,62,77])

mask_b = cv2.inRange(HSV, lower_1_b, lower_2_b)
cv2.imshow("mask",mask_b)
cv2.waitKey(0)
mask = cv2.bitwise_or(mask_b,mask_w)
kernel = np.ones((3,3),np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
cv2.imshow("mask",mask)
print(mask_w)
print(mask_b)
cv2.waitKey(0)

points = [[[ 40.,35.],[132.,34.],[223.,32.],[314., 33.],[405. , 30.],[500. , 29.],[589. , 26.],[683. , 26.] ,[777. , 25.]],
          [[ 38., 127.],[129., 126.],[221., 124.],[313., 123.],[405., 123.], [496., 121.],[589., 119.],[680., 118.],[774., 118.]],
          [[36., 218.],[128., 217.],[220., 216.],[312., 215.],[403., 214.],[495., 212.],[588., 210.],[680., 210.],[773., 209.]],
          [[33., 310.],[124., 309.],[219., 308.],[310., 307.],[400., 305.],[492., 302.],[584., 302.],[677., 301.],[772., 300.]],
          [[ 32., 399.],[124., 398.],[216., 398.],[309., 395.],[400., 394.],[491., 394.],[583., 394.],[679., 393.],[771., 393.]],
          [[ 28., 493.],[120., 489.],[214., 488.],[306., 486.],[399., 485.],[491., 483.],[584., 484.],[676., 483.],[769., 483.]],
          [[ 27., 583.],[120., 582.],[212., 580.],[304., 579.],[396., 579.],[490., 576.],[583., 577.],[677., 576.],[772., 576.]],
          [[ 24., 677.],[118., 675.],[210., 674.],[304., 672.],[396., 672.],[488., 670.],[583., 670.],[676., 670.],[768., 670.]],
          [[ 24., 770.],[116., 770.],[209., 770.],[301., 767.],[395., 766.],[488., 766.],[582., 767.],[675., 765.],[769., 766.]]]

boxes = np.zeros((8,8,4))

for i in range(8):
    for j in range(8):
        # print(i,j)
        boxes[i][j][0] = points[i][j][0]
        boxes[i][j][1] = points[i][j][1]
        boxes[i][j][2] = points[i+1][j+1][0]
        boxes[i][j][3] = points[i+1][j+1][1]


contours,_= cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

required_contoures = []
required_contoures_mid_point = []
cnt_rect = []

for cnt in contours:
    area = cv2.contourArea(cnt)
    if(area > 300):
        (x, y, w, h) = cv2.boundingRect(cnt)
        required_contoures.append(cnt)
        required_contoures_mid_point.append([x+int(w/2),y+int(h/2)])

def rectContains(rect,mid_point):
    logic = rect[0]<mid_point[0]<rect[2] and rect[1]<mid_point[1]<rect[3]
    return logic

for i in range(8):
    for j in range(8):
        for mid_point in required_contoures_mid_point:
            if(rectContains(boxes[i][j],mid_point)):
                cv2.rectangle(img,(int(boxes[i][j][0]),int(boxes[i][j][1])),(int(boxes[i][j][2]),int(boxes[i][j][3])),(255,0,0),2)
                cv2.putText(img,"({},{})".format(i,j),(int(boxes[i][j][2]-70),int(boxes[i][j][3])-50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
cv2.imshow("img",img)


cv2.waitKey(0)
cv2.destroyAllWindows()

