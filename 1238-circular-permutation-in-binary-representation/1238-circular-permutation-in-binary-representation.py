from collections import deque


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        deq = deque()
        index = None
        for i in range(0, 2 ** n):
            item = i ^ (i>>1)
            if item == start:
                index = i
            deq.append(item)

        deq.rotate(-index)

        return list(deq)
