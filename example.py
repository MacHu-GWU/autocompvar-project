#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from autocompvar.metadata import gen_code

metadata = {
    "classname": "Food", # it's the class name
    "attrs": [], # it's the attributes list in order, if no attributes, use empty list
    "collection": [ # list of sub class
        {
            "classname": "FoodCategory",
            "attrs": ["id", "name"],
            "keys": ["name"], # key is the attributes that indexable. typically the value is non-repeat integer or string
            "data": {"id": 1, "name": "Fruit"}, # the data for the instance
            "collection": [
                {
                    "classname": "Fruit",
                    "attrs": ["id", "name"],
                    "keys": ["id", "name"],
                    "data": {"id": 1, "name": "Apple"},
                },
                {
                    "classname": "Fruit",
                    "attrs": ["id", "name"],
                    "keys": ["id", "name"],
                    "data": {"id": 2, "name": "Banana"},
                },
            ],
        },
        {
            "classname": "FoodCategory",
            "attrs": ["id", "name"],
            "keys": ["name"],
            "data": {"id": 2, "name": "Meat"},
            "collection": [
                {
                    "classname": "Meat",
                    "attrs": ["id", "name"],
                    "keys": ["id", "name"],
                    "data": {"id": 1, "name": "Pork"},
                },
                {
                    "classname": "Meat",
                    "attrs": ["id", "name"],
                    "keys": ["id", "name"],
                    "data": {"id": 2, "name": "Beef"},
                },
            ],
        },
    ],
}

code = gen_code(metadata)
print(code)