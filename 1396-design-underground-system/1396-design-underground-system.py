class UndergroundSystem:

    def __init__(self):
        self.departure = {}
        self.travel = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.departure.update({
            id: (stationName, t)
        })

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        id_departure = self.departure.get(id)
        start_end = f'{id_departure[0]}_{stationName}'
        travels = self.travel.get(start_end, [0, 0])
        travels[0] += t-id_departure[1]
        travels[1] += 1
        self.travel.update({
            start_end: travels
        })

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel_info = self.travel.get(f'{startStation}_{endStation}')
        return travel_info[0] / travel_info[1]