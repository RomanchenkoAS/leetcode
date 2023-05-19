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
        # cols = [set() for _ in range(9)]
        cols = [set()] * 9
        boxes = [set()] * 9

        print(cols)
        # print(boxes)

        for li, line in enumerate(board):

            # Reset list for row
            row.clear()
            for ci, cell in enumerate(board[li]):
                # print(cell)

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

            # After row is processed


s = Solution()

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(s.isValidSudoku(board))
