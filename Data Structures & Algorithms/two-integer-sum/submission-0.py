class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        recordOfSum = {}
        otherInt = 0
        indexCounter = 0

        for i in nums:
            otherInt = target - i

            if otherInt in recordOfSum:
                return [recordOfSum[otherInt], indexCounter]
            else:
                recordOfSum[i] = indexCounter
            
            indexCounter += 1 