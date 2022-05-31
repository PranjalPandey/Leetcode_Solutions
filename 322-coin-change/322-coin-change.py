class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for i in range(amount+1)]
        if amount==0:
            return 0
        for coin in coins:
            if coin>amount:
                continue
            dp[coin]=1
            for i in range(coin+1,amount+1):
                dp[i] = min(dp[i],dp[i-coin]+1)
        return -1 if dp[amount]==amount+1 else dp[amount]
        