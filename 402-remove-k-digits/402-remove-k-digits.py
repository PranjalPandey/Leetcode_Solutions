class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==k:
            return "0"
        stack = []
        for n in num:
            while stack and k and stack[-1]>n:
                k-=1
                stack.pop()
            stack.append(n)
        while k>0:
            stack.pop()
            k-=1
        ans = "".join(stack).lstrip("0")
        if ans == "":
            return "0"
        return ans