from bs4 import BeautifulSoup
import os
import datetime
from data.time_zone import date_to_timezone
from data.time_zone import date_to_weekday
from uti.utility import write_to_csv_file
from uti.utility import write_to_json_file
from uti.utility import deEmojify
import string


class Graph:
    def __init__(self, folder, save_as_csv=True):
        self.folder = folder
        self.source_dir = "/home/xucan/Downloads/Telegram Desktop/" + self.folder+ "/Chat/chat.csv"# source file folder from telegram

    def build_graph(self):
        #build a grah

# The main function, the entry point
if __name__ == '__main__':
    a_parser = Graph("Scamily")
    a_parser.build_graph()
