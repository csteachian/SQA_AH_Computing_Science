# Challenge 1
# Adapt the code provided so that the list is sorted in descending order.

myList = [3,4,9,7,1]

for index in range (1,len(myList)):
#store the value to be inserted into the array
 currentvalue = myList[index]
 position = index


  #shift the rest of the array one to the right
 while position > 0 and myList[position-1]<currentvalue: # changed > to <
   myList[position] = myList[position-1]
   position -= 1


 #insert the value into the array
 myList[position] = currentvalue


print(myList)