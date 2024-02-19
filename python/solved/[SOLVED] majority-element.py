from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        remembered_number = None
        counter = 0

        for num in nums:
            if counter == 0:
                remembered_number = num
            counter += (1 if num == remembered_number else -1)

        return remembered_number

s = Solution()
input_list = [3, 3, 4]
print(s.majorityElement(input_list))
