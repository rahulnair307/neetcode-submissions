class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1     # index of last number
              
        while i >= 0:
            if 0 <= digits[i] <= 8:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                i -= 1

        digits.insert(0, 1)
        return digits
            