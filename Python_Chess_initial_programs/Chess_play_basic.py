import cv2
import numpy as np
import chess
import chess
import chess.engine

fen_line = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
board = chess.Board(fen=fen_line)

chess_board = []
current_player_bool_position = []

for row in fen_line.split('/'):
    bool_row = []
    chess_row = []
    for cell in list(row):
        # print(cell,cell.isnumeric())
        if cell.isnumeric():
            for i in range(int(cell)):
                # print("0",end=" ")
                chess_row.append(str(1))
                bool_row.append(0)
        else:
            # print(cell,end=" ")
            chess_row.append(cell)
            bool_row.append(1)
    # print(" ")
    chess_board.append(chess_row)
    current_player_bool_position.append(bool_row)
chess_board = np.array(chess_board)
current_player_bool_position = np.array(current_player_bool_position)
print(chess_board)
print(current_player_bool_position)

img1 = cv2.imread("Python_Chess_initial_programs/Images/4.jpg")
img2 = cv2.imread("Python_Chess_initial_programs/Images/4.jpg")

img1 = cv2.resize(img1,(800,800))
img2 = cv2.resize(img2,(800,800))

# points = [[[ 40.,35.],[132.,34.],[223.,32.],[314., 33.],[405. , 30.],[500. , 29.],[589. , 26.],[683. , 26.] ,[777. , 25.]],
#           [[ 38., 127.],[129., 126.],[221., 124.],[313., 123.],[405., 123.], [496., 121.],[589., 119.],[680., 118.],[774., 118.]],
#           [[36., 218.],[128., 217.],[220., 216.],[312., 215.],[403., 214.],[495., 212.],[588., 210.],[680., 210.],[773., 209.]],
#           [[33., 310.],[124., 309.],[219., 308.],[310., 307.],[400., 305.],[492., 302.],[584., 302.],[677., 301.],[772., 300.]],
#           [[ 32., 399.],[124., 398.],[216., 398.],[309., 395.],[400., 394.],[491., 394.],[583., 394.],[679., 393.],[771., 393.]],
#           [[ 28., 493.],[120., 489.],[214., 488.],[306., 486.],[399., 485.],[491., 483.],[584., 484.],[676., 483.],[769., 483.]],
#           [[ 27., 583.],[120., 582.],[212., 580.],[304., 579.],[396., 579.],[490., 576.],[583., 577.],[677., 576.],[772., 576.]],
#           [[ 24., 677.],[118., 675.],[210., 674.],[304., 672.],[396., 672.],[488., 670.],[583., 670.],[676., 670.],[768., 670.]],
#           [[ 24., 770.],[116., 770.],[209., 770.],[301., 767.],[395., 766.],[488., 766.],[582., 767.],[675., 765.],[769., 766.]]]

points = np.load('Python_chess_intermediate_programs/cess_board_points.npz')['points']

boxes = np.zeros((8,8,4))
for i in range(8):
    for j in range(8):
        # print(i,j)
        boxes[i][j][0] = points[i][j][0]
        boxes[i][j][1] = points[i][j][1]
        boxes[i][j][2] = points[i+1][j+1][0]
        boxes[i][j][3] = points[i+1][j+1][1]

img1_HSV = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
img2_HSV = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)

lower_1_w = np.array([16,25,179])
lower_2_w = np.array([255,255,255])

lower_1_b = np.array([0,0,0])
lower_2_b = np.array([255,62,77])

mask_w = cv2.inRange(img1_HSV, lower_1_w, lower_2_w)
mask_b = cv2.inRange(img1_HSV, lower_1_b, lower_2_b)

mask = cv2.bitwise_or(mask_b,mask_w)

kernel = np.ones((3,3),np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

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

bool_position = np.zeros((8,8),dtype=int)
for i in range(8):
    for j in range(8):
        cv2.putText(img1,"{}".format(chess_board[i][j]),(int(boxes[i][j][2]-20),int(boxes[i][j][3])-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
        for mid_point in required_contoures_mid_point:
            if(rectContains(boxes[i][j],mid_point)):
                cv2.rectangle(img1,(int(boxes[i][j][0]),int(boxes[i][j][1])),(int(boxes[i][j][2]),int(boxes[i][j][3])),(255,0,0),2)
                cv2.putText(img1,"({},{})".format(i,j),(int(boxes[i][j][2]-70),int(boxes[i][j][3])-50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
                bool_position[i][j] = 1
                continue
    
print(bool_position)
difference = bool_position - current_player_bool_position
print(difference)
position_of_negative = np.where(difference==-1)
position_of_positive = np.where(difference==1)
print("move from ",position_of_negative,"moces to",position_of_positive)
player =chess_board[position_of_negative]
chess_board[position_of_negative] = "1"
chess_board[position_of_positive] = player
print(chess_board)
cv2.imshow("img",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()