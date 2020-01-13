import numpy as np
from scipy.optimize import fsolve

def func(p):
    # x, y = p
    # return (2 * x * x + y * y - 1, x * x * x + 6 * x * x * y - 1)
    return (0.5 * np.sin(p[1] / 3.0) - p[0] + 1, 0.3 * np.cos(p[0]) - p[1])


guess = (0.65, 0.35)
x, y = fsolve(func, guess)
print (x, y, func((x, y)))
