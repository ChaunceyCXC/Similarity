import numpy as np
from IPython.display import display, HTML
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pandas as pd
import re

class Usr2Vector:
    def __init__(self, folder):
        self.folder = folder
        self.source_dir = "/home/chauncey/Downloads/Telegram Desktop/" + self.folder  # source file folder from telegram
        self.normal_train = os.path.join(self.source_dir, "Chat/train.txt")
        self.parse_datelist_by_person = os.path.join(self.source_dir, "Chat/datelist_by_person.csv")
        self.cnn_train = os.path.join(self.source_dir, "Chat/cnn_train.txt")
        self.dic_file_path = os.path.join(self.source_dir, "Chat/dict.json")
        self.rnn_train = os.path.join(self.source_dir, "Chat/rnn_train.txt")

    def generate_dictinoary_data(text):
        word_to_index = dict()
        index_to_word = dict()
        corpus = []
        count = 0
        vocab_size = 0

        for row in text:
            for word in row.split():
                word = word.lower()
                corpus.append(word)
                if word_to_index.get(word) == None:
                    word_to_index.update({word: count})
                    index_to_word.update({count: word})
                    count += 1
        vocab_size = len(word_to_index)
        length_of_corpus = len(corpus)

        return word_to_index, index_to_word, corpus, vocab_size, length_of_corpus



if __name__ == '__main__':
    processor = TimePatternProcessor("Scamily")
    processor.save_cnn_train()
    processor.save_rnn_train()
    processor.save_time_vector()
    processor.readNarray()
