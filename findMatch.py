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

ids = []
file = open('input2.txt', 'r')
for line in file:
    ids.append(line.strip())
file.close()

counter = 0
idLength = len(ids[0])
myDict = {}
for x in ids:
    myDict[x] = {}
    for y in ids:
        myDict[x][y] = []

for x in ids:
    for y in ids:
        for counter in range(0, idLength):
            if (x in myDict and y in myDict[x]):
                if (x[counter] is y[counter]):
                    myDict[x][y].append(0)
                else:
                    myDict[x][y].append(1)
                error = 0
                for j in myDict[x][y]:
                    error += j
                    if error > 1:
                        del myDict[x][y]
                        break;
finalList = []

print myDict
