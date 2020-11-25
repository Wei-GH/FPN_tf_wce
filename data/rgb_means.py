# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
# path = 'E:\\zflPro\\f-r-cnn\\traindata\\shiyan3B\\dataforFRCNN\\JPEGImages\\'
path = "/home/symip/zhuofalin/FPN_tf_wce/data/wce_occupation/wce_occupation_train/JPEGImages/"
# traintxtfile = 'E:\\zflPro\\f-r-cnn\\traindata\\shiyan3B\\dataforFRCNN\\ImageSets\\Main\\train.txt'
trainimage = []
# with open(traintxtfile, 'r') as f:
#     lines = f.readlines()
# for line in range(len(lines)):
#     trainimage.append(lines[line].split('\n')[0])

def compute(path):
    file_names = os.listdir(path)

    per_image_Rmean = []

    per_image_Gmean = []

    per_image_Bmean = []

    for file_name in file_names:
        # filename = file_name.split('.')[0]
        # if filename in trainimage:
        img = cv2.imread(os.path.join(path, file_name), 1)
        per_image_Bmean.append(np.mean(img[:, :, 0]))
        per_image_Gmean.append(np.mean(img[:, :, 1]))
        per_image_Rmean.append(np.mean(img[:, :, 2]))

    R_mean = np.mean(per_image_Rmean)

    G_mean = np.mean(per_image_Gmean)

    B_mean = np.mean(per_image_Bmean)

    return R_mean, G_mean, B_mean


if __name__ == '__main__':
    R, G, B = compute(path)
    print(R, G, B)
    # / home / symip / zhuofalin / FPN_tf_wce / data / wce_normal / wce_normal_train / JPEGImage / 000010661.j
    # pg
    # / home / symip / zhuofalin / FPN_tf_wce / data / wce_normal / wce_normal_train / JPEGImage