class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ball_counts = {}
        for ball_number in range(lowLimit, highLimit + 1):
            ball_number_to_str = str(ball_number)
            sum_digits = sum([int(text) for text in ball_number_to_str])
            ball_counts.update({sum_digits: ball_counts.get(sum_digits, 0) + 1})

        return max(ball_counts.values())