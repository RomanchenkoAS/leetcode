class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []

        for i, x in enumerate(nums):
            if (target - x) in nums:
                result.append(i)
                result.append(nums.index(target - x))
                return result


solution = Solution()

nums = [2, 9, 11, 3, 5, 6, 7]
target = 15

result = solution.twoSum(nums, target)

print(result)