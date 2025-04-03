# tic_tac_toe/logic/minimax.py

from tic_tac_toe.logic.models import Mark, Move


def minimax(
    move: Move, maximizer: Mark, choose_highest_score: bool = False
) -> int:
    if move.after_state.game_over:
        return move.after_state.evaluate_score(maximizer)
    return (max if choose_highest_score else min)(
        minimax(next_move, maximizer, not choose_highest_score)
        for next_move in move.after_state.possible_moves
    )