#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    divCount = 0
    i = 0
    while i <len(str(n)):
        k = int(str(n)[i])
        if k != 0 and n%k == 0:
            divCount = divCount + 1
        i = i + 1
    return divCount
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
