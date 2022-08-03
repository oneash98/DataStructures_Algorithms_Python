### `__str__`

내장함수 str()를 구현하기 위해 호출

클래스로 객체를 생성 후, `print(객체)`를 했을 때, object 클래스의 `__str__`메서드가 호출되어 문자열 정보 반환.

`__str__`을 오버라이딩하여 원하는 출력 방식을 구현할 수 있음

```python
class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return '{0}의 값은 {1}입니다.'.format(self.name, self.value)

myClass = MyClass(name, value)
print(myClass)
>>> name의 값은 value입니다.
```

참고로, `print(객체)`, `print(str(객체))`, `print(객체.__str__)` 모두 같은 결과 반환