import numpy as np
from scipy.optimize import fsolve, minimize
from matplotlib import pyplot as plt 

def norm(a):
    x = 0.0
    for i in a:
        x = x + (i * i)
    return np.sqrt(x)


def func(p):
    # x, y = p
    # return (2 * x * x + y * y - 1, x * x * x + 6 * x * x * y - 1)
    return np.array([np.exp((p[0] + 5.) / 15.) - 2 - p[1], -3. * np.log(p[0] / 3.) + 15 - p[1]])


def fnorm(p):
    return norm(func(p))


# TODO: to make a guess you may need a plot
# TODO: remember that more than one answer is possible
# TODO: if shit happens try to change the guess

x = np.arange(20., 50., 0.1)
y1 = np.exp((x + 5.) / 15.) - 2
y2 = -3. * np.log(x / 3.) + 15

plt.plot(x, y1, 'b')
plt.plot(x, y2, 'r')
plt.show()

guess = np.array([30., 9.])
x, y = fsolve(func, guess)
print (x, y, func((x, y)))
x, y = minimize(fnorm, guess).x
print (x, y, func((x, y)))
