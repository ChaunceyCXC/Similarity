import datetime
from uti.utility import read_json
from statistics import mean
import numpy as np
Global_lenght = 100
def datetime_rnn(dateliststr):
    date_vector_list1 =[]
    date_vector_list2 =[]
    datelist_str = dateliststr[1:-1]
    date_list = datelist_str.split(",")
    if len(date_list) < Global_lenght:
        return None, None
    for i in range(Global_lenght):
        date = date_list[i]
        date_vector=[]
        date = date.strip()
        datestring = date[1:-1]
        date_ = datetime.datetime.strptime(datestring, '%d.%m.%Y %H:%M:%S')
        date_vector.append(date_.hour)
        date_vector.append(date_.year)
        date_vector.append(date_.month)
        date_vector.append(date_.day)
        date_vector.append(date_.weekday())
        if i < Global_lenght/2:
            date_vector_list1.append(date_vector)
        else :
            date_vector_list2.append(date_vector)
    return date_vector_list1, date_vector_list2
def date_list_to_cnn_h(dateliststr):

    cnn_vector = [0] * 2184
    if not dateliststr:
        return None
    datelist_str = dateliststr[1:-1]
    date_list = datelist_str.split(",")
    for i in range(len(date_list)):
        date = date_list[i]
        date = date.strip()
        y_date = datetime.datetime.strptime(date[1:-1], '%d.%m.%Y %H:%M:%S')
        x_date = datetime.datetime.strptime("03.01.2022 00:00:00", '%d.%m.%Y %H:%M:%S')
        diff = y_date - x_date
        hours = int(diff.seconds / 3600)
        if 0 <= hours <= 2183:
            cnn_vector[hours] += 1
    return cnn_vector

def date_list_to_cnn_h_train(dateliststr):

    cnn_vector_1 = [0] * 2184
    cnn_vector_2 = [0] * 2184
    if not dateliststr:
        return None, None
    datelist_str = dateliststr[1:-1]
    date_list = datelist_str.split(",")
    isTrue = True
    if len(date_list) < Global_lenght:
        return None, None
    for i in range(len(date_list)):
        date = date_list[i]
        date = date.strip()
        y_date = datetime.datetime.strptime(date[1:-1], '%d.%m.%Y %H:%M:%S')
        x_date = datetime.datetime.strptime("03.01.2022 00:00:00", '%d.%m.%Y %H:%M:%S')
        diff = y_date - x_date
        hours = int(diff.seconds / 3600)
        if 0 <= hours <= 2183:
            if isTrue:
                cnn_vector_1[hours] += 1
            else:
                cnn_vector_2[hours] += 1
    return cnn_vector_1, cnn_vector_2





def date_list_to_vector(dataliststr):
     timezone_f_1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
     timezone_f_2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
     if not dataliststr:
         return None, None
     datelist_str = dataliststr[1:-1]
     date_list = datelist_str.split(",")
     if len(date_list) < Global_lenght :
         return None, None
     for i in range(Global_lenght):
         date = date_list[i]
         date = date.strip()
         hour = date_to_hour(date[1:-1])
         index = int(hour)
         if i < Global_lenght/2:
             timezone_f_1[index] += 1
         else:
             timezone_f_2[index] += 1
     return timezone_f_1, timezone_f_2

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
