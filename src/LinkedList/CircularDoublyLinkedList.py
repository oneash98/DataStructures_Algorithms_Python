from re import L


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class CDLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
                break

    def createCDLL(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode

    def insertNode(self, value, location):
        if self.head == None:
            return "리스트가 존재하지 않습니다"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                newNode.next = nextNode
                newNode.prev = tempNode
                tempNode.next = newNode
                nextNode.prev = newNode