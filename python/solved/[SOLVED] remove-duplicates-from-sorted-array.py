from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_pointer = 1

        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                nums[unique_pointer] = nums[index]
                unique_pointer += 1

        return unique_pointer


S = Solution()
inputs = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(S.removeDuplicates(inputs))
