from collections import deque
class MinStack:

    def __init__(self):
        self.data = deque()
        self.curr_min = deque()

    def push(self, val: int) -> None:
        if not self.data:
            self.data.append(val)
            self.curr_min.append(val)
        else:
            self.data.append(val)
            self.curr_min.append(min(val,self.curr_min[-1]))

    def pop(self) -> None:
        if self.data:
            self.data.pop()
            self.curr_min.pop()
            

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        return self.curr_min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()