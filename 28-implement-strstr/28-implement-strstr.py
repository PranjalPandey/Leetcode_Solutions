class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            h = haystack.index(needle)
            return h
        except:
            return -1