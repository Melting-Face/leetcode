class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num_seq = {}

        for key, num in enumerate(sorted(nums)):
            if num_seq.get(num, None) is None:
                num_seq[num] = key

        rst = [num_seq[num] for num in nums]
        
        return rst