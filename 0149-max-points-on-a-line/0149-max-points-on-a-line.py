from fractions import Fraction
from collections import Counter


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        number_of_points = len(points)
        if number_of_points == 1:
            return 1

        tilt_list = []
        
        for i in range(number_of_points):
            tilt_set = set()
            for j in range(number_of_points):
                if i == j:
                    continue
                first_point = points[i]
                second_point = points[j]

                x_rate_of_change = second_point[0] - first_point[0]
                y_rate_of_change = second_point[1] - first_point[1]

                if x_rate_of_change == 0:
                    tilt_set.add(f"{second_point[0]}NaN")
                    continue

                if y_rate_of_change == 0:
                    tilt_set.add(f"NaN{second_point[1]}")
                    continue

                tilt = Fraction(y_rate_of_change / x_rate_of_change)
                y_intercept = first_point[1] - round(first_point[0] * tilt, 9)
                tilt_set.add(f"{tilt}-{y_intercept}")
            tilt_list += list(tilt_set)

        tilt_counts = Counter(tilt_list).most_common()
        return tilt_counts[0][1]