#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataIO import textfile
from autocompvar.metadata import gen_code
from autocompvar.name_convention import to_variable_name

data = {
    "classname": "CreatureType",
    "attrs": [],
    "collection": [
        {"classname": "Info", "attrs": ["id", "name"], "keys": ["id", "name"], "data": {"id": 0, "name": "None"}},
        {"classname": "Info", "attrs": ["id", "name"], "keys": ["id", "name"], "data": {"id": 1, "name": "Beast"}},
        {"classname": "Info", "attrs": ["id", "name"], "keys": ["id", "name"], "data": {"id": 2, "name": "Dragonkin"}},
        {"classname": "Info", "attrs": ["id", "name"], "keys": ["id", "name"], "data": {"id": 3, "name": "Demon"}},
        {"classname": "Info", "attrs": ["id", "name"], "keys": ["id", "name"], "data": {"id": 4, "name": "Elemental"}},
        {"classname": "Info", "attrs": ["id", "name"], "keys": ["id", "name"], "data": {"id": 5, "name": "Giant"}},
        {"classname": "Info", "attrs": ["id", "name"], "keys": ["id", "name"], "data": {"id": 6, "name": "Undead"}},
        {"classname": "Info", "attrs": ["id", "name"], "keys": ["id", "name"], "data": {"id": 7, "name": "Humanoid"}},
        {"classname": "Info", "attrs": ["id", "name"], "keys": ["id", "name"], "data": {"id": 8, "name": "Critter"}},
        {"classname": "Info", "attrs": ["id", "name"], "keys": ["id", "name"], "data": {"id": 9, "name": "Mechanical"}},
        {"classname": "Info", "attrs": ["id", "name"], "keys": ["id", "name"], "data": {"id": 10, "name": "NotSpecified"}},
        {"classname": "Info", "attrs": ["id", "name"], "keys": ["id", "name"], "data": {"id": 11, "name": "Totem"}},
        {"classname": "Info", "attrs": ["id", "name"], "keys": ["id", "name"], "data": {"id": 12, "name": "NonCombatPet"}},
        {"classname": "Info", "attrs": ["id", "name"], "keys": ["id", "name"], "data": {"id": 13, "name": "GasCloud"}},
    ],
}

code = gen_code(data)
path = to_variable_name(data["classname"]) + ".py"
textfile.write(code, path)

