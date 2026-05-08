class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stack_value, stack_index = stack.pop()
                result[stack_index] = index - stack_index
            
            stack.append((temp, index))
        
        return result

