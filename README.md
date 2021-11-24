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

## My training weight
https://drive.google.com/file/d/18qZEDDLE6-Jg4Iu8OtzEQ5N61He5XExK/view?usp=sharing

## Colab link
run inferene and bench mark and generating submission file
https://colab.research.google.com/drive/1O15T8mucMoTuJ2d3qc2TWErEhDZBSQcc?usp=sharing

## Reference
* https://github.com/ultralytics/yolov5
* https://github.com/chia56028/Street-View-House-Numbers-Detection
