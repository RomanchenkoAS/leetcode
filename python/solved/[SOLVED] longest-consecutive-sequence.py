"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time."""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        s = sorted(list(set(nums)))
        
        max_length = 0
        current_length = 1
        current = s[0]
        
        for i in range(1, len(s)):
            if s[i] == current + 1:
                current_length += 1
                current += 1
            else:
                max_length = max(current_length, max_length)
                current_length = 1
                current = s[i]
        
        return max(max_length, current_length)
            
        
# nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
nums = [9,1,4,7,3,-1,0,5,8,-1,6]

s = Solution()

print(s.longestConsecutive(nums))