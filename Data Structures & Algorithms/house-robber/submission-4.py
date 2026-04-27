class Solution:
    def rob(self, nums: List[int]) -> int:
        # if two adjacent houses broken into same night -> cannot do this
        # max money you can rob without robbing two back to back

        # Bottom-Up - Tabulation
        # building up a array
            # at each index of this array we want to see what is the maximum money we can rob at that point
            
            # OPTION 1: whenever we see we can choose to not rob it and use the money from index before
            # OPTION 2: immidiate money + two steps prev 
            
            # recurrence relation max(dp[i-1], dp[i-2]+nums[i])
        
        # # Naive Recursive Solution
        # # Time: O(2^n)
        # # Space: O(n)
        # n = len(nums)
        # def helper(i):
        #     if i == 0:
        #         return nums[0]
        #     if i == 1:
        #         return max(nums[0], nums[1])

        #     return max(nums[i]+helper(i-2), helper(i-1))
        # return helper(n-1)

        # # Top Down DP (Memoized)
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # if n == 2:
        #     return max(nums[0], nums[1])

        # memo = {0:nums[0], 1:max(nums[0],nums[1])}

        # def helper(i):
        #     if i in memo:
        #         return memo[i]
        #     else:
        #         memo[i] = max(nums[i]+helper(i-2), helper(i-1))
        #         return memo[i]
        # return helper(n-1)

        # # Bottom-Up -> Tabulation build up the DP array
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # if n == 2:
        #     return max(nums[0], nums[1])
        # dp = [0]* n
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, n):
        #     dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        # return dp[n-1]


        # Bottom-Up -> constant space with prev and curr
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, n):
            prev, curr = curr, max(curr, nums[i] + prev)
        
        return curr