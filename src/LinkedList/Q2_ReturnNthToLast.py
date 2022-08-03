# 뒤에서 n번째 찾기

from os import link
from LinkedList import LinkedList

def nthToLast(linkedList, n):
    len_of_list = len(linkedList)
    tempNode = linkedList.head
    index = 0
    while tempNode:
        if len_of_list - index == n:
            return tempNode.value
            break
        else:
            tempNode = tempNode.next
            index += 1

linkedList = LinkedList()
linkedList.generate(10, 0, 99)
print(linkedList)
print(nthToLast(linkedList, 2))