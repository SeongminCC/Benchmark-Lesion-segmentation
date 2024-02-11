## unet ##
python main.py \
--exp-name unet-CVC \
--model unet \
--data-name CVC-ClinicDB \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler 

python main.py \
--exp-name unet-ISIC \
--model unet \
--data-name ISIC-2017 \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name unet-Kvasir \
--model unet \
--data-name Kvasir-SEG \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name unet-wound \
--model unet \
--data-name wound \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name unet-benign \
--model unet \
--data-name breast-cancer-benign \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name unet-malignant \
--model unet \
--data-name breast-cancer-malignant \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name unet-BKAI \
--model unet \
--data-name BKAI-IGH_NeoPolyp \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name unet-Neck \
--model unet \
--data-name Neck \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name unet-Waterloo \
--model unet \
--data-name Waterloo_skin \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

## unet++ ##
python main.py \
--exp-name unet++-CVC \
--model unet++ \
--data-name CVC-ClinicDB \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name unet++-ISIC \
--model unet++ \
--data-name ISIC-2017 \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name unet++-Kvasir \
--model unet++ \
--data-name Kvasir-SEG \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name unet++-wound \
--model unet++ \
--data-name wound \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name unet++-benign \
--model unet++ \
--data-name breast-cancer-benign \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name unet++-malignant \
--model unet++ \
--data-name breast-cancer-malignant \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name unet++-BKAI \
--model unet++ \
--data-name BKAI-IGH_NeoPolyp \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name unet++-Neck \
--model unet++ \
--data-name Neck \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name unet++-Waterloo \
--model unet++ \
--data-name Waterloo_skin \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

## segnet ##
python main.py \
--exp-name segnet-CVC \
--model segnet \
--data-name CVC-ClinicDB \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name segnet-ISIC \
--model segnet \
--data-name ISIC-2017 \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name segnet-Kvasir \
--model segnet \
--data-name Kvasir-SEG \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name segnet-wound \
--model segnet \
--data-name wound \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name segnet-benign \
--model segnet \
--data-name breast-cancer-benign \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name segnet-malignant \
--model segnet \
--data-name breast-cancer-malignant \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name segnet-BKAI \
--model segnet \
--data-name BKAI-IGH_NeoPolyp \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name segnet-Neck \
--model segnet \
--data-name Neck \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name segnet-Waterloo \
--model segnet \
--data-name Waterloo_skin \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

## fcn ##
python main.py \
--exp-name fcn-CVC \
--model fcn \
--data-name CVC-ClinicDB \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcn-ISIC \
--model fcn \
--data-name ISIC-2017 \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcn-Kvasir \
--model fcn \
--data-name Kvasir-SEG \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcn-wound \
--model fcn \
--data-name wound \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcn-benign \
--model fcn \
--data-name breast-cancer-benign \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcn-malignant \
--model fcn \
--data-name breast-cancer-malignant \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcn-BKAI \
--model fcn \
--data-name BKAI-IGH_NeoPolyp \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcn-Neck \
--model fcn \
--data-name Neck \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcn-Waterloo \
--model fcn \
--data-name Waterloo_skin \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler


## fcbformer ##
python main.py \
--exp-name fcbformer-CVC \
--model fcbformer \
--data-name CVC-ClinicDB \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcbformer-ISIC \
--model fcbformer \
--data-name ISIC-2017 \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcbformer-Kvasir \
--model fcbformer \
--data-name Kvasir-SEG \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcbformer-wound \
--model fcbformer \
--data-name wound \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcbformer-benign \
--model fcbformer \
--data-name breast-cancer-benign \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcbformer-malignant \
--model fcbformer \
--data-name breast-cancer-malignant \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcbformer-BKAI \
--model fcbformer \
--data-name BKAI-IGH_NeoPolyp \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcbformer-Neck \
--model fcbformer \
--data-name Neck \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name fcbformer-Waterloo \
--model fcbformer \
--data-name Waterloo_skin \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler


## deeplabv3 ##
python main.py \
--exp-name deeplabv3-CVC \
--model deeplabv3 \
--data-name CVC-ClinicDB \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name deeplabv3-ISIC \
--model deeplabv3 \
--data-name ISIC-2017 \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name deeplabv3-Kvasir \
--model deeplabv3 \
--data-name Kvasir-SEG \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name deeplabv3-wound \
--model deeplabv3 \
--data-name wound \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name deeplabv3-benign \
--model deeplabv3 \
--data-name breast-cancer-benign \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name deeplabv3-malignant \
--model deeplabv3 \
--data-name breast-cancer-malignant \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name deeplabv3-BKAI \
--model deeplabv3 \
--data-name BKAI-IGH_NeoPolyp \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name deeplabv3-Neck \
--model deeplabv3 \
--data-name Neck \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name deeplabv3-Waterloo \
--model deeplabv3 \
--data-name Waterloo_skin \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler


## colonsegnet ##
python main.py \
--exp-name colonsegnet-CVC \
--model colonsegnet \
--data-name CVC-ClinicDB \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name colonsegnet-ISIC \
--model colonsegnet \
--data-name ISIC-2017 \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name colonsegnet-Kvasir \
--model colonsegnet \
--data-name Kvasir-SEG \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name colonsegnet-wound \
--model colonsegnet \
--data-name wound \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name colonsegnet-benign \
--model colonsegnet \
--data-name breast-cancer-benign \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name colonsegnet-malignant \
--model colonsegnet \
--data-name breast-cancer-malignant \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name colonsegnet-BKAI \
--model colonsegnet \
--data-name BKAI-IGH_NeoPolyp \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name colonsegnet-Neck \
--model colonsegnet \
--data-name Neck \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler

python main.py \
--exp-name colonsegnet-Waterloo \
--model colonsegnet \
--data-name Waterloo_skin \
--epochs 100 \
--batch-size 16 \
--use-wandb \
# --use-scheduler