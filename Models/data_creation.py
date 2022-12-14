
import chess.pgn

pgn = open("test.pgn")

first_game = chess.pgn.read_game(pgn)
second_game = chess.pgn.read_game(pgn)

first_game.headers["Event"]

 # Iterate through all moves and play them on a board.

#f = open('Models/lichess_db_standard_rated_2013-01.pgn')

#print(len(f.readlines()))

pieces = {'wp1': 'a2', 'wp2': 'b2', 'wp3': 'c2', 'wp4': 'd2', 'wp5': 'e2', 'wp6': 'f2', 'wp7': 'g2', 'wp8': 'h2',
            'wr1': 'a1', 'wr2': 'h1', 'wn1': 'b1', 'wn2': 'g1', 'wb1': 'c1', 'wb2': 'f1', 'wq': 'd1', 'wk': 'e1',
            'bp1': 'h7', 'bp2': 'g7', 'bp3': 'f7', 'bp4': 'e7', 'bp5': 'd7', 'bp6': 'c7', 'bp7': 'b7', 'bp8': 'a7',
            'br1': 'h8', 'br2': 'a8', 'bn1': 'g8', 'bn2': 'b8', 'bb1': 'f8', 'bb2': 'c8', 'bq': 'd8', 'bk': 'e8'}

def capturePiece():
    pass

def updatePos(m):
    start, dest = m[0:2], m[2:4]
    for piece, pos in pieces.items():
        if pos == start:
            pieces[piece] = dest
        elif pos == dest:
            pieces[piece] = 'captured'

board = first_game.board()
for move in first_game.mainline_moves():
    updatePos(str(move))
    board.push(move)
print(pieces)