from typing import List


class Solution:
    def get_falling_sum(self, pos: int, matrix: List[List[int]], subsum: int) -> int:
        print(pos, matrix, len(matrix), subsum)
        if len(matrix) == 0:
            return sum
        else:
            # Positions that are allowed for falling to
            positions = [new_pos for new_pos in [pos - 1, pos, pos + 1] if 0 <= new_pos <= len(matrix[0])]

        return sum

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        sum = 0
        submatrix = matrix[1:]
        for position, column in enumerate(matrix[0]):
            sub_sum = self.get_falling_sum(position, submatrix, 0)
        return 0


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
s = Solution()
print(s.minFallingPathSum(matrix))
