import random
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import csv
import pandas as pd

# read file
costs = pd.read_csv("costs.csv")
costs = costs.to_numpy()

np_bins = [i for i in range(40)]
square_hist = [0 for i in range(40)]
square = 0

budget = 1510

# straight up where you land
def landings(np_bins, square_hist, square):
    for i in range(10000):
        num1 = random.randint(0,6)
        num2 = random.randint(0,6)
        square = (square + (num1 + num2)) % 40
        square_hist[square] += 1
        if square == 30:
            square = 10

    plt.bar(np_bins, square_hist)
    plt.show()

#how much you pay
def pay(np_bins, square_hist, square, costs):
    for i in range(10000):
        num1 = random.randint(0,6)
        num2 = random.randint(0,6)
        square = (square + (num1 + num2)) % 40

        if square == 12 or square == 28:
            square += (7 * (num1 + num2))
        else:
            square_hist[square] += costs[square]

        if square == 30:
            square = 10

    plt.bar(np_bins, square_hist)
    plt.show()
    landings(np_bins, square_hist, square)

    
landings(np_bins, square_hist, square)
pay(np_bins, square_hist, square, costs)




