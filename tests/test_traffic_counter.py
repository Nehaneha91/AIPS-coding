import sys
import unittest
from datetime import date, datetime

sys.path.append(".")
from utils.traffic_counter import TrafficCounter

# Different test data includig edge cases
test_filename = "tests/test_traffic_data.txt"
test_filename_2_records = "tests/test_data_2_records.txt"
test_filename_no_cont_records = "tests/test_data_no_cont.txt"


class TestTrafficCounterMethods(unittest.TestCase):
    def test_total_cars_seen(self):
        """
        Testing total number of cars seen in the file provided
        """
        traffic_counter = TrafficCounter(test_filename)
        result = traffic_counter.total_cars_seen()
        self.assertEqual(result, 227)

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
        result_dict = traffic_counter.daily_car_seen()
        self.assertEqual(expected_dict, result_dict)

    def test_top_3_half_hours_more_records(self):
        """
        Testing top 3 half hours which has most number of cars \
        in the whole file provided, when file has more than 3 records
        """
        traffic_counter = TrafficCounter(test_filename)
        expected_dict = {
            datetime.fromisoformat("2021-12-01 07:30:00"): 46,
            datetime.fromisoformat("2021-12-01 08:00:00"): 42,
            datetime.fromisoformat("2021-12-01 07:00:00"): 25,
        }
        result_dict = traffic_counter.top_half_hours(3)
        self.assertEqual(expected_dict, result_dict)
    
    def test_top_3_half_hours_less_records(self):
        """
        EDGE CASE
        Testing top 3 half hours which has most number of cars \
        in the whole file provided, when the file has less than 3 records
        """
        traffic_counter = TrafficCounter(test_filename_2_records)
        expected_dict = {
            datetime.fromisoformat("2021-12-01T05:00:00"): 5,
            datetime.fromisoformat("2021-12-01T05:30:00"): 12,
        }
        result_dict = traffic_counter.top_half_hours(3)
        self.assertEqual(expected_dict, result_dict)

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
        result_dict = traffic_counter.least_cars_period(3)
        self.assertEqual(expected_dict, result_dict)

    def test_least_cars_period_less_records(self):
        """
        EDGE CASE
        Testing the 1.5 hour period with least cars is as expected
        This time file just have 2 records so the result should be empty dict
        """
        traffic_counter = TrafficCounter(test_filename_2_records)
        result_dict = traffic_counter.least_cars_period(3)
        self.assertEqual(len(result_dict), 0)

    def test_least_cars_period_no_cont_records(self):
        """
        EDGE CASE
        Testing the 1.5 hour period with least cars is as expected
        This time file doesn't have any set of 1.5 hour continuous records
        so the result should be empty dict
        """
        traffic_counter = TrafficCounter(test_filename_no_cont_records)
        result_dict = traffic_counter.least_cars_period(3)
        self.assertEqual(len(result_dict), 0)


if __name__ == "__main__":
    unittest.main()
