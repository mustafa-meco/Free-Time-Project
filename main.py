from TimeRange import TimeRange
from Friend import Friend


def main():

    available_minutes = list(range(1440))

    f1 = Friend("Jim")
    f1.add_busy_range(TimeRange(start_time="08:00", end_time="10:00"))# 480 until 600 is not available
    f2 = Friend("Chris")
    f2.add_busy_range(TimeRange(start_time="12:00", end_time="14:00"))# 720 until 840 is not available

    for m in available_minutes[:]:
        for r in Friend.all_busy_minutes_range:
            if m in r:
                available_minutes.remove(m)

    print(available_minutes)
if __name__ == "__main__":
    main()
