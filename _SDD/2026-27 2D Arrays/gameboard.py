from dataclasses import dataclass
@dataclass
class square():
    position : int = 0
    player : str = ''
    pointer : int = 0

def displayBoard(gameboard):
    for row in range(9):
        output = ''
        for col in range(7):
            output += str(gameboard[row][col].position) + ', '
        print(output)
    print()

def initPosition(gameboard):
    # write code to set position of each square here
    return gameboard

# initialisation
gameboard = [[square for col in range(7)] for row in range(9)]
displayBoard(gameboard)
gameboard = initPosition(gameboard)
displayBoard(gameboard)