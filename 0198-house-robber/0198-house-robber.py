class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_length = len(nums)
        nums_list = [0 for i in range(nums_length)]

        for i in range(nums_length):
            nums_list[i] = max(nums_list[i], nums[i])
            for j in range(i+2, nums_length):
                nums_list[j] = max(nums_list[j], nums_list[i] + nums[j])

        max_robber = max(nums_list)
        return max_robber