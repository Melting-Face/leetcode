class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        flatten_matrix = sum(matrix, [])
        flatten_matrix.reverse()
        for i in range(0, n):
            for j in range(0, n):
                index = (n * j) + n - (i + 1)
                matrix[i][j] = flatten_matrix[index]
