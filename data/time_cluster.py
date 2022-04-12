import os

import numpy as np
import heapq
from uti.utility import read_csv_todf
from time_zone import date_list_to_vector
from time_zone import datetime_rnn

class Timecluster:
    def __init__(self):
        self.source_dir = "/home/chauncey/Downloads"   # source file folder from telegram
        self.embedding = os.path.join(self.source_dir, "normal_embedding.txt")
        self.limit = 0
    def accuracy(self):
        x = np.loadtxt(self.embedding, dtype=int)
        limit = self.limit
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
                    isCP = True
            for (value, index) in heap2:
                if index == i:
                    if not isCP:
                       count+=1
        print(count)



if __name__ == '__main__':
    processor = Timecluster()
    y = [1, 5, 10,15,20,30,40,50,60,70,80,90,100]
    for limit in y:
       processor.limit = limit*2
       processor.accuracy()

