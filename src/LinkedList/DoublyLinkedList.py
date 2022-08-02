class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, value):
        node = Node(value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node

    def insertNode(self, value, location):
        if self.head == None:
            return "리스트가 존재하지 않습니다"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
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
                nextNode.prev = newNode
                tempNode.next = newNode

    def deleteNode(self, location):
        if self.head == None:
            return "리스트가 존재하지 않습니다"
        else:       
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode


dLL = DLinkedList()
dLL.createDLL(3)
dLL.insertNode(0, 0)
dLL.insertNode(1, 1)
dLL.insertNode(2, 2)
dLL.insertNode(4, -1)
dLL.insertNode(5, -1)
for node in dLL:
    print(node.value)