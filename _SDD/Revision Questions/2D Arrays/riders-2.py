# FUNCTION calculateTotalPoints(races : 2D ARRAY OF INTEGER) RETURNS 2D ARRAY OF STRING
#     DECLARE results AS 2D ARRAY OF STRING [8] [2]
#     FOR index = 0 TO 7 DO
#         SET total TO 0
#         FOR counter = 0 TO 4 DO
#                SET total TO total + races[index][counter]
#         END FOR
#         SET results[index][0] TO “Rider “ + (index + 1)
#         SET results[index][1] TO total
#     END FOR
#     RETURN results
# END FUNCTION

races = [
    [5, 2, 0, 3, 1],
    [0, 1, 4, 0, 4], 
    [2, 0, 5, 1, 0], 
    [1, 3, 0, 5, 0], 
    [4, 0, 2, 0, 2], 
    [0, 4, 0, 2, 3], 
    [3, 5, 1, 0, 0], 
    [0, 0, 3, 4, 5]
]

def calculateTotalPoints(races):
    results = [ ['' for col in range(2)] for row in range(8)]
    for index in range(8):
        total = 0
        for counter in range(5):
            total = total + races[index][counter]
        results[index][0] = "Rider " + str(index+1)
        results[index][1] = str(total)
    return results

# main program
results = calculateTotalPoints(races)
for index in range(len(results)):
    print(results[index])
