# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 07:40:32 2021

@author: yan
"""

print('================Numpy============')
print("https://jalammar.github.io/visual-numpy/")
print('================Numpy============')  


import numpy as np

data=np.array([1, 2, 3]) # 3x1 array
print(data)

data=np.ones(3) # 3x1 one array
print(data)
data=np.zeros(3) # 3x1 zero array
print(data)
data=np.random.random(3)
print(data)

#-----------------------------------------------------------------------------
data=np.array([1, 2])
ones=np.ones(2)
print(data+ones)
print(data-ones)
print(data*ones)
print(data/ones)
# 这两个就是非常的奇怪，按照矩阵的乘除法，这个是不成立的

print(data*3.0)

#-----------------------------------------------------------------------------
print(data[0])
print(data[1])
print(data[0:2])

#-----------------------------------------------------------------------------
data=np.array([1, 2, 3, 4, 5])
print(data.min())
print(data.max())
print(data.sum())

#-----------------------------------------------------------------------------
data=np.array([[1, 2], [3, 4]]) # 2x2
print(data)
data=np.ones((3, 2)) # 3 x 2 array
print(data)

#-----------------------------------------------------------------------------
data=np.array([[1, 2], [3, 4]])
ones=np.ones((2, 2))
print(data + ones)

ones_row=np.ones((1, 2))
print(ones_row)
print(data+ones_row)
"""
一般情况下，只有同尺寸的函数才是可以相加减的，但是呢，还是
有一个特例的，就是这个ones的矩阵，就算是ones的矩阵的尺寸
不一样，但是仍然可以默认是一样的，然后进行加减乘除操作
"""

#-----------------------------------------------------------------------------
data=np.array([1, 2, 3])
powers_of_ten=np.array([[1, 10], [100, 1000], [10000, 100000]])
tmp_data=data.dot(powers_of_ten)
print(tmp_data)
"""
原来，就是在这个NumPy里面，这个操作*，还有dot是两个不同的含义，这个*操作就是
有点类似于The Hadamard product， dot则是传统矩阵中的乘法操作了。
"""

#-----------------------------------------------------------------------------
data=np.array([[1, 2],[3, 4],[5, 6]])
print(data[0, 1]) # 0行，1列的数据
print(data[1:3]) # 1-2行的所有数据
print(data[0:2,0]) # 0-2行，0列的所有数据

#-----------------------------------------------------------------------------
data=np.array([[1, 2],[3, 4],[5, 6]])
print(data.max())
print(data.min())
print(data.sum())
# 上面的是求整个matrix中的max，min，或者是sum

print(data.max(axis=0))
print(data.min(axis=0))
print(data.min(axis=1))
# 我还是不太明白这个axis的含义是个啥

#-----------------------------------------------------------------------------
print(data.T)
print(data)

data=np.array([1, 2, 3, 4, 5, 5])
data_shaped=data.reshape(2, 3)
print(data_shaped)
data_shaped=data.reshape(3, 2)
print(data_shaped)

#这个reshape的功能到底听好玩儿的，有点意思