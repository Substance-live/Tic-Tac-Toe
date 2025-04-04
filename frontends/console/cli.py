# frontends/console/cli.py

from tic_tac_toe.game.engine import TicTacToe

from .args import parse_args
from .renderers import ConsoleRenderer

def main() -> None:
    player1, player2, start_mark = parse_args()
    TicTacToe(player1, player2, ConsoleRenderer()).play(start_mark)
