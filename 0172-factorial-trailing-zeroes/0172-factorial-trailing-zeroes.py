class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0

        count = 0
        value = 1
        for i in range(1, n + 1):
            value *= i

        while True:
            value, remain = divmod(value, 10)
            if remain != 0:
                break
            count += 1
            
        return count
