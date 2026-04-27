class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHashMap = {}
        tHashMap = {}
        if len(s) != len(t):
            return False
            
        for char in s:
            sHashMap[char] = sHashMap.get(char, 0) + 1
        
        for char in t:
            tHashMap[char] = tHashMap.get(char, 0) + 1

        #if tHashMap == sHashMap:
            #return True
        for c in sHashMap:
            if sHashMap[c] != tHashMap.get(c, 0):
                return False
        
        return True
        