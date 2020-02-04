import cv2
import numpy as np
import chess 
board = chess.Board()

def fen2board(fen_line):
    chess_board = [] 
    for row in fen_line.split(' ')[0].split('/'):
        chess_row = []
        for cell in list(row):
            if cell.isnumeric():
                for i in range(int(cell)):
                    chess_row.append(str(' '))
            else:
                chess_row.append(cell)
        chess_board.append(chess_row)
    chess_board = np.array(chess_board)
    return chess_board

def map_move_to_number(move):
    map_num = 0
    for i in "12345678":
        for j in "abcdefgh":
            if move == str(j)+str(i):
                return map_num
            else:
                map_num += 1

img_1 = cv2.imread("1.jpg")
img_1 = cv2.resize(img_1,(800,800))     
side_img = np.zeros((800,800,3),dtype=np.uint8)
game_img = np.concatenate((img_1, side_img), axis=1)
overlay = game_img.copy()
cv2.putText(game_img,"Player Turn : ",(830,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
cv2.putText(game_img,"White ",(1050,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
# cv2.putText(game_img,"black ",(1050,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.putText(game_img,"Press",(830,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.putText(game_img,"'W'",(925,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
cv2.putText(game_img," when player moved ",(960,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)


padding_col = 0 
for i in fen2board(str(board.fen())):  
    padding_row = 0
    for j in i:
        if str(j).isupper():
            cv2.putText(game_img,"{}".format(j),(padding_row+850,padding_col+140),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        else:
            cv2.putText(game_img,"{}".format(j),(padding_row+850,padding_col+140),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        padding_row += 40
    padding_col += 40

print(board.piece_at(map_move_to_number("a1")))
player_move = "a1c2"
cv2.putText(game_img,"Opponent's last move : ",(830,480),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.putText(game_img,"{}".format(board.is_check()),(1210,480),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.putText(game_img,"is_check : ",(830,580),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.putText(game_img,"{}".format(board.is_check()),(1000,580),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.putText(game_img,"{}".format(board.piece_at(map_move_to_number(player_move[2:4]))),(830,530),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
cv2.putText(game_img," Moved from ",(850,530),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.putText(game_img,"{}".format(player_move[0:2]),(1070,530),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
cv2.putText(game_img," to ",(1100,530),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.putText(game_img,"{}".format(player_move[2:4]),(1155,530),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
cv2.rectangle(overlay, (420, 205), (595, 385),(0, 0, 255), -1)
cv2.addWeighted(overlay,0.3,game_img,0.7,0,game_img)

cv2.putText(game_img,"is_check mate : ",(830,620),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.putText(game_img,"{}".format(board.is_checkmate()),(1090,620),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
cv2.imshow('Game',game_img)
cv2.waitKey(0)