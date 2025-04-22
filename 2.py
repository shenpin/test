import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置均值和协方差矩阵
mean = [0, 0]  # 均值
covariance = [[1, 0], [0, 1]]  # 协方差矩阵（单位矩阵表示独立的正态分布）

# 生成二元正态分布的网格数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# 计算二维正态分布的概率密度函数（PDF）
pos = np.dstack((X, Y))
Z = np.exp(-0.5 * (np.sum(np.linalg.inv(covariance) @ pos.T, axis=0).T))

# 绘制三维图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# 设置标签
ax.set_xlabel('X轴')
ax.set_ylabel('Y轴')
ax.set_zlabel('密度')

plt.show()
