class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        point_count = 0
        for x1, y1 in points:
            tilt_map = {}
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue

                if x1 == x2:
                    count = tilt_map.get('N', 0)
                    tilt_map['N'] = count + 1
                    continue

                tilt = (y2 - y1) / (x2 - x1)
                count = tilt_map.get(tilt, 0)
                tilt_map[tilt] = count + 1

            point_count = max(point_count, max(tilt_map.values()))
        return point_count + 1