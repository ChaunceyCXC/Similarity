from bs4 import BeautifulSoup
import os
import datetime
from data.time_zone import date_to_timezone
from data.time_zone import date_to_weekday
from uti.utility import write_to_csv_file
from uti.utility import write_to_json_file
from uti.utility import deEmojify
import string


class TelegramParser:
    def __init__(self, folder, save_as_csv=True):
        self.folder = folder
        self.source_dir = "/home/xucan/Downloads/Telegram Desktop/" + self.folder# source file folder from telegram
        self.time_folder = os.path.join(self.source_dir, "Time")
        self.text_folder = os.path.join(self.source_dir, "Text")
        self.remove_deleted_account = True

    def parse_time(self):
        files = os.listdir(self.source_dir)
        files.sort()
        frequency = {}
        lastDate = "01.01.2000 00:00:00"
        for file in files:
            if file[-4:] == "html":
                file_path = self.source_dir + "/" + file
                a_products_desc_page = open(file_path, encoding='utf-8')
                a_beautiful_soup = BeautifulSoup(a_products_desc_page, features="html.parser")
                a_products_desc_page.close()
                history = a_beautiful_soup.find('div', {"class": "history"})
                divs = history.find_all('div', class_="body")
                for div in divs:
                    if div["class"] == ['body']:
                        date_div = div.find("div", class_="pull_right date details")
                        name_div = div.find("div", class_="from_name")
                        #                      text_div = div.find("div", class_="text")
                        if date_div is not None:
                            date = date_div["title"]
                            y_date = datetime.datetime.strptime(date, '%d.%m.%Y %H:%M:%S')
                            x_date = datetime.datetime.strptime(lastDate, '%d.%m.%Y %H:%M:%S')
                            diff = y_date - x_date
                            days, seconds = diff.days, diff.seconds
                            diff_hours = days * 24 + seconds / 3600

                            lastDate = date

                        else:
                            continue
                        if name_div is not None:
                            username = name_div.text.strip()
                            if username == "Deleted Account":
                                if self.remove_deleted_account:
                                    continue
                        else:
                            continue

                        if username not in frequency.keys():
                            frequency[username] = [date]
                        else:
                            frequency[username].append(date)

        csv_columns = ['username', 'average', 'variance', 'weekends']
        all_attributes = [csv_columns]

        for name in frequency.keys():

            timedict = {"timestamp list": frequency[name]}
            time_list = frequency[name]
            if len(time_list) < 10:
                continue
            mean_value, variance_value = date_to_timezone(time_list)
            weekends = date_to_weekday(time_list)
            an_attribute = [name, mean_value, variance_value, weekends]
            all_attributes.append(an_attribute)
            name = name.replace("/", "slash")
        #    write_to_json_file(os.path.join(self.source_dir,  "Time/"+name+".json"), timedict)
        out_filename = os.path.join(self.source_dir + "/attributes.csv")
        write_to_csv_file(out_filename, all_attributes)
    def parse_text(self):
        files = os.listdir(self.source_dir)
        files.sort()
        textdic={}
        for file in files:
            if file[-4:] == "html":
                file_path = self.source_dir + "/" + file
                a_products_desc_page = open(file_path, encoding='utf-8')
                a_beautiful_soup = BeautifulSoup(a_products_desc_page, features="html.parser")
                a_products_desc_page.close()
                history = a_beautiful_soup.find('div', {"class": "history"})
                divs = history.find_all('div', class_="body")
                for div in divs:
                    if div["class"] == ['body']:
                        date_div = div.find("div", class_="pull_right date details")
                        name_div = div.find("div", class_="from_name")
                        text_div = div.find("div", class_="text")
                        if date_div is None:
                            continue
                        if name_div is not None:
                            username = name_div.text.strip()
                            if username == "Deleted Account":
                                if self.remove_deleted_account:
                                    continue
                        else:
                            continue
                        if text_div is not None:
                            text = text_div.text.strip()
                        else:
                            continue
                        text = deEmojify(text)
                        if username not in textdic.keys():
                            textdic[username] = [text]
                        else:
                            textdic[username].append(text)
        for name in textdic.keys():
            text_dict = {"text list": textdic[name]}
            name = name.replace("/", "slash")
            write_to_json_file(os.path.join(self.source_dir, "Text/" + name + ".json"), text_dict)

# The main function, the entry point
if __name__ == '__main__':
    a_parser = TelegramParser("Scamily")
    a_parser.parse_time()
