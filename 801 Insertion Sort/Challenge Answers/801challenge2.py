# Challenge 2
# Adapt the code provided so that the number of swaps is counted
# and displayed to the user when the list is ordered.

myList = [3,4,9,7,1]
noSwaps = 0

for index in range (1,len(myList)):
#store the value to be inserted into the array
 currentvalue = myList[index]
 position = index


  #shift the rest of the array one to the right
 while position > 0 and myList[position-1]>currentvalue:
   myList[position] = myList[position-1]
   position -= 1
   noSwaps += 1 # add 1 to noSwaps


 #insert the value into the array
 myList[position] = currentvalue


print(myList)
print("There were",noSwaps,"swaps.")