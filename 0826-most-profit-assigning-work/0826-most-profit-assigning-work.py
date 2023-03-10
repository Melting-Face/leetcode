class Solution:
    def maxProfitAssignment(self, levels: List[int], profits: List[int], workers: List[int]) -> int:
        total = 0
        zip_level_profit = sorted(zip(levels, profits))
        workers = sorted(workers)
        i = 0
        earn = 0
        for worker in workers:
            temp = zip_level_profit[i:]
            for level, profit in temp:
                if level > worker: break
                elif profit >= earn: earn = profit 
                i += 1
            total += earn

        return total
