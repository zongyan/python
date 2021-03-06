"""############################################################################
# IDE: PyTorch 1.8.1-CPU, Miniconda3-2021.04, Python 3.7.10
#
# Note: all the training and testing data sets are already normalised, and two 
#       subfolders need to be created, one is called the 'Log', the other one 
#       is 'Models'
#
#       The code, and more details and explanations are referred to the following 
#       four links: 
#       0_preparing data:
#       https://visualstudiomagazine.com/articles/2021/02/02/pytorch-prepare.aspx    
#       1_defining a neural network
#       https://visualstudiomagazine.com/articles/2021/02/11/pytorch-define.aspx 
#       2_training a neural network
#       https://visualstudiomagazine.com/articles/2021/03/03/pytorch-neural-regression.aspx
#       3_evaluating a trained model
#       https://visualstudiomagazine.com/articles/2021/03/12/pytorch-model-accuracy.aspx
############################################################################"""
import numpy as np
import time
import torch as T
import matplotlib.pyplot as plt

use_cuda = T.cuda.is_available()
print(f"\ndebug: use_cuda is equal to {use_cuda} \n")
# device = T.device("cuda" if use_cuda else "cpu")
device = T.device("cpu")  # an object representing the device on which a 
                          # torch.Tensor is or will be allocated.
print(f"\ndebug: device is equal to {device} \n")

# -----------------------------------------------------------

