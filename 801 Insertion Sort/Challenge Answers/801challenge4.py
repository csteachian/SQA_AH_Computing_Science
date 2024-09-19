# Challenge 4
# Design a solution to receive a list of playing card suits
# and card value (e.g. jack of diamonds, three of clubs, etc) and
# sort these cards into ascending order.

from dataclasses import dataclass
@dataclass
class card():
  name : str = ''
  value : int = 0
  suit : str = ''

def getName(value):
  if value == 11:
    return "Jack"
  elif value == 12:
    return "Queen"
  elif value == 13:
    return "King"
  elif value == 1:
    return "Ace"
  else:
    return str(value)

def setupCardList(cardList):
  counter = 0
  suits = ['Hearts','Clubs','Diamonds','Spades']
  for suit in suits:
    for value in range(1,14):
      cardList[counter].value = value
      cardList[counter].suit = suit
      cardList[counter].name = getName(value)
      counter += 1
  return cardList

cardList = [card() for index in range(52)]
cardList = setupCardList(cardList)
print(cardList)


for index in range (1,len(cardList)):
#store the value to be inserted into the array
 currentvalue = cardList[index]
 position = index


  #shift the rest of the array one to the right
 while position > 0 and cardList[position-1].value>currentvalue.value:
   cardList[position] = cardList[position-1]
   position -= 1


 #insert the value into the array
 cardList[position] = currentvalue


print(cardList)
