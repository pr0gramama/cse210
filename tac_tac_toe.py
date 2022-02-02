# Tic Tac Toe by Mary Ann Overson for CSE 210
# Full disclosure: I made this game with the help of many sources, including
# this video: https://www.youtube.com/watch?v=n2o8ckO-lfk
# and this website https://www.askpython.com/python/examples/tic-tac-toe-using-python

def main():

    # Player is "x" if true, "o" if false
    player = True
    turns = 0
    
    # This is an array to create the board
    board = [
        ["*", "*", "*", ],
        ["*", "*", "*", ],
        ["*", "*", "*", ]
    ]

    # Loop to execute the game until it is over
    while turns < 9:
        active_player = current_player(player)
        display_board(board)
        player_turn = input(f"Player {turns} Choose a square (1-9) or 'q' to quit the game: ")
        if quit_game(player_turn):
            break
        if not check_turn(player_turn):
            print("Please try again.")
            continue
        player_turn = int(player_turn) - 1
        slot = position_array(player_turn)
        if occupied(slot, board):
            print("Please try again.")
            continue
        take_turn(slot, board, active_player)
        if win(active_player, board):
            print(f"{active_player.upper()}'s won!")
            break

        turns += 1
        if turns == 9:
            print("Cat's Game!  The game is a draw.")
        player = not player

# Function to display the board
def display_board(board):
    for row in board:
        for space in row:
            print(space + " ", end="")
        print()

# Check input is a number and 1-9
def check_turn(player_turn):
    if not is_number(player_turn):
        return False
    player_turn = int(player_turn)
    if not check_bounds(player_turn):
        return False
    return True

# Check input is a number
def is_number(player_turn):
    if not player_turn.isnumeric():
        print("Invalid input.  Please enter a number 1 through 9.")
        return False
    else:
        return True

# Check number input is 1 through 9
def check_bounds(player_turn):
    if player_turn > 9 or player_turn < 1:
        print("Invalid entry.  Please make sure number is 1 through 9.")
        return False
    return True

# Quit the game
def quit_game(player_turn):
    if player_turn.lower() == "q":
        print("Thank you for playing Tic Tac Toe.  Goodbye.")
        return True
    else:
        return False

# Checks to see if square is occupied
def occupied(slot, board):
    row = slot[0]
    column = slot[1]
    if board[row][column] != "*":
        print("That quare is occupied.")
        return True
    else:
        return False

# Functin to mark current player's selected square
def position_array(player_turn):
    row = int(player_turn / 3)
    column = player_turn
    if column > 2: column = int(column % 3)
    return (row, column)

# Marks current player
def take_turn(slot, board, active_player):
    row = slot[0]
    column = slot[1]
    board[row][column] = active_player

# Function to switch between players and their markers
def current_player(player):
    if player:
        return "x"
    else:
        return "o"

# Function to check if there is a winner (3 in a row, column or diagonal)
def win(player, board):
    if check_row(player, board):
        return True
    if check_column(player, board):
        return True
    if check_diagonal(player, board):
        return True
    return False

# Check each row
def check_row(player, board):
    for row in board:
        all_row = True
        for slot in row:
            if slot != player:
                all_row = False
                break
        if all_row:
            return True
    return False

# Check each column
def check_column(player, board):
    for column in range(3):
        all_column = True
        for row in range(3):
            if board[row][column] != player:
                all_column = False
                break
        if all_column:
            return True
    return False

# Check top left to bottom right
def check_diagonal(player, board):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player: 
        return True
    else:
        return False

if __name__ == "__main__":
    main()