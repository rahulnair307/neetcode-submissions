class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result = ""
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                result += int(k) * substring
                stack.append(result)
                result = ""
        
        return "".join(stack)