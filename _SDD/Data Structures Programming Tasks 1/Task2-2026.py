# AH Structures 1
# Using 1D Array of Records create a record structure for a customer
# buying a cinema ticket

# 5 customers in the array
# 1 customer with details added by you

# Information I think I'll need:
# screen no
# seat no
# date
# time
# movie name

class ticket:

    def __init__(self): # constructor
        self.movie_name = ""
        self.date = "01/01/2024"
        self.time = "12:00"
        self.screen_no = 1
        self.seat_no = "A1"

    def setMovieName(self, thisMovieName): # setter
        self.movie_name = thisMovieName

    def setOtherStuff(self, thisDate, thisTime, thisScreen, thisSeat):
        self.date = thisDate
        self.time = thisTime
        self.screen_no = thisScreen
        self.seat_no = thisSeat

    def getMovieName(self): #getter
        return self.movie_name

    def getOtherStuff(self):
        message = self.date + " - " + self.time + ": Screen " + str(self.screen_no) + "| Seat " + self.seat_no
        return message

customers = [ticket() for index in range(5)]

customers[0].setMovieName("Inside Out 2")
customers[0].setOtherStuff("06/09/2024", "16:00", 4, "J17")

print(customers[0].getMovieName(), customers[0].getOtherStuff())