import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import solve

# make sure that equation looks like that:
# y'' + p(x)y' + q(x)y = f(x)
# { alpha[0]y(a) + alpha[1]y'(a) = A
# { beta[0]y(b) + beta[1]y'(b) = B

def p1(x):
    return x * x * x + 1


def q1(x):
    return 1 - x * x


def f1(x):
    return np.exp(1 - 2.5 * x * x)


def p2(x):
    return 1.0 / x


def q2(x):
    return 0.0


def f2(x):
    return 1.0 / (x * x)


def finitedifferencemethod(p, q, f, a, b, ya ,yb, alpha, beta, n):
    h = (b - a) / float(n)
    x = list()
    d = list()
    for i in range(0, (n + 1)):
        x.append(a + float(i) * h)
        d.append(float(i) + 1.0)
    x = np.array(x)
    C = np.zeros((n + 1, n + 1), order='C')
    d = np.array(d)
    
    C[0][0] = alpha[0] * h + alpha[1]
    C[0][1] = alpha[1]
    d[0] = ya * h
    
    for i in range(1, n):
        C[i][i - 1] = 1 - h * p(x[i]) / 2.0
        C[i][i] = h * h * q(x[i]) - 2.0
        C[i][i + 1] = 1 + h * p(x[i]) / 2.0
        d[i] = f(x[i]) * h * h
    
    C[n][n - 1] = -beta[1]
    C[n][n] = beta[0] * h + beta[1]
    d[n] = yb * h
    
    y = solve(C, d)
   
    return x, y
    
a1, b1 = 1.0, 1.4
ya1, yb1 = 0.0, 0.05661
alpha1 = np.array([1.0, 0.0])
beta1 = np.array([1.0, 0.0])
resultx1, resulty1 = finitedifferencemethod(p2, q2, f2, a1, b1, ya1 ,yb1, alpha1, beta1, 5)
resultx2, resulty2 = finitedifferencemethod(p2, q2, f2, a1, b1, ya1 ,yb1, alpha1, beta1, 30)

fig, axs = plt.subplots(2, constrained_layout=True)
fig.suptitle("Finite difference")
axs[0].plot(resultx1, resulty1, 'b.-')
axs[1].plot(resultx2, resulty2, 'r.-')
plt.show()