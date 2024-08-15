"""
228. Summary Ranges

You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges,
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
"""
from typing import List


def append_range(ranges, current_range):
    if len(current_range) == 1:
        ranges.append(str(current_range[0]))
    elif len(current_range) > 1:
        ranges.append(f"{current_range[0]}->{current_range[-1]}")
    current_range.clear()


class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        ranges = []
        current_range = []

        prev = None
        for current_number in nums:
            if prev is not None:
                # Numbers are not adjacent
                if prev + 1 != current_number:
                    append_range(ranges, current_range)

            current_range.append(current_number)
            prev = current_number

        if prev not in current_range:
            current_range.append(prev)
        append_range(ranges, current_range)
        return ranges


sol = Solution()
# l = [0, 1, 2, 4, 5, 7]
# l = [0, 2, 3, 4, 6, 8, 9]
l = [-2147483648, -2147483647, 2147483647]
res = sol.summaryRanges(l)
print(res)
