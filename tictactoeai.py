import math
import random

# Tic-Tac-Toe board representation
board = [' ' for _ in range(9)]

# Define the players
HUMAN = 'X'
AI = 'O'

# Function to display the Tic-Tac-Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the board is full
def is_full(board):
    return ' ' not in board

# Function to check if the game is over
def is_game_over(board):
    return check_winner(board, HUMAN) or check_winner(board, AI) or is_full(board)

# Function to check if a player has won
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to evaluate the current state of the board for the AI
def evaluate(board):
    if check_winner(board, AI):
        return 1
    elif check_winner(board, HUMAN):
        return -1
    else:
        return 0

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if check_winner(board, AI):
        return 1
    if check_winner(board, HUMAN):
        return -1
    if is_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = AI
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = HUMAN
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# AI's move using Minimax and Alpha-Beta Pruning
def ai_move(board):
    best_move = -1
    best_eval = -math.inf
    alpha = -math.inf
    beta = math.inf

    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            eval = minimax(board, 0, False, alpha, beta)
            board[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i

    return best_move

# Main game loop
while True:
    print_board(board)

    # Human's move
    while True:
        try:
            human_move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= human_move < 9 and board[human_move] == ' ':
                board[human_move] = HUMAN
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

    # Check if the game is over
    if is_game_over(board):
        print_board(board)
        if check_winner(board, HUMAN):
            print("You win!")
        elif check_winner(board, AI):
            print("AI wins!")
        else:
            print("It's a draw!")
        break

    # AI's move
    ai_move_index = ai_move(board)
    board[ai_move_index] = AI

    # Check if the game is over
    if is_game_over(board):
        print_board(board)
        if check_winner(board, HUMAN):
            print("You win!")
        elif check_winner(board, AI):
            print("AI wins!")
        else:
            print("It's a draw!")
        break
