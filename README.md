Start a local server to play Tic-Tac-Toe:

```bash
flask run
```

Run unit tests:

```bash
python -m unittest lib_test.py
```

Generate all possible Tic-Tac-Toe boards through brute force and check that the GeeksForGeeks implementations of Minimax and Alpha-Beta pruning give the same move for each board as the `get_best_move` method in lib.py:

```bash
python compare_strategies.py
```