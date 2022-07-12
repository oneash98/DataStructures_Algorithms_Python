import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis = 1)

newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis = 0)


def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("Incorrect index")
    else:
        print(array[rowIndex][colIndex])

def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return str(i) + "&" + str(j)
    return "not found"


newTDArray = np.delete(twoDArray, 0, axis = 0)
print(newTDArray)