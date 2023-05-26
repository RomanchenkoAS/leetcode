"""Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        
        nums = sorted(nums)
        
        for i, num in enumerate(nums):
            target = -num
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                if target == nums[l] + nums[r]:
                    result.append([num, nums[l], nums[r]])
                    break
                elif target < nums[l] + nums[r]:
                    r -= 1
                else:
                    l += 1
                    
        return result
    
s = Solution()
nums = [-1,0,1,2,-1,-4]

print(s.threeSum(nums=nums)) 