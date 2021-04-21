# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 23:01:16 2021

This is a series of script files, according to the Deep Learning with PyTorch 
60 minutes tutorial from the folllowing link 
https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html

@author: Yan Zong
"""

"""
A typical training procedure for a neural network is as follows:
1. Define the neural network that has some learnable parameters (or weights)
2. Iterate over a dataset of inputs
3. Process input through the network
4. Compute the loss (how far is the output from being correct)
5. Propagate gradients back into the network’s parameters
6. Update the weights of the network, typically using a simple update rule: 
   weight = weight - learning_rate * gradient
"""

# define the neural networks
import torch
import torch.nn as nn # constructe NN by using this package
import torch.nn.functional as F

"""
1. Define the neural network that has some learnable parameters (or weights)
"""
class Net(nn.Module):
    """
    the 'self' variable represents the instance of the object itself.    
    "__init__" is a reseved method in python classes, which is the constructor 
    for a class. This method called when an object is created from the class 
    and it allow the class to initialize the attributes of a class.
    
    see the following two links for more details about '__init__' and 'self'
    https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
    and https://www.edureka.co/blog/init-in-python/
    """
    def __init__(self):
        super(Net, self).__init__() # ToDo: I know this is the inheritance, But still 
                                    # confuse with why this need to be used.
        # 1 input image channel, 6 output channels, 3x3 square convolution kernel
        self.conv1=nn.Conv2d(1, 6, 3)
        self.conv2=nn.Conv2d(6, 16, 3)
        # an affine operation: y = Wx + b
        self.fc1=nn.Linear(16 * 6 * 6, 120) # 6*6 from image dimension
        self.fc2=nn.Linear(120, 84) 
        self.fc3=nn.Linear(84, 10)
        
    def forward(self, x):
        x=F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x=F.max_pool2d(F.relu(self.conv2(x)), 2)
        x=x.view(-1, self.num_flat_features(x))
        x=F.relu(self.fc1(x))
        x=F.relu(self.fc2(x))
        x=self.fc3(x)
        return x
        
    def num_flat_features(self, x):
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        return num_features
        
print("the NN is \n")
net = Net()
print(net)

# only the forward function need to be definied, for the backward function, it 
# is automaticall definied by using autograd
params = list(net.parameters()) # The learnable parameters of a model are 
                                # returned by net.parameters()
print(len(params))
print(params[0].size())

"""
2. processing inputs and calling backward, Note that before calling the backward,
   the zero_grad() need to be used to clear the gradients buffer
"""
# the expected input data size is 32 x 32, and try to use a random input
input=torch.randn(1, 1, 32, 32)
print(input)
out=net(input)
print(out)

net.zero_grad() # reset the gradients buffer
out.backward(torch.randn(1, 10)) # backprops with random gradients
                                 # once the backward is called, the Autograd 
                                 # then calculates and stores the gradients 
                                 # for each model parameter in the parameter’s 
                                 # .grad attribute.     
                                 # ToDo: line 91, out.backward is used, but line 
                                 # 132 loss.backward is utilised, what is the 
                                 # difference -> ONLY use loss.backward, NOT out.backward
                                 
"""
3. compute the loss, ToDo, where is ' Propagate gradients back into the 
   network’s parameters', is this done automatically? --> yes, automatically
"""                                 
output=net(input)
target=torch.randn(10)
target=target.view(1, -1)
criterion=nn.MSELoss()

loss=criterion(output, target)
print(loss)

print(loss.grad_fn)  # MSELoss
print(loss.grad_fn.next_functions[0][0])  # Linear
print(loss.grad_fn.next_functions[0][0].next_functions[0][0])  # ReLU

net.zero_grad()
print('conv1.bias.grad before backward')
print(net.conv1.bias.grad)

# calling loss.backward(), the whole graph is differentiated w.r.t. the loss, 
# and all Tensors in the graph that have requires_grad=True will have their .grad 
# Tensor accumulated with the gradient.
loss.backward()
print('conv1.bias.grad after backward')
print(net.conv1.bias.grad)

"""
6. Update the weights of the network, and different opimiser is used 
"""
# weight = weight - learning_rate * gradient
learning_rate = 0.01
for f in net.parameters():
    f.data.sub_(f.grad.data*learning_rate)

'''
optimiser fails to affect the performance of trained NN, it ONLY can affect the 
training speed, but I still need to learn these different optimisers
'''    
import torch.optim as optim
optimizer =optim.SGD(net.parameters(), lr=0.01)   

optimizer.zero_grad()
output=net(input)
loss=criterion(output, target)
loss.backward()
optimizer.step() 