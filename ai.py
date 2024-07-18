import math

# Initialize the board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check for available moves
def available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

# Check for a win
def check_win(board, player):
    # Check rows, columns and diagonals
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in win_conditions:
        if all(board[x][y] == player for x, y in condition):
            return True
    return False

# Check for a draw
def check_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Minimax algorithm with Alpha-Beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in available_moves(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move[0]][move[1]] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in available_moves(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move[0]][move[1]] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Get the best move for the AI
def best_move(board):
    best_eval = -math.inf
    move = None
    for m in available_moves(board):
        board[m[0]][m[1]] = 'O'
        eval = minimax(board, 0, False, -math.inf, math.inf)
        board[m[0]][m[1]] = ' '
        if eval > best_eval:
            best_eval = eval
            move = m
    return move

# Main game loop
def play_game():
    board = initialize_board()
    human = 'X'
    ai = 'O'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human move
        human_move = input("Enter your move (row and column): ").split()
        row, col = int(human_move[0]), int(human_move[1])
        if board[row][col] == ' ':
            board[row][col] = human
        else:
            print("Invalid move, try again.")
            continue

        print_board(board)
        if check_win(board, human):
            print("You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        # AI move
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = ai
            print("AI moves to:", ai_move)
            print_board(board)
            if check_win(board, ai):
                print("AI wins!")
                break
            if check_draw(board):
                print("It's a draw!")
                break

    # Pause the program to view the result before exiting
    input("Press Enter to exit...")

if __name__ == "__main__":
    play_game()


