from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        if m == 1 and n == 1:
            return 1 if obstacleGrid[0][0] == 0 else 0

        if obstacleGrid[0][0] == 1 or obstacleGrid[n - 1][m - 1] == 1:
            return 0

        memo_table = [[None] * m for _ in range(n)]

        def countPaths(x: int, y: int):
            if x == 0 and y == 0:
                # Base case
                return 1

            if x < 0 or y < 0:
                # Out of bounds case
                return 0

            if obstacleGrid[x][y] == 1:
                # Encountered an obstacle
                return 0

            if memo_table[x][y] is not None:
                return memo_table[x][y]

            memo_table[x][y] = countPaths(x - 1, y) + countPaths(x, y - 1)
            return memo_table[x][y]

        return countPaths(n - 1, m - 1)


s = Solution()
obstacleGrid = [[1, 0]]
print(s.uniquePathsWithObstacles(obstacleGrid))
