from collections import Counter


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums:
            nums.sort()
            num_counter = Counter(nums)
            for key, value in num_counter.items():
                for _ in range(value - 1):
                    nums.remove(key)

        return len(nums)