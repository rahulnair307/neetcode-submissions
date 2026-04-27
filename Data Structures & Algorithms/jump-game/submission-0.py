class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # brute force is O(n^n) check for every PATH
        # when u cache it you can do O(n^2)
        # greedy is O(n)

        # Bottom-Up -> Tabulation
            # the dp array tells us at index what is false and what is true so then we wont have to redo the work

            #[2, 3, 1, 1, 4]
            #          *       * means this can be our goalpost 
            # shift the "goalpost" meaning the end closer to index 0 as possible
        goal = len(nums) - 1  #starts at end
        for i in range(len(nums)-1, -1, -1): # start last work way to beginning
            if i + nums[i] >= goal:
                goal = i
                
        if goal == 0:
            return True
        else:
            return False

