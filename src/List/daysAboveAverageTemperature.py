numOfDays = int(input("How many day's temperature? "))

tempList = []

for i in range(1, numOfDays + 1):
    temp = float(input("Day %d's high temp: " % i))
    tempList.append(temp)

sumOfTemp = sum(tempList)
average = sumOfTemp / numOfDays

days = 0
for temp in tempList:
    if temp > average:
        days += 1

print("Average =", average)
print(days, "day(s) above average")