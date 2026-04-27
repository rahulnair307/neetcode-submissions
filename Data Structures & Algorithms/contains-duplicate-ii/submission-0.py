class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()  # keep track of all the values in our window
        l = 0
        n = len(nums)

        for r in range(n):
            if abs(r - l) > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            
            window.add(nums[r])
        return False