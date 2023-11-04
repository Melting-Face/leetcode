class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        str_list = [[] for _ in range(numRows)]

        for index, char in enumerate(s):
            remain = index % ((2 * numRows) - 2)
            if remain < numRows:
                str_list[remain].append(char)
                continue
            str_list[numRows - 2 - remain].append(char)

        answer = "".join(["".join(s) for s in str_list])
        return answer