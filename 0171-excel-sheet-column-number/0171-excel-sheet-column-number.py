class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for index, char in enumerate(columnTitle[::-1]):
            num += (ord(char) - 64) * pow(26, index)

        return num