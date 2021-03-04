import chess
import random
import operator

DEPTH = 7
MAXVALUE = 9999
SAVED_MOVE = None

def next_move(board):
	"""
	What is the next best move?
	"""
	calculate_material(board)

	max(board, DEPTH, -MAXVALUE, MAXVALUE)
	if SAVED_MOVE is None:
		print("No moves found")
	else:
		print("Saved move", SAVED_MOVE)
	return SAVED_MOVE

def calculate_material(board):
	"""
	How is the material?
	"""

	material_values = {
		chess.PAWN: 1,
		chess.ROOK: 5,
		chess.KNIGHT: 3,
		chess.BISHOP: 3,
		chess.QUEEN: 9,
		chess.KING: 0,
	}
	black = 0
	white = 0

	if board.is_game_over():
		if board.result() == "1-0":
			return 999
		elif board.result() == "0-1":
			return - 999
		elif board.result() == "1/2-1/2":
			return 0

	for piece in board.piece_map().values():
		if piece.color == chess.WHITE:
			white += material_values[piece.piece_type]
		else:
			black += material_values[piece.piece_type]

	return white - black

def max(board, depth, alpha, beta):
	global SAVED_MOVE
	global DEPTH
	if depth == 0 or not board.legal_moves:
		return calculate_material(board)
	max_value = alpha
	for move in board.legal_moves:
		board.push(move)
		value = min(board, depth-1, max_value, beta)
		board.pop()
		if (value > max_value):
			max_value = value
			if depth == DEPTH:
				SAVED_MOVE = move
			if max_value >= beta:
				break
	return max_value

def min(board, depth, alpha, beta):
	if depth == 0 or not board.legal_moves:
		return calculate_material(board)
	min_value = beta
	for move in board.legal_moves:
		board.push(move)
		value = max(board, depth - 1, alpha, min_value)
		board.pop()
		if value < min_value:
			min_value = value
			if min_value <= alpha:
				break
	return min_value

board = chess.Board("8/8/3r1p2/k5p1/4N3/4P3/8/2K5 w - - 0 1")
next_move(chess.Board())
