from enums import Player, Board, GUI
from connect_four_logic import ConnectFour
import math
import random
import copy


EMPTY = 0
AI_PIECE = Player.YELLOW.value
WINDOW_LENGTH = 4


def evaluate_window(window, piece):
	score = 0
	opp_piece = Player.RED.value
	if piece == Player.RED.value:
		opp_piece = AI_PIECE

	if window.count(piece) == 4:
		score += 100
	elif window.count(piece) == 3 and window.count(EMPTY) == 1:
		score += 5
	elif window.count(piece) == 2 and window.count(EMPTY) == 2:
		score += 2

	if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
		score -= 4

	return score


def score_position(board, piece):
	score = 0

	## Score center column
	center_array = [int(i) for i in list(board[:, Board.COL.value//2])]
	center_count = center_array.count(piece)
	score += center_count * 3

	## Score Horizontal
	for r in range(Board.ROW.value):
		row_array = [int(i) for i in list(board[r,:])]
		for c in range(Board.COL.value-3):
			window = row_array[c:c+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score Vertical
	for c in range(Board.COL.value):
		col_array = [int(i) for i in list(board[:,c])]
		for r in range(Board.ROW.value-3):
			window = col_array[r:r+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score posiive sloped diagonal
	for r in range(Board.ROW.value-3):
		for c in range(Board.COL.value-3):
			window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	for r in range(Board.ROW.value-3):
		for c in range(Board.COL.value-3):
			window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	return score


def is_terminal_node(board: ConnectFour):
	return board.is_game_over(Player.RED.value) or board.is_game_over(AI_PIECE) or len(get_valid_locations(board)) == 0


def minimax(board: ConnectFour, depth, alpha, beta, maximizingPlayer):
	valid_locations = get_valid_locations(board)
	is_terminal = is_terminal_node(board)
	if depth == 0 or is_terminal:
		if is_terminal:
			if board.is_game_over(AI_PIECE):
				return (None, 100000000000000)
			elif board.is_game_over(Player.RED.value):
				return (None, -10000000000000)
			else: # Game is over, no more valid moves
				return (None, 0)
		else: # Depth is zero
			return (None, score_position(board, AI_PIECE))
	if maximizingPlayer:
		value = -math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			b_copy = copy.deepcopy(board)
			b_copy.drop(col, AI_PIECE)
			new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
			if new_score > value:
				value = new_score
				column = col
			alpha = max(alpha, value)
			if alpha >= beta:
				break
		return column, value

	else: # Minimizing player
		value = math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			b_copy = copy.deepcopy(board)
			b_copy.drop(col, Player.RED.value)
			new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
			if new_score < value:
				value = new_score
				column = col
			beta = min(beta, value)
			if alpha >= beta:
				break
		return column, value


def get_valid_locations(board):
	board = board.board
	valid_locations = []
	for col in range(Board.COL.value):
		if board[Board.ROW.value-1][col] == EMPTY:
			valid_locations.append(col)
	return valid_locations
