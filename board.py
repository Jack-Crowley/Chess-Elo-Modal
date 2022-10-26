import chess
import chess.svg

board = chess.Board()

while not board.is_checkmate():
    boardsvg = chess.svg.board(board, size=700) 
    outputfile = open('display.svg', "w")
    outputfile.write(boardsvg)
    outputfile.close()
    x=input()
    while len(x) != 4 or chess.Move.from_uci(x) not in list(board.legal_moves):
        x=input("Invalid Move - Try Again: ")
    board.push(chess.Move.from_uci(x))
outputfile = open('display.svg', "w")
outputfile.write("Checkmate")
outputfile.close()