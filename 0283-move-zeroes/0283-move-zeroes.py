class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_indexes = []
        for idx, num in enumerate(nums):
            if num == 0:
                zero_indexes.append(idx)

        while len(zero_indexes) > 0:
            index = zero_indexes.pop()
            del nums[index]
            nums.append(0)


