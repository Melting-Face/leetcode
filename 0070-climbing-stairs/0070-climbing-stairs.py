class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0] * n
        steps[0] = 1
        if n >= 2:
            steps[1] = 2
            for idx in range(2, n):
                steps[idx] = steps[idx - 1] + steps[idx - 2]
        return steps[-1]