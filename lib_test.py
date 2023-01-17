import lib

import unittest


class TestLib(unittest.TestCase):

	def setUp(self):
		self.empty_board = [
			["_", "_", "_"],
			["_", "_", "_"],
			["_", "_", "_"]]
		self.board_str = "X,_,O\nO,_,_\n_,X,_"
		self.board = [
			["X", "_", "O"],
			["O", "_", "_"],
			["_", "X", "_"]]
		self.ttt = lib.TicTacToe()

	def test_init(self):
		ttt = lib.TicTacToe()
		self.assertEqual(ttt.get_board(), self.empty_board)

	def test_set_board(self):
		self.ttt.set_board(self.board)
		self.assertEqual(self.ttt.get_board(), self.board)

	def test_set_board_from_string(self):
		self.ttt.set_board_from_string(self.board_str)
		self.assertEqual(self.ttt.get_board(), self.board)

	def test_board_to_string(self):
		self.ttt.set_board_from_string(self.board_str)
		self.assertEqual(self.ttt.board_to_string(), self.board_str)

	def test_reset(self):
		self.ttt.set_board(self.board)
		self.ttt.reset()
		self.assertEqual(self.ttt.get_board(), self.empty_board)

	def test_move_to_index(self):
		self.assertEqual(self.ttt.move_to_index(1, 2), 5)

	def test_index_to_move(self):
		self.assertEqual(self.ttt.index_to_move(5), (1, 2))

	def test_evaluate_column_win(self):
		board = [
			["X", "X", "O"],
			["_", "X", "O"],
			["_", "_", "O"]]
		self.ttt.set_board(board)
		self.assertEqual(self.ttt.evaluate(), "O")

	def test_evaluate_row_win(self):
		board = [
			["O", "O", "O"],
			["_", "O", "X"],
			["_", "X", "X"]]
		self.ttt.set_board(board)
		self.assertEqual(self.ttt.evaluate(), "O")

	def test_evaluate_left_to_right_diag_win(self):
		board = [
			["O", "O", "X"],
			["_", "O", "X"],
			["_", "X", "O"]]
		self.ttt.set_board(board)
		self.assertEqual(self.ttt.evaluate(), "O")

	def test_evaluate_right_to_left_diag_win(self):
		board = [
			["_", "O", "O"],
			["_", "O", "X"],
			["O", "X", "X"]]
		self.ttt.set_board(board)
		self.assertTrue(self.ttt.evaluate(), "O")

	def test_evaluate_tie(self):
		board = [
			["O", "X", "O"],
			["O", "X", "X"],
			["X", "O", "X"]]
		self.ttt.set_board(board)
		self.assertEqual(self.ttt.evaluate(), "T")

	def test_evaluate_undecided(self):
		board = [
			["O", "X", "O"],
			["O", "X", "X"],
			["X", "O", "_"]]
		self.ttt.set_board(board)
		self.assertEqual(self.ttt.evaluate(), "U")

	def test_play_move(self):
		self.ttt.play_move(1, 2, "X")
		board = [
			["_", "_", "_"],
			["_", "_", "X"],
			["_", "_", "_"]]
		self.assertEqual(self.ttt.get_board(), board)

	def test_full_game_x(self):
		board = [
			["_", "_", "_"],
			["_", "_", "_"],
			["_", "_", "_"]]
		self.ttt.set_board(board)
		# X__
		# ___
		# ___
		self.ttt.play_best_move("X")
		# X__
		# __O
		# ___
		self.ttt.play_move(1, 2, "O")
		# X_X
		# __O
		# ___
		self.ttt.play_best_move("X")
		# XOX
		# __O
		# ___
		self.ttt.play_move(0, 1, "O")
		# XOX
		# _XO
		# ___
		self.ttt.play_best_move("X")
		# XOX
		# _XO
		# O__
		self.ttt.play_move(2, 0, "O")
		self.ttt.play_best_move("X")
		final_board = [
			["X", "O", "X"],
			["_", "X", "O"],
			["O", "_", "X"]]
		self.assertEqual(self.ttt.get_board(), final_board)

	def test_full_game_o(self):
		board = [
			["X", "_", "_"],
			["_", "_", "_"],
			["_", "_", "_"]]
		self.ttt.set_board(board)
		# X__
		# _O_
		# ___
		self.ttt.play_best_move("O")
		# X__
		# _O_
		# X__
		self.ttt.play_move(2, 0, "X")
		# X__
		# OO_
		# X__
		self.ttt.play_best_move("O")
		# X__
		# OOX
		# X__
		self.ttt.play_move(1, 2, "X")
		# XO_
		# OOX
		# X__
		self.ttt.play_best_move("O")
		# XO_
		# OOX
		# XX_
		self.ttt.play_move(2, 1, "X")
		# XO_
		# OOX
		# XXO
		self.ttt.play_best_move("O")
		self.ttt.play_move(0, 2, "X")
		final_board = [
			["X", "O", "X"],
			["O", "O", "X"],
			["X", "X", "O"]]
		self.assertEqual(self.ttt.get_board(), final_board)

	def test_play_best_move1(self):
		board = [
			["_", "_", "_"],
			["_", "_", "_"],
			["_", "_", "_"]]
		# All moves result in a tie if both players
		# play optimally, so the function chooses the
		# first move.
		next_board = [
			["X", "_", "_"],
			["_", "_", "_"],
			["_", "_", "_"]]
		self.ttt.set_board(board)
		self.ttt.play_best_move("X")
		self.assertEqual(self.ttt.get_board(), next_board)

	def test_play_best_move2_corner_x(self):
		board = [
			["X", "_", "_"],
			["_", "_", "_"],
			["_", "_", "_"]]
		# Any other move results in a loss if X plays
		# optimally.
		next_board = [
			["X", "_", "_"],
			["_", "O", "_"],
			["_", "_", "_"]]
		self.ttt.set_board(board)
		self.ttt.play_best_move("O")
		self.assertEqual(self.ttt.get_board(), next_board)

	def test_play_best_move2_border_middle_x(self):
		board = [
			["_", "_", "_"],
			["X", "_", "_"],
			["_", "_", "_"]]
		# If X players optimally, then O cannot win.
		# This is the first move where O can tie.
		next_board = [
			["O", "_", "_"],
			["X", "_", "_"],
			["_", "_", "_"]]
		self.ttt.set_board(board)
		self.ttt.play_best_move("O")
		self.assertEqual(self.ttt.get_board(), next_board)

	def test_play_best_move2_center_x(self):
		board = [
			["_", "_", "_"],
			["_", "X", "_"],
			["_", "_", "_"]]
		# If X players optimally, then O cannot win.
		# This is the first move where O can tie.
		next_board = [
			["O", "_", "_"],
			["_", "X", "_"],
			["_", "_", "_"]]
		self.ttt.set_board(board)
		self.ttt.play_best_move("O")
		self.assertEqual(self.ttt.get_board(), next_board)

	def test_play_best_move3_non_center_o(self):
		board = [
			["X", "_", "O"],
			["_", "_", "_"],
			["_", "_", "_"]]
		# This move guarantees a win for X.
		# O must block and then X goes in the center.
		next_board = [
			["X", "_", "O"],
			["X", "_", "_"],
			["_", "_", "_"]]
		self.ttt.set_board(board)
		self.ttt.play_best_move("X")
		self.assertEqual(self.ttt.get_board(), next_board)

	def test_play_best_move3_center_o(self):
		board = [
			["X", "_", "_"],
			["_", "O", "_"],
			["_", "_", "_"]]
		# All moves result in a tie if both players
		# play optimally, so the function chooses the
		# first move.
		next_board = [
			["X", "X", "_"],
			["_", "O", "_"],
			["_", "_", "_"]]
		self.ttt.set_board(board)
		self.ttt.play_best_move("X")
		self.assertEqual(self.ttt.get_board(), next_board)

	def test_play_best_move_losing_state(self):
		# This is a winning state of the board for X,
		# so all moves for O result in a loss.
		# O picks the "earliest" empty space on the
		# board. It doesn't care how quickly it wins
		# or loses, but rather just want the final
		# outcome is.
		board = [
			["X", "O", "_"],
			["_", "_", "_"],
			["X", "_", "_"]]
		next_board = [
			["X", "O", "O"],
			["_", "_", "_"],
			["X", "_", "_"]]
		self.ttt.set_board(board)
		self.ttt.play_best_move("O")
		self.assertEqual(self.ttt.get_board(), next_board)

	def test_play_best_move_block_win(self):
		board = [
			["X", "_", "_"],
			["_", "O", "_"],
			["X", "_", "_"]]
		next_board = [
			["X", "_", "_"],
			["O", "O", "_"],
			["X", "_", "_"]]
		self.ttt.set_board(board)
		self.ttt.play_best_move("O")
		self.assertEqual(self.ttt.get_board(), next_board)

	def test_play_best_move_take_win(self):
		board = [
			["X", "O", "_"],
			["_", "O", "_"],
			["X", "_", "_"]]
		next_board = [
			["X", "O", "_"],
			["X", "O", "_"],
			["X", "_", "_"]]
		self.ttt.set_board(board)
		self.ttt.play_best_move("X")
		self.assertEqual(self.ttt.get_board(), next_board)

	def test_play_best_move_fill_board(self):
		board = [
			["X", "X", "O"],
			["O", "O", "X"],
			["X", "O", "_"]]
		next_board = [
			["X", "X", "O"],
			["O", "O", "X"],
			["X", "O", "X"]]
		self.ttt.set_board(board)
		self.ttt.play_best_move("X")
		self.assertEqual(self.ttt.get_board(), next_board)