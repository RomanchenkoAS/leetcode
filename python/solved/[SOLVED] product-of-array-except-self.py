class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        answers = [1] * length
        for i in range(1, length):
            answers[i] = answers[i - 1] * nums[i - 1]

        running_sum = nums[length - 1]
        for i in range(length - 2, -1, -1):
            answers[i] *= running_sum
            running_sum *= nums[i]
        return answers


s = Solution()
nums = [1, 2, 3, 4]
print(s.productExceptSelf(nums))
