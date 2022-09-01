class WordFilter:

    def __init__(self, words: List[str]):
        self.mp = {}
        for i, word in enumerate(words):
            for l in range(len(word)):
                for r in range(len(word)):
                    self.mp[word[:l+1], word[r:]] = i

    def f(self, prefix: str, suffix: str) -> int:
        return self.mp.get((prefix, suffix), -1)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)