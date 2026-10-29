class Human():
    def __init__(self): # Constructor
        self.__sex = '' # the __ is conventional for private attributes
        self.__hair_colour = ''
        self.__height_cm = 0
    
    def getHair_colour(self):
        return self.__hair_colour
    
    def setHair_colour(self, hair_colour):
        self.__hair_colour = hair_colour

class Teacher(Human):
    def __init__(self):
        Human.__init__(self) # I always forget this
        self.__likesHolidays = True

    def getPreference(self):
        return self.__likesHolidays

    def setPreference(self, likesHolidays):
        self.__likesHolidays = likesHolidays

    def setHair_colour(self, hair_colour): # overloaded
        Human.setHair_colour(self,"bald")

class Bear():
    def __init__(self):
        self.__eatsHumans = True

    def getFood(self):
        return "HUMANS!"

    def getHair_colour(self):
        return "RAWWWWRRRR!"

# main program
human1 = Teacher()
human1.setHair_colour("red")
#print(human1.getHair_colour())

humans = [Human() for x in range(5)]
humans[0].setHair_colour("blue")
humans[1].setHair_colour("green")
humans[2].setHair_colour("red")
humans[3].setHair_colour("brown")
humans[4].setHair_colour("white")
humans.append(human1)

human2 = Human()
human2.setHair_colour("black")
humans.append(human2)

thing = Bear()
humans.append(thing)

for x in range(len(humans)):
    print(humans[x].getHair_colour())



