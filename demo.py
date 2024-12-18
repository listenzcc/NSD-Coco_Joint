"""
File: demo.py
Author: Chuncheng Zhang
Date: 2024-12-17
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    The demo of how to use the coco_side and nsd_side in the util module.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-12-17 ------------------------
# Requirements and constants
import random
import skimage.io as io
import matplotlib.pyplot as plt
from rich import print

from util.nsd_side import NSD_Side
from util.coco_side import COCO_Side



# %% ---- 2024-12-17 ------------------------
# Function and class
nsd_side = NSD_Side()
coco_side = COCO_Side(coco_split='train2017')


# %% ---- 2024-12-17 ------------------------
# Play ground
# Randomly choose one image and display
sdf = nsd_side.shared1000_df
se = sdf.iloc[random.randint(0, len(sdf))]
idx = se.name
cocoId = se['cocoId']
cocoSplit = se['cocoSplit']
nsdId = se['nsdId']

nsd_path = nsd_side.get_shared1000_img_path_by_nsdId(nsdId)
print(nsd_path)
print(nsd_side.get_shared1000_img_path_by_idx(idx))
print(nsd_side.get_shared1000_img_path_by_cocoId(cocoId, cocoSplit))

# Get all of the image from the coco system
ball = coco_side.get_img_by_id(cocoId)
print(ball)

# Display the nsd and coco images
fig, axes = plt.subplots(1, 3, figsize=(8, 3))

# NSD: load and display image
I = io.imread(nsd_path)
ax = axes[0]
ax.set_title(f'NSD - {nsdId}')
ax.axis('off')
ax.imshow(I)

# COCO: use url to load image
# Image without annotation
img = ball['img']
I = io.imread(img['coco_url'])
ax = axes[1]
ax.set_title(f'COCO - {cocoId}')
ax.axis('off')
ax.imshow(I)

# Image with annotation
ax = axes[2]
ax.set_title(f'COCO - {cocoId}')
ax.axis('off')
ax.imshow(I)
coco_side.coco_inst.showAnns(ball['anns'], draw_bbox=False)

# Render
fig.tight_layout()
plt.show()

print(ball['supercategories'])
print(ball['names'])
print(ball['captions'])


# %% ---- 2024-12-17 ------------------------
# Pending


# %% ---- 2024-12-17 ------------------------
# Pending

# %%

# %%
