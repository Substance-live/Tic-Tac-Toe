# tic-tac-toe/logic/validators.py
from __future__ import annotations

import re

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tic_tac_toe.logic.models import Grid, GameState, Mark

from tic_tac_toe.logic.exceptions import InvalidGameState


def validate_grid(grid: Grid) -> None:
    if not re.match(r"^[\sXO]{9}$", grid.cells):
        raise ValueError("Must contain 9 cells of: X, O, or space")


def validate_game_state(game_state: GameState) -> None:
    validate_number_of_marks(game_state.grid)
    validate_starting_mark(game_state.grid, game_state.starting_mark)
    validate_winner(game_state.grid, game_state.starting_mark, game_state.winner)


def validate_number_of_marks(grid: Grid) -> None:
    if abs(grid.x_count - grid.o_count) > 1:
        raise InvalidGameState("Wrong numbers of Xs ans Os")


def validate_starting_mark(grid: Grid, start_mark: Mark):
    if grid.x_count > grid.o_count:
        if start_mark != 'X':
            raise InvalidGameState("Wrong start mark")
    elif grid.x_count < grid.o_count:
        if start_mark != 'O':
            raise InvalidGameState("Wrong start mark")


def validate_winner(grid: Grid, start_mark: Mark, winner: Mark) -> None:
    if winner == 'X':
        if start_mark == 'X':
            if grid.x_count <= grid.o_count:
                raise InvalidGameState("Wrong numbers of Xs")
        else:
            if grid.x_count != grid.o_count:
                raise InvalidGameState("Wrong numbers of Xs")
    elif winner == 'O':
        if start_mark == 'O':
            if grid.x_count >= grid.o_count:
                raise InvalidGameState("Wrong numbers of Os")
        else:
            if grid.x_count != grid.o_count:
                raise InvalidGameState("Wrong numbers of Os")
