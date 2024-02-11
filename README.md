# Benchmark on Lesion Segmentations including SOTAR(2022-10)   

When people who try to do lesion segmentation using deep learning model, It is difficult to decide deep learning model considering their type of medical images or their environment. And all the people in this situation have different needs respectively. *ex) efficiency, performance, low capacity, time, etc...*   

So, we compared 9 deep learning models on 6 medical datasets for lesion segmentations in this research.   
If you want to know more about this research, refer to our paper 

**[Publication]**  
Inho Jeong, Donghyeon Kim, Seongmin Jo, Hongryul Ahn. (2022).   
*Comparison of lesion segmentation deep learning models according to medical image types* 한국정보과학회 학술발표논문집,   
[This paper was within Top 10% in KSC2022 Thesis Contest](https://drive.google.com/file/d/1WF2dsHzyrh-AO1TXi9Ndd6PBuWzqniaR/view?usp=sharing)
# Datasets   
We decide datasets based on the bellow criteria.   

1. scar/wound image   
[ISIC-2017](https://challenge.isic-archive.com/data/#2017)   
[Foot Ulcer](https://paperswithcode.com/dataset/dfuc2021)   
2. endoscopic image(polyp)   
[CVC-ClinincDB](https://paperswithcode.com/dataset/cvc-clinicdb)   
[Kvasir-SEG](https://paperswithcode.com/dataset/kvasir-seg)   

3. utlasound image   
[benign/malignant Breast Ultrasound]()

![image](https://github.com/SeongminCC/Benchmark-Lesion-segmentation/assets/110529690/bc10e997-a24a-4933-bd17-deeed4de0a1e)

# Models   
We decide deep learning models based on the bellow criteria.   

1. Medical segmentation model
   - [UNet](https://paperswithcode.com/paper/u-net-convolutional-networks-for-biomedical)
   - [UNet++](https://paperswithcode.com/paper/unet-a-nested-u-net-architecture-for-medical)
   - [ColonSegNet](https://paperswithcode.com/paper/real-time-polyp-detection-localisation-and)  
     
  ![image](https://github.com/SeongminCC/Benchmark-Lesion-segmentation/assets/110529690/d17c4e55-9d9a-4cad-8e9b-f2e195852e94)

2. General segmentation model
   - [DeeplabV3+](https://github.com/VainF/DeepLabV3Plus-Pytorch)
   - [FCN](https://paperswithcode.com/method/fcn)
   - [SegNet](https://paperswithcode.com/method/segnet)
       
![image](https://github.com/SeongminCC/Benchmark-Lesion-segmentation/assets/110529690/ad45589c-c5f1-4cef-a6b3-71104b7aec2d)

3. sotor segmentation model
   - [ColonFormer](https://paperswithcode.com/paper/colonformer-an-efficient-transformer-based)
   - [ESFPNet](https://paperswithcode.com/paper/esfpnet-efficient-deep-learning-architecture)
   - [FCBFormer](https://paperswithcode.com/paper/fcn-transformer-feature-fusion-for-polyp)
       
![image](https://github.com/SeongminCC/Benchmark-Lesion-segmentation/assets/110529690/0c92d4dc-b05c-4337-81a9-f204b72c8417)


# Experiments
## Data Preprocessing
All images were processed at a resolution of **224 (width) * 224 (height)**, regardless of their original resolutions. Except for the ISIC Challenge dataset, all datasets were split into train set, validation set, and test set in a ratio of **6:2:2**.

| Dataset                              | Train set | Validation set | Test set |
|--------------------------------------|-----------|----------------|----------|
| ISIC Challenge                       | 2,000     | 150            | 150      |
| Wound                                | 831       | 278            | 278      |
| CVC-ClinicDB                         | 366       | 123            | 123      |
| Kvasir-SEG                           | 600       | 200            | 200      |
| Breast Ultrasound (Benign Tumors)    | 261       | 88             | 88       |
| Breast Ultrasound (Malignant Tumors) | 126       | 42             | 42       |

For quantitative evaluation of the designed datasets and models, we utilized the **Dice Score(1)**, commonly used in semantic segmentation. The loss function employed was **DiceBCELoss(2)**, as all datasets involved binary segmentation of background and lesion areas.  

$$ Dice Score = \frac{2 \times |Y \cap Y_{pred}|}{|Y \cup Y_{pred}|} \quad (1) $$

$$ Dice BCELoss = (1 - Dice Score) + Binary Cross Entropy \quad (2) $$

The training phase was designed using the PyTorch framework with a batch size of 8, learning rate of 1e-4, and weight decay of 1e-8. We employed the Adam optimizer and trained the model for a total of 100 epochs. During training, if the **Dice Score(2)** on the validation set does not improve for 20 epochs, the training is terminated, and the model saved up to that point is used for evaluation.

## Results
| Model          | ISIC Challenge | Wound   | Kvasir-SEG | CVC-ClinicDB | Breast Ultrasound (Benign Tumors) | Breast Ultrasound (Malignant Tumors) |
|----------------|----------------|---------|------------|--------------|------------------------------------|--------------------------------------|
| FCN (resnet101)       | 0.8477         | 0.8310  | 0.8779     | 0.8767       | 0.8128                             | 0.7531                               |
| SegNet (resnet101)    | 0.8328         | 0.8470  | 0.8672     | 0.8422       | 0.8013                             | 0.7415                               |
| DeepLab V3+ (resnet101) | 0.8519       | 0.8242  | 0.8616     | 0.8712       | 0.8350                             | 0.7720                               |
| U-Net          | 0.8295         | 0.8304  | 0.7891     | 0.7622       | 0.7779                             | 0.6687                               |
| U-Net++        | 0.8350         | 0.8100  | 0.7515     | 0.7289       | 0.7669                             | 0.7089                               |
| ColonSegNet    | 0.8199         | 0.8377  | 0.7471     | 0.6896       | 0.7048                             | 0.6455                               |
| FCBFormer      | 0.8642         | 0.8406  | 0.9830     | 0.8958       | 0.8583                             | 0.7974                               |
| ESFPNet-L      | 0.8541         | 0.8077  | 0.9804     | 0.8709       | 0.8210                             | 0.8050                               |
| ColonFormer    | 0.8456         | 0.8393  | 0.9773     | 0.8547       | 0.7945                             | 0.7984                               |



![image](https://github.com/SeongminCC/Benchmark-Lesion-segmentation/assets/110529690/448d1394-695e-4f55-803d-bb4e9005d1ee)
