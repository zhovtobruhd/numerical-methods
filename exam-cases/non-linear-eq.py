import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

def func(x):
    return x * x * x - 5 * x


def foo(theta): 
    # TODO: convert kilometers per hour to meters per second
    # TODO: ensure that you use radians instead of degrees
    return 3600.0 * np.tan(theta) - 1287.2939457501855 / (np.cos(theta) ** 2)


def binsearch(a : float, b : float, eps : float, f):
    while b - a > eps:
        if f(a) * f((a + b) / 2) < 0:
            b = (a + b) / 2
        else:
            a = (a + b) / 2
    return a


def chordsearch(a : float, b : float, eps : float, f):
    x = a - (((b - a) * f(a)) / (f(b) - f(a)))
    while np.abs(f(x)) > eps:
        if f(a)*f(x) < 0:
            b = x
        else: 
            a = x
        x = a - (((b - a) * f(a)) / (f(b) - f(a)))
    return x


def tangentsearch(x0 : float, eps : float, f, df):
    while np.abs(f(x0)) > eps:
        x0 = x0 - f(x0)/df(x0)
    return x0
    

def fixedpointitersearch(x0 : float, eps : float, g):
    while np.abs(g(x0) - x0) > eps:
        x0 = g(x0)
    return x0


tol = 1e-8
# x = np.arange(-5, 5, 0.1)
# y = func(x)
# suspicions = [-2.0, 0.2, 2.0]
x = np.arange(0.0, 1.28, 0.1)
y = foo(x)
plt.plot(x, y)
plt.grid(True)
plt.show()

result1 = optimize.fsolve(foo, 0.4, xtol=tol)
result2 = binsearch(0.3, 0.5, 1e-10, foo)
result3 = optimize.root(foo, 0.4, tol=tol)

print(result1, foo(result1))
print(result2, foo(result2))
print(result3.x, foo(result3.x))

# for i in suspicions:
#     print(func(optimize.fsolve(func, i, xtol=tol)))

