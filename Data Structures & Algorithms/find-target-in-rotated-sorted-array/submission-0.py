class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else: 
                r = m
    
        minIndex = l
        if minIndex == 0:
            l = 0
            r = n-1
        elif target >= nums[0] and target <= nums[minIndex - 1]:
            l = 0
            r = minIndex - 1
        else:
            l = minIndex
            r = n - 1
        ### normal binary search from here
        while l <= r:
            m = (l+r) // 2

            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        return -1   ## if not found