import os

import numpy as np

from uti.utility import read_csv_todf
from time_zone import date_list_to_vector


class TimePatternProcessor:
    def __init__(self, folder):
        self.folder = folder
        self.source_dir = "/home/chauncey/Downloads/Telegram Desktop/" + self.folder  # source file folder from telegram
        self.narray_path = os.path.join(self.source_dir, "Chat/vector.txt")
        self.parse_datelist_by_person = os.path.join(self.source_dir, "Chat/datelist_by_person.csv")
        self.narray_path_twice = os.path.join(self.source_dir, "Chat/cnn_train.txt")
        self.dic_file_path = os.path.join(self.source_dir, "Chat/dict.json")
        self.rnn_train = os.path.join(self.source_dir, "Chat/rnn_train.txt")

    def save_time_vector(self):
        if os.path.exists(self.narray_path):
            os.remove(self.narray_path)
        df = read_csv_todf(self.parse_datelist_by_person)
        date_list = df["datelist"]
        vectors = []
        for datestring in date_list:
            vector = date_list_to_vector(datestring)
            vectors.append(vector)

        n_array = np.asarray(vectors)
        print(n_array.shape)
        np.savetxt(self.narray_path, n_array, fmt='%d')

    def save_time_vector_twice(self):
        if os.path.exists(self.narray_path_twice):
            os.remove(self.narray_path_twice)
        df = read_csv_todf(self.parse_datelist_by_person)
        date_list = df["datelist"]
        vectors = []
        for datestring in date_list:
            vector = date_list_to_vector(datestring)
            vector.extend(vector)
            vectors.append(vector)

        n_array = np.asarray(vectors)
        print(n_array.shape)
        np.savetxt(self.narray_path_twice, n_array, fmt='%d')

    def savernn_train(self):
        if os.path.exists(self.rnn_train):
            os.remove(self.rnn_train)
        df = read_csv_todf(self.parse_datelist_by_person)
        date_list = df["datelist"]
        vectors = []
        for datestring in date_list:
            vector = date_list_to_vector(datestring)
            vectors.append(vector)

        n_array = np.asarray(vectors)
        print(n_array.shape)
        np.savetxt(self.narray_path, n_array, fmt='%d')

    def readNarray(self):
        x = np.loadtxt(self.narray_path_twice, dtype=int)
        print(type(x))
        print(x.shape)


if __name__ == '__main__':
    processor = TimePatternProcessor("Scamily")
    processor.save_time_vector_twice()
    processor.readNarray()
