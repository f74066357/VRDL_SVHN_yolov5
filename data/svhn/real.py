import os
import shutil
import matplotlib.image as image

img_path = 'train/' # path saves images to be tested
img_list = os.listdir(img_path)
img_list = sorted(img_list, key=lambda x: int(os.path.splitext(x)[0]))
file_len = len(img_list)
# print(file_len)
a=0
for i in range(file_len):
    if(img_list[i].split(".")[1]=='png'):
        x = img_list[i].split(".")[0]
        if(int(x)>28000):
            print(img_list[i])
            a=a+1 
            os.remove('train/'+img_list[i])

print(a)