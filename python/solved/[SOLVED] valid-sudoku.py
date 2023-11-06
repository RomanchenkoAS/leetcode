'''Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.'''


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # Get 3x3 pieces

        row = set()
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        def get_box(i, j):
            column = j // 3
            row = i // 3

            return row * 3 + column

        for li in range(9):

            # Reset list for row
            row.clear()
            for ci, cell in enumerate(board[li]):
                # print(cell)

                if cell == ".":
                    continue

                # Row
                if cell in row:
                    return False
                else:
                    row.add(cell)

                # Column
                if cell in cols[ci]:
                    return False
                else:
                    cols[ci].add(cell)

                # Box
                box_num = get_box(li, ci)

                if cell in boxes[box_num]:
                    return False
                else:
                    boxes[box_num].add(cell)

        return True


s = Solution()

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], 
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
         [".", "6", ".", ".", ".", ".", "2", "8", "."], 
         [".", ".", ".", "4", "1", "9", ".", ".", "5"], 
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(s.isValidSudoku(board))
