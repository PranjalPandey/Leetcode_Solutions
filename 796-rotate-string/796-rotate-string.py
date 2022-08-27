class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # count = len(s)
        if len(s)!=len(goal):
            return False
        # while count:
        #     if s==goal:
        #         return True
        #     s=s[1:]+s[0]
        #     count-=1
        # return False

        s+=s
        if goal in s:
            return True
        return False