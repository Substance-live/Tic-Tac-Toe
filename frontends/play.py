# frontends/play.py

from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import RandomComputerPlayer
from tic_tac_toe.logic.models import Mark

from console.player import ConsolePlayer
from console.renderers import ConsoleRenderer

player1 = ConsolePlayer(Mark('O'))
player2 = RandomComputerPlayer(Mark('X'))

TicTacToe(player1, player2, ConsoleRenderer()).play()