class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = int(dividend / divisor)
        if result >= (pow(2, 31) - 1):
            result = (pow(2, 31) - 1)
        if result <= -pow(2, 31):
            result = -pow(2, 31)
        return result
