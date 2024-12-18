"""
File: nsd_side.py
Author: Chuncheng Zhang
Date: 2024-12-17
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Find the images and their infomations in the NSD system.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-12-17 ------------------------
# Requirements and constants
import pandas as pd
from pathlib import Path
from . import logger, CONFIG



# %% ---- 2024-12-17 ------------------------
# Function and class
class NSD_Side(object):
    '''
    Name mapping:
        cocoId: Id of COCO image.
        nsdId: Image id of NSD image.
        idx: Index of NSD image.
    '''
    stimInfo_csv=Path(CONFIG.nsd.stimInfoCSV)
    shared1000_dir = Path(CONFIG.nsd.shared1000Dir)
    stimInfo_df:pd.DataFrame = None
    shared1000_df:pd.DataFrame = None

    def __init__(self):
        self.load_stimInfo()
        self.crop_shared1000()
        logger.debug(f'Initialized: {self}')

    def load_stimInfo(self):
        self.stimInfo_df = pd.read_csv(self.stimInfo_csv, index_col=0)
        logger.debug(f'Loaded {self.stimInfo_csv}')
        return self.stimInfo_df

    def crop_shared1000(self):
        self.shared1000_df = self.stimInfo_df[self.stimInfo_df['shared1000']].copy()
        self.shared1000_df.index = range(len(self.shared1000_df))
        return self.shared1000_df

    def get_shared1000_img_path(self, idx:int, nsdId:int):
        path = self.shared1000_dir.joinpath('shared{:04d}_nsd{:05d}.png'.format(idx+1, nsdId+1))
        return path

    def get_shared1000_img_path_by_idx(self, idx:int):
        nsdId = self.shared1000_df.iloc[idx]['nsdId']
        path = self.get_shared1000_img_path(idx, nsdId)
        return path

    def get_shared1000_img_path_by_nsdId(self, nsdId:int):
        idx = self.shared1000_df[self.shared1000_df['nsdId'] == nsdId].index[0]
        path = self.get_shared1000_img_path(idx, nsdId)
        return path

    def get_shared1000_img_path_by_cocoId(self, cocoId:int, cocoSplit:str):
        found = self.shared1000_df[self.shared1000_df['cocoSplit']==cocoSplit][self.shared1000_df['cocoId']==cocoId].iloc[0]
        idx = found.name
        nsdId = found['nsdId']
        path = self.get_shared1000_img_path(idx, nsdId)
        return path





# %% ---- 2024-12-17 ------------------------
# Play ground



# %% ---- 2024-12-17 ------------------------
# Pending



# %% ---- 2024-12-17 ------------------------
# Pending
