from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row_length = len(mat)
        col_length = len(mat[0])
        deq = deque()
        for i, row in enumerate(mat):
            for j, _ in enumerate(row):
                if mat[i][j] != 0:
                    deq.append((i, j, 0))
                    mat[i][j] = None

        while deq:
            i, j, value = deq.popleft()
            if (
                (j < col_length - 1 and mat[i][j + 1] == value)
                or (j > 0 and mat[i][j - 1] == value)
                or (i < row_length - 1 and mat[i + 1][j] == value)
                or (i > 0 and mat[i - 1][j] == value)
            ):
                mat[i][j] = value + 1
            else:
                deq.append((i, j, value + 1))
        return mat