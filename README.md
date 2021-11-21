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

use 'mat_to_yolo.py' to convert the data format

## Install  Dependencies
```
pip install -r requirements.txt
```

## Train 
```
python train.py --img [image size] --batch [batch size] --epochs [epochs] --data svhn.yaml --weights [pre-trained model]
```

## Inference
```
python detect.py --source data/svhn/test/ --weights runs/train/exp/weights/best.pt --conf 0 --save-txt --save-conf
```

## Generate answer
```
python predict.py
```


