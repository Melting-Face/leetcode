class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row_length = len(mat)
        col_length = len(mat[0])
        route_value = 0
        none_value_count = 999
        while none_value_count > 0:
            if route_value == 0:
                for i, row in enumerate(mat):
                    for j, value in enumerate(row):
                        if mat[i][j] != 0:
                            mat[i][j] = None
                route_value += 1
                continue

            none_value_count = 0
            for i, row in enumerate(mat):
                for j, value in enumerate(row):
                    if value is not None:
                        continue
                    if (
                        (j < col_length - 1 and mat[i][j + 1] == route_value - 1)
                        or (j > 0 and mat[i][j - 1] == route_value - 1)
                        or (
                            i < row_length - 1 and mat[i + 1][j] == route_value - 1
                        )
                        or (i > 0 and mat[i - 1][j] == route_value - 1)
                    ):
                        mat[i][j] = route_value
                    else:
                        none_value_count += 1
            route_value += 1
        return mat