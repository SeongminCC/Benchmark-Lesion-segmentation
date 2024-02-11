# dataset
from .augmentation import augmentation_train, augmentation_test
from .dataset import myDataSet

import glob
import os


def create_dataset(data_name = ''):
    
    '''
    args data_name
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
    '''
    
    datadir = '/data/segmentation'
    if data_name == "IRE":
        datadir = '/data/pulse_image'
    
    images_path = 'images/*'
    labels_path = 'labels/*'
    
    train_path = 'trainset'
    validation_path = 'validationset'
    test_path = 'testset'
    
    if data_name == 'CVC-ClinicDB':
        data_path = 'CVC-ClinicDB'
    elif data_name == 'ISIC-2017':
        data_path = 'ISIC-2017'
    elif data_name == 'Kvasir-SEG':
        data_path = 'Kvasir-SEG'
    elif data_name == 'wound':
        data_path = 'wound'
    elif data_name == 'breast-cancer-benign':
        data_path = 'breast-cancer'
        train_path = 'trainset_benign'
        validation_path = 'validationset_benign'
        test_path = 'testset_benign'
    elif data_name == 'breast-cancer-malignant':
        data_path = 'breast-cancer'
        train_path = 'trainset_malignant'
        validation_path = 'validationset_malignant'
        test_path = 'testset_malignant'
    elif data_name == 'BKAI-IGH_NeoPolyp':
        data_path = 'BKAI-IGH_NeoPolyp'
    elif data_name == 'Neck':
        data_path = 'Neck'
    elif data_name == 'Waterloo_skin':
        data_path = 'Waterloo_skin'
    elif data_name == "IRE":
        data_path = "IRE_ultrasound/dataset"
    else:
        print("오타났어요")
        return
    
    
    ## breast-cancer O
    train_images = glob.glob(os.path.join(datadir, data_path, train_path, images_path))  
    train_labels = glob.glob(os.path.join(datadir, data_path, train_path, labels_path))  
    train_images = [img for img in train_images if img.find('jpg')!= -1] # super pixels 이미지 제외

    valid_images = glob.glob(os.path.join(datadir, data_path, validation_path, images_path))
    valid_labels = glob.glob(os.path.join(datadir, data_path, validation_path, labels_path))
    valid_images = [img for img in valid_images if img.find('jpg')!= -1] # super pixels 이미지 제외
    
    test_images = glob.glob(os.path.join(datadir, data_path, test_path, images_path))
    test_labels = glob.glob(os.path.join(datadir, data_path, test_path, labels_path))
    test_images = [img for img in valid_images if img.find('jpg')!= -1] # super pixels 이미지 제외
    

    train_images = sorted(train_images)
    train_labels = sorted(train_labels)

    valid_images = sorted(valid_images)
    valid_labels = sorted(valid_labels)

    test_images = sorted(valid_images)
    test_labels = sorted(valid_labels)

    
    # 데이터셋 클래스 적용
    test_transforms = augmentation_test()

    custom_dataset_train = myDataSet(train_images, train_labels, transforms=test_transforms)
    # print("My custom training-dataset has {} elements".format(len(custom_dataset_train)))

    custom_dataset_val = myDataSet(valid_images, valid_labels, transforms=test_transforms)
    # print("My custom valing-dataset has {} elements".format(len(custom_dataset_val)))
    
    custom_dataset_test = myDataSet(test_images, test_labels, transforms=test_transforms)
    # print("My custom valing-dataset has {} elements".format(len(custom_dataset_val)))
    
    return custom_dataset_train, custom_dataset_val, custom_dataset_test


def create_data(data_name = ''):
    
    '''
    args data_name
        CVC-ClinicDB
        ISIC-2017
        Kvasir-SEG
        wound
        breast-cancer-benign
        breast-cancer-malignant
        BKAI-IGH_NeoPolyp
        Neck
        Waterloo_skin
    '''
    
    datadir = '/data/segmentation'
    images_path = 'images/*'
    labels_path = 'labels/*'
    
    train_path = 'trainset'
    validation_path = 'validationset'
    test_path = 'testset'
    
    if data_name == 'CVC-ClinicDB':
        data_path = 'CVC-ClinicDB'
    elif data_name == 'ISIC-2017':
        data_path = 'ISIC-2017'
    elif data_name == 'Kvasir-SEG':
        data_path = 'Kvasir-SEG'
    elif data_name == 'wound':
        data_path = 'wound'
    elif data_name == 'breast-cancer-benign':
        data_path = 'breast-cancer'
        train_path = 'trainset_benign'
        validation_path = 'validationset_benign'
        test_path = 'testset_benign'
    elif data_name == 'breast-cancer-malignant':
        data_path = 'breast-cancer'
        train_path = 'trainset_malignant'
        validation_path = 'validationset_malignant'
        test_path = 'testset_malignant'
    elif data_name == 'BKAI-IGH_NeoPolyp':
        data_path = 'BKAI-IGH_NeoPolyp'
    elif data_name == 'Neck':
        data_path = 'Neck'
    elif data_name == 'Waterloo_skin':
        data_path = 'Waterloo_skin'
    else:
        print("오타났어요")
        return
    
    
    ## breast-cancer O
    train_images = glob.glob(os.path.join(datadir, data_path, train_path, images_path))  
    train_labels = glob.glob(os.path.join(datadir, data_path, train_path, labels_path))  
    train_images = [img for img in train_images if img.find('jpg')!= -1] # super pixels 이미지 제외

    valid_images = glob.glob(os.path.join(datadir, data_path, validation_path, images_path))
    valid_labels = glob.glob(os.path.join(datadir, data_path, validation_path, labels_path))
    valid_images = [img for img in valid_images if img.find('jpg')!= -1] # super pixels 이미지 제외
    
    test_images = glob.glob(os.path.join(datadir, data_path, test_path, images_path))
    test_labels = glob.glob(os.path.join(datadir, data_path, test_path, labels_path))
    test_images = [img for img in valid_images if img.find('jpg')!= -1] # super pixels 이미지 제외
    

    train_images = sorted(train_images)
    train_labels = sorted(train_labels)

    valid_images = sorted(valid_images)
    valid_labels = sorted(valid_labels)

    test_images = sorted(valid_images)
    test_labels = sorted(valid_labels)
    return (train_images, train_labels), (valid_images, valid_labels), (test_images, test_labels)