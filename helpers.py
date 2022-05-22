def timerange_to_minutes(t_Str):
    """
    Return amount of minutes for timeranges in format HH:MM
    :param t_Str:
    :return:
    """
    # 05:00
    hour_str = t_Str.split(':')[0]
    minutes_str = t_Str.split(':')[1]

    hour_to_minutes = int(hour_str) * 60

    return hour_to_minutes + int(minutes_str)

def minutes_to_timerange_str(m):
    """
    Return a timerange string in format of HH:MM for the given integer
    :param m:
    :return:
    m = 90 -> 01:30
    """
    hour = m // 60
    hour_str = f"{hour:02d}"
    minutes = m % 60
    minutes_str = f"{minutes:02d}"
    return f"{hour_str}:{minutes_str}"

def prettify_available_minutes(l: list):
    grouped_list = []
    list_resettable = []
    # Group the list so that: [[0, 1, 2], [60,61, 62]]
    for element in l:
        if not list_resettable:
            list_resettable.append(element)
            continue
        if list_resettable[-1] + 1 != element:
            grouped_list.append(list_resettable[:])
            list_resettable.clear()
        list_resettable.append(element)
    grouped_list.append(list_resettable)

    time_ranges = []

    for group in grouped_list:
        start_time = minutes_to_timerange_str(m=group[0])
        end_time = minutes_to_timerange_str(m=group[-1])
        time_range_str = f"{start_time} - {end_time}"
        time_ranges.append(time_range_str)

    return time_ranges


# if __name__ == "__main__":
#     print(prettify_available_minutes())
    # time_str = input("enter time string: ")
    # print(timerange_to_minutes(time_str))
    # print(minutes_to_timerange_str(m=120))