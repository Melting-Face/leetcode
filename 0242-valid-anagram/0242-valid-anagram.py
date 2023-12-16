from collections import Counter
from itertools import zip_longest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        str_set = set()
        for s_str, t_str in zip_longest(s_counter, t_counter):
            if s_str not in str_set:
                if s_counter.get(s_str) != t_counter.get(s_str):
                    return False
                str_set.add(s_str)

            if t_str not in str_set:
                if s_counter.get(t_str) != t_counter.get(t_str):
                    return False
                str_set.add(t_str)

        return True
