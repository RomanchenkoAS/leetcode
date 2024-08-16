"""
605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot
be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an
integer n, return true if n new flowers can be planted in the flowerbed without violating the
no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        len_f = len(flowerbed)
        for pot_num in range(0, len_f):
            if n == 0:
                return True

            if flowerbed[pot_num] == 1:
                continue

            have_flower_to_the_left = (
                flowerbed[pot_num - 1] == 1 if pot_num > 0 else False
            )
            have_flower_to_the_right = (
                flowerbed[pot_num + 1] == 1 if pot_num < len_f - 1 else False
            )

            can_place_flower = not have_flower_to_the_left and not have_flower_to_the_right
            if can_place_flower:
                flowerbed[pot_num] = 1
                n -= 1

        return n <= 0


sol = Solution()
# flowerbed = [1, 0, 0, 0, 1]
# flowerbed = [0, 0, 1, 0, 0]
flowerbed = [1, 0, 0, 0, 1, 0, 0]
n = 2
res = sol.canPlaceFlowers(flowerbed, n)
print(res)
