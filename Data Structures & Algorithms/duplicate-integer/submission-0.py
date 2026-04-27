class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsExist = set()
        for i in nums:
            if i in numsExist:
                return True
            numsExist.add(i)

        return False