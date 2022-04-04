import os

import numpy as np

from uti.utility import read_csv_todf
from time_zone import date_list_to_vector
from time_zone import datetime_rnn

class Timecluster:
    def __init__(self, folder):
        self.folder = folder
        self.source_dir = "/home/xucan/Downloads/Telegram Desktop/" + self.folder  # source file folder from telegram
        self.embedding = os.path.join(self.source_dir, "Chat/train.txt")
    def accuracy(self):
        x = np.loadtxt(self.embedding, dtype=int)


    def vector_difference(self, v1, v2):
        np.linalg.norm(a-b)



if __name__ == '__main__':
    processor = TimePatternProcessor("Scamily")
    processor.save_cnn_train()
    processor.save_rnn_train()
    processor.save_time_vector()
