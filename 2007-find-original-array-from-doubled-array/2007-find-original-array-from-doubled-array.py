from collections import Counter


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        answer = []
        changed_length = len(changed)
        if changed_length > 0 and changed_length % 2 == 0:
            changed_counter = Counter(changed)
            for key in sorted(changed_counter.keys()):
                count = changed_counter.get(key)
                if count is None or count <= 0:
                    continue
                elif key == 0:
                    if count % 2 != 0:
                        answer.clear()
                        break
                    else:
                        answer.extend([key] * int(count / 2))
                else:
                    mutiple_count = changed_counter.get(key * 2)
                    if mutiple_count is None or count > mutiple_count:
                        answer.clear()
                        break
                    else:
                        changed_counter[key] = 0
                        changed_counter[key*2] = mutiple_count - count
                        answer.extend([key] * count)

        return answer
