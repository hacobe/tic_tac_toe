import tqdm
import lib
import geeksforgeeks_minimax
import geeksforgeeks_alpha_beta_pruning


def _is_over(board):
	for r in range(3):
		if board[r][0] != "_" and board[r][0] == board[r][1] and board[r][1] == board[r][2]:
			return True

	for c in range(3):
		if board[0][c] != "_" and board[0][c] == board[1][c] and board[1][c] == board[2][c]:
			return True

	if board[0][0] != "_" and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
		return True

	if board[0][2] != "_" and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
		return True

	for r in range(3):
		for c in range(3):
			if board[r][c] == "_":
				return False

	return True


def _gen_next_boards(board, turn, boards):
	if _is_over(board):
		return

	for r in range(3):
		for c in range(3):
			if board[r][c] != "_":
				continue

			next_board = []
			for r2 in range(3):
				next_board.append([])
				for c2 in range(3):
					next_board[r2].append(board[r2][c2])

			next_board[r][c] = turn

			for r2 in range(3):
				next_board[r2] = tuple(next_board[r2])
			next_board = tuple(next_board)

			if turn == "X":
				next_turn = "O"
			else:
				next_turn = "X"

			boards.append((next_board, next_turn))
			_gen_next_boards(
				next_board,
				next_turn,
				boards)


def _gen_boards():
	empty_board = (
		("_", "_", "_"),
		("_", "_", "_"),
		("_", "_", "_"),
	)
	boards = [(empty_board, "X")]
	_gen_next_boards(empty_board, "X", boards)
	return boards


if __name__ == "__main__":
	boards = _gen_boards()

	# "Total states = 549946"
	# https://github.com/potter1024/Unbeatable-TicTacToe-Algorithm
	assert len(boards) == 549946

	board_strs = []
	for i in tqdm.tqdm(range(len(boards))):
		board, turn = boards[i]
		if _is_over(board):
			continue

		board = list(board)
		for r in range(3):
			board[r] = list(board[r])

		alpha_beta_pruning_best_move = geeksforgeeks_alpha_beta_pruning.findBestMove(board, turn)
		minimax_best_move = geeksforgeeks_minimax.findBestMove(board, turn)
		lib_best_move = lib.find_best_move(board, turn)

		assert lib_best_move == minimax_best_move
		assert lib_best_move == alpha_beta_pruning_best_move