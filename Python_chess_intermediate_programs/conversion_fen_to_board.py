import numpy as np
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))+"/numpy_saved"

def fen2board(fen_line):
    chess_board = []
    current_player_bool_position = []
    for row in fen_line.split(' ')[0].split('/'):
        bool_row = []
        chess_row = []
        for cell in list(row):
            if cell.isnumeric():
                for i in range(int(cell)):
                    chess_row.append(str(1))
                    bool_row.append(0)
            else:
                chess_row.append(cell)
                bool_row.append(1)
        chess_board.append(chess_row)
        current_player_bool_position.append(bool_row)
    chess_board = np.array(chess_board)
    current_player_bool_position = np.array(current_player_bool_position)
    np.savez(dir_path+"/ches_board.npz",chess_board = chess_board)

def board2fen():
    board_array = np.load(dir_path+"/ches_board.npz")["chess_board"]
    fen_line = ''
    count = 0
    for i in range(8):
        empty = 0
        for j in range(8):
            if board_array[i][j].isnumeric():
                empty+=1
            else:
                if empty != 0:
                    fen_line+= str(empty)+ str(board_array[i][j])
                    empty = 0
                else:
                    fen_line += str(board_array[i][j])
        if empty != 0:
            fen_line += str(empty)
        if count != 7:
            fen_line += str('/')
            count +=1
    fen_line += " w KQkq - 0 1"
    return fen_line