# Question 1 - Find Missing Number

from gettext import find


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]

def findMissing(list, n):
    sum1 = n * (n + 1) / 2
    sum2 = sum(list)
    return int(sum1 - sum2)


# Q2 - Find pairs of integers whose sum is equal to a given number


def findPairs(list, target):
    pairList = []

    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                continue
            elif list[i] + list[j] == target:
                pairList.append([list[i], list[j]])
    
    return pairList


# Q3 - Check if an array contains a number in Python (numpy array와 linear search 사용)

import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def findNumber(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print("yes")


# Q4 - Find maximum product of two integers in array. (all elements are positive)

myArray = np.array([1, 3, 25, 32, 17, 34, 53, 28, 13, 22, 41, 23, 10, 9])

def findMaxProduct(array):
    maxProduct = 0

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            sum = array[i] + array[j]
            mul = array[i] * array[j]
            if sum > maxProduct: maxProduct = sum
            if mul > maxProduct: maxProduct = mul
        
    print(maxProduct)


# Q5 - Determine if a list has all unique characters in list

def isUnique(list):
    tempList = []
    for i in list:
        if i in tempList:
            return False
        else:
            tempList.append(i)
    return True


# Q6 - Permutation of Strings

def permutation(String1, String2):
    alphabets1 = list(String1)
    alphabets2 = list(String2)
    alphabets1.sort()
    alphabets2.sort()
    if alphabets1 == alphabets2:
        return True
    else:
        return False


# Q7 - Rotate Matrix. Rotate a N * N matrix by 90 degrees.

myArray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

def rotateMatrix(matrix):
    rows = len(matrix)
    rotatedMatrix = np.zeros((rows, rows))
    for i in range(rows):
        for j in range(rows):
            rotatedMatrix[j][rows - i - 1] = matrix[i][j]
    
    return rotatedMatrix

print(rotateMatrix(myArray))