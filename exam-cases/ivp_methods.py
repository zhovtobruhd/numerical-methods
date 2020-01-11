import numpy as np 
from scipy.integrate import RK45, odeint, solve_ivp
from matplotlib import pyplot as plt 

def func(x, y):
    # return y - 2 * x / y
    return x + y


def euler(f, a, b, y0, n):
    h = (b - a) / (n - 1.0)
    x = list()
    y = list()
    x.append(a)
    y.append(y0)
    for i in range(n - 1):
        x.append(x[i] + h)
        y.append(y[i] + h * f(x[i], y[i]))
    return x, y


def euler1mod(f, a, b, y0, n):
    h = (b - a) / (n - 1.0)
    x = list()
    y = list()
    x.append(a)
    y.append(y0)
    for i in range(0, 2 * (n - 1), 2):
        x.append(x[i] + h / 2.0)
        y.append(y[i] + h * f(x[i], y[i]) / 2.0)
        x.append(x[i] + h)
        y.append(y[i] + h * f(x[i + 1], y[i + 1]))
    return x, y


def euler2mod(f, a, b, y0, n):
    h = (b - a) / (n - 1.0)
    x = list()
    y = list()
    x.append(a)
    y.append(y0)
    for i in range(n - 1):
        fi = f(x[i], y[i])
        t = y[i] + h * fi
        x.append(x[i] + h)
        y.append(y[i] + h * (fi + f(x[i + 1], t)) / 2.0)
    return x, y


def rungekutta(f, a, b, y0, n):
    h = (b - a) / (n - 1.0)
    x = list()
    y = list()
    x.append(a)
    y.append(y0)
    for i in range(n - 1):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * f(x[i] + h, y[i] + k3)
        x.append(x[i] + h)
        y.append(y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0)
    return x, y


def predcorr(f, a, b, y0, n):
    h = (b - a) / (n - 1.0)
    x = list()
    y = list()
    fs = list()
    x.append(a)
    y.append(y0)
    fs.append(f(x[0], y[0]))
    for i in range(3):
        k1 = h * fs[i]
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * f(x[i] + h, y[i] + k3)
        x.append(x[i] + h)
        y.append(y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0)
        fs.append(f(x[i + 1], y[i + 1]))
    for i in range(3, n - 1):
        x.append(x[i] + h)
        ty = y[i] + h * (55 * fs[i] - 59 * fs[i - 1] + 37 * fs[i - 2] - 9 * fs[i - 3]) / 24.0
        tf = f(x[i + 1], ty)
        y.append(y[i] + h * (9 * tf + 19 * fs[i] - 5 * fs[i - 1] + fs[i - 2]) / 24.0)
        fs.append(f(x[i + 1], y[i + 1]))
    return x, y


ax = np.arange(0.0, 1.0, 0.0125)
result1 = solve_ivp(func, (0.0, 1.0), [1.0], method='RK45', first_step=0.0125, max_step=0.0125)
ax, result2 = euler(func, 0.0, 1.0, 1.0, 80)
#plt.plot(ax, result2, 'c.')
ax, result4 = euler2mod(func, 0.0, 1.0, 1.0, 80)
#plt.plot(ax, result4, 'y.')
ax, result5 = rungekutta(func, 0.0, 1.0, 1.0, 80)
plt.plot(ax, result5, 'k.')
ax, result6 = predcorr(func, 0.0, 1.0, 1.0, 80)
#plt.plot(ax, result6, 'b.')
plt.plot(result1.t, result1.y[0], 'r.')
plt.show()
print(result1)
# print(result2)
