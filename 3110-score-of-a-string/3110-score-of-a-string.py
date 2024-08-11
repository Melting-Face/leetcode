class Solution:
    def scoreOfString(self, s: str) -> int:
        before_ascii = ord(s[0])

        score = 0

        for char in s[1:]:
            current_ascii = ord(char)
            score += abs(current_ascii - before_ascii)
            before_ascii = ord(char)
            
        return score