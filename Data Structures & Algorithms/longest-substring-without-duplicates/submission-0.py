class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        resultLength = 0
        
        for r in range(len(s)):
            while s[r] in charSet:  # we will keep doing this until the duplicate is gone from the set
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            resultLength = max(resultLength, r - l + 1)  # previous length or the current size of the window
                                                        # the size of the window is the length of the contiguous non repeating subarray
        return resultLength