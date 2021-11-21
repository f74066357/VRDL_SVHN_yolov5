# VRDL_SVHN_yolov5
## Street View House Numbers detection

## Dataset:
SVHN dataset  
https://drive.google.com/drive/folders/1aRWnNvirWHXXXpPPfcWlHQuzGJdXagoc?usp=sharing
 - 33402 training images
 - 13068 testing images 

## Dataset Structure
```
data / svhn
        ├── train
        │     ├── 1.png
        │     ├── 1.txt
        │     ├── 2.png
        │     ├── 2.txt
        │     │     .
        │     │     .
        │     │     .
        │     ├── 28000.png
        │     └── 28000.txt
        ├── valid
        │     ├── 28001.png
        │     ├── 28001.txt
        │     ├── 28002.png
        │     ├── 28002.txt
        │     │     .
        │     │     .
        │     │     .
        │     ├── 33402.png
        │     └── 33402.txt
        └── test
              |-xxx.png
```

use 'data/svhn/mat_to_yolo.py' to convert the data format
in this repo I use softlink to represent dataset 

## Install  Dependencies
```
pip install -r requirements.txt
```

## Train 
```
python train.py [your parameter]
```
EX: python train.py --img 320 --batch 16 --epochs 50 --data svhn.yaml --weights yolov5m.pt

## Inference
```
python detect.py [your parameter]
```
EX: python detect.py --source data/svhn/test/ --weights runs/train/exp18/weights/best.pt --conf 0.25 --save-txt --save-conf

## Generate answer
```
python predict.py
```
* remember to modify 'detect-path' and 'score' (default:0) in code 

