import matplotlib.pyplot as plt
import numpy as np
def get_data(filename):
    fin = open("GraphicInfo/" + filename)
    data = fin.read().rstrip().split()
    res = []
    for i in data:
        if "0" <= i[0] <= "9" or (i[0] =="-" and "0" <= i[1] <= "9"):
            res.append(int(i))

    for i in range(len(res)):
        if (i % 4 == 0):
            gen.append(i + 1)
        if (i % 4 == 1):
            min.append(res[i])
        if (i % 4 == 2):
            avg.append(res[i])
        if (i % 4 == 3):
            max.append(res[i])
gen = []
min = []
avg = []
max = []
get_data("MoreNeuronsLearning.txt")
#get_data("onlyStump-2.txt")
plt.plot(np.array(max))
plt.show()