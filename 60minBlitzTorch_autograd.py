# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 16:49:59 2021

This is a series of script files, according to the Deep Learning with PyTorch 
60 minutes tutorial from the folllowing link 
https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html

@author: Yan Zong
"""
import torch, torchvision
model = torchvision.models.resnet18(pretrained=True) # loading a pretrained resnet18 model 
data=torch.rand(1, 3, 64, 64) # a single image with 3 channels, and height & width of 64
labels = torch.rand(1, 1000) # initialise the label with some random values

# send the data to the model to make a prediction. This is called the forward pass.
prediction = model(data)

loss=(prediction - labels).sum() # use prediction and label to calculate the error
                                 # this is a simple loss function, which is equal to 
                                 # the summation of all the error. This is different 
                                 # from MSE and CrossEntropy
                                 
# Backward propagation is kicked off when calling .backward() on the error 
# tensor. Autograd then calculates and stores the gradients for each model 
# parameter in the parameter’s .grad attribute.                               
loss.backward() # backward pass

# loading an optimizer, in this case SGD with a learning rate of 0.01 and 
# momentum of 0.9. Alll the parameters of the model are registered in the optimizer.
# ToDo: why they need to use the optimizer? --> according to line 34-36, the 
# optimiser is used to make a dradient descent. and the optimisation strategy 
# of SGD is used in this tutorial
optim = torch.optim.SGD(model.parameters(), lr=1e-2, momentum=0.9)

# calling .step() to initiate gradient descent. The optimizer adjusts each 
# parameter by its gradient stored in .grad.
optim.step() #gradient descent

