# Remove Duplicates

from LinkedList import LinkedList

def removeDups(linkedList):
    if linkedList.head == None:
        return
    else:
        tempNode = linkedList.head
        values = {tempNode.value}
        while tempNode.next:
            if tempNode.next.value not in values:
                values.add(tempNode.next.value)
                tempNode = tempNode.next
            else:
                tempNode.next = tempNode.next.next
        return linkedList

linkedList = LinkedList()
linkedList.generate(10, 0, 99)
print(linkedList)
print(removeDups(linkedList))