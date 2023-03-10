from collections import Counter

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = []
        counter_for_sum = Counter(sorted(nums, reverse=True)[0:k])
        for num in nums:
            try:
                num_count = counter_for_sum[num]
                if num_count > 0:
                    arr.append(num)
                    counter_for_sum[num] = num_count - 1
            except:
                pass
        
        return arr