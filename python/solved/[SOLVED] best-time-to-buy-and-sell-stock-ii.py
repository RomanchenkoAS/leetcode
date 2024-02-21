from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        last_price = prices[0]
        for price in prices[1:]:
            if price > last_price:
                profit += price - last_price
            last_price = price

        return profit


S = Solution()
input = [7, 6, 4, 3, 1]
print(S.maxProfit(input))
