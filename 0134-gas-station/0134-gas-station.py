class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_value = 0
        current_value = 0
        start_index = 0
        for i in range(0, len(gas)):
            current = gas[i] - cost[i]
            total_value += current
            current_value += current

            if current_value < 0:
                current_value = 0
                start_index = i + 1

        return start_index if total_value >= 0 else -1
