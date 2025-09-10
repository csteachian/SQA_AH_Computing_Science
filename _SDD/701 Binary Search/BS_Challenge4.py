# CHALLENGE 4
# -----------
# Test your program by searching for items that are:
# Near the start (left) of the list
# Near the end (right) of the list
# In the middle of the list
# In the first ¼ (approx.) of the list
# Make a note of the amount of comparisons being performed in the above searches.
# What is the worst-case and best-case results with regard to position and the amount of comparisons being performed?

# Best Case position  |   3     |   Amount of comparisons   |   1
# Worst Case position | 0,2,4,6 |   Amount of comparisons   |   3


def initialise():
 searchlist = [1,2,3,4,5,6,7]
 print("Original list:",searchlist)
 return searchlist


def BinarySearch(searchlist,goal):
 found = False
 startpos = 0
 endpos = len(searchlist) -1
 comparisons = 0 # new comparisons variable


 print ("Endpos at beginning = ",endpos)


 while (startpos <= endpos) and found == False:
     middle = (startpos+endpos)//2 #Integer Division
     comparisons += 1 # increment comparisons variable
     if searchlist[middle] == goal:
         found = True
     elif searchlist[middle]<goal:
         startpos = middle + 1
     else:
         endpos = middle -1

 print("The number of comparisons was:",comparisons) # display number of comparisons


 if found != True:
   middle = -1 
 return middle 


values = initialise()


goal = int(input("Enter goal"))
position = BinarySearch(values,goal) 
if position >= 0:
   print("Match has been found at position",position)
else:
   print("Goal not found")
