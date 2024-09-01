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

    board_positions = []

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

    def get_square_value(self, squareNumber):
        return self.positions[squareNumber][1]      # Gets square's value
       
    def get_square_coords(self, squareNumber):
        return self.positions[squareNumber][0]      # Gets square's coords
        
    def set_square_value(self, squareNumber, value):
        self.positions[squareNumber][1] = value                     # Setting square values
        self.values[self.get_square_coords(squareNumber)] = value   # In both positions and values

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

    def update_positions(self, square, tileChoice):
        positionObtained = self.get_square_coords()  # coords to corresponding user square
        self.board_positions.append(square)              # appending coords to list for later checking
        self.values[positionObtained] = tileChoice      # updating values with user's choice (X or O)


    def computer_tile(self, choice):
        if choice == "X":       # if the user has picked 'X' 
            self.Tile = "O"     # then computer gets assigned with 'O'

    # function to simulate computer's turn 
    def computer_move(self, tileChoice):
        computerSquare = randint(1, 9)

        while True:
            if computerSquare not in self.board_positions:
                self.board_positions.append(computerSquare)
                break
            else:
                computerSquare.randint(1, 9)

        Game.update_positions(computerSquare, tileChoice)

    
    # checking the board if there is a strke
    def checkStrike(self):

        

Header()
choice = input("Choose Wisely:")

while choice in ['X', 'O']:

    Game.computer_tile(choice)
    Game = TicTacToe_Game()
    Game.generate_board()
    

    squareChoice = input("Enter square number as seen on screen (Press any letter to exit.):")

    if not squareChoice.isdigit():
        print("Thanks for playing the game!", end="")
        break
    
    Game.update_positions(int(squareChoice), choice)
    Game.computer_move()











    