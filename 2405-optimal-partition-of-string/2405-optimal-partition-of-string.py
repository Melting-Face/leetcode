class Solution:
    def partitionString(self, s: str) -> int:
        partition_count = 1
        sub_string_set = set()
        for sub_string in s:
            if sub_string in sub_string_set:
                sub_string_set.clear()
                partition_count += 1
            sub_string_set.add(sub_string)
        return partition_count