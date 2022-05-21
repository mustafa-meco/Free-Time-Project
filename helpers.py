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

if __name__ == "__main__":
    time_str = input("enter time string")
    print(timerange_to_minutes(time_str))