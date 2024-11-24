# 1402 example 1
# Human class

class Human():
    def __init__(self): # Constructor
        self.__sex = '' # the __ is conventional for private attributes
        self.__hair_colour = ''
        self.__height_cm = 0
    
    def getHair_colour(self):
        return self.__hair_colour
    
    def setHair_colour(self, hair_colour):
        self.__hair_colour = hair_colour

    # ...

alice = Human() # creates instance of the Human class
bob = Human() # creates second instance of the Human class
alice.setHair_colour('red') # sets the attribute hair_colour to 'red' for the alice instance of the Human class
bob.setHair_colour('brown') # sets the attribute hair_colour to 'brown' for the bob instance of the Human class
print(alice.getHair_colour()) # displays the attribute hair_colour for the alice instance of the Human class
print(bob.getHair_colour()) # displays the attribute hair_colour for the bob instance of the Human class