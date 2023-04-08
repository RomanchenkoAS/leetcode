class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Faster
        for i in range(0, len(nums)):
            _tmp = target - nums[i]
            if _tmp in nums[i + 1:]:
                return [ i , nums[i + 1:].index(_tmp) + i + 1]

        # Slower 
        # i = 0
        # while True:
        #     if target - nums[i] in nums[i + 1:]:
        #         return [ i , nums[i + 1:].index(target - nums[i]) + i + 1]
        #     i += 1
            


solution = Solution()

nums = [3,3]
target = 6

result = solution.twoSum(nums, target)

print(result)
