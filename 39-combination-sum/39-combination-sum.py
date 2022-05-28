class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp=[[] for i in range(target+1)]
        for i in range(len(candidates)):
            for j in range(1,len(dp)):
                if candidates[i]==j:
                    dp[j].append([candidates[i]])
                elif candidates[i]<j:
                    rem = j-candidates[i]
                    for remaining in dp[rem]:
                        dp[j].append([candidates[i]]+remaining)
        return dp[target]