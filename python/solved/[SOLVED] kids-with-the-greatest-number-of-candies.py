""" There are n kids with candies. You are given an integer array candies, where each candies[i] represents 
the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving 
the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies. """


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        maximum = max(candies)

        # This is way too smart and therefore slower ;)
        # return [True if i + extraCandies >= maximum else False for i in candies]

        for index, amount in enumerate(candies):
            if amount + extraCandies >= maximum:
                candies[index] = True
            else:
                candies[index] = False

        return candies


sol = Solution()

candies = [2, 3, 5, 1, 3]
extraCandies = 3

result = sol.kidsWithCandies(candies, extraCandies)
print(result)
