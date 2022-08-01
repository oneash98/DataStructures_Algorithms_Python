from curses.panel import new_panel


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            else:
                node = node.next

    def createCSLinkedList(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node

    def insertCSLL(self, value, location):
        if self.head == None:
            return "리스트가 존재하지 않습니다"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traversalCSLL(self):
        if self.head == None:
            "리스트가 존재하지 않습니다"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.head:
                    break
    
    def searchCSLL(self, value):
        if self.head == None:
            return "리스트가 존재하지 않습니다"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.head:
                    return "node가 존재하지 않습니다."

    def deleteNode(self, location):
        if self.head == None:
            return "리스트가 존재하지 않습니다"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None         
                else:
                    node = self.head
                    while node:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node           
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                
                


csll = CSLinkedList()
csll.createCSLinkedList(1)
csll.insertCSLL(0, 0)
csll.insertCSLL(5, -1)
csll.insertCSLL(2, 2)
csll.insertCSLL(3, 3)
csll.insertCSLL(4, 4)

csll.traversalCSLL()