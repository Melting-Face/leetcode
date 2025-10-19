from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]
        items = list(permutations(nums, n))
        return "".join([str(num) for num in items[k - 1]])