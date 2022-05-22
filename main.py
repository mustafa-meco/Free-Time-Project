from TimeRange import TimeRange
from Friend import Friend


def main():

    available_minutes = list(range(1440))

    f1 = Friend("Jim")
    f1.add_busy_range(TimeRange(start_time="08:00", end_time="10:00"))# 480 until 600 is not available
    # f2 = Friend("Chris")
    # f2.add_busy_range(TimeRange(start_time="12:00", end_time="14:00"))

    for m in available_minutes[:]:
        if m in f1.busy_time_ranges[0].minutes_range:
            available_minutes.remove(m)

    print(available_minutes)
if __name__ == "__main__":
    main()
