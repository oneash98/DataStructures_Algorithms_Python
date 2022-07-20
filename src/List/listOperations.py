from numpy import average


myList = []

while(True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    myList.append(value)

average = sum(myList) / len(myList)

print('Average: ', average)