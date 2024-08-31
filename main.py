# Importing libraries

from random import randint

class TicTacToe_Game:

    userPositons = []
    boardPositions = []

    positions = {
        "square1": [(0, 0), "1"],
        "square2": [(0, 2), "2"],
        "square3": [(0, 4), "3"],
        "square4": [(2, 0), "4"],
        "square5": [(2, 2), "5"],
        "square6": [(2, 4), "6"],
        "square7": [(4, 0), "7"],
        "square8": [(4, 2), "8"],
        "square9": [(4, 4), "9"]
    }

    values = {
        (0, 0) : "1",
        (0, 2) : "2",
        (0, 4) : "3",
        (2, 0) : "4",
        (2, 2) : "5",
        (2, 4) : "6",
        (4, 0) : "7",
        (4, 2) : "8",
        (4, 4) : "9"
    }


    def __init__(self):
        pass

    # displaying the board
    def generate_board(self):
        for i in range(5):
            for j in range(5):
                if i % 2 == 0 and j % 2 == 0:
                    print(TicTacToe_Game.values[(i, j)], end="")
                elif j in [1, 3] and i in [0, 2, 4]:
                    print("|", end="")
                elif j in [1, 3] and i in [1, 3]:
                    print("+", end="")
                else:
                    print("-", end="")
            print()


        
    
test1 = TicTacToe_Game()
test1.generate_board()