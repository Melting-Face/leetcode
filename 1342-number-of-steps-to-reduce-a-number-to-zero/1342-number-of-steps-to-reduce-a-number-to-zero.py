class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while (num):
            step += 1
            if num % 2 == 0:
                num = num >> 1
            else:
                num = num - 1
        return step
