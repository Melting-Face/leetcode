class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            count = map.get(num, 0)
            count += 1
            if count % 2 == 1:
                map[num] = count
            else:
                del map[num]
        return list(map.keys())[0]