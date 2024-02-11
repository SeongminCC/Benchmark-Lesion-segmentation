# files and system
import os
import sys
import time
import random
import argparse
import wandb

from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob
from IPython.display import clear_output
# working with images
import cv2
import imageio
import scipy.ndimage
# import skimage.transform

import torchvision.transforms as transforms

import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F


# import torchsummary
from tqdm import notebook

sys.path.insert(0, '..')

# losses
from utils.metrics import iou_pytorch_eval, IoULoss, IoUBCELoss, DiceBCELoss , dice_pytorch_eval
from utils.metrics import iou_pytorch_test, dice_pytorch_test, precision_pytorch_test, recall_pytorch_test, fbeta_pytorch_test, accuracy_pytorch_test

# dataset
from utils.dataset import myDataSet
from utils.create_data import create_dataset

# models
from utils.create_model import create_model

# train
from train import fit, metric
from scheduler import CosineAnnealingWarmupRestarts



def torch_seed(random_seed):
    random.seed(random_seed)
    np.random.seed(random_seed)
    torch.manual_seed(random_seed)
    torch.cuda.manual_seed(random_seed)
    torch.backends.cudnn.deterministic = True
    
    
    
    
def run(args):
    DEVICE = torch.device("cuda:1" if torch.cuda.is_available() else "cpu") # select device for training, i.e. gpu or cpu
    
    """
    
    args(model)
        colonsegnet
        deeplabv3
        esfpnet ## mmcv 설치 필요~!
        fcbformer
        fcn
        segnet
        unet
        unet++
    
    
    args(data name)
        CVC-ClinicDB
        ISIC-2017
        Kvasir-SEG
        wound
        breast-cancer-benign
        breast-cancer-malignant
        BKAI-IGH_NeoPolyp
        Neck
        Waterloo_skin
        
        "IRE"
    """

    # torch_seed(random_seed = args.seed)
    epochs = args.epochs
    patience = args.patience
    BATCH_SIZE = args.batch_size
    
    model_name = args.model
    data_name = args.data_name
    
    # model
    model = create_model(model_name = model_name).to(DEVICE)
    
    # dataset
    custom_dataset_train, custom_dataset_val, custom_dataset_test = create_dataset(data_name = data_name)
    
    # dataloader
    dataloader_train = torch.utils.data.DataLoader(custom_dataset_train, batch_size=BATCH_SIZE, shuffle=True, num_workers=2) 
    dataloader_val = torch.utils.data.DataLoader(custom_dataset_val, batch_size=BATCH_SIZE, shuffle=False, num_workers=2) 
    dataloader_test = torch.utils.data.DataLoader(custom_dataset_test, batch_size=BATCH_SIZE, shuffle=False, num_workers=2) 
    
    # set training
    optimizer = torch.optim.Adam(model.parameters(), lr = args.lr, weight_decay = 1e-8)
    criterion = DiceBCELoss()
    
    # scheduler
    if args.use_scheduler:
        scheduler = CosineAnnealingWarmupRestarts(
            optimizer,
            first_cycle_steps = epochs/10,
            max_lr = args.lr,
            min_lr = 0.0001,
            warmup_steps = int(epochs/10 * 0.1),
            gamma = 0.8
        )
    else:
        scheduler = None
    
    
    
    if args.use_wandb:  # arg : use_wandb
        wandb.init(name=args.exp_name, project='Medical Image Segmentation', config=args) # arg
    
    
    fit(model=model, 
        dataloader_train=dataloader_train, 
        dataloader_val=dataloader_val, 
        criterion=criterion, 
        optimizer=optimizer, 
        scheduler = scheduler,
        DEVICE=DEVICE, 
        epochs=epochs, 
        model_name=model_name, 
        data_name=data_name, 
        patience=patience,
        use_wandb = args.use_wandb)
    
    
    # fit 함수가 종료된 후, 테스트 데이터에 대해 평가를 진행
    metric(model = model, 
           dataloader_test = dataloader_test, 
           DEVICE = DEVICE,
           model_name = model_name, 
           criterion = criterion,
           data_name = data_name)

    print('Test completed!')
     
    
    

    
    
if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Medical Image Segmentation")
    
    # experiment setting
    parser.add_argument('--exp-name', type = str, help = 'experiment') # 
    parser.add_argument('--model',type=str,default='unet',help='saved model directory') # 
    parser.add_argument('--data-name',type=str,default='CVC-ClinicDB',help='data name')
    parser.add_argument('--patience',type=int,default=20,help='patience for early stopping')
    parser.add_argument('--use-scheduler',action='store_true',help='use scheduler')
    

    # optimizer
    parser.add_argument('--lr',type=float,default=0.001,help='learning_rate')

    # train
    parser.add_argument('--epochs',type=int,default=100,help='the number of epochs')
    parser.add_argument('--batch-size',type=int,default=8,help='batch size')

    # seed
    parser.add_argument('--seed',type=int,default=1201,help='1201 is my birthday')

    # wandb
    parser.add_argument('--use-wandb',action='store_true',help='use wandb')

    args = parser.parse_args()
    
    
    run(args)
    
    
    
    
    
    
    
    
    
    
    
    
    