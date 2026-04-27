class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        n = len(prices)
        maxProfit = 0

        for r in range(n):
            while prices[r] - prices[l] < 0:
                l += 1
            currProfit = prices[r] - prices[l]
            maxProfit = max(maxProfit, currProfit)
        
        return maxProfit
        