from os import link
from LinkedList import LinkedList

def partition(linkedList, x):
    tempNode = linkedList.head
    linkedList.tail = linkedList.head

    while tempNode:
        nextNode = tempNode.next
        tempNode.next = None
        if tempNode.value < x:
            tempNode.next = linkedList.head
            linkedList.head = tempNode
        else:
            linkedList.tail.next = tempNode
            linkedList.tail = tempNode
        tempNode = tempNode.next
    if linkedList.next != None:
        linkedList.tail.next = None