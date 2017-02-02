#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataIO import textfile
from autocompvar.metadata import gen_code
from autocompvar.name_convention import to_variable_name

data = {
    "classname": "ItemClass",
    "attrs": [],
    "collection": [
        {"classname": "SubClass0",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 0, "name": "消耗品"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "消耗品"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 1,
                                  "name": "药水"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 2,
                                  "name": "药剂"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 3,
                                  "name": "合剂"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 4,
                                  "name": "卷抽"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 5,
                                  "name": "食物和饮料"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 6,
                                  "name": "物品强化"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 7,
                                  "name": "绷带"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 8,
                                  "name": "其他"}}]},
        {"classname": "SubClass1",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 1, "name": "容器"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "容器"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 1,
                                  "name": "灵魂袋"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 2,
                                  "name": "草药袋"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 3,
                                  "name": "附魔材料袋"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 4,
                                  "name": "工程学材料袋"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 5,
                                  "name": "宝石袋"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 6,
                                  "name": "矿石袋"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 7,
                                  "name": "制皮袋"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 8,
                                  "name": "铭文包"}}]},
        {"classname": "SubClass2",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 2, "name": "武器"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "单手斧"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 1,
                                  "name": "双手斧"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 2,
                                  "name": "弓"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 3,
                                  "name": "枪"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 4,
                                  "name": "单手锤"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 5,
                                  "name": "双手锤"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 6,
                                  "name": "长柄武器"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 7,
                                  "name": "单手剑"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 8,
                                  "name": "双手剑"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 10,
                                  "name": "法杖"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 11,
                                  "name": "异种武器 单手"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 12,
                                  "name": "异种武器 双手"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 13,
                                  "name": "拳套"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 14,
                                  "name": "其他"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 15,
                                  "name": "匕首"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 16,
                                  "name": "投掷武器"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 17,
                                  "name": "矛"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 18,
                                  "name": "弩"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 19,
                                  "name": "魔杖"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 20,
                                  "name": "鱼杆"}}]},
        {"classname": "SubClass3",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 3, "name": "珠宝"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "红色"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 1,
                                  "name": "蓝色"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 2,
                                  "name": "黄色"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 3,
                                  "name": "紫色"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 4,
                                  "name": "绿色"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 5,
                                  "name": "橙色"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 6,
                                  "name": "多彩"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 7,
                                  "name": "简易"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 8,
                                  "name": "棱彩"}}]},
        {"classname": "SubClass4",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 4, "name": "护甲"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "其它戒指等"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 1,
                                  "name": "布甲"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 2,
                                  "name": "皮甲"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 3,
                                  "name": "锁甲"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 4,
                                  "name": "板甲"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 5,
                                  "name": "小圆盾"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 6,
                                  "name": "盾牌"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 7,
                                  "name": "圣契"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 8,
                                  "name": "神像"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 9,
                                  "name": "图腾"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 10,
                                  "name": "魔印"}}]},
        {"classname": "SubClass5",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 5, "name": "材料"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "材料"}}]},
        {"classname": "SubClass6",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 6, "name": "弹药"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "无 魔杖"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 1,
                                  "name": "弩用"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 2,
                                  "name": "弓用"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 3,
                                  "name": "枪用"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 4,
                                  "name": "投掷武器"}}]},
        {"classname": "SubClass7",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 7, "name": "商品"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "商品"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 1,
                                  "name": "零件"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 2,
                                  "name": "爆炸物"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 3,
                                  "name": "装置"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 4,
                                  "name": "珠宝加工"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 5,
                                  "name": "布料"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 6,
                                  "name": "皮革"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 7,
                                  "name": "金属和矿石"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 8,
                                  "name": "肉类"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 9,
                                  "name": "草药"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 10,
                                  "name": "元素"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 11,
                                  "name": "其他"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 12,
                                  "name": "附魔"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 13,
                                  "name": "原料"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 14,
                                  "name": "护甲强化"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 15,
                                  "name": "武器强化"}}]},
        {"classname": "SubClass8",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 8, "name": "原子"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "原子"}}]},
        {"classname": "SubClass9",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 9, "name": "配方"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "书"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 1,
                                  "name": "制皮"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 2,
                                  "name": "裁缝"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 3,
                                  "name": "工程学"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 4,
                                  "name": "锻造"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 5,
                                  "name": "烹饪"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 6,
                                  "name": "炼金术"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 7,
                                  "name": "急救"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 8,
                                  "name": "付魔"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 9,
                                  "name": "钩鱼"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 10,
                                  "name": "珠宝加工"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 11,
                                  "name": "铭文"}}]},
        {"classname": "SubClass10",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 10, "name": "货币"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "货币"}}]},
        {"classname": "SubClass11",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 11, "name": "箭袋"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "箭袋 作废 "}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 1,
                                  "name": "箭袋 作废"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 2,
                                  "name": "箭袋"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 3,
                                  "name": "弹药袋"}}]},
        {"classname": "SubClass12",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 12, "name": "任务"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "任务"}}]},
        {"classname": "SubClass13",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 13, "name": "钥匙"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "钥匙"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 1,
                                  "name": "开锁工具"}}]},
        {"classname": "SubClass14",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 14, "name": "永久"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "永久"}}]},
        {"classname": "SubClass15",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 15, "name": "其它"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 0,
                                  "name": "垃圾"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 1,
                                  "name": "材料"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 2,
                                  "name": "宠物"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 3,
                                  "name": "节日"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 4,
                                  "name": "其他"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 5,
                                  "name": "坐骑"}}]},
        {"classname": "SubClass16",
         "attrs": ["id", "name"],
         "keys": ["name"],
         "data": {"id": 16, "name": "雕文"},
         "collection": [{"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 1,
                                  "name": "战士"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 2,
                                  "name": "圣骑士"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 3,
                                  "name": "猎人"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 4,
                                  "name": "盗贼"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 5,
                                  "name": "牧师"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 6,
                                  "name": "死亡骑士"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 7,
                                  "name": "萨满祭司"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 8,
                                  "name": "法师"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 9,
                                  "name": "术士"}},
                        {"classname": "Info",
                         "attrs": ["id", "name"],
                         "keys": ["name"],
                         "data": {"id": 11,
                                  "name": "德鲁伊"}}]}
    ],
}

code = gen_code(data)
path = to_variable_name(data["classname"]) + ".py"
textfile.write(code, path)