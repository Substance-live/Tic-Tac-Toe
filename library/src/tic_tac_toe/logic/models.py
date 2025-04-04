# tic_tac_toe/logic/models.py
from __future__ import annotations

import enum
import re
from dataclasses import dataclass
from functools import cached_property

from tic_tac_toe.logic.validators import validate_grid, validate_game_state
from tic_tac_toe.logic.exceptions import InvalidMove, UnknownGameScore

WINNING_PATTERNS = (
    "???......",
    "...???...",
    "......???",
    "?..?..?..",
    ".?..?..?.",
    "..?..?..?",
    "?...?...?",
    "..?.?.?..",
)


class Mark(enum.StrEnum):
    CROSS = 'X'
    NAUGHT = 'O'

    @property
    def other(self) -> Mark:
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT


@dataclass(frozen=True)
class Grid:
    cells: str = " " * 9

    def __post_init__(self) -> None:
        validate_grid(self)

    @cached_property
    def x_count(self) -> int:
        return self.cells.count("X")

    @cached_property
    def o_count(self) -> int:
        return self.cells.count("O")

    @cached_property
    def empty_count(self) -> int:
        return self.cells.count(" ")


@dataclass(frozen=True)
class Move:
    mark: Mark
    cell_index: int
    before_state: GameState
    after_state: GameState


@dataclass(frozen=True)
class GameState:
    grid: Grid
    starting_mark: Mark = Mark('X')

    def __post_init__(self):
        validate_game_state(self)

    @cached_property
    def current_mark(self) -> Mark:
        return self.starting_mark if self.grid.x_count == self.grid.o_count else self.starting_mark.other

    @cached_property
    def game_not_started(self) -> bool:
        return self.grid.empty_count == 9

    @cached_property
    def game_over(self) -> bool:
        return self.winner is not None or self.tie

    @cached_property
    def tie(self) -> bool:
        return self.winner is None and self.grid.empty_count == 0

    @cached_property
    def winner(self) -> Mark | None:
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return mark
        return None

    @cached_property
    def winning_cells(self) -> list[int]:
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return [
                        match.start()
                        for match in re.finditer(r"\?", pattern)
                    ]
        return []

    @cached_property
    def possible_moves(self) -> list[Move]:
        moves = []
        if not self.game_over:
            for match in re.finditer(r"\s", self.grid.cells):
                moves.append(self.make_move_to(match.start()))

        return moves

    def make_move_to(self, index: int) -> Move:
        if self.grid.cells[index] != ' ':
            raise InvalidMove("Cell is not empty")

        return Move(
            mark=self.current_mark,
            cell_index=index,
            before_state=self,
            after_state=GameState(
                Grid(
                    self.grid.cells[:index] +
                    self.current_mark +
                    self.grid.cells[index + 1:]
                ),
                self.starting_mark,
            ),
        )

    def evaluate_score(self, mark: Mark) -> int:
        if self.game_over:
            if self.tie:
                return 0
            elif self.winner is mark:
                return 1
            else:
                return -1
        raise UnknownGameScore("Game isn't over yet")


if __name__ == '__main__':
    game_state = GameState(Grid("XXOXOX  O"))
    print(game_state.possible_moves)
