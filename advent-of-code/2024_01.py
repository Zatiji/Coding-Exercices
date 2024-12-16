# PART ONE OF THE QUESTION : ---------------------------------------------

leftList_1 = []
rightList_1 = []

# setup
f = open("inputFiles/day_1.txt", "r")
for x in f:
    line = x.strip()
    # Split the line into two parts
    num1, num2 = line.split()
    # Convert the numbers from strings to integers
    num1 = int(num1)
    num2 = int(num2)
    # Add the numbers to the list
    leftList_1.append(num1)
    rightList_1.append(num2)
f.close

# We sort the lists and decalre a variable to get the distance
leftList_1.sort()
rightList_1.sort()
distance = 0

for i in range (0,len(leftList_1)) :
    distance += abs(leftList_1[i] - rightList_1[i])

print(distance)

# PART TWO OF THE QUESTION : -----------------------------------------------

leftList_2 = []
rightList_2 = []

# setup - same thing as part 1
f = open("inputFiles/day_1.txt", "r")
for x in f:
    line = x.strip()
    num1, num2 = line.split()

    num1 = int(num1)
    num2 = int(num2)

    leftList_2.append(num1)
    rightList_2.append(num2)
f.close

# we declare a variable to get the number of similarities and iterate in the list
similarities = 0
for i in range(0, len(leftList_2)) :
    similarities += ( leftList_2[i] * rightList_2.count(leftList_2[i]) )

print (similarities)





