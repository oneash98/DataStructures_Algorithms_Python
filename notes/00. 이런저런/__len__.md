### `__len__`

내장함수 len()을 구현하기 위하여 호출. 객체의 길이 반환

오버라이딩하여 원하는 출력방식 구현 가능

```python
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        node = self.head
        result = 0
        while node:
            result += 1
            node = node.next
        return result

linkedList = LinkedList()
print(len(linkedList))
```