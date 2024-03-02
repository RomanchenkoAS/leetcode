from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_ptr = right_ptr = 0  # Left and right ptrs
        sum = 0

        # set proper r
        for num in nums:
            sum += num
            right_ptr += 1
            if sum >= target:
                break
        if sum < target:
            return 0

        # for target = 7 and nums = [2, 3, 1, 2, 4, 3]
        # r = 4 | sum = 8

        length = right_ptr # That is r - l


target = 7
nums = [2, 3, 1, 2, 4, 3]
