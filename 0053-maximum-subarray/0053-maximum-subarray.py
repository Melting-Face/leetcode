class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_array = nums[0]
        value = max_sub_array
        for i in range(1, len(nums)):
            max_sub_array = max(max_sub_array + nums[i], nums[i])
            value = max(value, max_sub_array)
        return value
        