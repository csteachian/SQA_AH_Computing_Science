# Linear Search example

numbers = [9,16,34,48,57,59,72,82,90,91]

target = 82
counter = 0
found = False

while counter < len(numbers) and found == False:
    if numbers[counter] == target:
        found = True
    counter = counter + 1

if found == True:
    print("I found",target,"in",counter,"iterations.")
else:
    print("I didn't find",target)

