class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        result = [0, 0]
        count = 0
        while n > 0:
            n, x = divmod(n, 2)
            count += 1
            if count % 2:
                result[0] += x
            else:
                result[1] += x
        return result