"""
File: read_image.py
Author: Chuncheng Zhang
Date: 2024-12-13
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Read image from h5py.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-12-13 ------------------------
# Requirements and constants
import h5py
import numpy as np
import pandas as pd
import skimage.io as io
import matplotlib.pyplot as plt

from IPython.display import display
from pycocotools.coco import COCO

dataDir='./nsd'
dataType='train2017'
annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)

# Initialize COCO api for instance annotations.
# ! It is slow
coco=COCO(annFile)
display(coco)

# %% ---- 2024-12-13 ------------------------
# Function and class
# Display COCO categories and supercategories.
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
display(cats)

# Get all images containing given categories, select one at random.
catIds = coco.getCatIds(catNms=['person','dog','skateboard'])
imgIds = coco.getImgIds(catIds=catIds)
display(imgIds)

img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
display(img)

# %%


# %%


# Load and display image.
# I = io.imread('%s/images/%s/%s'%(dataDir,dataType,img['file_name']))
# use url to load image
I = io.imread(img['coco_url'])
plt.axis('off')
plt.imshow(I)
plt.show()

# load and display instance annotations
plt.imshow(I)
plt.axis('off')
annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
anns = coco.loadAnns(annIds)
coco.showAnns(anns)


# %% ---- 2024-12-13 ------------------------
# Play ground
# Read from the hdf5 ball.
# h5_file = h5py.File('./nsd/nsd_stimuli.hdf5', 'r')

with open('./nsd/nsd_stimuli.hdf5', 'rb') as f:
    h5_file = h5py.File(f)
    display(list(h5_file.items()))

    display(img)
    img_id = img['id']
    img_brick = h5_file['imgBrick']
    display(img_brick)
    display(img_brick[img_id].shape)

    plt.imshow(img_brick[img_id])
    plt.show()


# %% ---- 2024-12-13 ------------------------
# Pending
# Fetch image info.
csv = pd.read_csv('./nsd/nsd_stim_info_merged.csv', index_col=0)
# Select 'shared1000'
shared1000 = csv[csv['shared1000']]
display(csv)
display(shared1000)



# %% ---- 2024-12-13 ------------------------
# Pending
img

# %%
csv[csv['cocoId'] == 532481]

# %%
shared1000

# %%
