class Solution:
    def climbStairs(self, n: int) -> int:
        # Each step’s count depends only on the two previous step counts.
        # Because at each point you can only look back 1 or 2 steps.

        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 1
        curr = 2

        for i in range(3, n+1):
            prev, curr = curr, prev+curr
        
        return curr