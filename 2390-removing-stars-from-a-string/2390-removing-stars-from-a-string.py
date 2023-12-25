class Solution:
    def removeStars(self, s: str) -> str:
        sub_str = []
        for c in list(s):
            if c == "*":
                sub_str.pop()
                continue
            sub_str += [c]
        return "".join(sub_str)