class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        total_key_set = set(range(len(rooms)))
        key_set = set()
        current_key_set = set(rooms[0])
        while loop_key_set := (current_key_set - key_set):
            key_set |= current_key_set
            current_key_set.clear()
            for key in loop_key_set:
                current_key_set |= set(rooms[key])
        key_set |= {0}

        return not bool(total_key_set - key_set)
