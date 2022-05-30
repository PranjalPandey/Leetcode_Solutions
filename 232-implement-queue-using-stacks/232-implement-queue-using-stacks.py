class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:

        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            i = self.stack1[-1]
            self.stack1.pop()
            self.stack2.append(i)
        item = self.stack2[-1]
        self.stack2.pop()
        self.stack1 = self.stack2[::-1]
        self.stack2 = []
        return item

    def peek(self) -> int:
        while self.stack1:
            i = self.stack1[-1]
            self.stack1.pop()
            self.stack2.append(i)
        item= self.stack2[-1]
        self.stack1 = self.stack2[::-1]
        self.stack2 = []
        return item 

    def empty(self) -> bool:
        return True if not (self.stack1 or self.stack2) else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()