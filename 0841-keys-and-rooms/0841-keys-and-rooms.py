from copy import deepcopy

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        room = set(rooms[0])
        total_rooms = deepcopy(room)
        while room:
            temp_room = set()
            for key in room:
                room_set = set(rooms[key]) - total_rooms
                if room_set:
                    temp_room.update(room_set)
                    total_rooms.update(room_set)
            room = temp_room
        if 0 in total_rooms:
            total_rooms.remove(0)

        return len(total_rooms) == (len(rooms) - 1)
        