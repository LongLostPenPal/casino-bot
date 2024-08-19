# surface.py

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
# fig.add_subplot(221)：将图形窗口划分为 2 行 2 列，并在左上角（第一个位置）创建子图。
# fig.add_subplot(223)：将图形窗口划分为 2 行 2 列，并在左下角（第三个位置）创建子图。
ax = fig.add_subplot(111, projection='3d')

x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(x, y)

Z = np.add(-np.power(X, 3), np.power(Y, 2))

surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_rainbow)
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

