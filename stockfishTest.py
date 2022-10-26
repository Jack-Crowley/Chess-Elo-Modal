from stockfish import Stockfish

stockfish = Stockfish("stockfish_15_x64_avx2.exe")

stockfish.set_depth(20)
stockfish.set_skill_level(20)