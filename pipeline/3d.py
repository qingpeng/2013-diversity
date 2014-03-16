import numpy as np
import numpy
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def randrange(n, vmin, vmax):
    return (vmax-vmin)*np.random.rand(n) + vmin

fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(111,projection='3d')
n = 100

xs = [1,2,3,4,5]
xs = numpy.array(xs)
ys = [3,3,3,3,3]
zs = [10,8,5,2,1]
ys = numpy.array(ys)
zs = numpy.array(zs)
print xs
print ys
print zs
the_fourth_dimension = numpy.array([20.0,40.0,60.0,80.0,100.0])
the_fourth_dimension1 = randrange(5,0,100)
the_fourth_dimension1 = np.array([ 31.45767429,  39.05699197 , 67.41596086 , 18.7858045  , 43.47494953])
print the_fourth_dimension
colors = cm.hsv(the_fourth_dimension/max(the_fourth_dimension))
print colors
colmap = cm.ScalarMappable(cmap=cm.hsv)
colmap.set_array(the_fourth_dimension)

yg = ax.scatter(xs, ys, zs, c=colors, marker='o')

cb = fig.colorbar(colmap)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')


plt.show()