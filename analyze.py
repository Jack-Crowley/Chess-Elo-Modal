import chess
import chess.engine

#here we assume the engine file is in same folder as our python script
#Let's try our code with the starting position of chess:
fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
board = chess.Board(fen)
#Now make sure you give the correct location for your stockfish engine file
#...in the line that follows by correctly defining path
engine = chess.engine.SimpleEngine.popen_uci("stockfish_15_x64_avx2.exe")

if board.turn: print('White to move')
else: print('black to move')

for el in board.legal_moves:
    info = engine.analyse(board, chess.engine.Limit(time=1), root_moves=[el])
    t = str(info["score"])
    if t.startswith('#'):
            print(str(board.san(el))," eval = mate in ", t)
    else: print(str(board.san(el))," eval = ", round(int(t)/100.,2))
engine.quit()