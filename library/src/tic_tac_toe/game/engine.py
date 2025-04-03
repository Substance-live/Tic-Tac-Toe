# tic-tac-toe/game/engine.py

from dataclasses import dataclass

from tic_tac_toe.game.players import Player
from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.models import GameState, Grid, Mark
from tic_tac_toe.logic.exceptions import InvalidMove


@dataclass(frozen=True)
class TicTacToe:
    player1: Player
    player2: Player
    renderer: Renderer

    def play(self, start_mark: Mark = Mark('X')) -> None:
        game_state = GameState(Grid(), start_mark)
        while True:
            self.renderer.render(game_state)
            if game_state.game_over:
                break
            player = self.get_current_player(game_state)
            try:
                game_state = player.make_move(game_state)
            except InvalidMove:
                pass

    def get_current_player(self, game_state: GameState) -> Player:
        if game_state.current_mark is self.player1.mark:
            return self.player1
        else:
            return self.player2
