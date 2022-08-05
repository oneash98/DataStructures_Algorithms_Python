class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(e) for e in self.list]
        return '\n'.join(values)

    def push(self, value):
        self.list.append(value)

    def peek(self):
        return self.list[-1]


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.peek())
print(stack)
