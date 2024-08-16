"""
643. Maximum Average Subarray I
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10^-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums:
            return 0

        running_sum = left = right = 0
        running_max = None
        for right in range(0, len(nums)):

            running_sum += nums[right]

            if right == k - 1:
                running_max = running_sum
            elif right >= k:
                # Increment both pointers
                running_sum = running_sum - nums[left]
                left += 1
                running_max = max(running_max, running_sum)

            # print(left, right, running_sum, running_max)

        return running_max / k if running_max else running_sum / k


# nums = [4, 0, 4, 3, 3]
nums = [1,12,-5,-6,50,3]


k = 4
sol = Solution()
res = sol.findMaxAverage(nums, k)
print(res)
