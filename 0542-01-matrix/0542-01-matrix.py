class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row_length = len(mat)
        col_length = len(mat[0])
        dp = [None for _ in range(row_length * col_length)]
        route_value = 0
        while None in dp:
            if route_value == 0:
                for idx, value in enumerate(dp):
                    row, col = divmod(idx, col_length)
                    if mat[row][col] == 0:
                        dp[idx] = 0
                route_value += 1
                continue

            for idx, value in enumerate(dp):
                if value is not None:
                    continue
                row, col = divmod(idx, col_length)
                if (
                    (col < col_length - 1 and dp[idx + 1] == route_value - 1)
                    or (col > 0 and dp[idx - 1] == route_value - 1)
                    or (
                        row < row_length - 1 and dp[idx + col_length] == route_value - 1
                    )
                    or (row > 0 and dp[idx - col_length] == route_value - 1)
                ):
                    dp[idx] = route_value
                    mat[row][col] = route_value
            route_value += 1
        return mat

