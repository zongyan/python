# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a series of script files, according to the Deep Learning with PyTorch 
60 minutes tutorial from the folllowing link 
https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
"""

import torch
import numpy as np

"""
########## Tensor Initialisation ########## 
"""

"""created a tensor directly from data"""
data=[[1, 2], [3, 4]] # define a list by using []
print(f"data={data}") 
x_data=torch.tensor(data) # change the format from list to tensor
print(f"x_data={x_data}")

"""created a tensor from a numpy array"""
np_array=np.array(data) # change the format from list to array
x_np = torch.from_numpy(np_array) # change the format from array to tensor

"""created a tensor from another tensor"""
x_ones = torch.ones_like(x_data) # retain the properties of x_data
print(f"Ones Tensor: \n {x_ones} \n")
print(f"Ones Tensor:  {x_ones} ")

x_rand = torch.rand_like(x_data, dtype=torch.float) # overrides the datatype of x_data
print(f"Random Tensor: \n {x_rand} \n")

""""created a tensor with random or constant values"""
shape=(2,3) # this is a tuple of tensor dimension
# or shape = (2, 3,) works
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"random tensor : \n {rand_tensor} \n")
print(f"Ones tensor : \n {ones_tensor} \n")
print(f"Zeros tensor : \n {zeros_tensor} \n")

"""
########## Tensor Attributes ########## 
"""
tensor = torch.rand(3, 4)
print(f"shape of tensor :{tensor.shape}")
print(f"datatype of tensor :{tensor.dtype}")
print(f"device tensor is stored on :{tensor.device}")

"""
########## Tensor Operation ########## 
"""
if torch.cuda.is_available(): # move tensor to GPU is available
    tensor=tensor.to('cuda')
    
tensor = torch.ones(4,4)
print(f"tensor : \n {tensor} \n")
tensor[:, 1] = 0
print(f"tensor : \n {tensor} \n")

""" joining tensors by using the cat """
t0 = torch.cat([tensor, tensor,tensor], dim=0) # same as dim=-2
print(t0)
t1 = torch.cat([tensor, tensor,tensor], dim=1) # same as dim=-1
print(t1)

""" multiplying tensors """
# the element-wise product， see the example of the following link 
# https://en.wikipedia.org/wiki/Hadamard_product_(matrices)
print(f"tensor.mul(tensor) \n {tensor.mul(tensor)} \n") 
print(f"tensor * tensor \n {tensor * tensor} \n") # alternative solution

# This computes the matrix multiplication between two tensors
print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)} \n")
print(tensor.T) # transpose of tensor
print(f"tensor * tensor.T \n {tensor @ tensor.T} \n") # alternative syntax
# ToDo, what does the matric multipiication mean

# In-place operations 
print(tensor, "\n")
tensor.t_() # transpose 
print(tensor)
tensor.add_(5) # add 5 for each element
print(tensor)

x=torch.ones_like(tensor) # created a tensor with the same structre of tensor
print(x, "\n")
x.copy_(tensor) # copy from the tensor
print(x, "\n")

"""
########## Bridge with NumPy ########## 
"""
# Tensor to Numpy array
t=torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

t.add_(1) # A change in the tensor reflects in the NumPy array.
print(f"t: {t}")
print(f"n: {n}")

# Numpy to Tensor
n=np.ones(5)
t=torch.from_numpy(n)
np.add(n, 1, out=n) # Changes in the NumPy array reflects in the tensor.
print(f"t: {t}")
print(f"n: {n}")