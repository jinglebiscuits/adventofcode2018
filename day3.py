file = open('input3.txt', 'r')
claims = [line.strip() for line in file]
list = []
for point in claims:
    splitList = point.split()
    list.append(tuple([splitList[2].strip(":").split(","), splitList[3].split("x")]))
myDict = {}
yourDict = {}
for row in list:
    for x in range(int(row[1][0])):
        for y in range(int(row[1][1])):
            theTuple = tuple([int(row[0][0]) + x, int(row[0][1]) + y])
            if theTuple in myDict:
                yourDict[theTuple] = 0
            else:
                myDict[theTuple] = 0
print len(yourDict.keys())
