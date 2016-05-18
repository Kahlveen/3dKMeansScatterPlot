from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D
import random
from sklearn.cluster import KMeans
import numpy as np

km_n_clusters = 3


fig = pylab.figure()
ax = Axes3D(fig)

x = range(0,20)
y = range(40,60)
z = range(70,90)

mat = np.array([x,y,z]).T

random.shuffle(x, lambda:random.gauss(0.5,0.1))
random.shuffle(y, lambda:random.gauss(0.5,0.1))
random.shuffle(z, lambda:random.gauss(0.5,0.1))

# groups the first element of x with first element of y as one corrdinate set
ax.scatter(x,y,z)

clt = KMeans(n_clusters=km_n_clusters)
clt.fit(mat)

flatClt = clt.cluster_centers_.flatten()
xclt = flatClt[::km_n_clusters]
yclt = flatClt[1::km_n_clusters]
zclt = flatClt[2::km_n_clusters]

ax.scatter(xclt,yclt,zclt,c='r')
pyplot.show()


