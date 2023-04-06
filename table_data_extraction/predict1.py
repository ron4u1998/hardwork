from mmdet.apis import init_detector, inference_detector
from mmdet.core import encode_mask_results
import mmcv
import os
import numpy as np

# Specify the path to model config and checkpoint file
config_file = 'default_runtime1.py'
checkpoint_file = 'latest.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cpu')
img = 'test/20221201_102213 (copy).jpg' # or img = mmcv.imread(img), which will only load it once
result = inference_detector(model, img)
# print(result)
model.show_result(img, result, out_file='test_result/'+ img.split('/')[1].split('.')[0]+'.jpg')
# bbox = result[0]
# print(bbox)
seg = np.asarray(result[1][0], dtype=bool)
# print(type(seg))
seg = seg.astype(np.uint8)
print(type(seg))
seg=seg[0]


import json
import numpy as np
from pycocotools import mask
from skimage import measure

ground_truth_binary_mask = seg

fortran_ground_truth_binary_mask = np.asfortranarray(ground_truth_binary_mask)
encoded_ground_truth = mask.encode(fortran_ground_truth_binary_mask)
ground_truth_area = mask.area(encoded_ground_truth)
ground_truth_bounding_box = mask.toBbox(encoded_ground_truth)
contours = measure.find_contours(ground_truth_binary_mask, 0.5)

annotation = {
        "segmentation": [],
        "area": ground_truth_area.tolist(),
        "iscrowd": 0,
        "image_id": 123,
        "bbox": ground_truth_bounding_box.tolist(),
        "category_id": 1,
        "id": 1
    }
for contour in contours:
    contour = np.flip(contour, axis=1)
    segmentation = contour.ravel().tolist()
    annotation["segmentation"].append(segmentation)
print(json.dumps(annotation, indent=4))