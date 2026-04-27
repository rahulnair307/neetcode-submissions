class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # #recursive solution O(2^n)
        # n = len(cost)
        # def minCost(i):
        #     if i<2:
        #         return 0
        #     return min(cost[i-2]+minCost(i-2), 
        #                 cost[i-1]+minCost(i-1))
        # return minCost(n)

        # # TopDown DP (Memoization)
        # n = len(cost)
        # memo = {0:0, 1:0}
        # def minCost(i):
        #     if i in memo:
        #         return memo[i]
        #     else:
        #         memo[i] = min(cost[i-2] + minCost(i-2), 
        #                 cost[i-1] + minCost(i-1))
        #         return memo[i]
        # return minCost(n)

        # Bottom-Up DP (Tabulation)
        n = len(cost)
        dp = [0] * (n+1) # need to find the minimum cost to get OUT of the stair so need to do +1
        
        for i in range(2,n+1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])

        return dp[n]
