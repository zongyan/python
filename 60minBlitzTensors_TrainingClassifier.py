# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 19:14:54 2021

This is a series of script files, according to the Deep Learning with PyTorch 
60 minutes tutorial from the folllowing link 
https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html

@author: Yan Zong
"""
'''
when deal with image, text, audio and video data, the standard python packages
that load data into numpy array. Then it can be converted to torch.Tensor

In this example, the images in CIFAR-10 are of size 3x32x32, i.e. 3-channel color
images of 32x32 pixels in size.
'''

'''
Load and normalise CIFAR10
The output of torchvision datasets are in the range of [0, 1]. need to transform
them to Tensors of normalised range [-1, 1]. It seems that for Machine Learning, 
the input data need to be mapped between [-1, 1], since I also see this normalisation
in the ELM (extreme learning machine)
'''
import torch
import torchvision
import torchvision.transforms as transforms

# ToDo: I understand two data sets (i.e. training and testing) are created. 
# However, I do NOT understand syntax of this torchvision package, if need, 
# come back
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

batch_size = 4
# for training data set
trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
                                          shuffle=True, num_workers=2)
# for testing data set
testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                       download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
                                         shuffle=False, num_workers=2)

classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

# # show some of the training images
# import matplotlib.pyplot as plt
# import numpy as np

# def imshow(img):
#     img = img / 2 + 0.5 # unnormalise
#     npimg = img.numpy()
#     plt.imshow(np.transpose(npimg, (1, 2, 0)))
#     plt.show()
    
# dataiter = iter(trainloader)
# images, labels = dataiter.next()

# # show images
# imshow(torchvision.utils.make_grid(images))
# # print labels
# print(' '.join('%5s' % classes[labels[j]] for j in range(batch_size)))

'''
2. Define a Convolutional Neural Network
'''
import torch.nn as nn 
import torch.nn.functional as F

# ToDo: I know the basic idea of how to define the neural networks. But for how
# to do develop NN, I need more knowledge.
class Net(nn.Module):
    def __init__(self):
        super().__init__() # compared with previous NN, it seem both 
                           # versions [super(), super(Net, self)] are okay
        self.conv1=nn.Conv2d(3, 6, 5)
        self.pool=nn.MaxPool2d(2, 2)
        self.conv2=nn.Conv2d(6, 16, 5)
        self.fc1=nn.Linear(16 * 5 * 5, 120)
        self.fc2=nn.Linear(120, 84)
        self.fc3=nn.Linear(84, 10)
        
    def forward(self, x):
        x=self.pool(F.relu(self.conv1(x)))
        x=self.pool(F.relu(self.conv2(x)))
        x=x.view(-1, 16 * 5 * 5)
        x=F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x=self.fc3(x)
        return x
    
net=Net()

'''
3. Define a Loss function and optimizer
'''
import torch.optim as optim

criterion = nn.CrossEntropyLoss()
optimiser=optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

'''
4. Train the network

This is when things start to get interesting. We simply have to loop over our 
data iterator, and feed the inputs to the network and optimize.

ToDo: need to check both variable i and data, since I am still confused with 
the functions of these two variables
'''
for epoch in range(2):
        
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        # get the inputs; data is a list of [inputs, labels]
        inputs, labels = data
        
        # zero the parameter gradients
        optimiser.zero_grad()
        
        # forward + backward + optimize
        outputs=net(inputs)
        loss=criterion(outputs, labels)
        loss.backward()
        optimiser.step()
        
        # print statistics
        running_loss += loss.item()
        if i % 2000 == 1999: # print every 2000 mini-batches
            print('[%d, %5d] loss: %.3f' % 
                  (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0
            
print('Finished Training')

'''
5. Save the trained model
'''
PATH='./cifar_net.pth'
torch.save(net.state_dict(),PATH) # save to the root folder of this file.

'''
6. Test the network on the test data
ToDo: this need to be reviewed later
'''
dataiter = iter(testloader)
images, labels = dataiter.next()

# print images
# imshow(torchvision.utils.make_grid(images))
print('GroundTruth: ', ' '.join('%5s' % classes[labels[j]] for j in range(4)))

net = Net()
net.load_state_dict(torch.load(PATH))

outputs = net(images)

_, predicted = torch.max(outputs, 1)

print('Predicted: ', ' '.join('%5s' % classes[predicted[j]]
                              for j in range(4)))

# ----------------------------------------------------------------------------
correct = 0
total = 0
with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print('Accuracy of the network on the 10000 test images: %d %%' % (
    100 * correct / total))

class_correct = list(0. for i in range(10))
class_total = list(0. for i in range(10))
with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = net(images)
        _, predicted = torch.max(outputs, 1)
        c = (predicted == labels).squeeze()
        for i in range(4):
            label = labels[i]
            class_correct[label] += c[i].item()
            class_total[label] += 1


for i in range(10):
    print('Accuracy of %5s : %2d %%' % (
        classes[i], 100 * class_correct[i] / class_total[i]))