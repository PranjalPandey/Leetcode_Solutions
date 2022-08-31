class FreqStack:

    '''
    {
    2:3,
    4:3
    }
    '''
    def __init__(self):
        self.freq = defaultdict(int)
        self.freq_stack = []
        

    def push(self, key: int) -> None:
        
        self.freq[key] += 1
        if self.freq[key] > len(self.freq_stack):
            self.freq_stack.append([key])
        else:
            self.freq_stack[self.freq[key]-1].append(key)
        
    def pop(self) -> int:
        m = self.freq_stack[-1].pop()
        if len(self.freq_stack[-1]) == 0:
            self.freq_stack.pop()
        self.freq[m] -= 1
        return m
         

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()