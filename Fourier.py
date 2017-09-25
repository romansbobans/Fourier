import math
import matplotlib.pyplot as plt
import numpy as np
from math import pi
from math import sin
from math import cos


def calculate(n, period=8, bits=None):
    if bits is None:
        bits = [0, 1, 1, 0, 0, 0, 1, 0]
    aValue = 0.0
    bValue = 0.0
    # return aValue, bValue
    for index, bit in enumerate(bits):
        idx1 = index+1
        sin1 = sin(n * math.pi * idx1 / 4)
        cos1 = cos(n * math.pi * index / 4)
        sin2 = sin(n * math.pi * index / 4)
        cos2 = cos(n * math.pi * idx1 / 4)
        aValue += bit * (sin1 - sin2)
        bValue += bit * (cos1 - cos2)
    return aValue / (n * pi), bValue / (n * pi)


def draw(symbol, period):
    print(type(symbol))
    print(type(list(symbol)[0]))
    join = "0"+bin(int.from_bytes(symbol[0].encode(), 'big'))[2:]
    binary = list(map(int, list(join)))
    print(binary)
    c = sum(binary) * 2 / period
    product = None
    harmonics = 14
    for n in range(1, harmonics+1):
        an, bn = calculate(n, period, binary)
        array = np.array(method_name(an, bn, n, period))
        #plt.figure(n)
        #plt.plot(array)
        plt.figure(harmonics+1)
        plt.plot(array, label = "Nr.{}".format(n))
        if product is None:
            product = array
        else:
            product = product + array
    product += c
    product /= 2
    plt.figure(harmonics+1)
    plt.plot(product, label = "Result")
    plt.legend(bbox_to_anchor=(-0.1, 1.02, 1.22, .02), loc="best",
               ncol=7, mode="expand", borderaxespad=0.)
    plt.show()


def method_name(a1, b1, n, period):
    values = []

    for x in np.arange(0.0, period, 0.01):
        apart = math.cos(2 * math.pi * n * x / period)
        bpart = math.sin(2 * math.pi * n * x / period)
        values.append(a1 * apart + b1 * bpart)
    return values


if __name__ == "__main__": draw('M', 8)