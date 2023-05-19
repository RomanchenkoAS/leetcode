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
        
        s = set(nums)
        
        print(s)
        
        max_length = 0
        length_current = 1
        
        current = min(s)
        s.remove(current)
        
        print(current)
        
        while s:
            if current + 1 in s:
                current += 1
                s.remove(current)
                length_current += 1
            else:
                max_length = max(max_length, length_current)
                length_current = 1
                current = min(s)
                s.remove(current)
                
        return max(max_length, length_current)
        
        
# nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
nums = [9,1,4,7,3,-1,0,5,8,-1,6]

s = Solution()

print(s.longestConsecutive(nums))