class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = int(''.join(map(str, num)))
        return list(map(int, list(str(n + k))))