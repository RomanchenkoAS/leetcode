from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_ptr = right_ptr = sum = 0  # Left and right ptrs

        # set proper right_ptr
        min_length = None
        for num in nums:
            sum += num
            right_ptr += 1
            if sum >= target:
                min_length = right_ptr
                right_ptr -= 1
                break
        if sum < target:
            return 0

        if min_length is None:
            min_length = right_ptr

        # That will stop when right_ptr goes out of boundaries of list
        while right_ptr <= len(nums) - 1:
            # Check how far we can move left pointer
            while True:
                if sum - nums[left_ptr] >= target:
                    sum -= nums[left_ptr]
                    left_ptr += 1
                    min_length = min(right_ptr - left_ptr + 1, min_length)
                else:
                    break

            # Last action - move right
            right_ptr += 1
            if right_ptr <= len(nums) - 1:
                sum += nums[right_ptr]

        return min_length


# target = 15
target = 7
# nums = [5,1,3,5,10,7,4,9,2,8]
nums = [2, 3, 1, 2, 4, 3]

s = Solution()
print(s.minSubArrayLen(target, nums))
