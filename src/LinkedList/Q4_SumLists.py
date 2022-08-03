# list1 = 7 -> 1 -> 6
# list2 = 5 -> 9 -> 2
# 617 + 295 = 912
# sumList = 2 -> 1 -> 9

from LinkedList import LinkedList

def sumLists(lList1, lList2):
    node1 = lList1.head
    node2 = lList2.head
    carry = 0
    ll = LinkedList()

    while node1 or node2:
        sum = node1.value + node2.value + carry
        if sum // 10 == 0:
            carry = 0
        else:
            carry = 1
            sum = sum % 10
        ll.add(sum)
        node1 = node1.next
        node2 = node2.next
    
    if carry == 1:
        ll.add(1)
        
    return ll

ll1 = LinkedList()
ll1.generate(3, 0, 9)
ll2 = LinkedList()
ll2.generate(3, 0, 9)

print(ll1)
print(ll2)
print(sumLists(ll1, ll2))