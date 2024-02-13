from collections import deque


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        deq = deque()
        start_index = None
        for index in range(0, 2 ** n):
            item = index ^ (index >> 1)
            if item == start:
                start_index = index
            deq.append(item)

        deq.rotate(-start_index)

        return list(deq)
