import time

class Player:
    Human = -1
    Blank = 0
    Computer = 1

def print_board(board):
    print()
    for i in range(9):
        if (i == 2) or (i == 5) or (i == 8):
            if board[i] == Player.Human:
                print(" X", end="")
            elif board[i] == Player.Computer:
                print(" O", end="")
            else:
                print("  ", end="")
        else:
            if board[i] == Player.Human:
                print("  X |", end="")
            elif board[i] == Player.Computer:
                print("  O |", end="")
            else:
                print("    |", end="")
        if ((i + 1) % 3 == 0) and (i != 8):
            print("\n----|----|----")
    print("\n")

def play_game(board):
    winner = False
    while not winner:
        # Human move
        input_move = int(input("Your Move: "))
        while board[input_move - 1] != Player.Blank:  # Check Valid Move
            input_move = int(input("Invalid move.\nTry again: "))
        board[input_move - 1] = Player.Human
        print_board(board)
        time.sleep(1)

        # Check for winner
        if three_in_a_row(board, Player.Human):
            winner = True
            print("You win!")
            return

        # Check for draw
        if draw(board):
            winner = True
            print("It's a draw!")
            return

        # Computer move
        input_move = intelligence(board)
        board[input_move] = Player.Computer
        print_board(board)

        # Check for winner
        if three_in_a_row(board, Player.Computer):
            winner = True
            print("Computer wins!")
            return

        # Check for draw
        if draw(board):
            winner = True
            print("It's a draw!")
            return

def three_in_a_row(board, player):
    # Check rows
    if ((board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player)):
        return True

    # Check columns
    if ((board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player)):
        return True

    # Check diagonals
    if ((board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)):
        return True

    return False

def draw(board):
    for i in range(9):
        if board[i] == Player.Blank:
            return False
    return True

def intelligence(board):
    # Check for a winning move
    for i in range(9):
        if board[i] == Player.Blank:
            board[i] = Player.Computer
            if three_in_a_row(board, Player.Computer):
                board[i] = Player.Blank  # Undo the move
                return i
            board[i] = Player.Blank  # Undo the move

    # Check for a blocking move
    for i in range(9):
        if board[i] == Player.Blank:
            board[i] = Player.Human
            if three_in_a_row(board, Player.Human):
                board[i] = Player.Blank  # Undo the move
                return i
            board[i] = Player.Blank  # Undo the move

    # Prioritize the center, then corners, and finally edges
    if board[4] == Player.Blank:
        return 4  # Center

    # Corners
    for i in [0, 2, 6, 8]:
        if board[i] == Player.Blank:
            return i

    # Edges
    for i in [1, 3, 5, 7]:
        if board[i] == Player.Blank:
            return i

    return 0

def main():
    play = 'Y'
    while play.upper() == 'Y':
        board = [Player.Blank] * 9

        # Choose who goes first
        choice = input("Do you want to go first? (Y/N): ").upper()
        if choice == 'Y':
            print_board(board)
            play_game(board)
        else:
            board[4] = Player.Computer  # Computer always goes middle first
            print_board(board)
            play_game(board)

        play = input("Do you want to play again? (Y/N): ").upper()
        print()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
