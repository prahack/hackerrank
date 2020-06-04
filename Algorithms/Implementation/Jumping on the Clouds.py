#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i != len(c)-1 :
        if c[i+1] == 1:
            jumps = jumps + 1
            i = i + 2
        elif i < len(c)-2:
            if c[i+2] == 0:
                jumps = jumps + 1
                i = i + 2
            else:
                jumps = jumps + 1
                i = i + 1
        else:
            jumps = jumps + 1
            i = i + 1
    return jumps



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
