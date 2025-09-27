class Solution:
    def reverse(self, x: int) -> int:
        share = abs(x)
        result = ""

        while share >= 10:
            share, remainder = divmod(share, 10)
            result += str(remainder)

        result += str(share)
        result = int(result)

        if x < 0:
            result *= -1

        if not(-pow(2, 31) <= result <= pow(2, 31) - 1):
            return 0

        return result