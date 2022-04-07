import os

import numpy as np
import heapq
from uti.utility import read_csv_todf
from time_zone import date_list_to_vector
from time_zone import datetime_rnn

class Timecluster:
    def __init__(self, folder):
        self.folder = folder
        self.source_dir = "/home/chauncey/Downloads/Telegram Desktop/" + self.folder  # source file folder from telegram
        self.embedding = os.path.join(self.source_dir, "Chat/lstm_embedding.txt")
    def accuracy(self):
        x = np.loadtxt(self.embedding, dtype=int)
        limit = 30
        AdjDic = {}
        for i in range(200):
            AdjDic[i] = []
        for i in range(200):
            for j in range(i + 1, 200):
                dis = np.linalg.norm(x[i] - x[j])
                if len(AdjDic[i]) < limit:
                    heapq.heappush(AdjDic[i], (-dis, j))
                elif dis < -AdjDic[i][0][0]:
                    heapq.heappop(AdjDic[i])
                    heapq.heappush(AdjDic[i], (-dis, j))
                if len(AdjDic[j]) < limit:
                    heapq.heappush(AdjDic[j], (-dis, i))
                elif dis < -AdjDic[j][0][0]:
                    heapq.heappop(AdjDic[j])
                    heapq.heappush(AdjDic[j], (-dis, i))
        count = 0

        for i in range(100):
            heap1 = AdjDic[i]
            heap2 = AdjDic[i + 1]
            isCP = False
            for (value, index) in heap1:
                if index == i + 1:
                    count+=1
            for (value, index) in heap2:
                if index == i:
                    count+=1
            if isCP:
                count += 1
        print(count)



if __name__ == '__main__':
    processor = Timecluster("Scamily")
    processor.accuracy()

