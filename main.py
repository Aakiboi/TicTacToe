# Importing libraries

from random import randint

def Header():
    print("+---------------------------------+")
    print("|  Welcome to the TicTacToe Game! |")
    print("+---------------------------------+")
    print("|      Choose your Champion!      |")
    print("+--------- X --- | --- O ---------+")

class TicTacToe_Game:

    Tile = "X"

    boardPositions = []

    strikePossibilities = (
        [(0, 0),]
    )

    positions = {
        1: [(0, 0), "1"],
        2: [(0, 2), "2"],
        3: [(0, 4), "3"],
        4: [(2, 0), "4"],
        5: [(2, 2), "5"],
        6: [(2, 4), "6"],
        7: [(4, 0), "7"],
        8: [(4, 2), "8"],
        9: [(4, 4), "9"]
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
                    print(self.values[(i, j)], end="")
                elif j in [1, 3] and i in [0, 2, 4]:
                    print("|", end="")
                elif j in [1, 3] and i in [1, 3]:
                    print("+", end="")
                else:
                    print("-", end="")
            print()

    def updatePositions(self, square, tileChoice):
        positionObtained = self.positions[square][0]    # coords to corresponding user square
        self.boardPositions.append(square)              # appending coords to list for later checking
        self.values[positionObtained] = tileChoice      # updating values with user's choice (X or O)

    def computerTile(self, choice):
        if choice == "X":       # if the user has picked 'X' 
            self.Tile = "O"     # then computer gets assigned with 'O'

    def computerMove(self, tileChoice):
        computerSquare = randint(1, 9)

        while True:
            if computerSquare not in self.boardPositions:
                self.boardPositions.append(computerSquare)
                break
            else:
                computerSquare.randint(1, 9)

        Game.updatePositions(computerSquare, tileChoice)

    
    def checkStrike(self):
        

Header()
choice = input("Choose Wisely:")

while choice in ['X', 'O']:

    Game.computerTile(choice)
    Game = TicTacToe_Game()
    Game.generate_board()
    

    squareChoice = input("Enter square number as seen on screen (Press any letter to exit.):")

    if not squareChoice.isdigit():
        print("Thanks for playing the game!", end="")
        break
    
    Game.updatePositions(int(squareChoice), choice)
    Game.computerMove()











    