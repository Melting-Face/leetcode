class Solution:
    def findComplement(self, num: int) -> int:
        num_to_binary = bin(num)
        num_to_binary_length = len(num_to_binary) - 2
        base_to_binary = bin(pow(2, num_to_binary_length) - 1)
        return int(base_to_binary, 2) - int(num_to_binary, 2)