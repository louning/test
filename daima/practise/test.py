import numpy as np
import random
import matplotlib.pyplot as plt
# e1 = np.array([np.arange(5)]*5)
# print(e1)
# 原型：numpy.tile(A,reps)
# tile共有2个参数，A指待输入数组，reps则决定A重复的次数。整个函数用于重复数组A来构建新的数组
# e2 = np.tile(np.arange(5),(5,1))
# print(e2)
# e3 = np.zeros((5,5))
# e3 += np.arange(5)
# print(e3)

# xx, yy = np.meshgrid(np.arange(-5, 5, .01), np.arange(-5, 5, .01))
# zz = np.sin(xx**2+yy**2)/(xx**2+yy**2)
# plt.contourf(xx, yy, zz)
# plt.show()

color = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])
print(color)