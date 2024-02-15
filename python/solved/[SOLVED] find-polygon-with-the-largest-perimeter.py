from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1

        sorted_reversed_nums = sorted(nums, reverse=True)
        running_sum = sum(sorted_reversed_nums)
        edges = len(sorted_reversed_nums)

        for num in sorted_reversed_nums:
            if num >= running_sum - num:
                # cannot be an edge
                edges -= 1
                running_sum -= num
                continue
            else:
                # is an edge
                if edges >= 3:
                    return running_sum
                else:
                    return -1
        return -1


s = Solution()
nums = [1, 12, 1, 2, 5, 50, 3]
# nums = [1, 1, 2]
# nums = [1, 5, 1, 7]
# nums = [5, 5, 5]

res = s.largestPerimeter(nums)
print(res)
