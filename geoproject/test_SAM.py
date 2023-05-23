import torch
import torchvision
print("PyTorch version:", torch.__version__)
print("Torchvision version:", torchvision.__version__)
print("CUDA is available:", torch.cuda.is_available())

# Easy implementation of SAM (need CUDA)
# SAM Github :
# https://github.com/facebookresearch/segment-anything#model-checkpoints

import numpy as np
import matplotlib.pyplot as plt
import cv2

import sys
sys.path.append("..")
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor


        
image = cv2.imread('houses.jpg')  #Try houses.jpg or neurons.jpg
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

"""
plt.figure(figsize=(10,10))
plt.imshow(image)
plt.axis('off')
plt.show()
"""

#specify the right path
sam_checkpoint = r"D:\téléchargements\sam_vit_h_4b8939.pth"
model_type = "vit_h"

sam_checkpoint = r"D:\téléchargements\sam_vit_b_01ec64.pth"
model_type = "vit_b"

device = "cuda"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
#sam.to(device=device)

#segmentation mask
mask_generator_ = SamAutomaticMaskGenerator(
    model=sam
)

masks = mask_generator_.generate(image)

print(len(masks))