from operator import itemgetter
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []
        for log in logs:
            
            if log[-1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
        letter= sorted(letter, key = lambda l: (l.split()[1:],l.split()[0]))
        # ans = []
        # for i in letter+digit:
        #     ans.append(" ".join(i))
        return letter+digit