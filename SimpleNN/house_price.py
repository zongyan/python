# predict price from AC, sq ft, style, nearest school
# PyTorch 1.8.1-CPU Miniconda3-2021.04  Python 3.7.10
# Windows 10 

# The code, and more details and explanations are referred to the following 
# three links: 
# https://visualstudiomagazine.com/articles/2021/02/11/pytorch-define.aspx 
# https://visualstudiomagazine.com/articles/2021/03/03/pytorch-neural-regression.aspx
# https://visualstudiomagazine.com/articles/2021/03/12/pytorch-model-accuracy.aspx

# Note: all the training and testing data sets are already normalised, and two 
# subfolders need to be created, one is called the 'Log', the other one is 'Models'

import numpy as np
import time
import torch as T

use_cuda = T.cuda.is_available()
print(f"\ndebug: use_cuda is equal to {use_cuda} \n")
# device = T.device("cuda" if use_cuda else "cpu")
device = T.device("cpu")  # an object representing the device on which a 
                          # torch.Tensor is or will be allocated.
print(f"\ndebug: device is equal to {device} \n")

# -----------------------------------------------------------

class HouseDataset(T.utils.data.Dataset): # T.utils.data.Dataset is an abstract 
                                          # class representing a Dataset
  # AC  sq ft   style  price   school
  # -1  0.2500  0 1 0  0.5650  0 1 0
  #  1  0.1275  1 0 0  0.3710  0 0 1
  # air condition: -1 = no, +1 = yes
  # style: art_deco, bungalow, colonial
  # school: johnson, kennedy, lincoln

  def __init__(self, src_file, m_rows=None):
    all_xy = np.loadtxt(src_file, max_rows=m_rows,
      usecols=[0,1,2,3,4,5,6,7,8], delimiter="\t",
      # usecols=range(0,9), delimiter="\t",
      comments="#", skiprows=0, dtype=np.float32)

    tmp_x = all_xy[:,[0,1,2,3,4,6,7,8]]
    tmp_y = all_xy[:,5].reshape(-1,1)    # 2-D required

    self.x_data = T.tensor(tmp_x, \
      dtype=T.float32).to(device)
    self.y_data = T.tensor(tmp_y, \
      dtype=T.float32).to(device)

  def __len__(self):
    return len(self.x_data) # returns the number of items in an object, which 
                            # also depends on the type of data object, see the 
                            # following comments
    """
    import torch as T
    
    debug_x = T.rand((3))
    print(debug_x)
    print(len(debug_x)) # equal to 3
    
    debug_x = T.rand((2, 3))
    print(debug_x)
    print(len(debug_x)) # equal to 2
    
    debug_x = T.rand((3, 4, 5))
    print(debug_x)
    print(len(debug_x)) # equal to 3    
    """
                            
  def __getitem__(self, idx):
    preds = self.x_data[idx,:]  # or just [idx]
    price = self.y_data[idx,:] 
    return (preds, price)       # tuple of two matrices 

# -----------------------------------------------------------

class Net(T.nn.Module): # base class for all neural network modules.
  def __init__(self):
    super(Net, self).__init__()
    self.hid1 = T.nn.Linear(8, 10)  # 8-(10-10)-1
    self.hid2 = T.nn.Linear(10, 10) # applies a linear transformation to the 
    self.oupt = T.nn.Linear(10, 1) # incoming data: Y=XW+B

    """
    randomly configre the weights, and set the biases to zero, for most neural 
    regression problems, the uniform_() and xavier_uniform_() work well, and the 
    uniform_() in the following form, that is T.nn.init.uniform_(self.hid1.weight,
    -0.05, 0.05). This means the range of random values should be definied. 
    
    For convenience, I prefer use the xavier_uniform_(), and xavier_uniform_() 
    computes the range values based on the number of nodes in the layer to 
    which it is applied.
    """
    T.nn.init.xavier_uniform_(self.hid1.weight)
    T.nn.init.zeros_(self.hid1.bias)
    T.nn.init.xavier_uniform_(self.hid2.weight)
    T.nn.init.zeros_(self.hid2.bias)
    T.nn.init.xavier_uniform_(self.oupt.weight)
    T.nn.init.zeros_(self.oupt.bias)

  def forward(self, x):
    """
    Multiple versions of functions (e.g. relu) exist mostly. There is no easy 
    way to deal with the confusion of multiple versions of some PyTorch 
    functions.

    What I can do is to compare the difference of them when using the this 
    activation function.

    relu() and tanh() usually work well for neural regression problems
    """
    z = T.relu(self.hid1(x))
    z = T.relu(self.hid2(z))
    z = self.oupt(z)  # no activation
    return z

# -----------------------------------------------------------

def accuracy(model, ds, pct):
  # assumes model.eval()
  # percent correct within pct of true house price
  n_correct = 0; n_wrong = 0

  for i in range(len(ds)):
    (X, Y) = ds[i]            # (predictors, target)
    with T.no_grad():
      oupt = model(X)         # computed price

    abs_delta = np.abs(oupt.item() - Y.item())
    max_allow = np.abs(pct * Y.item())
    if abs_delta < max_allow:
      n_correct +=1
    else:
      n_wrong += 1

  acc = (n_correct * 1.0) / (n_correct + n_wrong)
  return acc

# -----------------------------------------------------------

