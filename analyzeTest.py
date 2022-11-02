import chess
import chess.engine

def stockfish_evaluation(board, time_limit = 0.01):
    engine = chess.engine.SimpleEngine.popen_uci("stockfish_15_x64_avx2.exe")
    result = engine.analyse(board, chess.engine.Limit(time=time_limit))
    engine.quit()
    return result['score']

board = chess.Board("nnbqkbnr/ppppqppp/8/8/8/8/PPPPPPPP/NNBQKBNR w KQkq - 0 1")
result = stockfish_evaluation(board)
print(result)