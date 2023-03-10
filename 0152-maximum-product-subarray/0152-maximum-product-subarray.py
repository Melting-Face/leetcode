class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_product = nums[0]
        max_product = nums[0]
        return_value = max_product
        for i in range(1, len(nums)):
            min_product, max_product= min(nums[i], min_product * nums[i], max_product * nums[i]), max(nums[i], min_product * nums[i], max_product * nums[i])
            return_value = max(return_value, max_product)
        return return_value
