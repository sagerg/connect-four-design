from src.enums import Player, Board, GUI
from src.connect_four_logic import ConnectFour
import math
import random
import copy


EMPTY = 0
AI_PIECE = Player.YELLOW.value
WINDOW_LENGTH = 4


""" score_position helper
"""
def evaluate_window(window: list, piece: int) -> int:
	score = 0
	opponent = Player.RED.value

    # Make getting 4 in a row a priority
	if window.count(piece) == 4:
		score += 100
		
    # If 3 pieces connect, try to add the last winning piece
	elif window.count(piece) == 3 and window.count(EMPTY) == 1:
		score += 10
		
    # If 2 pieces connect, try to make moves to add 2 pieces
	elif window.count(piece) == 2 and window.count(EMPTY) == 2:
		score += 5

    # Block opponent from getting 4 in a row
	if window.count(opponent) == 3 and window.count(EMPTY) == 1:
		score -= 50

	return score


""" Give heuristic for Minimax
"""
def score_position(board: ConnectFour, piece: int) -> int:
	board: list[list[int]] = board.board
	score = 0

	## Score center column
	center_array = [board[i][Board.COL.value//2] for i in range(Board.ROW.value)]
	center_count = center_array.count(piece)
	score += center_count * 6

	## Score Horizontal
	for r in range(Board.ROW.value):
		row_array = [board[r][j] for j in range(Board.COL.value)]
		for c in range(Board.COL.value-3):
			window = row_array[c:c+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score Vertical
	for c in range(Board.COL.value):
		col_array = [board[i][c] for i in range(Board.ROW.value)]
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


""" Terminal node that checks if game has been won or there are no more moves to make
"""
def is_terminal_node(board: ConnectFour) -> bool:
	return board.is_game_over(Player.RED.value) or board.is_game_over(AI_PIECE) or len(get_valid_locations(board)) == 0


""" Minimax algorithm with Alpha-beta pruning
"""
def minimax(board: ConnectFour, depth, alpha, beta, maximizingPlayer: bool) -> tuple[int]:
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


""" Helper function for getting all possible columns that the player can drop a piece in
"""
def get_valid_locations(board):
	board: list[list[int]] = board.board
	valid_locations = []
	for col in range(len(board[0])):
		if board[0][col] == EMPTY:
			valid_locations.append(col)
	return valid_locations
