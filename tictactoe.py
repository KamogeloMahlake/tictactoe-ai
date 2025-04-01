"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if len(actions(board)) % 2 == 0:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                possible_actions.add((i, j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    copy_board = deepcopy(board)
    if action not in actions(board):
        raise Exception

    elif board[i][j] is EMPTY:
        copy_board[i][j] = player(copy_board)
    else:
        raise Exception 
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        elif board[0][i] and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or len(actions(board)) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    match winner(board):
        case "X":
            return 1
        case "O":
            return -1
        case None:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == X:
        return max(board)[1]
    return min(board)[1]


def min(board):
    if terminal(board):
        return [utility(board), None]
    value = math.inf
    move = None

    for action in actions(board):
        x, _ = max(result(board, action))
        if x < value:
            value, move = x, action
            if value == -1:
                break
    return [value, move]


def max(board):
    if terminal(board):
        return [utility(board), None]
    
    value = -math.inf
    move = None

    for action in actions(board):
        x, _ = min(result(board, action))

        if x > value:
            value, move = x, action
            if value == 1:
                break
    return [value, move]
