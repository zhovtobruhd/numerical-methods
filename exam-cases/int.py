import numpy as np 
from scipy.integrate import simps, trapz

x = np.arange(0., 5.5, 0.5)
y = x**2
print(trapz(y, x))
print(simps(y, x))

x = np.arange(0., 5.1, 0.1)
y = x**2
print(trapz(y, x))
print(simps(y, x))

x = np.array([10., 20., 30., 40., 50., 60., 70., 80., 90., 100., 110.])
l = np.array([2., 3.5, 5., 2.5, 1.2, 1.8, 1.7, 2.2, 2.7, 3.5, 3.4])
u = np.array([18., 21., 19., 20., 20., 18., 15., 12., 16.5, 18., 12.])
print(trapz(u, x) - trapz(l, x))
print(simps(u, x) - simps(l, x))
