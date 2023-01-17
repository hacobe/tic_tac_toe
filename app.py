import lib
from flask import Flask, render_template_string, request, make_response

app = Flask(__name__)

TEXT = """
<!doctype html>
<html>
  <head><title>Tic Tac Toe</title></head>
  <body>
    <h1>Tic Tac Toe</h1>
    <h2>{{msg}}</h2>
    <form action="" method="POST">
      You're playing as: {{player}}
      <button type="submit" name="change_player" {{"" if allow_player_choice else "disabled"}}>
        Change your player
      </button>
      <table>
        {% for r in range(0, 3) %}
        <tr>
          {% for c in range(0, 3) %}
          <td>
            <button
              type="submit"
              name="choice"
              value="{{ttt.move_to_index(r, c)}}"
              {{"" if board[r][c] == empty_marker and is_undecided else "disabled"}} >
 				       {{board[r][c]}}
            </button>
          </td>
          {% endfor %}
        </tr>
        {% endfor %}
      </table>
      <button type="submit" name="reset">Start Over</button>
    </form>
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
  ttt = lib.TicTacToe()

  player = request.cookies.get("player")
  if player:
    other_player = lib._get_other_player(player)
  else:
    player = lib.PLAYER1
    other_player = lib.PLAYER2

  board_str = request.cookies.get("board")
  if board_str:
    ttt.set_board_from_string(board_str)

  msg = "play move"
  allow_player_choice = True
  outcome = lib.UNDECIDED

  if "choice" in request.form:
    move_index = int(request.form["choice"])
    r, c = ttt.index_to_move(move_index)

    outcome = ttt.evaluate()
    if outcome == lib.UNDECIDED:
      ttt.play_move(r, c, player)

    outcome = ttt.evaluate()
    if outcome == lib.UNDECIDED:
      ttt.play_best_move(other_player)

    outcome = ttt.evaluate()
    if outcome == player:
      msg = "{0} wins".format(player)
    elif outcome == other_player:
      msg = "{0} wins".format(other_player)
    elif outcome == lib.TIE:
      msg = "X and O tie"

    allow_player_choice = False
  elif "reset" in request.form:
    ttt.reset()
    player = lib.PLAYER1
  elif "change_player" in request.form:
    player = other_player
    if player == lib.PLAYER2:
      ttt.play_best_move(lib.PLAYER1)
    allow_player_choice = False

  is_undecided = (outcome == lib.UNDECIDED)
  resp = make_response(
    render_template_string(
      TEXT, ttt=ttt, board=ttt.get_board(), player=player,
      msg=msg, allow_player_choice=allow_player_choice,
      is_undecided=is_undecided,
      empty_marker=lib.EMPTY))
  resp.set_cookie("board", ttt.board_to_string())
  resp.set_cookie("player", player)

  return resp