import numpy as np
from matplotlib import pyplot as plt
x = np.arange(-np.pi, np.pi, 0.1)
y = ((np.sin(x) + 1) * 32768.0).astype(int)

print(x, len(x))
print(y)

plt.plot(x, y)
plt.show()
