class Solution:
    def reverseWords(self, s: str) -> str:
        # s = "  hello  world"
        st = list(reversed(s.split()))
        return " ".join(st)
        
        
        