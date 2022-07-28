from re import A


class MyClass():
    a = 1

    def __iter__(self):
        while self.a <= 5:
            yield self.a
            self.a += 1

instance = MyClass()

for i in instance:
    print(i)