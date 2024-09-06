# AH Structures 2
# Using OOP Classes create a class for a customer buying a cinema ticket.
# To keep the class encapsulated you should also create setter and getter
# methods to modify and display the data.

# 5 customers in the array
# 1 customer with details added by you

class ticket:

    def __init__(self):
        self.movie_name = ""
        self.date = "01/01/2024"
        self.time = "12:00"
        self.screen_no = 1
        self.seat_no = "A1"
    
    def setMovie_Name(self, movie):
        self.movie_name = movie
    
    def getMovie_Name(self):
        return self.movie_name
    
    def setSeat_No(self, seatno):
        self.seat_no = seatno
    
customers = [ticket() for index in range(5)]
customers[0].setMovie_Name("Inside Out 2")
print(customers[0].getMovie_Name())