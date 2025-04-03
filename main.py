from tic_tac_toe.logic.minimax import minimax
from tic_tac_toe.logic.models import GameState, Grid, Mark

import textwrap

def preview(cells):
    print(
        textwrap.dedent(
            """\
             A   B   C
           ------------
        1 ┆  {0} │ {1} │ {2}
          ┆ ───┼───┼───
        2 ┆  {3} │ {4} │ {5}
          ┆ ───┼───┼───
        3 ┆  {6} │ {7} │ {8}
    """
        ).format(*cells)
    )

game_state = GameState(Grid(" X "
                            "   "
                            "   "), starting_mark=Mark("X"))
for move in game_state.possible_moves:
    print("Score:", minimax(move, maximizer=Mark("X")))
    preview(move.after_state.grid.cells)
    print("-" * 10)