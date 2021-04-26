import random
import torch
import math
import torch.nn as nn


class testnet(torch.nn.Module):
    def __init__(self,in_dim,n_hidden_1,n_hidden_2,n_hidden_3,out_dim):
        super(testnet,self).__init__()
        self.layer1=nn.Sequential(nn.Linear(in_dim,n_hidden_1))
        self.layer2=nn.Sequential(nn.Linear(n_hidden_1,n_hidden_2))
        self.layer3 = nn.Sequential(nn.Linear(n_hidden_2, n_hidden_3))
        self.layer4=nn.Sequential(nn.Linear(n_hidden_3,out_dim))
    def forward(self,x):
        x=self.layer1(x)
        x = torch.relu(x)
        x=self.layer2(x)
        x = torch.relu(x)
        x=self.layer3(x)
        x = torch.relu(x)
        x = self.layer4(x)
        return x


# Create Tensors to hold input and outputs.
x0 = torch.rand(1, 200)
x1 = torch.rand(1, 200)
x2 = torch.rand(1, 200)
x3 = torch.rand(1, 200)
x = torch.stack((x0, x1, x2,x3), 0)
x = x.view(4,200).t()
y = x0 + x1*x2
y =y.reshape((200,1))
# Construct our model by instantiating the class defined above
model = testnet(4,8,8,8,1)

# Construct our loss function and an Optimizer. Training this strange model with
# vanilla stochastic gradient descent is tough, so we use momentum
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-2)

for t in range(8000):
    # Forward pass: Compute predicted y by passing x to the model
    y_pred = model(x)

    # Compute and print loss
    loss = criterion(y_pred, y)
    if t % 4 == 1:
        # print(t, loss.item())
        # print(y_pred[0:10].view(1,10))
        # print(y[0:10].reshape((1,10)))
        print(t,loss)
        # model.print_gradient()
    # Zero gradients, perform a backward pass, and update the weights.
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
# model.first_layer_gradient(merge = False)