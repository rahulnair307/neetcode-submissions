class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        leftIndex = 0
        maxWindowSize = 0
        
        for rightIndex in range(len(s)):
            while s[rightIndex] in hashSet:
                hashSet.remove(s[leftIndex])
                leftIndex += 1
            # now duplicates are gone
            hashSet.add(s[rightIndex])
            maxWindowSize = max(maxWindowSize, rightIndex - leftIndex + 1)
        return maxWindowSize
                

