class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for _ in s:
            if _ in ("(","{","["):
                stack.append(_)
            else:
                if stack and stack[-1]=="(" and _==")":
                    stack.pop()
                elif stack and stack[-1]=="{" and _=="}":
                    stack.pop()
                elif stack and stack[-1]=="[" and _=="]":
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False