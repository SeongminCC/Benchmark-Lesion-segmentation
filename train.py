import numpy as np
import pandas as pd
import time
import os

# losses
from utils.metrics import iou_pytorch_eval, IoULoss, IoUBCELoss, DiceBCELoss , dice_pytorch_eval
from utils.metrics import iou_pytorch_test, dice_pytorch_test, precision_pytorch_test, recall_pytorch_test, fbeta_pytorch_test, accuracy_pytorch_test

from collections import OrderedDict
import torch
import wandb


def train(model, dataloader_train, dataloader_val, criterion, optimizer,model_name, data_name, DEVICE):
    running_loss, running_iou, running_dice = 0, 0, 0
    val_loss, val_iou, val_dice = 0, 0, 0
    fps_list = []
    
    model.train()
    for i, (imgs, masks) in enumerate(dataloader_train):
        imgs, masks = imgs.to(DEVICE), masks.to(DEVICE)
        
        prediction = model(imgs)
        
        if isinstance(prediction, tuple):
            prediction = prediction[0]

        optimizer.zero_grad()
        loss = criterion(prediction, masks)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        running_iou += iou_pytorch_eval(prediction, masks)
        running_dice += dice_pytorch_eval(prediction, masks)
        print("\r Iter.: {} of {}, Loss: {:.6f}, IoU:  {:.6f},  Dice:  {:.6f}".format(i, len(dataloader_train), running_loss/(i+1), running_iou/(i+1), running_dice/(i+1)), end="")
        
    model.eval()
    with torch.no_grad():
        for i, (imgs, masks) in enumerate(dataloader_val):
            imgs, masks = imgs.to(DEVICE), masks.to(DEVICE)
            
            ## FPS 측정 ##
            for j in range(imgs.size(0)):
                start_time = time.time()
                prediction = model(imgs[j].unsqueeze(0))
                end_time = time.time()

                elapsed_time = end_time - start_time
                fps = 1 / elapsed_time
                fps_list.append(fps)

            predictions = model(imgs)
            loss = criterion(predictions, masks)
            val_loss += loss.item()
            val_iou += iou_pytorch_eval(predictions, masks).item()
            val_dice += dice_pytorch_eval(predictions, masks).item()
    
    avg_fps = sum(fps_list) / len(fps_list)
    
    
    return OrderedDict([('loss',running_loss/len(dataloader_train)), ('iou',running_iou/len(dataloader_train)), ('dice',running_dice/len(dataloader_train))]), OrderedDict([('loss',val_loss/len(dataloader_val)), ('iou',val_iou/len(dataloader_val)), ('dice',val_dice/len(dataloader_val)), ('fps', avg_fps)])    



# 각 image 1장에 대한 fps 계산 #
## gpu 를 사용한 fps & cpu 코어 2개 사용한 fps 측정 ##
def test(model, dataloader_test, criterion, DEVICE, model_name, data_name):
    test_loss, test_iou, test_dice = 0, 0, 0
    fps_list_gpu = []
    fps_list_cpu = []
    
    checkpoint_path = "/data2/medical/_checkpoints" + f"/ckpt_{model_name}_{data_name}.pth"
    print(checkpoint_path)
    model.load_state_dict(torch.load(checkpoint_path, map_location=DEVICE)['net'])
    model.eval()
    
    # cpu 코어 2개 사용
    torch.set_num_threads(2)
    
    with torch.no_grad():
        for i, (imgs, masks) in enumerate(dataloader_test):
            imgs, masks = imgs.to(DEVICE), masks.to(DEVICE)
            
            ## FPS 측정 (GPU) ##
            for j in range(imgs.size(0)):
                start_time = time.time()
                prediction = model(imgs[j].unsqueeze(0))
                end_time = time.time()

                elapsed_time = end_time - start_time
                fps_gpu = 1 / elapsed_time
                fps_list_gpu.append(fps_gpu)

            ## FPS 측정 (CPU) ##
            model.to('cpu')
            for j in range(imgs.size(0)):
                start_time = time.time()
                prediction = model(imgs[j].cpu().unsqueeze(0))
                end_time = time.time()

                elapsed_time = end_time - start_time
                fps_cpu = 1 / elapsed_time
                fps_list_cpu.append(fps_cpu)
            model.to(DEVICE)

            predictions = model(imgs)
            loss = criterion(predictions, masks)
            test_loss += loss.item()
            test_iou += iou_pytorch_eval(predictions, masks).item()
            test_dice += dice_pytorch_eval(predictions, masks).item()
    
    avg_fps_gpu = sum(fps_list_gpu) / len(fps_list_gpu)
    avg_fps_cpu = sum(fps_list_cpu) / len(fps_list_cpu)
    return OrderedDict([('loss',test_loss/len(dataloader_test)), ('iou',test_iou/len(dataloader_test)), ('dice',test_dice/len(dataloader_test)), ('fps_gpu', avg_fps_gpu), ('fps_cpu', avg_fps_cpu)])


## batch 당 fps 계산 ##
# def test(model, dataloader_test, criterion, DEVICE, model_name, data_name):
#     test_loss, test_iou, test_dice = 0, 0, 0
#     fps_list = []
    
#     checkpoint_path = "/data2/medical/_checkpoints" + f"/ckpt_{model_name}_{data_name}.pth"
#     print(checkpoint_path)
#     model.load_state_dict(torch.load(checkpoint_path, map_location=DEVICE)['net'])
#     model.eval()
#     with torch.no_grad():
#         for i, (imgs, masks) in enumerate(dataloader_test):
#             imgs, masks = imgs.to(DEVICE), masks.to(DEVICE)
            
