from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        if len(prices) == 2:
            diff = prices[0] - prices[1]
            return 0 if diff < 0 else diff

        low = prices[0]
        diff = 0
        for price in prices:
            if price < low:
                low = price
            else:
                if price - low > diff:
                    diff = price - low

        return diff


s = Solution()
test_case = [7, 1, 5, 3, 6, 4]
print(s.maxProfit(test_case))
