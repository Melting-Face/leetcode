class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 1
        longest_count = 1
        prev_num = 0
        cur_num = 0
        max_num = 0
        for num in nums:
            cur_num = num
            if prev_num == num:
                count += 1
            else:
                if prev_num > max_num:
                    longest_count = count
                    max_num = prev_num
                elif prev_num == max_num:
                    longest_count = max(longest_count, count)
                prev_num = num
                count = 1

        if cur_num > max_num:
            longest_count = count
        elif cur_num == max_num:
            longest_count = max(longest_count, count)

        return longest_count