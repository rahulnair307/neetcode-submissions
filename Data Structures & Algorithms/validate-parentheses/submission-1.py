'''
- given a string with different types of parentheses (),{},[]
- all parentheses will start with opening bracket and each closing bracket needs to match inorder
- to keep record of this ordering it is best to use a stack this stack will store the opening parentheses and when the closing comes you can pop and eliminate the pair and go til end of string and there should be nothing in stack as well
- to keep the comparison of opening and closing parentheses types using a hashmap and utilizing its O(1) lookup can be very helpful so it can eliminate a lot of if else statements
    - the hashmap will keep track of the closing parentheses type as the key and the value will be opening parenthesis and i can check when it is in stack then i can pop
'''
class Solution:
    def isValid(self, s: str) -> bool:
        charStack = []
        parenthesesMap = { "}" : "{", ")" : "(", "]" : "[" }    # mapping the closing to opening parentheses
        openParentheses = parenthesesMap.values()
        for char in s:
            if char in openParentheses:
                charStack.append(char)
            else:
                if charStack and parenthesesMap[char] == charStack[-1]:
                    charStack.pop()
                else:
                    return False
        return not charStack

