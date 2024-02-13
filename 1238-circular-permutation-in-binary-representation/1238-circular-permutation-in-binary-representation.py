class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        items = [i^(i>>1) for i in range(0, 2 ** n)]
        index = items.index(start)
        output = items[index:] + items[:index]
        return output