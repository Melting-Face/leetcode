class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        rst = nums[-1] * nums[-2] - nums[1] * nums[0]
        return rst