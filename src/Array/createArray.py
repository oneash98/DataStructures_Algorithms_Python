from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1.3, 1.5, 1.6])

arr1.insert(6, 7)



def traverseArray(array):
    for i in array:
        print(i)


def accessElement(array, index):
    if index > len(array):
        print('error')
    else:
        print(array[index])

def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The element does not exist"
