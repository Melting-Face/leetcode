from copy import deepcopy


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        directions = (
            (0, 1),
            (0, -1),
            (-1, 0),
            (-1, 1),
            (-1, -1),
            (1, 0),
            (1, 1),
            (1, -1),
        )

        temp_board = deepcopy(board)
        for i, row in enumerate(temp_board):
            for j, col in enumerate(row):
                count = 0
                for x, y in directions:
                    try:
                        if (i + x) < 0 or (j + y) < 0:
                            continue
                        count += temp_board[i + x][j + y]
                    except IndexError:
                        continue
                if col and (count < 2 or count > 3):
                    board[i][j] = 0
                if not col and count == 3:
                    board[i][j] = 1