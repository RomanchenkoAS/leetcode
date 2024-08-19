"""
334. Increasing Triplet Subsequence
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such
that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l = len(nums)

        if l < 3:
            return False
        elif l == 3:
            return nums[0] < nums[1] < nums[2]

        min_val = mid_val = float('+inf')
        for num in nums:
            if num < min_val:
                min_val = num
            elif min_val < num < mid_val:
                mid_val = num
            elif min_val < mid_val < num:
                return True

        return False


# nums = [2, 1, 5, 0, 4, 6]
nums = [20, 100, 10, 12, 5, 13]
sol = Solution()
res = sol.increasingTriplet(nums)
print(res)
