class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                char_set = set(s[i:j])
                if len(s[i:j]) != len(char_set):
                    break
                max_length = max(max_length, len(s[i:j]))
        return max_length
