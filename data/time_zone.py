import datetime
from uti.utility import read_json
from statistics import mean
import numpy as np



def date_list_to_vector(dataliststr):
     timezone_f = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
     if not dataliststr:
         return timezone_f
     datelist_str = dataliststr[1:-1]
     date_list = datelist_str.split(",")
     for date in date_list:
         date = date.strip()
         hour = date_to_hour(date[1:-1])
         index = int(hour)
         timezone_f[index] += 1
     return timezone_f

def date_to_hour(date_time):
    y_date = datetime.datetime.strptime(date_time, '%d.%m.%Y %H:%M:%S')
    day = date_time[:- 8]
    midnight = day + "00:00:00"
    x_date = datetime.datetime.strptime(midnight, '%d.%m.%Y %H:%M:%S')
    diff = y_date - x_date
    seconds = diff.seconds
    diff_hours = seconds / 3600
    return diff_hours


def date_to_weekday(timeliest):
    weekday_list = {}
    for i in range(7):
        weekday_list[i] = 0
    for date_time in timeliest:
        date_ = datetime.datetime.strptime(date_time, '%d.%m.%Y %H:%M:%S')
        week_day = date_.weekday()

        weekday_list[week_day] += 1
    total = 0
    for i in range(7):
        total += weekday_list[i]
    return (weekday_list[5] + weekday_list[6]) / total


def date_to_timezone(timeliest):
    li = []
    mean_value = -100
    for date_time in timeliest:
        t_hour = date_to_hour(date_time)
        if mean_value == -100:
            li.append(t_hour)
        else:
            if t_hour > mean_value:
                if t_hour - mean_value > mean_value - t_hour + 24:
                    t_hour = t_hour - 24
            else:
                if mean_value - t_hour > t_hour + 24 - mean_value:
                    t_hour = t_hour + 24
            li.append(t_hour)
        mean_value = mean(li)

    if mean_value < 0:
        mean_value += 24
    elif mean_value > 24:
        mean_value -= 24
    variance_value = np.var(li)
    return mean_value, variance_value


if __name__ == '__main__':
    date = "06.09.2021 23:43:25"
    hour = date_to_hour(date)
    print(hour)
