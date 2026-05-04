class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_to_opening = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in closing_to_opening: # if it is a closing bracket
                if stack and stack[-1] == closing_to_opening[c]:    # checks if exist and checks the top of stack
                    stack.pop()
                else:
                    return False

            else:   # opening parenthesis
                stack.append(c)
        
        return not stack
