from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        last_index = len(nums) - 1
        if last_index < 2:
            return 0
        if nums[0] >= last_index:
            return 1

        jumps = 0
        pos = 0
        while pos < last_index:
            fuel = nums[pos]  # This is basically remaining jump length

            furthest_position = 0  # Index of furthest possible jump
            best_position = 0  # Index from which furthest jump is possible

            inspected_position = pos

            # This loop will inspect every location that we can reach from current jump
            while fuel > 0:
                fuel -= 1
                inspected_position += 1

                possible_best_position = inspected_position + nums[inspected_position]
                if possible_best_position > furthest_position:
                    # Early return case:
                    # we can finish from that particular index by jumping there and making one more jump
                    if possible_best_position >= last_index:
                        return jumps + 2
                    furthest_position = possible_best_position
                    best_position = inspected_position

            jumps += 1
            pos = best_position
        return jumps


# nums = [2,3,1,1,4]
# nums = [1, 2, 3]
# nums = [2, 3, 1]
nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
s = Solution()
print(s.jump(nums))
