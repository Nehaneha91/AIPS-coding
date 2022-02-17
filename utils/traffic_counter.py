from collections import Counter
from datetime import datetime
from typing import Dict, Tuple


class TrafficCounter:
    def __init__(self, filename: str) -> None:
        """
        This method takes the filename to read the data from
        Reads the actual file in the format gives
        For example:
        if the file contains - 2021-12-01T05:00:00 5
        it reads the file and convert the first value of the row as datetime
        and converts the second value of the row as int value as it is a count
        """
        self.filename = filename
        self.traffic_counter = {}
        self._read_file()

    def _read_file(self) -> None:
        with open(self.filename) as traffic_file:
            records = traffic_file.read().splitlines()
        for record in records:
            date_time, count = record.split(" ")
            date_time_1 = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S")
            self.traffic_counter[date_time_1] = int(count)

    def total_cars_seen(self) -> int:
        return sum(self.traffic_counter.values())

    def daily_car_seen(self) -> Dict[datetime, int]:
        daily_traffic = {}
        for date_time, count in self.traffic_counter.items():
            day = date_time.date()
            if day not in daily_traffic:
                daily_traffic[day] = 0
            daily_traffic[day] += count
        return daily_traffic

    def top_half_hours(self, n) -> Dict[datetime, int]:
        cars_counter = Counter(self.traffic_counter)
        return dict(cars_counter.most_common(n))

    def least_cars_period(self, n) -> Tuple[str, int]:
        date_time_stamps = sorted(self.traffic_counter.keys())
        dict_1 = {}

        for i in range(len(date_time_stamps) - n + 1):
            cont_keys = date_time_stamps[i : i + n]
            value = sum([self.traffic_counter[key] for key in cont_keys])
            period_key = "{} - {}".format(cont_keys[0], cont_keys[-1])
            dict_1[period_key] = value

        return min(dict_1.items(), key=lambda x: x[1])
