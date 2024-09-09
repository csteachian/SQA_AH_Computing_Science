from dataclasses import dataclass

@dataclass
class node():
  data : str = ''
  nextptr : int = -1

colour = [node() for x in range(710)] # file allocation table
headptr = 318 # position of first node

# set up nodes
colour[318].data = 'Australia'
colour[318].nextptr = 706

colour[706].data = 'France'
colour[706].nextptr = 153

colour[153].data = 'USA'
colour[153].nextptr = 1

colour[241].data = 'Germany'
colour[241].nextptr = 439

colour[439].data = 'UK'
colour[439].nextptr = 208

colour[208].data = 'Brazil'
colour[208].nextptr = -1

# add node to middle of linked list
colour[1].data = 'Russia'
colour[1].nextptr = 241

print("headptr : ",headptr)
for x in range(710):
  print(x,": ",colour[x].data, "-> ",colour[x].nextptr)

# Process linked list
nextptr = headptr
while nextptr != -1:
  data = colour[nextptr].data
  nextptr = colour[nextptr].nextptr
  print(data)
