# CHALLENGE 2
# -----------
# Adapt your program so that your binary search is now a function which returns the position of the element
# and will return -1 if no result has been found.

def initialise():
 searchlist = [1,2,3,4,5,6,7]
 print("Original list:",searchlist)
 return searchlist


def BinarySearch(searchlist,goal):
 found = False
 startpos = 0
 endpos = len(searchlist) -1


 print ("Endpos at beginning = ",endpos)


 while (startpos <= endpos) and found == False:
     middle = (startpos+endpos)//2 #Integer Division
     if searchlist[middle] == goal:
         found = True
     elif searchlist[middle]<goal:
         startpos = middle + 1
     else:
         endpos = middle -1


 if found != True:
   middle = -1 # if not found set middle to -1
 return middle # pass back the value of middle to the calling code


values = initialise()


goal = int(input("Enter goal"))
position = BinarySearch(values,goal) # call to BinarySearch now returns the value of the position where the goal was found
if position >= 0:
   print("Match has been found at position",position)
else:
   print("Goal not found")
