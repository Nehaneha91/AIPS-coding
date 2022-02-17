import sys
import unittest
from datetime import date, datetime

sys.path.append(".")
from utils.traffic_counter import TrafficCounter

test_filename = "tests/test_traffic_data.txt"


class TestTrafficCounterMethods(unittest.TestCase):
    def test_total_cars_seen(self):
        """
        Testing total number of cars seen in the file provided
        """
        traffic_counter = TrafficCounter(test_filename)
        self.assertEqual(traffic_counter.total_cars_seen(), 227)

    def test_daily_car_seen(self):
        """
        Testing the daily count of the file provided is as expected
        Checking the format of the output is dictionary as \
        specified in the return type
        """
        traffic_counter = TrafficCounter(test_filename)
        expected_dict = {
            date.fromisoformat("2021-12-01"): 179,
            date.fromisoformat("2021-12-02"): 48,
        }
        self.assertEqual(expected_dict, traffic_counter.daily_car_seen())

    def test_top_half_hours(self):
        """
        Testing top 3 half hours which has most number of cars \
        in the whole file provided
        """
        traffic_counter = TrafficCounter(test_filename)
        expected_dict = {
            datetime.fromisoformat("2021-12-01 07:30:00"): 46,
            datetime.fromisoformat("2021-12-01 08:00:00"): 42,
            datetime.fromisoformat("2021-12-01 07:00:00"): 25,
        }
        self.assertEqual(expected_dict, traffic_counter.top_half_hours(3))

    def test_least_cars_period(self):
        """
        Testing the 1.5 hour period with least cars is as expected
        """
        traffic_counter = TrafficCounter(test_filename)
        expected_dict = {
            datetime.fromisoformat("2021-12-02 05:00:00"): 5,
            datetime.fromisoformat("2021-12-02 05:30:00"): 2,
            datetime.fromisoformat("2021-12-02 06:00:00"): 4,
        }
        self.assertEqual(expected_dict, traffic_counter.least_cars_period(3))


if __name__ == "__main__":
    unittest.main()
