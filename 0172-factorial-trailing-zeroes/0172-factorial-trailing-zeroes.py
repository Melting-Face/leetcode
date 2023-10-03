class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0

        count = 0
        for i in range(5, n + 1, 5):
            value = i
            while True:
                value = value // 5
                count += 1
                if value % 5:
                    break
                    
        return count
