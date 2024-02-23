from typing import List


# Recursive solution is pretty slow
# class Solution:
#     def isReachable(self, nums, i) -> bool:
#         for index in range(0, i):
#             if nums[index] + index >= i:
#                 return self.isReachable(nums, index) if i > 0 else True
#
#         return False
#     def canJump(self, nums: List[int]) -> bool:
#         return self.isReachable(nums, len(nums) - 1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gasoline = nums[0]
        for num in nums[1:]:
            if gasoline <= 0:
                return False
            if num >= gasoline:
                gasoline = num
            else:
                gasoline -= 1
        return True

# nums = [3, 2, 1, 0, 4]
# nums = [2, 3, 1, 1, 4]
nums = [1,1,1,0]
S = Solution()
print(S.canJump(nums))
