from typing import List


class Solution:
    def get_falling_sum(self, pos: int, matrix: List[List[int]], subsum: int) -> int:
        print(f"{pos=}, {matrix=}, {len(matrix)=}, {subsum=}")
        if len(matrix) == 0:
            return subsum
        else:
            # Positions that are allowed for falling to
            positions = [new_pos for new_pos in [pos - 1, pos, pos + 1] if 0 <= new_pos < len(matrix[0])]
            # print(f"{positions=}")
            tuples = [(matrix[0][position], position) for position in positions]
            minimum_element, minimum_position = min(tuples)
            print(f"{minimum_position=} | {minimum_element=}")
            submatrix = matrix[1:]
            subsum += minimum_element
            return self.get_falling_sum(minimum_position, submatrix, subsum)

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        sums = []
        submatrix = matrix[1:]
        for position, element in enumerate(matrix[0]):
            sub_sum = self.get_falling_sum(position, submatrix, element)
            sums.append(sub_sum)
        return min(sums)


# matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
# matrix = [[-19, 57], [-40, -5]]
matrix = [[100, -42, -46, -41], [31, 97, 10, -10], [-58, -51, 82, 89], [51, 81, 69, -51]]
s = Solution()
print(s.minFallingPathSum(matrix))
