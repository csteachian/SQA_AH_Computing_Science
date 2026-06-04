from dataclasses import dataclass
@dataclass
class square():
    position : int = 0
    player : str = ''
    pointer : int = 0

def displayBoard(gameboard):
    for row in range(len(gameboard)):
        print(str(gameboard[row][col].position) + ', ')
    print()

def initPosition(gameboard):
    # task 2
    # write code to set position of each square here
    return gameboard

# initialisation

# setup 1-D array of records (gameboard) here - task 1

displayBoard(gameboard)
gameboard = initPosition(gameboard) # task 2
displayBoard(gameboard)