class Solution:
    '''
    - nonDecreasing order is basically sorted in increasing order that could have duplicates
    - in-order so we have to update to the array we are given this is the tricky part
    - count the number of unique values
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]: 
                nums[l] = nums[r]
                l+=1

        return l