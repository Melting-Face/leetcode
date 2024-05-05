class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            if len(s[i:len(s)]) <= max_length:
                break
            for j in range(i + 1, len(s) + 1):
                char_arr = list(s[i:j])
                char_set = set(char_arr)
                if len(char_arr) != len(char_set):
                    break
                max_length = max(max_length, len(char_arr))
        return max_length
