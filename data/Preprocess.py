import os

import numpy as np

from uti.utility import read_csv_todf
from time_zone import date_list_to_vector
from time_zone import datetime_rnn

class TimePatternProcessor:
    def __init__(self, folder):
        self.folder = folder
        self.source_dir = "/home/xucan/Downloads/Telegram Desktop/" + self.folder  # source file folder from telegram
        self.normal_train = os.path.join(self.source_dir, "Chat/train.txt")
        self.parse_datelist_by_person = os.path.join(self.source_dir, "Chat/datelist_by_person.csv")
        self.cnn_train = os.path.join(self.source_dir, "Chat/cnn_train.txt")
        self.dic_file_path = os.path.join(self.source_dir, "Chat/dict.json")
        self.rnn_train = os.path.join(self.source_dir, "Chat/rnn_train.txt")

    def save_time_vector(self):
        if os.path.exists(self.normal_train):
            os.remove(self.normal_train)
        df = read_csv_todf(self.parse_datelist_by_person)
        date_list = df["datelist"]
        vectors = []
        for datestring in date_list:
            vector = date_list_to_vector(datestring)
            vectors.append(vector)

        n_array = np.asarray(vectors)
        print(n_array.shape)
        np.savetxt(self.normal_train, n_array, fmt='%d')

    def save_cnn_train(self):
        if os.path.exists(self.cnn_train):
            os.remove(self.cnn_train)
        df = read_csv_todf(self.parse_datelist_by_person)
        date_list = df["datelist"]
        vectors = []
        for datestring in date_list:
            vector = date_list_to_vector(datestring)
            vector.extend(vector)
            vectors.append(vector)

        n_array = np.asarray(vectors)
        print(n_array.shape)
        np.savetxt(self.cnn_train, n_array, fmt='%d')

    def save_rnn_train(self):
        if os.path.exists(self.rnn_train):
            os.remove(self.rnn_train)
        df = read_csv_todf(self.parse_datelist_by_person)
        date_list = df["datelist"]
        vectors = []
        for datestring in date_list:
            vector = datetime_rnn(datestring)
            if vector:
                vectors.append(vector)

        n_array = np.asarray(vectors)
        (x, y, z )= n_array.shape
        nre_array = n_array.reshape((x, y*z))
        print(nre_array.shape)
        np.savetxt(self.rnn_train, nre_array, fmt='%d')

    def readNarray(self):
        x = np.loadtxt(self.narray_path_twice, dtype=int)
        print(type(x))
        print(x.shape)


if __name__ == '__main__':
    processor = TimePatternProcessor("Scamily")
    processor.save_cnn_train()
    processor.save_rnn_train()
    processor.save_time_vector()
