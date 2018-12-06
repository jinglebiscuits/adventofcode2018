file = open('input4.txt', 'r')

dates = [line.strip() for line in file]
file.close()
print dates[0]

datesStrip1 = [line.strip("[") for line in dates]
datesStrip2 = [line.strip("]") for line in datesStrip1]
print datesStrip2[3]
