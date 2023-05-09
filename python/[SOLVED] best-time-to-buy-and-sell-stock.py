class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 10**4
        profit = 0
        for n in prices:
            buy = min(n, buy)
            dif = n - buy
            profit = max(profit, dif)
        return profit
    
s = Solution()

# input = [7,1,5,3,6,4]
input = [1,4,2]
# input = [3,2,6,5,0,3]

print(s.maxProfit(input))