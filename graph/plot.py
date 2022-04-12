import matplotlib.pyplot as plt

cnn = [30,48,55, 58, 64,74,79,85,89, 95,99,100,100]
rnn= [6 ,10,20 ,26,32,41,57,70,78,84,90,97,100]
lstm = [5,8,19,27,32,47,62,69,76,87,93,98,100]
Fc= [2, 17, 27, 34, 38, 50, 61, 74, 81, 87, 94, 98,100]
y=[1, 5, 10,15,20,30,40,50,60,70,80,90,100]


plt.plot(y[:8],cnn[:8], 's-', color ='r', label = "CNN-encoder")
plt.plot(y[:8],lstm[:8], 'o-', color ='y', label = "LSTM-encoder")
plt.plot(y[:8],rnn[:8], '^-', color ='g', label = "RNN-encoder")
plt.plot(y[:8],Fc[:8], 'p-', color ='b', label = "FC-encoder")
plt.xlabel("thresthod (%)")
plt.ylabel("Successfully linked Rate(%)")
plt.legend(loc = "best")
plt.show()