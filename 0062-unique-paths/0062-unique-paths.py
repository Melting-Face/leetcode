class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

        return paths[n - 1][m - 1]