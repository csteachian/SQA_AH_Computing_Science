# 801example.py
# Insertion sort

from dataclasses import dataclass

@dataclass
class PERSON():
  height : float = 0.0
  weight : float = 0.0
  bmi : float = 0.0

def showOrderedBMI(thisList):
  for index in range(len(thisList)):
     print(index,":",thisList[index].bmi)
  print("---")

def calcBMI(myWeight, myHeight):
   return round(myWeight / (myHeight ** 2),2)

PEOPLE = [PERSON() for index in range(5)]
PEOPLE[0].height = 1.75
PEOPLE[0].weight = 70.5
PEOPLE[0].bmi = calcBMI(PEOPLE[0].weight,PEOPLE[0].height)

PEOPLE[1].height = 1.62
PEOPLE[1].weight = 55.8
PEOPLE[1].bmi = calcBMI(PEOPLE[1].weight,PEOPLE[1].height)

PEOPLE[2].height = 1.88
PEOPLE[2].weight = 95.2
PEOPLE[2].bmi = calcBMI(PEOPLE[2].weight,PEOPLE[2].height)

PEOPLE[3].height = 1.70
PEOPLE[3].weight = 82.3
PEOPLE[3].bmi = calcBMI(PEOPLE[3].weight,PEOPLE[3].height)

PEOPLE[4].height = 1.80
PEOPLE[4].weight = 68.0
PEOPLE[4].bmi = calcBMI(PEOPLE[4].weight,PEOPLE[4].height)

print("Pass 0")
showOrderedBMI(PEOPLE)

for index in range (1,len(PEOPLE)):
    #store the record/object to be inserted into the array
    currentrecord = PEOPLE[index]
    position = index

    #shift the rest of the array one to the right
    while position > 0 and PEOPLE[position-1].bmi>currentrecord.bmi:
        PEOPLE[position] = PEOPLE[position-1]
        position -=1

    #insert the value into the array
    PEOPLE[position] = currentrecord
    
    # show each pass
    print("Pass",index)
    showOrderedBMI(PEOPLE)