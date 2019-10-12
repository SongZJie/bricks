from mpl_toolkits.mplot3d import Axes3D

from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math as math

data = np.genfromtxt(r"F:\A_data\sanweimor\mohr2.csv",delimiter=',')


fig = figure()
ax=Axes3D(fig)

#生成空间莫尔圆
x1 = data[:,0]
x2 = data[:,2]
x3 = data[:,4]
z1 = data[:,1]
z2 = data[:,3]
z3 = data[:,5]
y1 = [0]*61
y2 = [0]*61
y3 = [0]*61


x4 = data[:,7]
x5 = data[:,9]
x6 = data[:,11]
z4 = data[:,8]
z5 = data[:,10]
z6= data[:,12]
y4 = [100]*61
y5 = [100]*61
y6 = [100]*61


x7 = data[:,14]
x8 = data[:,16]
x9 = data[:,18]
z7 = data[:,15]
z8 = data[:,17]
z9 = data[:,19]
y7 = [200]*61
y8 = [200]*61
y9 = [200]*61

ax.plot(x1,y1,z1,'k')
ax.plot(x2, y2, z2,'k')
ax.plot(x3, y3, z3,'k')

ax.plot(x4, y4, z4,'k')
ax.plot(x5, y5, z5,'k')
ax.plot(x6, y6, z6,'k')

ax.plot(x7, y7, z7,'k')
ax.plot(x8, y8, z8,'k')
ax.plot(x9, y9, z9,'k')


#空间直线
'''
x_t = np.linspace(90,610,10)
t = 86 + (x_t * np.tan(5.71*math.pi/180))
y_t = [1]*10

ax.plot (x_t,y_t,t)  
'''
# 空间平面或者曲面，Z是空间关于想，x，y的函数
X = np.linspace(50,1000,10)
Y = np.linspace(0, 250,10)
X, Y = np.meshgrid(X, Y)

Z = 22 + (X * np.tan(21 *math.pi/180)) + (Y * np.tan(19 *math.pi/180))
#Z = 28 + X * 0.42 + Y * 0.38
#Z = 30 + (X * np.tan(23 *math.pi/180)) + (Y * np.tan(20 *math.pi/180))
ax.plot_surface(X, Y, Z, rstride=16, cstride=16,  cmap='GnBu')

'''
ax.plot_surface(x, y, z, rstride = 1,   # row 行步长
                 cstride = 2,           # colum 列步长
                 cmap=plt.cm.hot )      # 渐变颜色    cmap='rainbow'
				 
				  	    cmaps = [('Perceptually Uniform Sequential', [
								'viridis', 'plasma', 'inferno', 'magma']),
								('Sequential', [
									'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
									'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
									'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
								('Sequential (2)', [
									'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
									'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
									'hot', 'afmhot', 'gist_heat', 'copper']),
								('Diverging', [
									'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
									'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']),
								('Qualitative', [
									'Pastel1', 'Pastel2', 'Paired', 'Accent',
									'Dark2', 'Set1', 'Set2', 'Set3',
									'tab10', 'tab20', 'tab20b', 'tab20c']),
								('Miscellaneous', [
									'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
									'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
									'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'])]
'''

ax.set_xlabel('Normal stress/kPa')
ax.set_ylabel('Matrix suction/kPa')
ax.set_zlabel('Shear stress/kPa')

legend()

show()