frequency = 0
file = open('input.txt', 'r')
for line in file:
    frequency += int(line)
file.close()
print str(frequency)
