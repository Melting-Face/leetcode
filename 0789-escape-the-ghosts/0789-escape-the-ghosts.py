class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        target_x, target_y = target
        target_distance = abs(target_x) + abs(target_y)
        for ghost_x, ghost_y in ghosts:
            relative_distance = abs(target_x - ghost_x) + abs(target_y - ghost_y)
            if relative_distance <= target_distance:
                return False

        return True