import numpy as np
from scipy import linalg
import math 

def norm(a):
    x = 0.0
    for i in a:
        x = x + (i * i)
    
    return math.sqrt(x)

def iterations(C, d, eps):
    x = d
    lx = 0.0
    while norm(lx - x) > eps:
        lx = x
        x = np.dot(C, x) + d
    
    return x


def jacobi(A, b, eps): # TODO: reset A, b again
    n = A.shape[0]
    
    for i in range(n):
        b[i] = b[i] / A[i][i]
        A[i] = -A[i] / A[i][i]
        A[i][i] = 0.0
    
    return iterations(A, b, eps)


A = np.array([0.14, 0.24, -0.84, 1.07, -0.83, 0.56, 0.64, 0.43, -0.38]).reshape(3, 3)
b = np.array([1.11, 0.48, -0.83])
x = linalg.solve(A, b)

print(x, np.dot(A, x))

A = np.array([10.0, 5.0, 1.0, 1.0, 7.0, 1.0, -2.0, 6.0, 1.0]).reshape(3, 3)
b = np.array([3.0, 5.0, 1.0])
x = linalg.solve(A, b)

print(x, np.dot(A, x))