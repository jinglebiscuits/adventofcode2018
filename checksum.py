twoCount = 0
threeCount = 0

def sortThem(serialNumber):
    global twoCount
    global threeCount
    countDict = {}
    for char in serialNumber:
        if (char in countDict):
            countDict[char] = countDict[char] + 1
        else:
            countDict[char] = 1
    if (2 in countDict.values()):
        twoCount += 1
    if (3 in countDict.values()):
        threeCount += 1
    countDict.values()

file = open('input2.txt', 'r')
for line in file:
    sortThem(line.strip());
file.close()

outcome = "two count: " + str(twoCount) + " three count: " + str(threeCount) + " and answer is: " + str(twoCount * threeCount)
print outcome
