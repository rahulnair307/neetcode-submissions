class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHashMap = {}
        tHashMap = {}

        for char in s:
            sHashMap[char] = sHashMap.get(char, 0) + 1
        
        for char in t:
            tHashMap[char] = tHashMap.get(char, 0) + 1

        if tHashMap == sHashMap:
            return True

        return False