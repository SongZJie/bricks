# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np

# Fixing random state for reproducibility
#读取数据，此种方法只能读csv格式，其他格式可导入pandas读取
data = np.genfromtxt("J:\OneDrive - Platinum\py-project/test.csv",delimiter=',')


def polygon_under_graph(xlist, ylist):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (xlist, ylist) line graph.  Assumes the xs are in ascending order.
    """
    return [(xlist[0], 0.), *zip(xlist, ylist), (xlist[-1], 0.)]


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make verts a list, verts[i] will be a list of (x,y) pairs defining polygon i
verts = []

# Set up the x sequence
#定义x轴
xs = data[1:, 0]

# The ith polygon will appear on the plane y = zs[i]
#定义有几个面
zs = range(1,10)

#每个面上的数据值
ys_1 = data[1:, 1]
ys_2 = data[1:, 2]
ys_3 = data[1:, 3]
ys_4 = data[1:, 4]
ys_5 = data[1:, 5]
ys_6 = data[1:, 6]
ys_7 = data[1:, 7]
ys_8 = data[1:, 8]
ys_9 = data[1:, 9]

verts.append(polygon_under_graph(xs, ys_1))
verts.append(polygon_under_graph(xs, ys_2))
verts.append(polygon_under_graph(xs, ys_3))
verts.append(polygon_under_graph(xs, ys_4))
verts.append(polygon_under_graph(xs, ys_5))
verts.append(polygon_under_graph(xs, ys_6))
verts.append(polygon_under_graph(xs, ys_7))
verts.append(polygon_under_graph(xs, ys_8))
verts.append(polygon_under_graph(xs, ys_9))
print(verts)

#定义颜色
poly = PolyCollection(verts, facecolors=[ 'r', 'g', 'b', 'y', 'r', 'g', 'b', 'y', 'r'], alpha=.6)
ax.add_collection3d(poly, zs=zs, zdir='y')

#定义坐标轴
ax.set_xlim(1977, 2017)
ax.set_ylim(0, 10)
ax.set_zlim(0, 1.5)
my_x_ticks = np.arange(1977, 2017, 5)
my_y_ticks = np.arange(0, 10, 1)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
#定义轴标签
ax.set_xlabel('YEAR')
ax.set_ylabel('SITE')
ax.set_zlabel('DATA')

plt.show()
