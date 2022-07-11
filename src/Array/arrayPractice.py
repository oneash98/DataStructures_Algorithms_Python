from array import *

# 1. Create an Array and traverse.

my_array = array('i', [1, 2, 3, 4, 5])

for i in my_array:
    print(i)


# 2. Access individual elements through indexes

print(my_array[0])


# 3. Append any value to the array using append() method

my_array.append(6)


# 4. Insert value in an array using insert() method

my_array.insert(0, 11)


# 5. Extend python array using extend() method

my_array1 = array('i', [10, 11, 12])
my_array.extend(my_array1)


# 6. Add items from list into array using fromlist() method

tempList = [20, 21, 22]
my_array.fromlist(tempList)


# 7. Remove any array element using remove() method

my_array.remove(22)


# 8. Remove last array element using pop() method

my_array.pop()


# 9. Fetch any element through its index using index() method

print(my_array.index(20))


# 10. Reverse a python array using reverse() method

my_array.reverse()


# 11. Get array buffer information through buffer_info() method

print(my_array.buffer_info())


# 12. Check for number of occurrences of an element using count() method

print(my_array.count(10))


# 13. Convert array to string using tostring() method

strTemp = my_array.tobytes()
ints = array('i')
ints.frombytes(strTemp)


# 14. Convert array to a python list with same elements using tolist() method

print(my_array.tolist())


# 15. Append a string to char array using fromstring() method

# 16. Slice elements from an array

print(my_array[1:4])
