from bs4 import BeautifulSoup
import os
import datetime
from uti.utility import write_to_csv_file
from uti.utility import write_to_json_file
from uti.utility import deEmojify
import string
import pandas as pd


class TelegramParser:
    def __init__(self, folder):
        self.folder = folder
        self.source_dir = "/home/chauncey/Downloads/Telegram Desktop/" + self.folder  # source file folder from telegram
        self.parse_csv = os.path.join(self.source_dir, "Chat/chat.csv")
        self.parse_csv_datelist = os.path.join(self.source_dir, "Chat/chat_datelist.csv")
        self.parse_datelist_by_person = os.path.join(self.source_dir, "Chat/datelist_by_person.csv")
        self.dic_file_path = os.path.join(self.source_dir, "Chat/dict.json")  # outout2: usernmae to number dictionary

    def parse(self):
        if os.path.exists(self.parse_csv):
            os.remove(self.parse_csv)
        if os.path.exists(self.dic_file_path):
            os.remove(self.dic_file_path)
        csv_columns = ['date', 'username', 'text']
        files = os.listdir(self.source_dir)
        files.sort()
        dict = {}
        all_messages = [csv_columns]
        index = 0

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
                        if date_div is not None:
                            date = date_div["title"]

                        else:
                            continue
                        if name_div is not None:
                            username = name_div.text.strip()
                            if username == "Deleted Account":
                                continue
                        else:
                            continue
                        if text_div is not None:
                            text = text_div.text.strip()
                        else:
                            text = "NOT TEXT"

                        text = deEmojify(text)

                        if text != "NOT TEXT" and text != "":
                                a_new_message = {"date": date, "username": username, "text": text}
                                all_messages.append([date, username, text])


        write_to_csv_file(self.parse_csv, all_messages)

        write_to_json_file(self.dic_file_path, dict)

    def parse_date_list(self):
        if os.path.exists(self.parse_csv_datelist):
            os.remove(self.parse_csv_datelist)
        df = pd.read_csv(self.parse_csv)

        groupdf = df.groupby(["username", "text"]).date.apply(list).reset_index(name="datelist")
        groupdf.to_csv(self.parse_csv_datelist, index=False)

    def parse_date_by_person(self):
        if os.path.exists(self.parse_datelist_by_person):
            os.remove(self.parse_datelist_by_person)
        df = pd.read_csv(self.parse_csv)

        groupdf = df.groupby(["username"]).date.apply(list).reset_index(name="datelist")
        groupdf.to_csv(self.parse_datelist_by_person, index=False)


# The main function, the entry point
if __name__ == '__main__':
    a_parser = TelegramParser("Scamily")
    a_parser.parse()
    a_parser.parse_date_by_person()
