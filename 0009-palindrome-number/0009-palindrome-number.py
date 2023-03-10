class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_to_str = str(x)
        return num_to_str[::-1] == num_to_str
        