from importlib.abc import Traversable
from re import L


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in linked list
    def insertSLL(self, value, location):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    def traverseNode(self):
        if self.head == None:
            print("존재하지 않습니다")
        else:
            node = self.head
            while node != None:
                print(node.value)
                node = node.next

    def searchNode(self, value):
        if self.head == None:
            return "리스트가 존재하지 않습니다"
        else:
            node = self.head
            while node != None:
                if node.value == value:
                    return node.value
                node = node.next
            return "존재하지 않습니다"

    def deleteNode(self, location):
        if self.head == None:
            print("리스트가 존재하지 않습니다")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node.next != self.tail:
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteAll(self):
        if self.head == None:
            print("리스트가 존재하지 않습니다")
        else:
            self.head = None
            self.tail = None

sLinkedList = SLinkedList()
sLinkedList.insertSLL(1, -1)
sLinkedList.insertSLL(2, -1)
sLinkedList.insertSLL(3, -1)
sLinkedList.insertSLL(4, -1)

sLinkedList.deleteNode(-1)
sLinkedList.traverseNode()