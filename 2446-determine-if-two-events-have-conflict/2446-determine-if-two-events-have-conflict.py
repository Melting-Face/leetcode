from datetime import datetime

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        s1, e1 = [datetime.strptime(e, "%H:%M") for e in event1]
        s2, e2 = [datetime.strptime(e, "%H:%M") for e in event2]
        return s1 <= s2 <= e1 or s2 <= s1 <= e2