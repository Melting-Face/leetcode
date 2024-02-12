class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleets = sorted(zip(speed, position), key=lambda x: (-x[1], x[0]))
        fleet_speed, fleet_position = car_fleets[0]
        fleet_time = (target - fleet_position) / fleet_speed
        fleet_count = 1
        for current_speed, current_position in car_fleets[1:]:
            current_time = (target - current_position) / current_speed
            if current_time <= fleet_time:
                continue

            fleet_time = current_time
            fleet_count += 1
        return fleet_count