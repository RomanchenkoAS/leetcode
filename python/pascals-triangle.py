from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for i in range(numRows):
            row = []
            for slot in range(i + 1):
                if slot == 0 or slot == i:
                    row.append(1)

                elif i > 0:
                    row.append(rows[i - 1][slot - 1] + rows[i - 1][slot])

            rows.append(row)
        return rows


sol = Solution()
print(sol.generate(5))
