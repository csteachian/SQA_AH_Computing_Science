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

from dataclasses import dataclass

@dataclass
class ticket:
    movie_name : str = ""
    date : str = "01/01/2024"
    time : str = "12:00"
    screen_no : int = 1
    seat_no : str = "A1"

customers = [ticket for index in range(5)]

customers[0].movie_name = "Inside Out 2"
customers[0].date = "06/09/2024"
customers[0].time = "16:00"
customers[0].screen_no = 4
customers[0].seat_no = "J17"

print(customers[0].movie_name, customers[0].date, customers[0].time, customers[0].screen_no, customers[0].seat_no)