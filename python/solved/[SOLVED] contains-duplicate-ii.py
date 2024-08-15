"""
219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False

        if k >= len(nums):
            return len(nums) != len(set(nums))

        left = right = 0
        numbers_inside_window = set()

        for right in range(0, k + 1):

            current = nums[right]
            if current in numbers_inside_window:
                return True

            numbers_inside_window.add(current)

        while right < len(nums) - 1:
            if nums[left] in numbers_inside_window:
                numbers_inside_window.remove(nums[left])

            left += 1
            right += 1

            current = nums[right]
            if current in numbers_inside_window:
                return True

            numbers_inside_window.add(current)

        return False


def main():
    options = [
        ([1, 2, 3, 1], 3),
        ([1, 0, 1, 1], 1),
        ([1, 2, 3, 1, 2, 3], 2),
        ([1], 1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)
    ]
    nums, k = options[4]
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))


if __name__ == '__main__':
    main()
