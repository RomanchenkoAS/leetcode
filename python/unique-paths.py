class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = {}

        def countPaths(x, y):
            if (x, y) in table:
                return table[(x, y)]

            if x == 0 and y == 0:
                return 1

            if x < 0 or y < 0:
                return 0

            table[(x, y)] = countPaths(x - 1, y) + countPaths(x, y - 1)
            return table[(x, y)]

        return countPaths(m - 1, n - 1)


m = 3
n = 2

sol = Solution()

print(sol.uniquePaths(m, n))
