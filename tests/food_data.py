#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataIO import textfile
from autocompvar.metadata import gen_code
from autocompvar.name_convention import to_variable_name

data = {
    "classname": "Food",
    "attrs": [],
    "collection": [
        {
            "classname": "FoodCategory",
            "attrs": ["id", "name"],
            "keys": ["name"],
            "data": {"id": 1, "name": "Fruit"},
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
    
code = gen_code(data)
path = to_variable_name(data["classname"]) + ".py"
textfile.write(code, path)

# Copy following code to food_data.py
"""
if __name__ == "__main__":
    assert food.name____Fruit.id == 1
    assert food.name____Meat.id == 2
    assert food.name____Fruit.name == "Fruit"
    assert food.name____Meat.name == "Meat"

    assert food.name____Fruit.id____1.id == 1
    assert food.name____Fruit.id____2.id == 2
    assert food.name____Fruit.name____Apple.name == "Apple"
    assert food.name____Fruit.name____Banana.name == "Banana"

    assert food.name____Meat.id____1.id == 1
    assert food.name____Meat.id____2.id == 2
    assert food.name____Meat.name____Pork.name == "Pork"
    assert food.name____Meat.name____Beef.name == "Beef"
"""