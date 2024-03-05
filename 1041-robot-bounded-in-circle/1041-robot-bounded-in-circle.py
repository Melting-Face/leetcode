class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """1041. Robot Bounded In Circle
        The robot is initially at (0, 0) facing the north direction.

        Args:
            instructions: The robot can receive one of three instructions (G, L, R)

        Returns:
            Whether the robot is in place
        """
        place = [0, 0]
        direction = [0, 1]
        for _ in range(4):
            for instruction in instructions:
                if instruction == "R":
                    direction = [-direction[1], direction[0]]
                elif instruction == "L":
                    direction = [direction[1], -direction[0]]
                else:
                    place[0] += direction[0]
                    place[1] += direction[1]
            if place == [0, 0]:
                return True
        return False