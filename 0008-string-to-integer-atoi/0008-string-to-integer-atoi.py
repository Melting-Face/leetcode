class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        is_minus = False
        if s.startswith("-"):
            is_minus = True
            s = s[1:]
        elif s.startswith("+"):
            is_minus = False
            s = s[1:]
        nums = {str(i) for i in range(0, 10)}
        result = ""
        for char in s:
            if char not in nums:
                break
            result += char
        if not result:
            result = "0"

        result = int(result) * (-1 if is_minus else 1)

        if result <= -pow(2, 31):
            result = -pow(2, 31)
        
        if result >= (pow(2, 31) - 1):
            result = (pow(2, 31) - 1)

        return result