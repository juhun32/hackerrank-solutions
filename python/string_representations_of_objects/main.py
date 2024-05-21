#!/bin/python3

import math
import os
import random
import re
import sys


class Car:
    def init(self, speed, unit):
        self.speed = speed
        self.unit = unit

    def str(self):
        return "Car with the maximum speed of " + str(self.speed) + " " + str(self.unit)


class Boat:
    def init(self, speed):
        self.speed = speed

    def str(self):
        return "Boat with the maximum speed of " + str(self.speed) + " knots"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUTPATH"], "w")
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        fptr.write("%s\n" % vehicle)
    fptr.close()
