## Challenge
##  1. Modify the code so that the program asks the user for their
##     initials and for a row and column on the bus
##  2. It then checks to see if the row and column are free
##  3. If it is free the initials are added to that 2D array location
##  4. If it is not free an error message is displayed and the user
##     asked for another row and column 

# Bus example

seat = [ ['' for col in range(5)] for row in range(2)]
seat[0][0] = 'D'

seat[0][1] = 'AB'
seat[0][2] = 'MD'
seat[1][4] = 'LL'
seat[1][0] = 'ES'

seat[1][2] = 'T'

for row in range(2):
  print(seat[row])

##  1. Modify the code so that the program asks the user for their
##     initials and for a row and column on the bus
initials = input("Please enter initials: ")
myrow = int(input("Please enter row on bus (0/1): "))
mycol = int(input("Please enter column on bus (0-4): "))

##  2. It then checks to see if the row and column are free
while seat[myrow][mycol] != '':
  ##  4. If it is not free an error message is displayed and the user
  ##     asked for another row and column 
  print("The seat is already taken.")
  myrow = int(input("Please enter row on bus (0/1): "))
  mycol = int(input("Please enter column on bus (0-4): "))

print("The seat is free.")
##  3. If it is free the initials are added to that 2D array location
seat[myrow][mycol] = initials

for row in range(2):
  print(seat[row])