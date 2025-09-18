# Linked List Default
# Basically the most basic of linked lists - singly

from dataclasses import dataclass
import random

letters = ['A','B','C','D','E','F','G']

@dataclass
class node:
    data : str = ''
    nextPtr : int = -1

def displayNode(thisNode):
    print(thisNode.data)
    if thisNode.nextPtr == -1:
        print("End of the list.")
    else:
        print("Going to this node next: ", thisNode.nextPtr)
        input()
        displayNode(singlyLinkedList[thisNode.nextPtr])

singlyLinkedList = [node() for x in range(10)]
for x in range(10):
    singlyLinkedList[x].data = random.choice(letters)
    singlyLinkedList[x].nextPtr = random.randint(-1,9)
headPtr = 4
print(singlyLinkedList)
firstNode = singlyLinkedList[headPtr]
displayNode(firstNode)