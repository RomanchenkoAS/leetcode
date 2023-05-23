"""Given an array of integers temperatures represents the daily temperatures, return an array 
answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer 
temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead."""


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        index = len(temperatures) - 1
        stack = []
        result = [-1 for i in range(len(temperatures))]
        print(result)
        
        while index >= 0:
            current = temperatures[index]
            print("current day temperature", current)
            
            # Copy stack
            copied = stack[::-1]
            print("current stack copied: ", copied)
            
            # Check if bigger is in stack
            for i, temp in enumerate(copied):
                if temp > current:
                    result[index] = i
                
            stack.append(current)
            
            print("Current result: ", result, "\n\n")
            
            index -= 1
            
            
        return result


s = Solution()

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

print(s.dailyTemperatures(temperatures=temperatures))
