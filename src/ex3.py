#!/usr/env python3

import numpy as np
import matplotlib.pyplot as plt

f0 = 440
w0 = f0 * 2 * np.pi
samples = 100

# Constants
r = 1

# Initial conditions
y_n1 = 0
y_n2 = 0
x_n1 = 0

def plant(x):
    global y_n1, y_n2, x_n1
    y = 2 * r * np.cos(w0) * y_n1 - r * r * y_n2 + r * np.sin(w0) * x_n1
    y_n1 = y
    y_n2 = y_n1
    x_n1 = x
    return y

if __name__ == "__main__":
    x = 1
    y = []
    y.append(plant(x))
    for i in range(samples):
        y.append(plant(0))
    plt.plot(y)
    plt.show()
    
