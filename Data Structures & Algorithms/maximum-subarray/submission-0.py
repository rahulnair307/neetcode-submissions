class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [-2, 7, -3, 4]
        # kind of like sliding window increment right pointer but left pointer gets shifted if our prefix is (-) negative
        # TC: O(n)

        maxSub = nums[0]
        currSum = 0

        for n in nums:
            if currSum<0:
                currSum = 0
            currSum += n
            maxSub = max(maxSub, currSum)
        return maxSub
