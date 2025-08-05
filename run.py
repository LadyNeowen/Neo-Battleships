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

def check_hit(hidden_board, player_board, row, col):
    if hidden_board[row][col] == "@":
        print("It's a HIT!!! 💣💥 Well done captain! ")
        player_board[row][col] = "X"
        return True
    else:
        print("Aargh! It's a miss! 💦")
        player_board[row][col] = "O"
        return False

def play_game():
    # Intro and setup
    print_intro()
    player_name = input("Please enter your name: ")
    print(f"\n Welcome to NeoBattleships, {player_name}!")
    print(" You have 10 turns to sink all 4 ships.\nGod speed sailor!\n")

    player_board = [["~"] * 5 for _ in range(5)]
    hidden_board = [["~"] * 5 for _ in range(5)]
    place_ships(hidden_board)

    # Game loop
    hits = 0
    max_hits = 4
    turn = 1
    max_turns = 10

    while hits < max_hits and turn <= max_turns:
        print_board(player_board)
        print()
        print(f"Turn {turn} of {max_turns}")
        print()

        while True:
            row, col = shoot()
            if player_board[row][col] in ["X", "O"]:
                print("\nYou already shot there captain!!\nTry again somewhere else.\n")
            else:
                break

        was_hit = check_hit(hidden_board, player_board, row, col)
        if was_hit:
            hits += 1
            print(f"Total hits: {hits}/{max_hits}")
        else:
            print(f"Total hits: {hits}/{max_hits}")

        turn += 1