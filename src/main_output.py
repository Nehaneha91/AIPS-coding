import sys
sys.path.append(".")

from utils.traffic_counter import TrafficCounter


def get_traffic_analytics():
    filename = input("Enter the filename along with full path (a/b.txt): ")
    traffic_counter = TrafficCounter(filename)

    print("*****************************************")
    print("Total cars seen in the input = {}".format(traffic_counter.total_cars_seen()))

    print("\n\n*****************************************")
    print("Daily car seen is as below - ")
    daily_car_count = traffic_counter.daily_car_seen()
    for day, count in daily_car_count.items():
        print("{} {}".format(day, count))

    print("\n\n*****************************************")
    print("top 3 half hours car seen is as below - ")
    top_3_half_hours = traffic_counter.top_half_hours(3)
    for date_time, count in top_3_half_hours.items():
        print("{} {}".format(date_time, count))

    print("\n\n*****************************************")
    print("The 1.5 hour period with least cars - ")
    period, count = traffic_counter.least_cars_period(3)
    print("{} has least car count which is = {}".format(period, count))


if __name__ == "__main__":
    get_traffic_analytics()
