class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # a two pointer sliding window solution where i will have left and right pointer 
        l = 0
        r = 1
        temp = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                temp = max(temp, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1

        
        return temp
