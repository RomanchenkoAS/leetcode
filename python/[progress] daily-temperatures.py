"""Given an array of integers temperatures represents the daily temperatures, return an array 
answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer 
temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead."""

class Solution(object):
    def dailyTemperatures(self, temps):
        
        result = [0] * len(temps)
        stack = []
        
        for i, t in enumerate(temps):
            while stack and temps[stack[-1]] < t:
                max_index = stack.pop()
                result[max_index] = i - max_index
                
            stack.append(i)
            
        return result                
        
    # def dailyTemperatures(self, temperatures):
    #     """
    #     :type temperatures: List[int]
    #     :rtype: List[int]
    #     """
        
    #     index = len(temperatures) - 1
    #     stack = []
    #     result = []
    #     max_seen = 0
        
    #     while index >= 0:
    #         current = temperatures[index]
            
    #         if (current > max_seen):
    #             max_seen = current
    #             result.append(0)
    #             index -= 1
    #             stack.append(current)
    #             continue
            
    #         mod = False
            
    #         stack_length = len(stack) - 1
    #         for i in range(0, stack_length + 1):
    #             if stack[stack_length - i] > current:
    #                 result.append(i + 1)
    #                 mod = True
    #                 break
            
    #         if not mod:
    #             result.append(0)
                
    #         stack.append(current)
            
    #         index -= 1
        
            
    #     return result[::-1]


s = Solution()

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# temperatures = [30,40,50,60]


print(s.dailyTemperatures(temperatures))

