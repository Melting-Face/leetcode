from itertools import product
from string import ascii_lowercase


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lower_to_list = list(ascii_lowercase)
        num_to_str = {
            "2": lower_to_list[:3],
            "3": lower_to_list[3:6],
            "4": lower_to_list[6:9],
            "5": lower_to_list[9:12],
            "6": lower_to_list[12:15],
            "7": lower_to_list[15:19],
            "8": lower_to_list[19:22],
            "9": lower_to_list[22:],
        }

        arr = []
        for digit in digits:
            arr.append(num_to_str[digit])

        results = []
        if arr:
            for product_tuple in product(*arr):
                results.append("".join(product_tuple))

        return results