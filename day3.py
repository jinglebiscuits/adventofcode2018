file = open('input3.txt', 'r')
claims = [line.strip() for line in file]
list = []
for point in claims:
    splitList = point.split()
    list.append(tuple([splitList[2].strip(":").split(","), splitList[3].split("x")]))
myDict = {}
for x in range(int(list[0][1][0])):
    for y in range(int(list[0][1][1])):
        myDict[tuple([int(list[0][0][0]) + x, int(list[0][0][1]) + y])] = 0
print myDict
