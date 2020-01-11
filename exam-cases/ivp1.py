import numpy as np 
from scipy.integrate import RK45, odeint, solve_ivp
from matplotlib import pyplot as plt 

def v():
    return 5

def func(t, Y):
    return np.array([v() * np.cos(Y[2]), v() * np.sin(Y[2]), - v() / (2.47 / np.tan(np.pi / 6.) + 1.456 / 2.)])

Y0 = np.array([5., 2., 0.])
result1 = solve_ivp(func, (0.0, 5.0), Y0, method='RK45', first_step=0.0125, max_step=0.0125, vectorized=True)
plt.plot(result1.y[0], result1.y[1])
plt.show()
