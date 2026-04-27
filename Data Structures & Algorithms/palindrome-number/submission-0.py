class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverseNumber = 0
        temp = x
        
        while temp > 0:
            reverseNumber = (reverseNumber * 10) + (temp  % 10)
            temp = temp // 10
        
        if reverseNumber == x:
            return True
        
        return False