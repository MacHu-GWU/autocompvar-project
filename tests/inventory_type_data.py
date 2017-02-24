#!/usr/bin/env python
# -*- coding: utf-8 -*-

from autocompvar import create_data_script

metadata = {
    "classname": "InventoryType",
    "attrs": [],
    "collection": [
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 0, "name": "无", "name_en": "None", "item_surfix": "", "modifier": 0.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 1, "name": "头部", "name_en": "Head", "item_surfix": "之帽", "modifier": 1.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 2, "name": "颈部", "name_en": "Neck", "item_surfix": "之项链", "modifier": 9.0/16.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 3, "name": "肩部", "name_en": "Shoulder", "item_surfix": "之肩甲", "modifier": 3.0/4.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 4, "name": "衬衣", "name_en": "Shirt", "item_surfix": "之衬衣", "modifier": 0.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 5, "name": "胸部", "name_en": "Chest", "item_surfix": "之胸甲", "modifier": 1.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 6, "name": "腰部", "name_en": "Waist", "item_surfix": "之腰带", "modifier": 3.0/4.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 7, "name": "腿部", "name_en": "Legs", "item_surfix": "之腿甲", "modifier": 1.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 8, "name": "脚部", "name_en": "Feet", "item_surfix": "之靴", "modifier": 3.0/4.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 9, "name": "手腕", "name_en": "Wrist", "item_surfix": "之护腕", "modifier": 9.0/16.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 10, "name": "手部", "name_en": "Hands", "item_surfix": "之手套", "modifier": 3.0/4.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 11, "name": "手指", "name_en": "Finger", "item_surfix": "之戒", "modifier": 9.0/16.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 12, "name": "饰品", "name_en": "Trinkets", "item_surfix": "之饰物", "modifier": 17.0/25.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 13, "name": "单手", "name_en": "OneHand", "item_surfix": "", "modifier": 27.0/64.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 14, "name": "盾牌", "name_en": "Shield", "item_surfix": "之盾", "modifier": 9.0/16.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 15, "name": "弓 弩", "name_en": "Bows", "item_surfix": "", "modifier": 81.0/256.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 16, "name": "背部", "name_en": "Back", "item_surfix": "之披风", "modifier": 9.0/16.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 17, "name": "双手武器", "name_en": "TwoHand", "item_surfix": "", "modifier": 1.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 18, "name": "袋子", "name_en": "Bags", "item_surfix": "之背包", "modifier": 0.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 19, "name": "徽章", "name_en": "Tabard", "item_surfix": "之徽章", "modifier": 0.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 20, "name": "长袍", "name_en": "Robe", "item_surfix": "之袍", "modifier": 1.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 21, "name": "主手武器", "name_en": "MainHand", "item_surfix": "", "modifier": 27.0/64.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 22, "name": "副手武器", "name_en": "OffHand", "item_surfix": "", "modifier": 27.0/64.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 23, "name": "副手物品", "name_en": "Tomb", "item_surfix": "", "modifier": 9.0/16.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 24, "name": "弹药", "name_en": "Waist", "item_surfix": "", "modifier": 0.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 25, "name": "投掷武器和魔杖", "name_en": "Thrown", "item_surfix": "", "modifier": 81.0/256.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 26, "name": "枪械", "name_en": "Gun", "item_surfix": "之枪", "modifier": 81.0/256.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 27, "name": "箭袋", "name_en": "Quiver", "item_surfix": "之箭袋", "modifier": 0.0}},
        {"classname": "Info", "attrs": ["id", "name", "name_en", "item_surfix", "modifier"], "keys": ["name", "name_en"], "data": {"id": 28, "name": "图腾 圣物 圣契 符印", "name_en": "Waist", "item_surfix": "", "modifier":  81.0/256.0}},
    ],
}

create_data_script(metadata)