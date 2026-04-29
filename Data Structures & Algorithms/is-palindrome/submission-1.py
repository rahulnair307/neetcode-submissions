class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l <= r:
            if not self.isAlphanumeric(s[l]):
                l += 1
            elif not self.isAlphanumeric(s[r]):
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else: 
                l += 1
                r -= 1
        
        return True
    
    def isAlphanumeric(self, character):
        return ((ord('A') <= ord(character) <= ord('Z')) or
            (ord('a') <= ord(character) <= ord('z')) or
            (ord('0') <= ord(character) <= ord('9')))