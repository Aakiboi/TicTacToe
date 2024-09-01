# Importing libraries

from random import randint

def Header():
    print("+---------------------------------+")
    print("|  Welcome to the TicTacToe Game! |")
    print("+---------------------------------+")
    print("|      Choose your Champion!      |")
    print("+--------} X --- | --- O {--------+")

class TicTacToe_Game:

    Tile = "X"

    board_positions = []

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
        positionObtained = self.get_square_coords(square)       # coords to corresponding user square
        self.board_positions.append(square)                     # appending coords to list for later checking
        self.set_square_value(square, tileChoice)               # updating values with user's choice (X or O)

    def computer_tile(self, choice):
        if choice == "X":       # if the user has picked 'X' 
            self.Tile = "O"     # then computer gets assigned with 'O'

    # function to simulate computer's turn 
    def computer_move(self):
        computerSquare = randint(1, 9)

        while True:
            if computerSquare not in self.board_positions:
                self.board_positions.append(computerSquare)
                break
            else:
                computerSquare = randint(1, 9)

        self.update_positions(computerSquare, self.Tile)

    
    # checking the board if there is a strike
    def check_strike(self):
        if self.get_square_value(1) == self.get_square_value(2) == self.get_square_value(3):
            return(self.get_square_value(1))
        elif self.get_square_value(4) == self.get_square_value(5) == self.get_square_value(6):
            return(self.get_square_value(4))
        elif self.get_square_value(7) == self.get_square_value(8) == self.get_square_value(9):
            return(self.get_square_value(7))
        elif self.get_square_value(1) == self.get_square_value(4) == self.get_square_value(7):
            return(self.get_square_value(1))
        elif self.get_square_value(2) == self.get_square_value(5) == self.get_square_value(8):
            return(self.get_square_value(2))
        elif self.get_square_value(3) == self.get_square_value(9) == self.get_square_value(6):
            return(self.get_square_value(3))
        elif self.get_square_value(1) == self.get_square_value(5) == self.get_square_value(9):
            return(self.get_square_value(1))
        elif self.get_square_value(7) == self.get_square_value(5) == self.get_square_value(3):
            return(self.get_square_value(7)) 
        else:
            return(False)
        
        
Header()
choice = input("Choose Wisely: ")

while choice in ['X', 'O']:

    
    Game = TicTacToe_Game()
    Game.computer_tile(choice.upper())
    Game.generate_board()
    

    squareChoice = input("Enter square number as seen on screen (Press any letter to exit.): ")

    if not squareChoice.isdigit():
        print("Thanks for playing the game!", end="")
        break

    elif len(Game.board_positions) == 10:
        print("Thanks for playing the game. It is a draw!", end="")
        break

    if int(squareChoice) not in Game.board_positions:
        Game.update_positions(int(squareChoice), choice)
        Game.computer_move()

        if Game.check_strike() != False:
            print(Game.check_strike() + " won!")
            print("Thank you for playing the game!", end="")
            break
    
    else:
        print("Enter a valid square number!")
