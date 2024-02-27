import heapq
import math


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """1492. The kth Factor of n

        Args:
            n: Integer of factors to be obtained
            k: Rank in ascending order of factor

        Returns:
            k-th factor in ascending order
        """
        factor_set = {1, n}
        end_index = int(n / 2 if n % 2 == 0 else math.ceil(n / 3))
        for index in range(2, end_index + 1):
            share, remain = divmod(n, index)
            if remain == 0:
                factor_set.update([index, share])

        if len(factor_set) < k:
            return -1
        
        return heapq.nsmallest(k, factor_set)[-1]
