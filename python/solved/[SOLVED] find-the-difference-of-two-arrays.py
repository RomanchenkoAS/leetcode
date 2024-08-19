"""
2215. Find the Difference of Two Arrays
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

- answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
- answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2.
 Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2.
 Therefore, answer[1] = [4,6].

Example 2:
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included
once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
"""
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_1 = set(nums1)
        set_2 = set(nums2)

        l1 = len(nums1)
        l2 = len(nums2)
        length = max(l1, l2)

        a1 = set()
        a2 = set()

        for idx in range(0, length):
            n1 = nums1[idx] if idx < l1 else None
            n2 = nums2[idx] if idx < l2 else None
            if n1 == n2:
                continue
            if n1 is not None and n1 not in set_2:
                a1.add(n1)
            if n2 is not None and n2 not in set_1:
                a2.add(n2)
        return [list(a1), list(a2)]


# nums1 = [-68, -80, -19, -94, 82, 21, -43]
# nums2 = [-63]

nums1 = [80, 5, -20, 33, 26, 29]
nums2 = [-69, 0, -36, 52, -84, -34, -67, -100, 80]

sol = Solution()
res = sol.findDifference(nums1, nums2)
print(res)
