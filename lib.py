EMPTY = "_"
BOARD_DIM = 3
PLAYER1 = "X"
PLAYER2 = "O"
TIE = "T"
UNDECIDED = "U"


def _get_other_player(player):
	if player == PLAYER1:
		return PLAYER2
	return PLAYER1


def _evaluate(board):
	for r in range(3):
		if board[r][0] != "_" and board[r][0] == board[r][1] and board[r][1] == board[r][2]:
			return board[r][0]

	for c in range(3):
		if board[0][c] != "_" and board[0][c] == board[1][c] and board[1][c] == board[2][c]:
			return board[0][c]

	if board[0][0] != "_" and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
		return board[0][0]

	if board[0][2] != "_" and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
		return board[0][2]

	for r in range(3):
		for c in range(3):
			if board[r][c] == "_":
				return UNDECIDED

	return TIE


def _get_best_move_and_score(board, player, alpha=-float('inf'), beta=float('inf')):
	other_player = _get_other_player(player)
	outcome = _evaluate(board)
	if outcome == player:
		return None, 1
	elif outcome == other_player:
		return None, -1
	elif outcome == TIE:
		return None, 0

	best_score = -float('inf')
	for r in range(BOARD_DIM):
		for c in range(BOARD_DIM): 
			if board[r][c] != EMPTY:
				continue
			board[r][c] = player
			_, score = _get_best_move_and_score(board, other_player, -beta, -alpha)
			score = -1 * score
			if score > best_score:
				best_score = score
				best_move = (r, c)
			board[r][c] = EMPTY
	
			alpha = max(alpha, best_score)
			if beta <= alpha:
				return best_move, best_score

	return best_move, best_score


def find_best_move(board, player):
	best_move, _ = _get_best_move_and_score(board, player)
	return best_move


class TicTacToe:

	def __init__(self):
		self.reset()

	def reset(self):
		self.board = []
		for i in range(BOARD_DIM):
			self.board.append([])
			for _ in range(BOARD_DIM):
				self.board[i].append(EMPTY)

	def get_board(self):
		return self.board

	def set_board(self, board):
		self.board = []
		for i in range(BOARD_DIM):
			self.board.append([])
			for j in range(BOARD_DIM):
				self.board[i].append(board[i][j])

	def set_board_from_string(self, board_str):
		self.board = []
		for line in board_str.split("\n"):
			self.board.append(line.split(","))

	def board_to_string(self):
		board_str = ""
		lines = []
		for r in range(BOARD_DIM):
			lines.append(",".join(self.board[r]))
		return "\n".join(lines)

	def move_to_index(self, r, c):
		return r * BOARD_DIM + c

	def index_to_move(self, index):
		c = index % BOARD_DIM
		r = index // BOARD_DIM
		return r, c

	def evaluate(self):
		return _evaluate(self.board)

	def play_move(self, r, c, player):
		if player != PLAYER1 and player != PLAYER2:
			raise ValueError("Invalid choice of player")

		if r < 0 or r >= BOARD_DIM:
			raise ValueError("Illegal move")

		if c < 0 or c >= BOARD_DIM:
			raise ValueError("Illegal move")

		if self.board[r][c] != EMPTY:
			raise ValueError("Illegal move")

		self.board[r][c] = player

	def play_best_move(self, player):
		r, c = find_best_move(self.board, player)
		self.play_move(r, c, player)

