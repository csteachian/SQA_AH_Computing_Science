# 901example1.py
# Bubble Sort

listA = [5,3,8,6,7,2,4,1]
print(listA) # show unsorted list

#start from the right 
for outer in range (len(listA)-1,0,-1):
    for inner in range(outer):
        #compare two adjacent values
        if listA[inner]>listA[inner+1]:
	        #assign one of the values to a temp variable
            temp = listA[inner]
            #overwrite one of the values
            listA[inner] = listA[inner+1]
            #replace with the temp value
            listA[inner+1] = temp
    
print(listA) # show sorted list