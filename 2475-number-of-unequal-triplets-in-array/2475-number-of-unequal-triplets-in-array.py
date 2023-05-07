class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        result = 0
        for i, num in enumerate(nums):
            first_nums = nums[i + 1: ]
            if not first_nums:
                continue

            num_list = [num]

            for j, first_num in enumerate(first_nums):
                second_nums = first_nums[j + 1: ]
                if not second_nums or first_num in num_list:
                    continue

                total_num_list = num_list + [first_num]
                for second_num in second_nums:
                    if second_num not in total_num_list:
                        result += 1
        return result