def add_time(hour, hour2):
    hourlist = hour.split()
    pm_or_am = hourlist[1]
    realhour = hourlist[0]
    realhourreal = realhour.split(":")
    hour_finally = realhourreal[0]
    mins_finally = realhourreal[1]

    hour2list = hour2.split(":")
    hour_finally2 = hour2list[0]
    mins_finally2 = hour2list[1]

    hour_finally_secs = int(hour_finally) * 60 * 60
    hour_finally_secs2 = int(hour_finally2) * 60 * 60

    mins_finally_secs = int(mins_finally) * 60
    mins_finally_secs2 = int(mins_finally2) * 60

    secs1 = hour_finally_secs + mins_finally_secs
    secs2 = hour_finally_secs2 + mins_finally_secs2

    result_secs = secs1 + secs2


    result_first = result_secs / 60
    result_semi = int(result_first)
    secs = result_secs % 60
    hours = result_semi / 60
    mins = result_semi % 60
    result1 = int(hours)
    hours_str = str(result1)
    mins_str = str(mins)
    result = hours_str + ":" + mins_str
    if int(hours_str) > 12:
        resu = int(hours_str) - 12
        resu1 = str(resu) + ":" + mins_str
        if pm_or_am == "PM":
            print(resu1 + "AM")
        else:
            print(resu1 + "PM")

    else:
        if pm_or_am == "AM":
            print(result + "AM")
        else:
            print(result + "PM")


add_time("12:12 AM", "3:10")