import numpy as np 

def df(x, y):
    result = list()
    n = len(x)
    h = x[1] - x[0]
    for i in range(n):
        if i == 0:
            result.append((y[i + 1] - y[i]) / h)
        elif i + 1 == n:
            result.append((y[i] - y[i - 1]) / h)
        else:
            result.append((y[i + 1] - y[i - 1]) / (2 * h))
    return result
            
def ddf(x, y):
    result = list()
    n = len(x)
    h = x[1] - x[0]
    for i in range(n):
        if i == 0:
            result.append((y[i + 2] - 2 * y[i + 1] + y[i]) / (h * h))
        elif i + 1 == n:
            result.append((y[i] - 2 * y[i - 1] + y[i - 2]) / (h * h))
        else:
            result.append((y[i + 1] - 2 * y[i] + y[i - 1]) / (h * h))
    return result

x = np.array([0.0, 0.5, 1.0])
y = np.array([301.0, 283.0, 269.0])

df1 = df(x, y)
ddf1 = ddf(x, y)
print(df1)
print(ddf1)
