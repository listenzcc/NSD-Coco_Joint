"""
File: __init__.py
Author: Chuncheng Zhang
Date: 2024-12-16
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Initialization of the NSD-COCO-Joint Project.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-12-16 ------------------------
# Requirements and constants
from omegaconf import OmegaConf
from loguru import logger



# %% ---- 2024-12-16 ------------------------
# Function and class



# %% ---- 2024-12-16 ------------------------
# Play ground
CONFIG = OmegaConf.load('./config.yaml')
logger.add('./log/{}.log'.format(CONFIG.project.name), rotation='5MB')



# %% ---- 2024-12-16 ------------------------
# Pending



# %% ---- 2024-12-16 ------------------------
# Pending
