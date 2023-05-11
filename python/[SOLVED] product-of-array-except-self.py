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
        n = len(nums)
        left = [1] * n
        right = [1] * n
        
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
            
        for i in range(n-2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        return [right[i] * left[i] for i in range(0,n)]


s = Solution()

# input = [-1,1,0,-3,3]
input = [1, 2, 3, 4]

print("initial:")
print(input)

print(s.productExceptSelf(input))
