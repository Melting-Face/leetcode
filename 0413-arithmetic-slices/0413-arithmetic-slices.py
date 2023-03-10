class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        prev_interval = None
        prev_num = None
        acc = 1
        answer = 0
        for idx, num in enumerate(nums):
            if idx != 0:
                interval = num - prev_num
                if interval == prev_interval:
                    acc += 1
                elif idx != 1 and interval != prev_interval:
                    if acc >= 2:
                        answer += sum(range(acc))
                    acc = 1
                prev_interval = interval
            prev_num = num

        if acc >= 2:
            answer += sum(range(acc))

        return answer