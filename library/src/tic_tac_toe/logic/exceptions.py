# tic-tac-toe/logic/exceptions.py

class InvalidMove(Exception):
    """Raised when the move is invalid."""


class InvalidGameState(Exception):
    """Raised when the game state is invalid."""


class UnknownGameScore(Exception):
    """Raised when the game score is unknown."""
