import torch
class MnistNN(torch.nn.Module):
    
    """
    Class to define model for mnist 
    """
    
    def __init__(self, input_size=28*28, hidden_size=200, output_size=10):
        super(MnistNN, self).__init__()
        self.fc1 = torch.nn.Linear(input_size, hidden_size)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        x = x.view(x.size(0), -1)  # Flatten input tensor
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
from torchvision import models, transforms
import time
import copy
from torch.utils.data import DataLoader, Dataset


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")