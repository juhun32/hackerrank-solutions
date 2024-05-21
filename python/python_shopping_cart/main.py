#!/bin/python3

import math
import os
import random
import re
import sys


class Item:
    # Implement the Item here
    def init(self, name: str, price: int):
        self.name = name
        self.price = price


class ShoppingCart:
    # Implement the ShoppingCart here
    def init(self):
        self.items = list()

    def add(self, item: Item):
        self.items.append(item)

    def total(self):
        result = 0
        for item in self.items:
            result += item.price
        return result

    def len(self):
        return len(self.items)


if __name__ == '__main__':
    fptr = open(os.environ["OUTPUTPATH"], "w")

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(len(cart)) + "\n")
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)

    fptr.close()
