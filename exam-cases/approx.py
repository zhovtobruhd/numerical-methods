import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt


def func(x, a):
    return a[0] - a[1] * x * x


def phi(a):
    global q, h
    summ = 0.0
    for i in range(len(q)):
        summ += (h[i] - func(q[i], a)) ** 2
    return summ



q = np.array([5.0, 20.0, 30.0, 35.0])
h = np.array([209.0, 194.0, 165.0, 142.0])
suspicion = [1.0, 1.0]
a = optimize.minimize(phi, suspicion).x

print(a)

x = np.arange(5.0, 35.0, 0.1)
y = func(x, a)
r = h - func(q, a)

result = func(32.0, a)

fig, axs = plt.subplots(2, figsize=tuple((6.4, 4.8)), constrained_layout=True)

fig.suptitle("approximation")

axs[0].plot(q, h, 'ro')
axs[0].plot(x, y, 'b')
axs[0].scatter([32.0], [result])
axs[1].plot(q, r)
plt.savefig("img.png", format="png")
plt.show()

print(result)