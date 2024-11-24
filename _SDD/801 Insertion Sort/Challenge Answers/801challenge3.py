# Challenge 3
# Use the code provided as a guide to create a new program
# which sorts a list of characters from the alphabet into ascending order.

myList = ['G','X','b','P','z']


for index in range (1,len(myList)):
#store the value to be inserted into the array
 currentvalue = myList[index]
 position = index


  #shift the rest of the array one to the right
 while position > 0 and ord(myList[position-1])>ord(currentvalue): # added ord
   myList[position] = myList[position-1]
   position -= 1


 #insert the value into the array
 myList[position] = currentvalue


print(myList)