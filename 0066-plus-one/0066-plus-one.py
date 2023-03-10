class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rst = [str(digit) for digit in digits]
        rst = list(str(int(''.join(rst)) + 1))
        rst = [int(r) for r in rst]
        return rst