import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y = np.array([4, 4, 2, 3, 6, 6, 6, 6, 3, 1, 2, 5])
xl = list(x)
yl = list(y)

def distance(xl, yl, i, k):
    l = []
    for j in range(1, k+1):
        l.append(abs(yl[i + j] - yl[i]))
        l.append(abs(yl[i - j] - yl[i]))
    return sum(l)
print(distance(xl, yl, 6, 2))

def max_d(xl, yl, j=2):
    dis = []
    for i in range(j, len(yl) - j):
        dis.append(distance(xl, yl, i, j))
    print(dis)
    return dis.index(max(dis)) + j

print(max_d(x, y))