def accuracy_quick(model, dataset, pct):
  # assumes model.eval()
  n = len(dataset)
  X = dataset[0:n][0]  # all predictor values
  Y = dataset[0:n][1]  # all target prices
  with T.no_grad():
    oupt = model(X)      # all computed prices

  max_deltas = T.abs(pct * Y)    # max allowable deltas
  abs_deltas = T.abs(oupt - Y)   # actual differences
  
  results = abs_deltas < max_deltas  # [[True, False, . .]]
  acc = T.sum(results, dim=0).item() / n  # dim not needed
  return acc

# -----------------------------------------------------------

def baseline_acc(ds, pct):
  # linear regression model accuracy using just sq. feet
  # y = 1.9559x + 0.0987 (from separate program)
  n_correct = 0; n_wrong = 0
  for i in range(len(ds)):
    (X, Y) = ds[i]           # (predictors, target)
    x = X[1].item()          # sq feet predictor
    y = 1.9559 * x + 0.0987  # computed

    abs_delta = np.abs(oupt.item() - Y.item())
    max_allow = np.abs(pct * Y.item())
    if abs_delta < max_allow:
      n_correct +=1
    else:
      n_wrong += 1

  acc = (n_correct * 1.0) / (n_correct + n_wrong)
  return acc   

# -----------------------------------------------------------

def main():
  # 0. get started
  print("\nBegin predict House price \n")
  """
  see the following link
  https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/
  and 'Generating the Random Numbers.pdf' for more details
  """
  T.manual_seed(4)  # sets the seed values, and the trainined model is reproducible
  np.random.seed(4)
  
  # 1. create DataLoader objects
  print("Creating Houses Dataset objects ")
  train_file = "./houses_train.txt"  # all data sets are normalised
  train_ds = HouseDataset(train_file)  # all 200 rows

  test_file = "./houses_test.txt"
  test_ds = HouseDataset(test_file)  # all 40 rows

  bat_size = 10
  train_ldr = T.utils.data.DataLoader(train_ds,
    batch_size=bat_size, shuffle=True)
  """
  DataLoader: combines a dataset and a sampler, and provides an iterable over 
  the given dataset. Please see the following link:  
  https://pytorch.org/docs/stable/data.html?highlight=dataloader#torch.utils.data.DataLoader
  """
  
  # 2. create network
  net = Net().to(device) # specify a device (i.e. cpu or cuda) for use

  # 3. train model
  max_epochs = 500
  ep_log_interval = 50
  lrn_rate = 0.005

  loss_func = T.nn.MSELoss()
  # optimizer = T.optim.SGD(net.parameters(), lr=lrn_rate)
  optimizer = T.optim.Adam(net.parameters(), lr=lrn_rate)

  print("\nbat_size = %3d " % bat_size)
  print("loss = " + str(loss_func))
  print("optimizer = Adam")
  print("max_epochs = %3d " % max_epochs)
  print("lrn_rate = %0.3f " % lrn_rate)

  print("\nStarting training with saved checkpoints")
  net.train()  # set mode
  for epoch in range(0, max_epochs):
    T.manual_seed(1+epoch)  # recovery reproducibility
    epoch_loss = 0  # for one full epoch

    for (batch_idx, batch) in enumerate(train_ldr):
      (X, Y) = batch                 # (predictors, targets)
      optimizer.zero_grad()          # prepare gradients
      oupt = net(X)                  # predicted prices
      loss_val = loss_func(oupt, Y)  # avg per item in batch
      epoch_loss += loss_val.item()  # accumulate avgs
      loss_val.backward()            # compute gradients
      optimizer.step()               # update wts

    if epoch % ep_log_interval == 0:
      print("epoch = %4d   loss = %0.4f" % \
       (epoch, epoch_loss))

      # save checkpoint
      dt = time.strftime("%Y_%m_%d-%H_%M_%S")
      fn = "./Log/" + str(dt) + str("-") + \
       str(epoch) + "_checkpoint.pt"

      info_dict = { 
        'epoch' : epoch,
        'net_state' : net.state_dict(),
        'optimizer_state' : optimizer.state_dict() 
      }
      T.save(info_dict, fn)

  print("Done ")

  # 4. evaluate model accuracy
  print("\nComputing model accuracy")
  net.eval()
  acc_train = accuracy(net, train_ds, 0.10) 
  print("Accuracy (within 0.10) on train data = %0.4f" % \
    acc_train)

  acc_test = accuracy(net, test_ds, 0.10) 
  print("Accuracy (within 0.10) on test data  = %0.4f" % \
    acc_test)

  # base_acc_train = baseline_acc(train_ds, 0.10) 
  # print("%0.4f" % base_acc_train)  # 0.7000
  # base_acc_test = baseline_acc(test_ds, 0.10)    
  # print("%0.4f" % base_acc_test)   # 0.7000

  # 5. make a prediction
  print("\nPredicting price for AC=no, sqft=2300, ")
  print(" style=colonial, school=kennedy: ")
  unk = np.array([[-1, 0.2300,  0,0,1,  0,1,0]],
    dtype=np.float32)
  unk = T.tensor(unk, dtype=T.float32).to(device) 

  with T.no_grad():
    pred_price = net(unk)
  pred_price = pred_price.item()  # scalar
  str_price = \
    "${:,.2f}".format(pred_price * 1000000)
  print(str_price)

  # 6. save final model (state_dict approach)
  print("\nSaving trained model state")
  fn = "./Models/houses_model.pth" # directory path
  T.save(net.state_dict(), fn)

  # saved_model = Net()
  # saved_model.load_state_dict(T.load(fn))
  # use saved_model to make prediction(s)

  print("\nEnd House price demo")

if __name__ == "__main__":
  main()

