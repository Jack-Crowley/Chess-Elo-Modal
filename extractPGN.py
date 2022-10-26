import chess.pgn

pgn = open("test.pgn")

first_game = chess.pgn.read_game(pgn)
second_game = chess.pgn.read_game(pgn)

first_game.headers["Event"]

 # Iterate through all moves and play them on a board.
board = first_game.board()
for move in first_game.mainline_moves():
    print(move)
    board.push(move)
    boardsvg = chess.svg.board(board, size=700) 
    outputfile = open('display.svg', "w")
    outputfile.write(boardsvg)
    outputfile.close()
    input()