import numpy as np
import random 
random.seed(1)

# Create a new board with value 0 in all positions
def create_board():
    board = np.zeros((3,3), dtype=int)
    return board

# create_board()

# Allow the player to mark a position by using a tuple len of 2
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
    return board

board = create_board()
# place(board, 1, (0,0))

def possibilities(board):
    not_occupied = np.where(board == 0)
    return list(zip(not_occupied[0], not_occupied[1]))

# print(possibilities(board))

def random_place(board, player):
    available = possibilities(board)
    if len(available) > 0:
        play = random.choice(available)
    place(board, player, play)
    return board

# board = create_board()

# for square in range(3):
#     for player in [1, 2]:
#         random_place(board, player)

# print(board)

def row_win(board, player):
    if np.any(np.all(board == player,axis=1)): 
        return True
    else:
        return False

# row_win(board, 1)

def col_win(board, player):
    if np.any(np.all(board==player,axis=0)):
        return True
    else:
        return False

# print(col_win(board, 1))

def diag_win(board, player):
    if np.any(np.diag(board)==player):
        return True
    else:
        return False
    
# print(diag_win(board, 1))

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if col_win(board, player) or row_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner -= 1
    return winner


# board[1,1] = 2
# print(evaluate(board))

def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
#    print(board)
    return winner

# def startegy

# board[1,1] = 2

results = [play_game() for i in range(0, 5)]

print(results.count(1))
