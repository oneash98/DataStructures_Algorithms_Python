# Use single python list to implement three stacks

class MultiStack:
    def __init__(self, stackSize):
        self.numberOfStacks = 3
        self.list = [0] * (stackSize * self.numberOfStacks)
        self.sizes = [0] * self.numberOfStacks
        self.stackSize = stackSize

    def isFull(self, stackNum):
        if self.sizes[stackNum] == self.stackSize:
            return True
        else:
            return False

    def isEmpty(self, stackNum):
        if self.sizes[stackNum] == 0:
            return True
        else:
            return False

    def indexOfTop(self, stackNum):
        offset = stackNum * self.stackSize
        return offset + self.sizes[stackNum] - 1

    def push(self, value, stackNum):
        if self.isFull(stackNum):
            return "Stack is full"
        else:
            self.sizes[stackNum] += 1
            self.list[self.indexOfTop(stackNum)] = value

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            return "Stack is empty"
        else:
            value = self.list[self.indexOfTop(stackNum)]
            self.list[self.indexOfTop(stackNum)] = 0
            self.sizes[stackNum] -= 1
            return value

    def peek(self, stackNum):
        value = self.list[self.indexOfTop(stackNum)]
        return value

myStack = MultiStack(6)
print(myStack.isFull(0))
print(myStack.isEmpty(1))
myStack.push(1, 0)
myStack.push(2, 0)
myStack.push(3, 2)
print(myStack.peek(1))