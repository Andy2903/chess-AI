import chess
import random

debug = {}


def next_move(board):
    '''
    What is the next best move?
    '''
    return random.choice(list(board.legal_moves))

# next_move(chess.Board())
