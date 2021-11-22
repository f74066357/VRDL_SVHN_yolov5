import os
import cv2
import json

image_path = "data/svhn/test/"
label_path = "runs/detect/exp/labels/"
img_list = os.listdir(image_path)
img_list = sorted(img_list, key=lambda x: int(os.path.splitext(x)[0]))
file_len = len(img_list)
print(file_len)
imgnames = []
for i in range(file_len):
    filename = img_list[i][:-4]
    imgnames.append(filename)

data = []
for i in range(len(imgnames)):
    if not os.path.isfile(label_path + imgnames[i] + ".txt"):
        pass
    else:
        f = open(label_path + imgnames[i] + ".txt", "r")
        contents = f.readlines()
        im = cv2.imread(image_path + imgnames[i] + ".png")
        h, w, c = im.shape
        for content in contents:
            content = content.replace("\n", "")
            c = content.split(" ")
            w_center = w * float(c[1])
            h_center = h * float(c[2])
            width = w * float(c[3])
            height = h * float(c[4])
            left = int(w_center - width / 2)
            top = int(h_center - height / 2)

            category_id = int(c[0])
            image_id = int(imgnames[i])
            bbox = [left, top, width, height]
            score = float(c[5])
            k = {}
            k = {
                "image_id": image_id,
                "score": score,
                "category_id": category_id,
                "bbox": bbox,
            }
            data.append(k)
        f.close()

with open("answer.json", "w") as outfile:
    json.dump(data, outfile, indent=4)
