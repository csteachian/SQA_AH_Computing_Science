from dataclasses import dataclass
@dataclass
class square():
    position : int = 0
    player : str = ''
    pointer : int = 0

def displayBoard(gameboard):
    for row in range(len(gameboard)):
        print(str(gameboard[row].position) + ', ')
    print()

def initPosition(gameboard):
    # task 2
    # write code to set position of each square here
    for index in range(len(gameboard)):                # <-----------------------------------------
        gameboard[index].position = index + 1          # <-----------------------------------------
    return gameboard

# initialisation

# setup 1-D array of records (gameboard) here - task 1
gameboard = [square() for index in range(50)]          # <-----------------------------------------

displayBoard(gameboard)
gameboard = initPosition(gameboard) # task 2
displayBoard(gameboard)