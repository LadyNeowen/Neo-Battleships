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