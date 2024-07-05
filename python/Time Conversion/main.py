#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hh = s[0:2]
    hh = int(hh)
    dn = s[8:]
    print(dn)
    result = ""
    if dn == 'PM':
        if hh == 12:
            result = hh
        else:
            result = hh + 12
    else:
        if hh == 12:
            result = '0' + str(hh - 12)
        else:
            result = '0' + str(hh)
         
    return str(result) + s[2:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
