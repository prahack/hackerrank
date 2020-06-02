#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    nextJumpIndex = (0 + k)%len(c)
    while nextJumpIndex != 0:
        if(c[nextJumpIndex] == 1):
            e = e - 3
        else :
            e = e - 1
        nextJumpIndex = (nextJumpIndex + k)%len(c)
    if(c[nextJumpIndex] == 1):
        return e - 3
    else :
        return e - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
