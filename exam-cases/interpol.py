import numpy as np
from numpy.polynomial.polynomial import Polynomial
from scipy.interpolate import lagrange
from matplotlib import pyplot as plt

def pol(x, a):
    result = 0
    for i in range(len(a)):
        result += (x ** i) * a[len(a) - i - 1]
    return result



def linearInterpolation(x0, x, y): 
    length = len(x)
    index = 0
    for i in range(length):
        if (x[i] >= x0):
            index = i - 1
            break
    return ((x0 - x[index + 1]) * y[index] / (x[index] - x[index + 1]) + (x0 - x[index]) * y[index + 1] / (x[index + 1] - x[index]))


def squareInterpolation(x0, x, y):
    length = len(x)
    index = 0
    for i in range(length):
        if (x[i] >= x0):
            index = i - 1
            break
    if index == 0:
        return (((x0 - x[index + 1]) * (x0 - x[index + 2])) / ((x[index] - x[index + 1]) * (x[index] - x[index + 2]))) * y[index] + (((x0 - x[index]) * (x0 - x[index + 2])) / ((x[index + 1] - x[index]) * (x[index + 1] - x[index + 2]))) * y[index + 1] + (((x0 - x[index]) * (x0 - x[index + 1])) / ((x[index + 2] - x[index]) * (x[index + 2] - x[index + 1]))) * y[index + 2]
    else: 
        return (((x0 - x[index]) * (x0 - x[index + 1])) / ((x[index - 1] - x[index]) * (x[index - 1] - x[index + 1]))) * y[index - 1] + (((x0 - x[index - 1]) * (x0 - x[index + 1])) / ((x[index] - x[index - 1]) * (x[index] - x[index + 1]))) * y[index] + (((x0 - x[index - 1]) * (x0 - x[index])) / ((x[index + 1] - x[index - 1]) * (x[index + 1] - x[index]))) * y[index + 1]


def lagrangeInterpolation(x0, x, y): 
    summ = 0
    for i in range(len(x)):
        mult = 1
        for j in range(len(x)):
            if not i == j:
                mult = mult * (x0 - x[j]) / (x[i] - x[j])
        summ = summ + mult * y[i]
    return summ


def interpolation(f, xi, x, y):
    res = list()
    for i in xi:
        res.append(f(i, x, y))
    return res


x = np.array([0.5, 2.5, 4.5, 6.5, 8.5])
y = np.array([4.0, 205.0, 1240.0, 3840.0, 8750.0])

# grid
ax = np.arange(0.5, 8.5, 0.05) 

# linear interploation
linearResult = interpolation(linearInterpolation, ax, x, y)

# square interpolation
squareResult = interpolation(squareInterpolation, ax, x, y)

# lagrange interpolation
coef = np.array(Polynomial(lagrange(x, y)).coef)
lagrangeResult = pol(ax, coef)

# plotting
fig, axs = plt.subplots(3, figsize=tuple((6.4, 15.0)), constrained_layout=True)

fig.suptitle("interpolation", fontsize=32.0)

axs[0].plot(ax, linearResult, 'r')
axs[1].plot(ax, squareResult, 'y')
axs[2].plot(ax, lagrangeResult, 'g')
axs[0].plot(x, y, 'b.')
axs[1].plot(x, y, 'b.')
axs[2].plot(x, y, 'b.')
axs[0].grid(True)
axs[1].grid(True)
axs[2].grid(True)
axs[0].set_title('linear', fontsize=14)
axs[1].set_title('square', fontsize=14)
axs[2].set_title('lagrange', fontsize=14)
# plt.plot()
plt.show()


print(linearInterpolation(3.0, x, y), squareInterpolation(3.0, x, y), lagrangeInterpolation(3.0, x, y))
# print(Polynomial(result).coef)