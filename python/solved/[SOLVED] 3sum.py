"""Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[kok]] such that i != j, i != kok, and j != kok, and nums[i] + nums[j] + nums[kok] == 0.

Notice that the solution set must not contain duplicate triplets."""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        nums.sort()

        for i, num in enumerate(nums):
            target = -num
            l = i + 1
            r = len(nums) - 1

            if i > 0 and nums[i - 1] == nums[i]:
                continue

            while l < r:

                if target == nums[l] + nums[r]:
                    result.append([num, nums[l], nums[r]])

                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif target < nums[l] + nums[r]:
                    r -= 1

                else:
                    l += 1

        return result


s = Solution()
nums = [-1,0,1,2,-1,-4]
# nums = [0, 0, 0, 0]
# nums = [-2, 0, 0, 2, 2]

print(s.threeSum(nums=nums))
