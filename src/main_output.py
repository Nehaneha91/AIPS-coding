import sys

sys.path.append(".")

from utils.traffic_counter import TrafficCounter

"""
This method is implemented to do some analysis on traffic data
it used traffic counter utility from utils folder
it performs different analysis such as -
    - Total number of cars seen in the input file
    - Daily breakdown of the cars seen
    - Top 3 half hours where the cars seen are maximum
    - 1.5 hour continuous period with least cars
and finally displays the output on the console
"""


def get_traffic_analytics():
    print("-------Traffic count analysis-----\n\n")
    filename = input("Enter the filename along with full path (a/b.txt): ")
    traffic_counter = TrafficCounter(filename)

    print("*****************************************")
    print("Total cars seen in the input = {}".format(traffic_counter.total_cars_seen()))

    print("\n*****************************************")
    print("Daily car seen is as below - ")
    daily_car_count = traffic_counter.daily_car_seen()
    for day, count in daily_car_count.items():
        print("{} {}".format(day, count))

    print("\n*****************************************")
    print("top 3 half hours car seen is as below - ")
    top_3_half_hours = traffic_counter.top_half_hours(3)
    for date_time, count in top_3_half_hours.items():
        print("{} {}".format(date_time.isoformat(), count))

    print("\n*****************************************")
    least_cars_period = traffic_counter.least_cars_period(3)
    if least_cars_period:
        print("Below is the least cars period for 3 continuous half hour records - ")
        for date_time, count in least_cars_period.items():
            print("{} {}".format(date_time.isoformat(), count))
    else:
        print("file doesn't have even one set of 3 continuous half hour records")


if __name__ == "__main__":
    get_traffic_analytics()
