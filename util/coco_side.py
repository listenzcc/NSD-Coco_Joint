"""
File: coco_side.py
Author: Chuncheng Zhang
Date: 2024-12-16
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Find images and their infomations from the COCO system.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-12-16 ------------------------
# Requirements and constants
from collections import defaultdict, OrderedDict
from pathlib import Path
from pycocotools.coco import COCO

from . import logger, CONFIG



# %% ---- 2024-12-16 ------------------------
# Function and class
class COCO_Side(object):
    '''
    Abbreviations:
        cat: Category.
        name: Category name.
        sup: Super catetory name.
        id: Image id.
        ann: Annotations.
        pkp: Person keypoints of the image.
        cap: Caption of the image context.

    COCO supercategories: 
        outdoor food indoor appliance sports person animal vehicle furniture accessory electronic kitchen

    COCO categories: 
        person bicycle car motorcycle airplane bus train truck boat traffic light fire hydrant stop sign parking meter bench bird cat dog horse sheep cow elephant bear zebra giraffe backpack umbrella handbag tie suitcase frisbee skis snowboard sports ball kite baseball bat baseball glove skateboard surfboard tennis racket bottle wine glass cup fork knife spoon bowl banana apple sandwich orange broccoli carrot hot dog pizza donut cake chair couch potted plant bed dining table toilet tv laptop mouse remote keyboard cell phone microwave oven toaster sink refrigerator book clock vase scissors teddy bear hair drier toothbrush
    '''
    annotations_dir=Path(CONFIG.coco.annotations)
    # Initialized from the smaller one.
    # The split is 'val2017' (smaller) or 'train2017' (larger).
    coco_split='train2017' 
    coco_inst:COCO = None
    coco_pkps:COCO = None
    coco_caps:COCO = None
    category_dict:dict = None

    def __init__(self, coco_split:str=None):
        if coco_split:
            self.coco_split = coco_split
        self.load_data()
        self.load_category_dict()
        logger.debug(f'Initialized {self}')

    def load_data(self):
        # Instance.
        path = self.annotations_dir.joinpath(f'instances_{self.coco_split}.json')
        self.coco_inst = COCO(path)
        logger.debug(f'Loaded instance {path}')

        # Captures.
        path = self.annotations_dir.joinpath(f'captions_{self.coco_split}.json')
        self.coco_caps = COCO(path)
        logger.debug(f'Loaded captions {path}')

        # Person keypoints.
        # path = self.annotations_dir.joinpath(f'person_keypoints_{self.coco_split}.json')
        # self.coco_pkps = COCO(path)
        # logger.debug(f'Loaded person keypoints {path}')
        return

    def load_category_dict(self):
        cats = self.get_all_cats()
        # Convert cats into dict.
        self.category_dict = {e['id']: e for e in cats}
        logger.debug(f'Got category_dict: {self.category_dict}')
        return self.category_dict

    def load_imgs(self, id_array:list):
        info_array = self.coco_inst.loadImgs(id_array)
        return info_array

    def get_img_by_id(self, id:int):
        # Get img dict.
        img = self.load_imgs([id])[0]

        # Get annotation array.
        annIds = self.coco_inst.getAnnIds(id)

        # Get annotations and update with category and supercategory names.
        anns = self.coco_inst.loadAnns(annIds)
        [e.update(dict(
            name=self.category_dict[e['category_id']]['name'],
            supercategory=self.category_dict[e['category_id']]['supercategory']
            )) for e in anns]

        # I want the sum area inside every supercategory and name.
        # And order them by the area in decreasing order.
        supercategories = defaultdict(lambda: 0)
        names = defaultdict(lambda: 0)
        for e in anns:
            names[e['name']] += int(e['area'])
            supercategories[e['supercategory']] += int(e['area'])
        
        def _in_order(dct):
            lst = [(k, v) for k, v in dct.items()]
            lst = sorted(lst, key=lambda e: e[1], reverse=True)
            return OrderedDict(lst)
        
        supercategories = _in_order(supercategories)
        names = _in_order(names)

        # Get captions.
        capIds = self.coco_caps.getAnnIds(id)
        captions = self.coco_caps.loadAnns(capIds)
        captions = [e['caption'] for e in captions]

        return dict(
            img=img,
            supercategories=supercategories,
            names=names,
            anns=anns,
            captions=captions)

    def get_all_cats(self):
        all_cats = self.coco_inst.loadCats(self.coco_inst.getCatIds())
        return all_cats

    def get_cat_ids_by_catNms(self, catNms:list):
        cat_ids = self.coco_inst.getCatIds(catNms=catNms)
        return cat_ids



# %% ---- 2024-12-16 ------------------------
# Play ground



# %% ---- 2024-12-16 ------------------------
# Pending



# %% ---- 2024-12-16 ------------------------
# Pending
