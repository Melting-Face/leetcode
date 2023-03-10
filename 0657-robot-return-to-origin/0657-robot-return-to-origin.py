from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_count = Counter(moves)
        return move_count.get('L') == move_count.get('R') and move_count.get('U') == move_count.get('D')
