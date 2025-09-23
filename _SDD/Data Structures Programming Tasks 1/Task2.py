# AH Structures 2
# Using OOP Classes create a class for a customer buying a cinema ticket.
# To keep the class encapsulated you should also create setter and getter
# methods to modify and display the data.

# 5 customers in the array
# 1 customer with details added by you

class ticket:

    def __init__(self):
        self.movie_name = ""
        self.__date = "01/01/2024"
        self.__time = "12:00"
        self.__screen_no = 1
        self.__seat_no = "A1"
    
    def setMovie_Name(self, movie):
        self.movie_name = movie
    
    def getMovie_Name(self):
        return self.movie_name
    
    def setDate(self, moviedate):
        self.date = moviedate
    
    def getDate(self):
        return self.date

    def setTime(self, movietime):
        self.time = movietime
    
    def getTime(self):
        return self.time

    def setScreen_No(self, screen_no):
        self.screen_no = screen_no
    
    def getScreen_No(self):
        return self.screen_no
    
    def setSeat_No(self, seatno):
        self.seat_no = seatno

    def getSeat_No(self):
        return self.seat_no
    
customers = [ticket() for index in range(5)]

customers[1].movie_name = "Minions"
customers[1].setDate("4/4/44")

customers[0].setMovie_Name("Inside Out 2")
customers[0].setDate("06/09/2024")
customers[0].setTime("16:00")
customers[0].setScreen_No(4)
customers[0].setSeat_No("J17")
print(customers[0].getMovie_Name(), customers[0].getDate(),
      customers[0].getTime(), customers[0].getScreen_No(),
      customers[0].getSeat_No()
      )