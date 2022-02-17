from collections import Counter
from datetime import datetime, timedelta
from typing import Dict, Tuple


class TrafficCounter:
    def __init__(self, filename: str) -> None:
        """
        This class takes the filename to read the data from
        Reads the actual file in the format given
        For example:
        if the file contains a record like
        `2021-12-01T05:00:00 5`
        it reads the file and convert the first value of the row as datetime
        and converts the second value of the row as int value as it is a count
        Args:
        filename: Name of the file with full path to read the data from
        Usage:
        ```
        filename = "A/b.txt"
        traffic_counter = TrafficCounter(filename)
        ```
        """
        self.filename = filename
        self.traffic_counter = {}
        self._read_file()

    def _read_file(self) -> None:
        """
        Its a private method that is called to initlaise traffic counter
        it reads the file and convert the record into dictionary
        it takes care of data type conversion for further analysis
        """
        with open(self.filename) as traffic_file:
            records = traffic_file.read().splitlines()
        for record in records:
            date_time, count = record.split(" ")
            date_time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S")
            self.traffic_counter[date_time] = int(count)

    def total_cars_seen(self) -> int:
        """
        counts the total cars seen in the whole file
        return the count as an int value
        """
        return sum(self.traffic_counter.values())

    def daily_car_seen(self) -> Dict[datetime, int]:
        """
        This method counts the car seen in a day
        It saves the output in a dictionary where \
        a key represents a day and value corresponds to the car seen
        """
        daily_traffic = {}
        for date_time, count in self.traffic_counter.items():
            day = date_time.date()
            if day not in daily_traffic:
                daily_traffic[day] = 0
            daily_traffic[day] += count
        return daily_traffic

    def top_half_hours(self, n) -> Dict[datetime, int]:
        """
        This method return the top n half hours where the car count is maximum
        """
        cars_counter = Counter(self.traffic_counter)
        return dict(cars_counter.most_common(n))

    def least_cars_period(self, n) -> Tuple[str, int]:
        """
        This method return the least car seen in a continuous period of n intervals
        this was a bit trciky due to below reasons based on 1.5 hours period
        -  assumption -  sometime machine can break and it misses some records
           solution opted - put a condition to filter records that are continuous
        -  ask - to display 1.5 hours period of least car but 3 intervals will have \
        gap of 1 hour as we are recording the start time of half hour
           solution opted - to display continuous nicely, period outputted will have start time \
           of first interval and end time of last interval
        """
        date_time_stamps = sorted(self.traffic_counter.keys())
        cont_period_count = {}

        for i in range(len(date_time_stamps) - n + 1):
            cont_keys = date_time_stamps[i : i + n]
            if cont_keys[-1] == cont_keys[0] + timedelta(hours=1):
                count = sum([self.traffic_counter[key] for key in cont_keys])
                period_key = "{} - {}".format(
                    cont_keys[0], cont_keys[-1] + timedelta(hours=0.5)
                )
                cont_period_count[period_key] = count

        return min(cont_period_count.items(), key=lambda x: x[1])
