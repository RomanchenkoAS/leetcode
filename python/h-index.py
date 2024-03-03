class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        current_h = 0
        for index, paper in enumerate(citations, start=1):
            current_h += 1
            if paper < current_h:
                return current_h - 1
        return current_h


citations = [3, 0, 6, 1, 5]
# citations = [100]
s = Solution()
print(s.hIndex(citations))
