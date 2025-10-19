from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        items = list(permutations(nums, len(nums)))
        return [list(item) for item in items]