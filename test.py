import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("stockfish_15_x64_avx2.exe")

pgn = open("./test.pgn")
board = chess.Board("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1")

# # Limit our search so it doesn't run forever
# info = engine.analyse(board, chess.engine.Limit(depth=20))

# Get the 3 best moves
info = engine.analyse(board, chess.engine.Limit(depth=20), multipv=1)

for i in info:
    print(i)

# # Info is now an array with at most 3 elements
# # If there aren't 3 valid moves, the array would have less than 3 elements
# print(info[0])
# print(info[1])
# print(info[2])

engine.quit()