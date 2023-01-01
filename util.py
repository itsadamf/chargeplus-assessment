from datetime import datetime

def calculate_timediff(in_time, out_time):
    out_time = datetime.strptime(out_time, "%Y-%m-%d %H:%M");

    diff = out_time - in_time;
    str_diff = str(diff);
    split_diff = str_diff.split(":");

    hour = split_diff[0];
    minutes = split_diff[1];

    w_day = out_time.weekday();

    # need to check whether the day is weekday or weekend
    if (w_day < 4):
        n_day = "weekday";
    else:
        n_day = "weekend";

    return {
        "hour": int(hour),
        "minutes": int(minutes),
        "day": n_day
    }