"""
https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
"""

def isMovesLeft(board):
	for i in range(3):
		for j in range(3) :
			if board[i][j] == '_':
				return True
	return False

def evaluate(b, player, opponent):
	"""Evaluates the score.

	10 is a win
	-10 is a loss
	0 is not a win or loss (could be a tie or non-terminal state of game)
	"""
	for row in range(3):
		if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
			if b[row][0] == player:
				return 10
			elif b[row][0] == opponent :
				return -10

	for col in range(3):
		if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
			if b[0][col] == player:
				return 10
			elif b[0][col] == opponent:
				return -10

	if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
		if b[0][0] == player:
			return 10
		elif b[0][0] == opponent:
			return -10

	if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
		if b[0][2] == player:
			return 10
		elif b[0][2] == opponent:
			return -10

	return 0

def minimax(board, isMax, player, opponent, alpha, beta) :
	score = evaluate(board, player, opponent)
	if score == 10:
		return score

	if score == -10:
		return score

	if isMovesLeft(board) == False:
		return 0

	if isMax:
		best = -1000
		for i in range(3):
			for j in range(3):
				if board[i][j] == '_':
					board[i][j] = player
					best = max(best, minimax(board, not isMax, player, opponent, alpha, beta))
					board[i][j] = '_'

					alpha = max(alpha, best)
					if beta <= alpha:
						break
		return best
	else:
		best = 1000
		for i in range(3):
			for j in range(3):
				if board[i][j] == '_':
					board[i][j] = opponent
					best = min(best, minimax(board, not isMax, player, opponent, alpha, beta))
					board[i][j] = '_'

					beta = min(beta, best)
					if beta <= alpha:
						break

		return best

def findBestMove(board, player):
	if player == "X":
		opponent = "O"
	else:
		opponent = "X"

	bestVal = -1000
	bestMove = (-1, -1)
	alpha = -float('inf')
	beta = float('inf')

	for i in range(3):
		for j in range(3):
			if board[i][j] == '_':
				board[i][j] = player
				moveVal = minimax(board, False, player, opponent, alpha, beta)
				board[i][j] = '_'

				if moveVal > bestVal: 
					bestMove = (i, j)
					bestVal = moveVal

	return bestMove


if __name__ == "__main__":
	board = [
	    [ 'X', 'O', 'X' ],
	    [ 'O', 'O', 'X' ],
	    [ '_', '_', '_' ]
	]
	bestMove = findBestMove(board, "X")
	print("The Optimal Move is :")
	print("ROW:", bestMove[0], " COL:", bestMove[1])