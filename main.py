import helpers as h
from TimeRange import TimeRange
from Friend import Friend
from custom_list import CustomList



def main():

    available_minutes = CustomList(range(1440))
    # print("Hello in Free Time Checker App")
    # print("Here you can find the suitable time to hang out\nwith your friends besides your busy times")
    # f_no = 1
    # f_new = True
    # while f_new == True
    #     f = Friend(input(f"Please enter the name of Friend no. #{f_no}: "))
    #     f.all_busy_minutes_range(TimeRange)

    f1 = Friend("Jim")
    f1.add_busy_range(TimeRange(start_time="08:00", end_time="10:00"))# 480 until 600 is not available
    f2 = Friend("Chris")
    f2.add_busy_range(TimeRange(start_time="08:00", end_time="14:00"))# 720 until 840 is not available

    for m in available_minutes[:]:
        for r in Friend.all_busy_minutes_range:
            if m in r:
                available_minutes.remove_if_exist(m)

    for tr in h.prettify_available_minutes(available_minutes):
        print(f"You can meet in {tr}")
if __name__ == "__main__":
    main()
