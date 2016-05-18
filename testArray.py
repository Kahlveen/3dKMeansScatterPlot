import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
flatA = a.flatten()
x = flatA[::3]
y = flatA[1::3]
z = flatA[2::3]
print x
print y
print z


b = np.array([x,y,z]).T
print b



