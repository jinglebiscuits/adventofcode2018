frequency = 0
frequencyDictionary = {0:0}
lookingForDupe = True
while lookingForDupe:
    file = open('input.txt', 'r')
    for line in file:
        frequency += int(line)
        if (frequency not in frequencyDictionary):
            frequencyDictionary[frequency] = frequency
        else:
            print "first dupe is {}".format(frequency)
            lookingForDupe = False
            break
    file.close()
print str(frequency)
