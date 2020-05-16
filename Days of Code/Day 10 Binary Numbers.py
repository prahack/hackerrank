#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary = bin(n)
    max1s = 0
    i=0
    c=0
    while i<len(binary) :
        if binary[i] == '0':
            if c>max1s:
                max1s = c
            c=0
        if binary[i] == '1':
            c=c+1
        i=i+1
    if c>max1s:
        max1s = c
    print (max1s)
