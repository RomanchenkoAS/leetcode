class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            _tmp = target - nums[i]
            if _tmp in nums[i + 1:]:
                return [ i , nums[i + 1:].index(_tmp) + i + 1]


solution = Solution()

nums = [2,7,11,15]
target = 9

result = solution.twoSum(nums, target)

print(result)
