# PART ONE OF THE QUESTION : ----------------------------

listsTable = []

# setup
with open("inputFiles/day_2.txt", 'r') as file:
    for line in file:
        # Strip leading/trailing whitespace, split the line into numbers, and convert to integers
        numbers = list(map(int, line.strip().split()))
        listsTable.append(numbers)

# we create the methods to awnser the question
def isReportSafe(list):
    safe = True
    maxIndex = len(list) - 1

    for i in range(0, len(list)):
        if (i == maxIndex):
            break
        # check the gap condition
        elif (abs(list[i] - list[i+1]) < 1 or abs(list[i] - list[i]) > 3):
            safe = False
            break
        #check the "all increasing/decreasing condition"
        elif (i != 0):
            if (allIncreaseDecrease(list, i) == False):
                safe = False
                break
            else:
                pass

    return safe

# we either want : ALL increasing or ALL decreasing
def allIncreaseDecrease(list, i):
    return ( (list[i - 1] < list[i] and list[i] < list[i + 1]) and (list[i - 1] > list[i] and list[i] > list[i + 1]) )


# We iterate on the table to find the secure codes and put the results in a variable
numberSafeReports = 0

for intList in listsTable:
    if (isReportSafe(intList) == True):
        numberSafeReports += 1

print(numberSafeReports)