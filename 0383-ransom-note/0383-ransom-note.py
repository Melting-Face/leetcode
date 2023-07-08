from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = Counter(list(ransomNote))
        magazine_counter = Counter(list(magazine))

        value = True
        for r in ransom_counter:
            value = (magazine_counter.get(r, 0) >= ransom_counter.get(r, 0))
            if not value:
                break
        return value