# CHALLENGE 1
# -----------
# Adapt the code provided so that the initialise function uses each of the following searchlists and goals.
# Record the value of middle when a match is found.

# searchlist                  |   goal    |   middle
# [1,3,5,7,9,11,13,17,18,19]  |   17      |   7
# [90,90,91,92,92,93]         |   90      |   0
# [10,15,25,26,60,90,100]     |   15      |   1

def initialise():
 searchlist = [10,15,25,26,60,90,100]
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


 if found == True:
   print("Match has been found at position",middle)
 else:
   print("Goal not found")


values = initialise()


goal = int(input("Enter goal"))
BinarySearch(values,goal)
