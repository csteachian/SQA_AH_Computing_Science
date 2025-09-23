from dataclasses import dataclass

@dataclass
class node():
  data : str = ''
  nextptr : int = -1

fat = [node() for x in range(12)]
headptr = 5 # position of first node

fat[5].data = 'C1'
fat[6].data = 'C2'
fat[10].data = 'C3'
fat[11].data = 'C4'
fat[5].nextptr = 6
fat[6].nextptr = 10
fat[10].nextptr = 11
fat[11].nextptr = -1

print("headptr : ",headptr)
for x in range(12):
  print(x,": ",fat[x].data, "-> ",fat[x].nextptr)

# Process linked list
nextptr = headptr
while nextptr != -1:
  data = fat[nextptr].data
  nextptr = fat[nextptr].nextptr
  print(data)
