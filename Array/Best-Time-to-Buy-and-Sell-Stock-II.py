class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max, start, l = 0, prices[0], len(prices)

        for i in range(0, l):
            if start < prices[i]:
                max += prices[i] - start
            start = prices[i]
        
        return max