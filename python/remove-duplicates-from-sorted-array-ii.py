from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = {}

        for i in range(len(nums) - 1, -1, -1):
            seen.setdefault(nums[i], 0)
            seen[nums[i]] += 1
            if seen[nums[i]] > 2:
                nums.pop(i)

        return len(nums)

S = Solution()
input_list = [1,1,1,2,2,3]
print(S.removeDuplicates(input_list))
