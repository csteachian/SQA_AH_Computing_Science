# CHALLENGE 3
# -----------
# Adapt your program above to keep track of the amount of comparisons - this is when
# the midpoint is being checked against the goal state.
# This should be displayed inside the function.

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
