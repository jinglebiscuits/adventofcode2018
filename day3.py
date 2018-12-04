file = open('input3.txt', 'r')
claims = [line.strip() for line in file]
list = []
for point in claims:
    splitList = point.split()
    list.append(tuple([splitList[2].strip(":").split(","), splitList[3].split("x")]))
myDict = {}
yourDict = {}
ids = []

def getRect(row):
    point = row.split()[2].strip(":").split(",")
    x = int(point[0])
    y = int(point[1])

    dimensions = row.split()[3].split("x")
    width = int(dimensions[0])
    height = int(dimensions[1])
    return tuple([x, y, width, height])

def getRectXMax(rect):
    return rect[0] + rect[2]

def getRectYMax(rect):
    return rect[1] + rect[3]

def overlaps(rect1, rect2):
    condition1 = (getRectXMax(rect1) < rect2[0])
    condition2 = (getRectXMax(rect2) < rect1[0])
    condition3 = (getRectYMax(rect1) < rect2[1])
    condition4 = (getRectYMax(rect2) < rect1[1])
    overlapping = condition1 or condition2 or condition3 or condition4
##    print rect1, rect2, overlapping
    return not (condition1 or condition2 or condition3 or condition4)

for claim in claims:
    overlapCount = 0
    for claimb in claims:
        if claimb != claim:
            if (overlaps(getRect(claim), getRect(claimb))):
                overlapCount += 1
    if (overlapCount == 0):
        print claim, overlapCount

for row in list:
    for x in range(int(row[1][0])):
        for y in range(int(row[1][1])):
            theTuple = tuple([int(row[0][0]) + x, int(row[0][1]) + y])
            if theTuple in myDict:
                yourDict[theTuple] = 0
            else:
                myDict[theTuple] = 0
print len(yourDict.keys())

