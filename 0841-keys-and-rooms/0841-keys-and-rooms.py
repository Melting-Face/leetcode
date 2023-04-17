from copy import deepcopy

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        remain_rooms = set(rooms[0])
        total_rooms = deepcopy(remain_rooms)
        while remain_rooms:
            temp_room = set()
            for key in remain_rooms:
                room_set = set(rooms[key]) - total_rooms
                if room_set:
                    temp_room.update(room_set)
                    total_rooms.update(room_set)
            remain_rooms = temp_room
        if 0 in total_rooms:
            total_rooms.remove(0)

        return len(total_rooms) == (len(rooms) - 1)
        