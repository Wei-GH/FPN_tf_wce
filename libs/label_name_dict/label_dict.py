# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from libs.configs import cfgs


class_names = [
        'occupation', 'normal']

classes_originID = {
    'occupation': 1, 'normal': 2}


def get_coco_label_dict():
    originID_classes = {item: key for key, item in classes_originID.items()}
    NAME_LABEL_MAP = dict(zip(class_names, range(len(class_names))))
    return NAME_LABEL_MAP

if cfgs.DATASET_NAME == 'occupation':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'occupation': 1
    }
elif cfgs.DATASET_NAME == 'normal':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'normal': 1
    }
elif cfgs.DATASET_NAME == 'WIDER':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'face': 1
    }
elif cfgs.DATASET_NAME == 'icdar':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'text': 1
    }
elif cfgs.DATASET_NAME.startswith('DOTA'):
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'roundabout': 1,
        'tennis-court': 2,
        'swimming-pool': 3,
        'storage-tank': 4,
        'soccer-ball-field': 5,
        'small-vehicle': 6,
        'ship': 7,
        'plane': 8,
        'large-vehicle': 9,
        'helicopter': 10,
        'harbor': 11,
        'ground-track-field': 12,
        'bridge': 13,
        'basketball-court': 14,
        'baseball-diamond': 15
    }
elif cfgs.DATASET_NAME == 'coco':
    NAME_LABEL_MAP = get_coco_label_dict()
elif cfgs.DATASET_NAME == 'pascal':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'aeroplane': 1,
        'bicycle': 2,
        'bird': 3,
        'boat': 4,
        'bottle': 5,
        'bus': 6,
        'car': 7,
        'cat': 8,
        'chair': 9,
        'cow': 10,
        'diningtable': 11,
        'dog': 12,
        'horse': 13,
        'motorbike': 14,
        'person': 15,
        'pottedplant': 16,
        'sheep': 17,
        'sofa': 18,
        'train': 19,
        'tvmonitor': 20
    }
elif cfgs.DATASET_NAME == 'bdd100k':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'bus': 1,
        'traffic light': 2,
        'traffic sign': 3,
        'person': 4,
        'bike': 5,
        'truck': 6,
        'motor': 7,
        'car': 8,
        'train': 9,
        'rider': 10
    }
else:
    assert 'please set label dict!'


def get_label_name_map():
    reverse_dict = {}
    for name, label in NAME_LABEL_MAP.items():
        reverse_dict[label] = name
    return reverse_dict


LABEl_NAME_MAP = get_label_name_map()
