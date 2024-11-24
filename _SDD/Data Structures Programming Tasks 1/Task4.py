from dataclasses import dataclass

@dataclass
class node():
  data : str = ''
  nextptr : int = -1

colour = [node() for x in range(12)] # file allocation table
headptr = 5 # position of first node

# set up nodes
# Red
# Orange
# Yellow
# Green
# Blue
# Indigo
# Violet
colour[5].data = 'Red'
colour[0].data = 'Orange'
colour[10].data = 'Yellow'
colour[11].data = 'Green'
colour[1].data = 'Blue'
colour[9].data = 'Indigo'
colour[3].data = 'Violet'
colour[5].nextptr = 0
colour[0].nextptr = 10
colour[10].nextptr = 11
colour[11].nextptr = 1
colour[1].nextptr = 9
colour[9].nextptr = 3
colour[3].nextptr = -1

print("headptr : ",headptr)
for x in range(12):
  print(x,": ",colour[x].data, "-> ",colour[x].nextptr)

# Process linked list
nextptr = headptr
while nextptr != -1:
  data = colour[nextptr].data
  nextptr = colour[nextptr].nextptr
  print(data)
