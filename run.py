"""
Python Battleship Game
Legend

'X' for hit battleship
'~' for available space
'O' for missed shot
'@' for placed battleship
"""

def print_intro():
    print(" ..You wake up with a throbbing ache \n at the back of your skull.\n As you rise up slowly your eyes widen..\n You are standing on the deck of a \n giant ship! \n All of a sudden a cannonblast goes off \n right next to you and a man shouts: \n Hey you!! What's your name? \n Nevermind that! YOU are in charge now! \n Where should we aim the cannons \n captain?!")
    print()
    print()


def print_board(board):
    print(" ", " ".join("12345"))
    for letter, row in zip("ABCDE", board):
        print(letter, " ".join(row))

def place_ships(board, num_ships=4):
    placed = 0
    while placed < num_ships:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if board[row][col] == "~":
            board[row][col] = "@"
            placed += 1

def shoot():
    while True:
        guess = input("Aim the cannons!!! (e.g. A5) \nSink these blasted land lubbers \nright into the abyss! \n ").upper()
        if len(guess) < 2:
            print("\nYou can't shoot there cap..\nTry something like A1.")
            continue
       
        row_letter = guess[0]
        col_number = guess[1:]
        row_index = "ABCDE".find(row_letter)
       
        if row_index == -1 or not col_number.isdigit():
            print("\nYou can't shoot there cap..\nTry something like A1")
            continue
       
        col_number = int(col_number)
        if not (1 <= col_number <= 5):
            print("\nYou can't shoot there cap..\nTry something like A1")
            continue
       
        col_index = col_number - 1
        return row_index, col_index