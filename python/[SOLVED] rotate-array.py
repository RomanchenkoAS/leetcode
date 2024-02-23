from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if k >= length:
            k = k % length

        if k == 0:
            return None

        def get_new_index(index):
            return (index + k) % length

        # O(1) Space + O(N) time solution
        starting_element_index = i = 0
        buffer = None
        for count in range(length):
            if i == starting_element_index and count > 0:
                # Renew cycle if we made a full circular rotation
                i += 1
                starting_element_index += 1
                buffer = None

            next_index = get_new_index(i)
            if buffer is None:
                # First iteration of a cycle
                buffer = nums[next_index]
                nums[next_index] = nums[i]
            else:
                # Subsequent iterations
                nums[next_index], buffer = buffer, nums[next_index]
            i = next_index

S = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# nums = [1, 2]
kok = 3
S.rotate(nums, kok)
