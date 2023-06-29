class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        tmp = 0
        for num in nums:
            tmp += num
            answer.append(tmp)
        return answer