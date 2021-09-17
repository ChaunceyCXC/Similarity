import datetime
import os

from data.time_zone import date_to_timezone, date_to_weekday
from uti.utility import read_json, write_to_csv_file
from statistics import mean
import numpy as np
import os


def get_time_attribute(folder):
    csv_columns = ['username', 'average', 'variance', 'Weekends']
    all_attributes = [csv_columns]
    for filename in os.listdir(folder):
        timestamp_dic = read_json(os.path.join(folder, filename))
        username = filename[:-5]
        time_list = timestamp_dic["timestamp list"]
        mean_value, variance_value = date_to_timezone(time_list)
        weekends = date_to_weekday(time_list)
        an_attribute = [username, mean_value, variance_value, weekends]
        all_attributes.append(an_attribute)
    out_filename = os.path.join(folder + "attributes.csv")
    write_to_csv_file(out_filename, all_attributes)


if __name__ == '__main__':
    folder = "/home/xucan/Downloads/Telegram Desktop/scam/Time"
    get_time_attribute(folder)