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

    def getSex(self):
        return self.__sex
    
    def setSex(self, sex):
        self.__sex = sex

    def getHeight(self):
        return self.__height
    
    def setHeight(self, height):
        self.__height = height
    # ...

# MAIN PROGRAM
import random
colours_of_hair = ['red','brown','blonde','black']
sexOptions = ['male','female']

people = [Human() for index in range(10)]
for index in range(10):
    people[index].setHair_colour(random.choice(colours_of_hair))
    people[index].setSex(random.choice(sexOptions))
    people[index].setHeight(random.randint(90,190))
    print("HUMAN",index,":",people[index].getHair_colour(),people[index].getSex(),people[index].getHeight())
