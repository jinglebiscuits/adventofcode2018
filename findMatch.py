ids = []
file = open('input2.txt', 'r')
for line in file:
    ids.append(line.strip())
file.close()

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

for x in myDict:
    for y in myDict[x]:
        if 1 in myDict[x][y]:
            myIndex = myDict[x][y].index(1)
            print y[:myIndex] + y[(myIndex + 1):]
