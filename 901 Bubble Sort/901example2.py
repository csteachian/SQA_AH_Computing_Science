# 901example2.py
# Bubble Sort

# The following code sets up the record structure to be sorted
from dataclasses import dataclass
@dataclass
class person():
    height : float = 0.0
    weight : float = 0.0
    bmi : float = 0.0

def calcBMI(height, weight):
    return round(weight / (height**2),2)

PEOPLE = [person() for index in range(5)]
PEOPLE[0].height = 1.75
PEOPLE[0].weight = 70.5
PEOPLE[0].bmi = calcBMI(PEOPLE[0].height, PEOPLE[0].weight)
PEOPLE[1].height = 1.62
PEOPLE[1].weight = 55.8
PEOPLE[1].bmi = calcBMI(PEOPLE[1].height, PEOPLE[1].weight)
PEOPLE[2].height = 1.88
PEOPLE[2].weight = 95.2
PEOPLE[2].bmi = calcBMI(PEOPLE[2].height, PEOPLE[2].weight)
PEOPLE[3].height = 1.70
PEOPLE[3].weight = 82.3
PEOPLE[3].bmi = calcBMI(PEOPLE[3].height, PEOPLE[3].weight)
PEOPLE[4].height = 1.80
PEOPLE[4].weight = 68.0
PEOPLE[4].bmi = calcBMI(PEOPLE[4].height, PEOPLE[4].weight)

# End of setup code

print(PEOPLE) # show unsorted values

passes = 0
comparisons = 0
swaps = 0

for outer in range (len(PEOPLE)-1,0,-1):
    passes += 1
    for inner in range(outer):
        comparisons += 1
        
        if PEOPLE[inner].bmi>PEOPLE[inner+1].bmi:
            swaps += 1
            temp = PEOPLE[inner]
            PEOPLE[inner] = PEOPLE[inner+1]
            PEOPLE[inner+1] = temp
    
    print("Pass ",passes)

print(PEOPLE) # show sorted values