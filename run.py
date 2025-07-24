

# Creates the board
def create_board():
    return [['~' for x in range(8)] for x in range(8)]

# Show the board to the player
def print_board(board):
    print('  A B C D E F G H')
    print('--------------')
    row_number = 1
    for row in board:
        print(str(row_number) + '|' + ' '.join(row) + '|')


# Randomly place 5 ships on the board
def place_ships():
    pass

# Ask the player where to shoot
def get_player_move(rows, columns):
    """
    Asks the player to make a move, for example "A5").
    Input is then converted into a row and column on the board.
    """
    while True:
        try:
            guess = input("Enter your guess (For example, 'A5'):  \n").strip().upper()
            col, row = ord(guess[0]) - ord('A'), int(guess[1:]) - 1
            if 0 <= row < rows and 0 <= col < columns:
                return row, col
            else:
                print("Invalid guess. Try again. \n")
        except (ValueError, IndexError, TypeError):
            print("Invalid guess. Try again. \n")

# Make the computer pick a random spot
def get_computer_move():
    pass

# Check if a ship is hit
def ships_hit():
    pass

# Counts how many ships are hit
def counts_ships():
    pass

# Main game function
def play_game():
    pass



# Start the game
#play_game()

