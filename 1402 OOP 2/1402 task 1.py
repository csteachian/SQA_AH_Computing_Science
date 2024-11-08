# 1402 taks 1
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

    # Complete the class implementation *for all setters and getters* using the UML diagram in OOP 2




# This code will generate errors to begin with.
# Once you have completed the class implementation above it should work.

charlie = Human()
charlie.setHair_colour('blonde')
charlie.setSex('male')
charlie.setHeight_cm(175)

print('Charlie is',charlie.getSex())
print('Charlie is',charlie.getHeight_cm(),'cm tall.')
print('Charlie''s hair is ',charlie.getHair_colour())