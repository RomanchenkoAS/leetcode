"""Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation."""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def product(array):
            prod = 1
            for i in array:
                prod *= i
            return prod
        result = []
        for i in range(len(nums)):
            # print(i)
            # print(nums[0:i])
            # print(nums[i+1:])
            result.append(product(nums[0:i])*product(nums[i + 1:]))
            
        
        return result
    
    
s = Solution()

# input = [-1,1,0,-3,3]
input = [1,2,3,4]

print(s.productExceptSelf(input))