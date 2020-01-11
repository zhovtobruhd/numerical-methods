import numpy as np 
from scipy.integrate import RK45, odeint, solve_ivp
from matplotlib import pyplot as plt 

def func(x, y):
    return 1.3 * y / x

result = solve_ivp(func, (0.5, 4.0), [75.0], method='RK45', first_step=0.1, max_step=0.1, rtol=1e-5, atol=1e-6)
print(result.t[-1])
print(result.y[0][-1])
