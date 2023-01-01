from datetime import datetime
import constant, util

# get constant weekday and weekend
weekday = constant.weekday;
weekend = constant.weekend;

# check the in and out
in_time = "2023-01-01 02:00"; # in time example
in_dt_object = datetime.strptime(in_time, "%Y-%m-%d %H:%M");
out_time = datetime.now();
out_dt_object = out_time.strftime("%Y-%m-%d %H:%M");

# use function from util
time_diff = util.calculate_timediff(in_dt_object, out_dt_object);

charge = 0;

def main():
    global charge;
    if (time_diff["day"] == "weekday"):
        if (time_diff["hour"] <= 3):
            if (time_diff["hour"] == 0 and time_diff["minutes"] <= 15):
                charge = 0;

            if (time_diff["hour"] > 0):
                charge = weekday["first_3_hours"];

            if (time_diff["hour"] == 3 and time_diff["minutes"] > 5):
                charge += weekday["sub_hour"];

        if (time_diff["hour"] > 3):
            charge = weekday["first_3_hours"];
            next_hour = time_diff["hour"] - 3;

            while next_hour >= 1:
                charge += weekday["sub_hour"];
                next_hour -= 1;
                
            if (time_diff["minutes"] > 5):
                charge += weekday["sub_hour"];

            if (charge > weekday["max_per_day"]):
                charge = weekday["max_per_day"];

    if (time_diff["day"] == "weekend"):
        if (time_diff["hour"] <= 3):
            if (time_diff["hour"] == 0 and time_diff["minutes"] <= 15):
                charge = 0;

            if (time_diff["hour"] > 0):
                charge = weekend["first_3_hours"];

            if (time_diff["hour"] == 3 and time_diff["minutes"] > 5):
                charge += weekend["sub_hour"];

        if (time_diff["hour"] > 3):
            charge = weekend["first_3_hours"];
            next_hour = time_diff["hour"] - 3;

            while next_hour >= 1:
                charge += weekend["sub_hour"];
                next_hour -= 1;
                
            if (time_diff["minutes"] > 5):
                charge += weekend["sub_hour"];

            if (charge > weekend["max_per_day"]):
                charge = weekend["max_per_day"];

    print("Charge: ", charge)

if __name__ == "__main__":
    main();


