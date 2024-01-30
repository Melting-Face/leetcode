class Solution:
    def coloredCells(self, n: int) -> int:
        output = 1
        for idx in range(0, n):
            output += (idx * 4)
        return output