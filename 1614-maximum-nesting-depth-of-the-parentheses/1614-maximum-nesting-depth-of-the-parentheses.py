class Solution:
    def maxDepth(self, s: str) -> int:
        depth, max_depth = 0, 0
        for sub_string in s:
            if sub_string == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif sub_string == ')':
                depth -= 1
        return max_depth
