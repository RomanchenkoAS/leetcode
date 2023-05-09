"""Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order."""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for n in nums:
            # Record frequency of each number in a dictionary
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1

        # Make a list out of this dict | sort it by the second item in tuple
        d = sorted(list(d.items()), key=lambda x: x[1])

        # Take k elements from the end of this list | take only first element of tuple
        return [x for x,y in d[-k:]]

s = Solution()

input = [4,1,-1,2,-1,2,3] , 2
print(s.topKFrequent(input[0], input[1]))