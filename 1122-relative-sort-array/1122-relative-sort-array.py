from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        output = []
        for value in arr2:
            value_count = counter.pop(value, 0)
            output = output + [value] * value_count

        keys = sorted(counter.keys())

        for key in keys:
            key_count = counter.pop(key, 0)
            output = output + [key] * key_count

        return output