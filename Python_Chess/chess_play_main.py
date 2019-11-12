import chess
import chess.engine

# create a board instance
board = chess.Board()

engine = chess.engine.SimpleEngine.popen_uci("Python_Chess\stockfish-10-win\Windows\stockfish_10_x64.exe")

while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.400))
    print("result :",result)
    print("result.move :",result.move)
    board.push(result.move)
    print(board,"\n\n")
engine.quit()