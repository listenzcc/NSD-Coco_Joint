"""
File: summary-nsd.py
Author: Chuncheng Zhang
Date: 2024-12-18
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Summary the supercategories and names of the NSD (shared1000) images.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-12-18 ------------------------
# Requirements and constants
import random
import pandas as pd
import seaborn as sns
import skimage.io as io
import matplotlib.pyplot as plt
from rich import print

from util.nsd_side import NSD_Side
from util.coco_side import COCO_Side


# %% ---- 2024-12-18 ------------------------
# Function and class
nsd_side = NSD_Side()
coco_side = COCO_Side(coco_split='train2017')


# %% ---- 2024-12-18 ------------------------
# Play ground
sdf = nsd_side.shared1000_df
buf = []
for i, se in sdf.iterrows():
    # Fetch the info.
    cocoId = se['cocoId']
    cocoSplit = se['cocoSplit']
    nsdId = se['nsdId']
    nsd_idx = se.name

    # Get the nsd_path and coco ball.
    nsd_path = nsd_side.get_shared1000_img_path_by_nsdId(nsdId)
    ball = coco_side.get_img_by_id(cocoId)

    # Fine the got info and append to the buf.
    supercategories = dict(ball['supercategories'])
    # supercategories.update(dict(
    #     nsdId=nsdId,
    #     nsd_idx = nsd_idx
    # ))
    buf.append(supercategories)

# Convert buf into the Dataframe.
table = pd.DataFrame(buf)
table

# %%

# Convert the table into go-nogo mode,
# fill the nan with 0 and others with 1.
table_flag = table.copy()
table_flag -= table_flag
table_flag += 1
table_flag.fillna(0, inplace=True)
table_flag


# %% ---- 2024-12-18 ------------------------
# Pending
sns.set_theme('notebook')

fig, axes = plt.subplots(3, 1, figsize=(10, 8))

ax = axes[0]
sns.heatmap(table, ax=ax)
ax.tick_params(axis='x', labelrotation=25)

ax = axes[1]
sns.barplot(table.sum(axis=0), ax=ax)
ax.tick_params(axis='x', labelrotation=25)
ax.set_ylabel('Area')

ax = axes[2]
sns.barplot(table_flag.sum(axis=0), ax=ax)
ax.tick_params(axis='x', labelrotation=25)
ax.set_ylabel('Count')

suptitle = 'Supercategories in NSD(shared1000) images'
fig.suptitle(suptitle)
fig.tight_layout()
fig.savefig(f'{suptitle}.jpg')
plt.show()



# %% ---- 2024-12-18 ------------------------
# Pending

# %%
