class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i, curSum):
            
            if curSum == target:
                res.append(path[:])  # has a another solution
                return
            
            if curSum > target or i == len(nums):   # no point in adding new number if curSum is greater than target
                return

            # decision skip the num
            backtrack(i+1, curSum)

            # decision use the num
            path.append(nums[i])
            backtrack(i, curSum + nums[i]) # do not want to do i+1 because we can use the same number!
            path.pop()


        backtrack(0, 0)
        return res
        