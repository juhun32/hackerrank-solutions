#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    maxInt = float('-inf')
    minInt = float('inf')
    for num in arr:
        if num > maxInt:
            maxInt = num
        if num < minInt:
            minInt = num
    
    print(sum(arr) - maxInt, sum(arr) - minInt)
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
