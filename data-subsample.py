import math
from random import gauss
import numpy as np
from random import choices
import matplotlib.pyplot as plt

# Q1.Resampling and generate different subsets of training data by randomly selecting data with replacement.

# Q2
mean = 2
variance = 8
random_numbers = [gauss(mean, math.sqrt(variance)) for i in range(100)]

# Q3
meanRand100 = np.mean(random_numbers)
varRand100 = np.var(random_numbers)
meanRand10 = []
varRand10 = []

for i in range(20):
    randTen = choices(random_numbers, k=10)
    meanRand10.append(np.mean(randTen))
    varRand10.append(np.var(randTen))

plotM = plt.hist(meanRand10)
plt.show()
plotV = plt.hist(varRand10)
plt.show()




