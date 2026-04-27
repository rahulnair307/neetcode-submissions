'''
- Brute Force Solution: go for each index and then rescan an dskip that i and multiply and append to new array this would be O(n^2)
- Optimized Solution: take the products of all the values and then go through array once and divide out that specific number and put in its place
- Optimal Solution: 
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # prefixProduct = [0] * len(n)

        # for i in range(len(n)):
        #     if i = 0:
        #         prefixProduct[i] = nums[i]
        #     else:    
        #         prefixProduct[i] = prefixProduct[i - 1] * prefixProduct[i]
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range((n) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res