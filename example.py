#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from autocompvar.metadata import gen_code

data = {
    "classname": "ItemType",
    "attrs": [],
    "collection": [
        {
            "classname": "SubClass",
            "attrs": ["id", "name"],
            "keys": ["name"],
            "data": {"id": 1, "name": "weapon"},
            "collection": [
                {
                    "classname": "Weapon",
                    "attrs": ["id", "name"],
                    "keys": ["name"],
                    "data": {"id": 1, "name": "sword"},
                },
                {
                    "classname": "Weapon",
                    "attrs": ["id", "name"],
                    "keys": ["name"],
                    "data": {"id": 2, "name": "dagger"},
                },
            ],
        },
        {
            "classname": "SubClass",
            "attrs": ["id", "name"],
            "keys": ["name"],
            "data": {"id": 2, "name": "armor"},
            "collection": [
                {
                    "classname": "Armor",
                    "attrs": ["id", "name"],
                    "keys": ["name"],
                    "data": {"id": 1, "name": "plate"},
                },
                {
                    "classname": "Armor",
                    "attrs": ["id", "name"],
                    "keys": ["name"],
                    "data": {"id": 2, "name": "armor"},
                },
            ],
        },
    ],
}

code = gen_code(data)
print(code)