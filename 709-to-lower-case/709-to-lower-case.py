class Solution:
    def toLowerCase(self, s: str) -> str:
        l = list(s)
        for ind,c in enumerate(l):
            if ord(c)<97 and c.isalpha():
                l[ind] = chr(ord(c)+32)
        return "".join(l)