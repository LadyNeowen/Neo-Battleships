from random import randint
scores = {'computer': 0, 'player': 0}

class Board:
    """
    The main board class which sets which board size the player choses,
    the number of ships, the players name input and the board type.
    (Player board or computers board)
    Has methods for adding ships depending on board size,
    the guesses made by player and computer and printing the board.
    """
        def __init__(self, size, num_ships, name, type):
            self.size = size
            self.board = [['.' for x in range(size)] for y in range(size)]
            self.num_ships = num_ships
            self.name = name
            self.type = type
            self.guesses = []
            self.ships = []

        def print(self):
            for row in self.board:
                print(' '.join(row))

