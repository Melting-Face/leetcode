class Solution:
    def findJudge(self, n: int, trusts: List[List[int]]) -> int:
        trust_set = set()
        trust_dict = {}
        for trust in trusts:
            trust_set.add(trust[0])
            trust_dict[trust[1]] = trust_dict.get(trust[1], 0) + 1

        for i in range(1, n + 1):
            if i not in trust_set and trust_dict.get(i, 0) == (n - 1):
                return i
        return -1