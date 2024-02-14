from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negatives = []
        positives = []
        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)
        result = []
        for positive, negative in zip(positives, negatives):
            result.append(positive)
            result.append(negative)
        return result


arr = [3, 1, -2, -5, 2, -4]
s = Solution()
res = s.rearrangeArray(arr)
print(res)
