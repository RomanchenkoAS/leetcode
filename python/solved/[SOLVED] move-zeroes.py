"""
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative
order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # Naive algorithm
        # list2 = [n for n in nums if n != 0]
        # for idx in range(0, len(nums)):
        #     if idx < len(list2):
        #         nums[idx] = list2[idx]
        #     else:
        #         nums[idx] = 0

        number_of_zeroes = left = right = 0

        # Left points at where we need to write next digit
        # Right is current digit we inspect in this loop iteration
        # number_of_zeroes is how many zeroes we've seen yet

        for right in range(0, len(nums)):
            current_digit = nums[right]

            if current_digit == 0:
                number_of_zeroes += 1
            else:
                while left < right:
                    if nums[left] == 0:
                        nums[left] = current_digit
                        nums[right] = 0
                        left += 1
                        break
                    left += 1

        for idx in range(len(nums) - number_of_zeroes, len(nums)):
            nums[idx] = 0


nums = [0, 1, 0, 3, 12]
# nums = [2, 1]

s = Solution()
s.moveZeroes(nums)
print(nums)
