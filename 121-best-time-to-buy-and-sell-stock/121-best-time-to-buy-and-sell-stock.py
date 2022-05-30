class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_so_far = 0
        for i,price in enumerate(prices):
            if price<min_price:
                min_price = price
            if max_so_far<(price-min_price):
                max_so_far = (price-min_price)
        return max_so_far
                