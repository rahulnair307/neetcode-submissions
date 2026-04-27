class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = float('inf')    # highest number possible
        i = 0
        # after this for loop we will get our minimum number our index can go til without getting out of bounds error
        for s in strs:
            if len(s) < minLength:
                minLength = len(s)
        
        while i < minLength:
            for s in strs[1:]:  # starts checking from the second word so we do not unneccassiarly check the first one
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1

        return s[:i]