from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of nums1 and nums2
        index1, index2 = m - 1, n - 1
        indexMerge = m + n - 1

        while index2 >= 0:
            if index1 >= 0 and nums1[index1] > nums2[index2]:
                nums1[indexMerge] = nums1[index1]
                index1 -= 1
            else:
                nums1[indexMerge] = nums2[index2]
                index2 -= 1
            indexMerge -= 1

s = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(s.merge(nums1, m, nums2, n))