#             ## FPS 측정 ##
#             start_time = time.time()
#             predictions = model(imgs)
#             end_time = time.time()

#             elapsed_time = end_time - start_time
#             fps = imgs.size(0) / elapsed_time
#             fps_list.extend([fps] * imgs.size(0))

                
#             loss = criterion(predictions, masks)
#             test_loss += loss.item()
#             test_iou += iou_pytorch_eval(predictions, masks).item()
#             test_dice += dice_pytorch_eval(predictions, masks).item()
    
#     avg_fps = sum(fps_list) / len(fps_list)
#     return OrderedDict([('loss',test_loss/len(dataloader_test)), ('iou',test_iou/len(dataloader_test)), ('dice',test_dice/len(dataloader_test)), ('fps', avg_fps)])






def metric(model, dataloader_test, DEVICE, model_name, criterion, data_name):
    best_iou, best_dice, best_loss = 0, 0, np.inf
    state = {}
    
    test_metrics = test(model = model,
                        dataloader_test = dataloader_test,
                        criterion = criterion,
                        DEVICE = DEVICE,
                        model_name = model_name,
                        data_name = data_name)
    
    print("\r Test Loss: {:.6f}, IoU: {:.6f}, Dice: {:.6f}, FPS(gpu): {:.2f}, FPS(cpu): {:.2f}".format(
        test_metrics['loss'], test_metrics['iou'], test_metrics['dice'], test_metrics['fps_gpu'], test_metrics['fps_cpu']))
    
    best_iou = max(best_iou, test_metrics['iou'])
    best_dice = max(best_dice, test_metrics['dice'])
    best_loss = min(best_loss, test_metrics['loss'])
    fps_cpu = test_metrics['fps_cpu']
    fps_gpu = test_metrics['fps_gpu']

    metrics_to_save = {
        'loss': best_loss,
        'dice': best_dice,
        'iou': best_iou,
        'fps_cpu': fps_cpu,
        'fps_gpu': fps_gpu
    }

    if not os.path.isdir('_checkpoints'):
        os.mkdir('_checkpoints')
    
    df = pd.DataFrame([metrics_to_save])
    csv_filename = f'./_checkpoints/results_{model_name}_{data_name}.csv'
    df.to_csv(csv_filename, index=False)

    print('Test results saved in {}'.format(csv_filename))

    
def fit(model, dataloader_train, dataloader_val, criterion, optimizer, scheduler, DEVICE, epochs, model_name, data_name, patience, use_wandb):
    best_iou, best_dice, best_loss = 0, 0, np.inf
    best_epoch_dice = -1
    state = {}
    lst_epoch_metric = []
    step = 0
    
    for epoch in range(epochs):
        print(f"epoch : {epoch}")
            
        train_metrics, val_metrics = train(model = model,
                             dataloader_train = dataloader_train,
                             dataloader_val = dataloader_val,
                             criterion = criterion,
                             optimizer = optimizer,
                             data_name = data_name,
                             model_name = model_name,
                             DEVICE = DEVICE)
        
#         val_metrics = val(model = model,
#                            dataloader_val = dataloader_val,
#                            criterion = criterion,
#                            data_name = data_name,
#                            model_name = model_name,
#                            DEVICE = DEVICE)
        
        print("\r Epoch: {} of {}, Iter.: {} of {}, Train Loss: {:.6f}, IoU: {:.6f}, Dice: {:.6f}".format(epoch, epochs, len(dataloader_train), len(dataloader_train), train_metrics['loss'], train_metrics['iou'], train_metrics['dice']))
        print("\r Epoch: {} of {}, Iter.: {} of {}, Valid Loss: {:.6f}, IoU: {:.6f}, Dice: {:.6f}, FPS: {:.2f}".format(epoch, epochs, len(dataloader_train), len(dataloader_train), val_metrics['loss'], val_metrics['iou'], val_metrics['dice'], val_metrics['fps']))
        
        if scheduler:
            scheduler.step()
        
        if use_wandb:
            metrics = OrderedDict(lr=optimizer.param_groups[0]['lr'])
            metrics.update([('train_' + k, v) for k, v in train_metrics.items()])
            metrics.update([('eval_' + k, v) for k, v in val_metrics.items()])
            wandb.log(metrics, step=step)
            
        step += 1
        
        best_iou = max(best_iou, val_metrics['iou'])
        best_dice = max(best_dice, val_metrics['dice'])
        best_loss = min(best_loss, val_metrics['loss'])
        fps = val_metrics['fps']
        best_epoch_dice = epoch if best_dice == val_metrics['dice'] else best_epoch_dice
        
#         model.load_state_dict(torch.load(f"/data2/medical/weight/{model_name}_{data_name}.pth"))
        
        if best_epoch_dice == epoch:
            # print('Saving..')
            state['net'] = model.state_dict()
            state['dice'] = best_dice
            state['iou'] = best_iou
            state['loss'] = best_loss
            state['epoch'] = epoch
            

            if not os.path.isdir('_checkpoints'):
                os.mkdir('_checkpoints')
            torch.save(state, f'/data2/medical/_checkpoints/ckpt_{model_name}_{data_name}.pth')


        elif best_epoch_dice + patience < epoch:
            print(f"\nEarly stopping. Target criteria has not improved for {patience} epochs.\n")
            break
    

    metrics_to_save = {
        'loss': state['loss'],
        'dice': state['dice'],
        'iou': state['iou'],
        'fps': val_metrics['fps']
    }

    df = pd.DataFrame([metrics_to_save])
    csv_filename = f'/data2/medical/_checkpoints/results_{model_name}_{data_name}.csv'
    df.to_csv(csv_filename, index=False)
    