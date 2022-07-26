### Shallow Copy VS Deep Copy

처음으로 공부한 개발 언어는 파이썬이었지만, 얕은복사와 깊은복사 개념에 대해 알게된 것은 자바를 공부하면서였다. 자바를 공부하면서 알게된 복사의 개념은 다음과 같았다.
- shallow: 주소값만 복사. 그렇기에 한쪽 변수에서 내용이 바뀌면 다른 변수에도 반영
- deep: 실제 데이터를 새로운 메모리 공간에 복사. 즉 두 객체는 완전히 독립적인 존재
  
<br/>

파이썬으로 자료구조를 공부하다가, copy 메서드가 얕은 복사라길래, 위의 내용과 동일하게 작동할 줄 알았다. 그런데 `old_list = new_list.copy()`로 리스트를 복사하고 id를 비교해보니 둘의 주소가 다르다..!

하나하나 확인해본 결과는 다음과 같았다.

```python
# 단순 대입
old_list = [1, 2, 3]
new_list = old_list

old_list is new_list
>>> True
```
이렇게 변수에 바로 대입하는 것은 자바와 동일하게 두 변수가 동일한 주소값을 참조한다.

<br/>

```python
# copy()
old_list = [1, 2, 3]
new_list = old_list.copy()

old_list is new_list
>>> False

id(old_list[0]) == id(new_list[0])
>>> True

old_list[0] = 0
old_list
>>> [0, 2, 3]
new_list
>>> [1, 2, 3]
id(old_list[0]) == id(new_list[0])
>>> False
```
copy() 메서드를 사용하여 복사를 했더니, 두 변수가 참조하는 주소값이 다르다. 분명 얕은복사랬는데.... 얕은 복사는 주소값을 복사한다 했는데... 내가 알던 개념과 다른 것 같다. 

리스트 자체의 주소값은 두 객체가 다르지만, element가 저장된 주소값은 동일하다. 하지만, 한쪽에서 값을 변경하면 다른 쪽에는 반영이되지 않고, 변경한 값이 가르키는 주소값도 달라져있다.

아직 나에게는 이해하기 어려운 부분이지만, 이러저러한 이유로 인해(쉽게 사용할 수 있도록 하기 위해?) 파이썬 리스트에는 값이 아닌 메모리 주소를 저장하고, 메모리 할당 구조가 좀 다르다는 것 같다.

그렇다면 copy()는 왜 deep이 아닌 shallow copy인가 하면...
```python
old_list = [[1, 2, 3], [4, 5, 6]]
new_list = old_list.copy()

old_list[0][0] == 0
old_list
>>> [[0, 2, 3], [4, 5, 6]]
new_list
>>> [[0, 2, 3], [4, 5, 6]]

id(old_list[0]) == id(new_list[0])
>>> True
```
element의 주소값은 동일하기 때문에, 이렇게 이중 리스트인 경우, 리스트 안의 리스트를 가르키는 주소값은 둘이 동일하다. 따라서 한 쪽을 바꿔도 다른 쪽에 반영이 된다. 

<br/>

모든 값들을 새로운 메모리에 할당하는 진정한 deep copy를 원한다면 deepcopy 메서드를 사용해야한다.
```python
import copy

new_list = copy.deepcopy(old_list)
```

<br/>

튜플의 경우에는 copy()메서드로 복사할 경우 주소값이 동일하다. 
```python
import copy

old_tuple = (1, 2, 3)
new_tuple = copy.copy(old_tuple)

old_tuple is new_tuple
>>> True
```