"""
A PyTorch Dataset can be seen as an interface that must be implemented. At a minimum,
a __init__() method which reads data from file into memory, 
a __len__() method which returns the total number of items in the source data, 
a __getitem__() method which returns a single data item, must be defined 

Because conversion to tensors is a relatively expensive operation, it's usually 
better to convert the data once in __init__() rather than repeatedly in 
the __getitem__() method.

To extract values from a Dataset, no need to call the __getitem__() method 
directly. If accessing a Dataset object using indexing, or using the built-in 
Python enumerate() function, the __getitem__ method() is automatically called.
"""
class HouseDataset(T.utils.data.Dataset): # T.utils.data.Dataset is an abstract 
                                          # class representing a Dataset
  # AC  sq ft   style  price   school
  # -1  0.2500  0 1 0  0.5650  0 1 0
  #  1  0.1275  1 0 0  0.3710  0 0 1
  # air condition: -1 = no, +1 = yes
  # style: art_deco, bungalow, colonial
  # school: johnson, kennedy, lincoln

  def __init__(self, src_file, m_rows=None):
    """
    Python has dozens of ways to read a text le into memory, I need to choose 
    the perference in the future.
    """
    all_xy = np.loadtxt(src_file, max_rows=m_rows,
      usecols=[0,1,2,3,4,5,6,7,8], delimiter="\t",
      # usecols=range(0,9), delimiter="\t",
      comments="#", skiprows=0, dtype=np.float32) # all columns are read
    
    print(f"\ndebug: all_xy is {all_xy} \n")     
    
    tmp_x = all_xy[:,[0,1,2,3,4,6,7,8]]
    # For regression problems, PyTorch requires a two-dimensional matrix of 
    # target values rather than a one-dimensional vector
    tmp_y = all_xy[:,5].reshape(-1,1)    # 2-D required
                                         # -1 in reshape() is to let the 
                                         # interpreter itself figure out the 
                                         # correct value for the number of rows.
                                         # the position of -1 should be the 
                                         # the number of rows.

    print(f"\ndebug: tmp_x is {tmp_x} \n")     
    print(f"\ndebug: tmp_y is {tmp_y} \n")     

    self.x_data = T.tensor(tmp_x, \
      dtype=T.float32).to(device)
    self.y_data = T.tensor(tmp_y, \
      dtype=T.float32).to(device)

    print(f"\nself.x_data is {self.x_data} \n")     
    print(f"\nself.y_data is {self.y_data} \n")     

  def __len__(self):
    return len(self.x_data) # returns the number of items in an object (the 
                            # actual number of lines of data read), which 
                            # also depends on the type of data object, see the 
                            # following comments
                            #
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

    # sample = {
    # 'predictors' : preds,
    # 'prices' : price
    # }
    # return sample   # A common alternative is to return the two matrices as 
    #                 # a Dictionary

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

    # item() is used to extract a single value, for current versions of PyTorch
    # this is unnecessary, but I will keep this 
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
  
  net.eval() # set mode
  
  original_e_delta_train = []  
  for i in range(len(train_ds)):
    (X, Y) = train_ds[i]    # (predictors, target)
    with T.no_grad():
      oupt = net(X)         # computed price
    
    delta = oupt.item() - Y.item()
    original_e_delta_train.append(delta)  
  
  original_e_delta_test = []
  for i in range(len(test_ds)):
    (X, Y) = train_ds[i]    # (predictors, target)
    with T.no_grad():
      oupt = net(X)         # computed price
    
    delta = oupt.item() - Y.item()
    original_e_delta_test.append(delta)  

  # 3. train model
  max_epochs = 500
  ep_log_interval = 50
  lrn_rate = 0.005

  loss_func = T.nn.MSELoss() # Create a criterion that measures the mean 
                             # squared error (squared L2 norm) between each 
                             # element in the input and target.
  # optimizer = T.optim.SGD(net.parameters(), lr=lrn_rate)
  optimizer = T.optim.Adam(net.parameters(), lr=lrn_rate)
  """
  For Adam, it's best to use a small initial learning rate because the algorithm 
  can dynamically change the learning rate during training. 
  
  PyTorch supports 11 different training optimization techniques. Understanding 
  all the details of PyTorch optimizers is difficult.
    
  Optimizers are important but it's better to learn about different optimizers 
  by experimenting with them slowly over time, with different problems. 
  """
  print("\nbat_size = %3d " % bat_size)
  print("loss = " + str(loss_func))
  print("optimizer = Adam")
  print("max_epochs = %3d " % max_epochs)
  print("lrn_rate = %0.3f " % lrn_rate)

  """
  The following is the high-level pseudo-code for training a neural network 
  loop max_epochs times
    loop thru all batches of train data
      read a batch of data (inputs, targets)
      compute outputs using the inputs
      compute error between outputs and targets
      use error to update weights and biases
    end-loop (all batches)
  end-loop (all epochs)
  """
  print("\nStarting training with saved checkpoints")
  net.train()  # set mode
  e_loss = []
  for epoch in range(0, max_epochs):
    T.manual_seed(1+epoch)  # recovery reproducibility
    # print(f"debug: the value of epoch is {epoch}")
    # during each epoch, the seed number is set to a new value (i.e. 1+epoch)
    epoch_loss = 0  # for one full epoch

    for (batch_idx, batch) in enumerate(train_ldr):
      (X, Y) = batch                 # (predictors, targets)
      optimizer.zero_grad()          # prepare and clear gradients
      oupt = net(X)                  # predicted prices
      loss_val = loss_func(oupt, Y)  # avg per item in batch, calculate the value 
                                     # of the loss function
      epoch_loss += loss_val.item()  # accumulate loss function value, the second 
                                     # solution of monitoring loss value is used
      loss_val.backward()            # This computes the gradients of the 
                                     # output node weights and bias, and then 
                                     # the hid2 layer gradients, and then the 
                                     # hid1 layer gradients.
      optimizer.step()               # the newly computed gradients is used to 
                                     # update all the weights and biases in the 
                                     # neural network. 
      # print(f"\ndebug: batch_idx is {batch_idx} \n") # --> batch index     
      # print(f"\ndebug: batch is {batch} \n") # --> batch index     
    
    e_loss.append(loss_val.item())
    
    if epoch % ep_log_interval == 0:
      print("epoch = %4d   loss = %0.4f" % \
       (epoch, epoch_loss))
      """
      see the following link
      https://python-reference.readthedocs.io/en/latest/docs/str/formatting.html
      for more details about the formats the string
      """

      # save checkpoint
      dt = time.strftime("%Y_%m_%d-%H_%M_%S")
      """
      print(time.strftime("%Y_%m_%d-%H_%M_%S"))
      output is: 2021_04_28-21_49_12
      
      对于一般表达式来说，反斜杠后直接回车即可实现续行，使用的关键在于反斜杠后不能用
      空格或者其他符号。
      """      
      fn = "./Log/" + str(dt) + str("-") + \
       str(epoch) + "_checkpoint.pt"

      info_dict = { 
        'epoch' : epoch,
        'net_state' : net.state_dict(),
        'optimizer_state' : optimizer.state_dict() 
      }
      T.save(info_dict, fn)

  print("Done ")

  fig = plt.figure(figsize=(6.5,6.5)) # width=6.5inches, height=6.5inches
  plt.plot(e_loss)
  plt.title("Evolution of Loss during the Training")
  plt.xlabel('Epoch')
  plt.ylabel('Summation of Loss in Each Epoch')  
  plt.show()   

  # 4. evaluate model accuracy
  print("\nComputing model accuracy")
  net.eval() # set mode
  """
  Set the trained model in evaluation mode.
  
  This has any effect only on certain modules. For example, in the Dropout module
  the outputs are scaled by a factor of 1/(1-p) during training; in evaluation, 
  the module simply computes an identity function.
  """
  acc_train = accuracy(net, train_ds, 0.10) 
  print("Accuracy (within 0.10) on train data = %0.4f" % \
    acc_train)

  e_delta_train = []  
  for i in range(len(train_ds)):
    (X, Y) = train_ds[i]    # (predictors, target)
    with T.no_grad():
      oupt = net(X)         # computed price
    
    delta = oupt.item() - Y.item()
    e_delta_train.append(delta)
    
  plt.figure(figsize=(6.5,6.5)) # width=6.5inches, height=6.5inches
  plt.plot(original_e_delta_train, label="Neural Network")
  plt.plot(e_delta_train, label="Trained Model")
  plt.legend(loc="best")
  plt.title("Error in the Training Data")
  plt.xlabel('Data')
  plt.ylabel('Error')  
  plt.show()   

  acc_test = accuracy(net, test_ds, 0.10) 
  print("Accuracy (within 0.10) on test data  = %0.4f" % \
    acc_test)
      
  e_delta_test = []
  for i in range(len(test_ds)):
    (X, Y) = train_ds[i]    # (predictors, target)
    with T.no_grad():
      oupt = net(X)         # computed price
    
    delta = oupt.item() - Y.item()
    e_delta_test.append(delta)
    
  plt.figure(figsize=(6.5,6.5)) # width=6.5inches, height=6.5inches
  plt.plot(original_e_delta_test, label="Neural Network")
  plt.plot(e_delta_test, label="Trained Model")
  plt.legend(loc="best")
  plt.title("Error in the Testing Data")
  plt.xlabel('Data')
  plt.ylabel('Error')  
  plt.show()   


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

  """
  When network predicting, disabling gradient calculation (i.e. set 'requires_grad'
  to False). 
  After that, enable gradient calculation set 'requires_grad' to previous value.

  This will reduce memory consumption for computations.
  """
  with T.no_grad(): # no need to compute the gradient since it isn't for training
    pred_price = net(unk)

  pred_price = pred_price.item()  # scalar
  str_price = \
    "${:,.2f}".format(pred_price * 1000000)
  print(str_price)

  # 6. save final model (state_dict approach)
  print("\nSaving trained model state")
  fn = "./Models/houses_model.pth" # directory path
  T.save(net.state_dict(), fn) # the state_dict (only weights and biases) 
                               # approach is used for storing the trained model. 
                               # The ".pth" extension is usually used for saving
                               # a trained model.
                               
  """
  Before loading a saved trained model, the model's class definition must
  be defined in the program. 
  """                           
  # saved_model = Net().to(device)
  # saved_model.load_state_dict(T.load(fn))
  # use saved_model to make prediction(s)

  print("\nEnd House price demo")

if __name__ == "__main__":
  main()

