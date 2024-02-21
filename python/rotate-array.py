from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return None

        if k > len(nums):
            k = k % len(nums)

        i = 0
        while True:
            next_i = i + k
            if next_i > len(nums):
                next_i -= len(nums)
            prev_number = nums[next_i]
            nums[next_i] = nums[i]

        # NOT SOLVED IN O(1) SPACE


            if i == 0:
                break

        # additional_list = [None] * len(nums)
        # for index in range(len(nums)):
        #     if index + k < len(nums):
        #         additional_list[index + k] = nums[index]
        #     else:
        #         additional_list[index + k - len(nums)] = nums[index]
        #
        # for i in range(len(nums)):
        #     nums[i] = additional_list[i]

S = Solution()
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = [1,2]
kok = 3
S.rotate(nums, kok)
