#!/usr/bin/env python3
import os
from math import pi
from math import factorial
import matplotlib.pyplot as plt

def gamma(n):
    return factorial(n - 1)

for n in range(2,51):
    x = []
    y = []
    for dr in range(0, 21):
        r = 1 + dr * 0.05
        V = pow(r, n) * pow(pi, n/2) / gamma(int(n/2))
        x.append(r)
        y.append(V)
        # print(f"Dimension: {n} \nRadius: {r} \nVolume: {V}")
    plt.title(f"Volume vs. Radius for n-Dimensions")
    plt.xlabel("Radius")
    plt.ylabel("Volume")
    plt.legend()
    plt.plot(x, y, label=f"d={n}")

plt.show()
