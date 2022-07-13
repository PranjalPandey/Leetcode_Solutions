from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = deque()
        stack2 = deque()
        for c in s:
            if c == '#':
                if stack1:
                    stack1.pop()
                else:
                    continue
            else:
                stack1.append(c)
        for c in t:
            if c == '#':
                if stack2:
                    stack2.pop()
                else:
                    continue
            else:
                stack2.append(c)
        
        if stack1 ==stack2:
            return True
        return False
        