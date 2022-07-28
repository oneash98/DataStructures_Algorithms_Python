### `__iter__`와 yield

클래스로 iterable한 객체를 만들고 싶다면 -> `__iter__`를 구현해야 한다.

아래와 같은 클래스가 있다고 하자.
```python
class MyClass():
    num = 1

instance = MyClass()
```
위 객체로 `for i in instance`와 같이 이터레이션을 하려고 하면 오류가 발생할 것이다. 반복할 내용이 없기 때문이다.

iterable 한 객체를 만들기 위해서는 클래스 내에 `__iter__()` 메서드를 구현해야 한다.

```python
class MyClass():
    num = 1

    def __iter__(self):
        while self.num <= 5:
            yield self.num
            self.num += 1

instance = MyClass()
for num in instance:
    print(num)
>>> 1
>>> 2
>>> 3
>>> 4
>>> 5
```
위와 같이 클래스 내에 `__iter__` 메서드로 이터레이션하고 싶은 내용을 구현하면 for 문으로 객체를 이터레이션할 수 있다.

`yield` 키워드는 제너레이터라는 객체를 생성한다. 만약 `yield` 대신 `return`을 사용하면 `__iter__()` 내의 반복문은 바로 중단되버릴 것이다.
```python
class MyClass():
    num = 1

    def __iter__(self):
        while self.num <= 5:
            return self.num # return 문이므로, 중단
            self.num += 1

instance = MyClass()
for num in instance:
    print(num)
>>> 1 
```

하지만, `yield`를 사용하면, 반환해야할 값을 어딘가에 저장해두는 듯한 역할을 한다. 

(yield 와 제너레이터의 정확한 개념 및 역할은 아직 잘 모르겠다. 일단 이 정도만 파악하고 넘어가자)

<br/>

### 링크드 리스트와 `__iter__`

링크드 리스트 객체로 각 node들을 순회하기 위해서도 `__iter__` 메서드로 iterable하게 만들어야 한다.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # 코드 구현
    # head - node - node - ... - node - tail 연결

linkedList = LinkedList()
```
위와 같이 링크드리스트 객체를 만들었다고 하자. `__iter__` 메서드 없이 node들을 출력하기 위해서는 아래와 같이 직접 node를 하나하나 찾아가야할 것이다.

```python
linkedList = LinkedList()
print(linkedList.head.value())
print(linkedList.head.next.value())
print(linkedList.head.next.next.value())
print(linkedList.head.next.next.next.value())
```

하지만, `__iter__`를 사용하면 위 사항이 해결된다.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    # 코드 구현

linkedList = LinkedList()
for node in linkedList:
    print(node.value)
```